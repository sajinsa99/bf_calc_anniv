import { execFile } from 'child_process';
import path from 'path';
import fs from 'fs';
import express from 'express';
import { fileURLToPath } from 'url';
import rateLimit from 'express-rate-limit';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express(); // nosemgrep: javascript.express.security.audit.express-check-csurf-middleware-usage.express-check-csurf-middleware-usage
app.disable('x-powered-by');

const PORT = process.env.PORT || 6001;
const PYTHON = process.env.PYTHON || 'python3';
const CALC_ANNIV_PY = path.join(__dirname, '..', 'calc-anniv.py');

function loadDotEnv() {
  try {
    const raw = fs.readFileSync(path.join(__dirname, '.env'), 'utf8');
    raw.split(/\r?\n/).forEach(line => {
      const m = line.match(/^\s*([A-Z_][A-Z0-9_]*)\s*=\s*(.*)\s*$/);
      if (m && !process.env[m[1]]) process.env[m[1]] = m[2].replace(/^['"]|['"]$/g, '');
    });
  } catch { /* .env absent → rely on real env vars */ }
}
loadDotEnv();

// Security headers middleware
app.use((req, res, next) => {
  res.setHeader('X-Content-Type-Options', 'nosniff');
  res.setHeader('X-Frame-Options', 'DENY');
  res.setHeader('Referrer-Policy', 'no-referrer');
  res.setHeader(
    'Content-Security-Policy',
    "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'"
  );
  next();
});

app.use(express.static(path.join(__dirname, 'public'), {
  setHeaders: (res) => res.setHeader('Cache-Control', 'no-cache'),
}));

const RE_DATE = /^\d{2}-\d{2}-\d{4}$/;
const RE_YEAR = /^\d{4}$/;

function isValidDateOrYear(val) {
  return RE_DATE.test(val) || RE_YEAR.test(val);
}

/**
 * Parse a JJ-MM-AAAA string into a Date object, or return null if invalid.
 * Rejects logically impossible dates like 99-99-9999.
 */
function parseFrDate(str) {
  if (!RE_DATE.test(str)) return null;
  const [dd, mm, yyyy] = str.split('-').map(Number);
  const d = new Date(yyyy, mm - 1, dd);
  if (d.getFullYear() !== yyyy || d.getMonth() !== mm - 1 || d.getDate() !== dd) return null;
  return d;
}

const apiLimiter = rateLimit({
  windowMs: 60 * 1000,
  max: 60,
  standardHeaders: true,
  legacyHeaders: false,
  message: { error: 'Trop de requêtes — réessayez dans une minute.' },
});

// GET /api/calc?date=JJ-MM-AAAA[&deces=...][&futur=...]
app.get('/api/calc', apiLimiter, (req, res) => {
  const { date, deces, futur } = req.query;

  // Guard against array-valued query params (?date=a&date=b)
  if (Array.isArray(date) || Array.isArray(deces) || Array.isArray(futur)) {
    return res.status(400).json({ error: 'Paramètres dupliqués non autorisés' });
  }

  if (!date || !parseFrDate(date)) {
    return res.status(400).json({ error: 'Paramètre date manquant ou invalide (format JJ-MM-AAAA requis, ex: 14-10-1938)' });
  }

  if (deces && futur) {
    return res.status(400).json({ error: 'Les paramètres deces et futur sont mutuellement exclusifs' });
  }

  if (deces && !isValidDateOrYear(deces)) {
    return res.status(400).json({ error: 'Paramètre deces invalide (format JJ-MM-AAAA ou AAAA requis)' });
  }

  if (deces && RE_DATE.test(deces) && !parseFrDate(deces)) {
    return res.status(400).json({ error: 'Paramètre deces invalide (date impossible)' });
  }

  if (futur && !isValidDateOrYear(futur)) {
    return res.status(400).json({ error: 'Paramètre futur invalide (format JJ-MM-AAAA ou AAAA requis)' });
  }

  if (futur && RE_DATE.test(futur) && !parseFrDate(futur)) {
    return res.status(400).json({ error: 'Paramètre futur invalide (date impossible)' });
  }

  const pyArgs = ['--json', '--date', date];
  if (deces) pyArgs.push('--deces', deces);
  if (futur) pyArgs.push('--futur', futur);

  execFile(PYTHON, [CALC_ANNIV_PY, ...pyArgs], { timeout: 10000 }, (err, stdout, stderr) => {
    if (err) {
      const detail = (stderr || err.message).trim();
      console.error('[calc-anniv.py error]', detail);
      return res.status(400).json({ error: detail });
    }
    try {
      const data = JSON.parse(stdout);
      res.json(data);
    } catch (e) {
      console.error('[parse error]', e.message, stdout.slice(0, 200));
      res.status(500).json({ error: 'Réponse invalide de calc-anniv.py' });
    }
  });
});

app.listen(PORT, () => {
  console.log(`calc_anniv_web running on port ${PORT}`);
});
