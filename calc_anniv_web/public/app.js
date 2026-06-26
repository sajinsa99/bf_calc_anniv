// ── DOM refs ──────────────────────────────────────────────────────────────────
const inputDate       = document.getElementById('input-date');
const btnCalc         = document.getElementById('btn-calc');
const statusEl        = document.getElementById('status');
const resultEl        = document.getElementById('result');
const decesFields     = document.getElementById('deces-fields');
const futurFields     = document.getElementById('futur-fields');
const inputDeces      = document.getElementById('input-deces');
const inputDecesAnnee = document.getElementById('input-deces-annee');
const inputFutur      = document.getElementById('input-futur');
const inputFuturAnnee = document.getElementById('input-futur-annee');
const decesDateGroup  = document.getElementById('deces-date-group');
const decesYearGroup  = document.getElementById('deces-year-group');
const futurDateGroup  = document.getElementById('futur-date-group');
const futurYearGroup  = document.getElementById('futur-year-group');
const decesAnneeOnly  = document.getElementById('deces-annee-only');
const futurAnneeOnly  = document.getElementById('futur-annee-only');
const modeRadios      = document.querySelectorAll('input[name="mode"]');

// ── Helpers ───────────────────────────────────────────────────────────────────
const RE_DATE = /^\d{2}-\d{2}-\d{4}$/;
const RE_YEAR = /^\d{4}$/;

function jourSemaineFr(isoDate) {
  const jours = ['dimanche', 'lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi'];
  const [y, m, d] = isoDate.split('-').map(Number);
  return jours[new Date(y, m - 1, d).getDay()];
}

function formatDateFr(isoDate) {
  const [y, m, d] = isoDate.split('-');
  return `${d}/${m}/${y} (${jourSemaineFr(isoDate)})`;
}

function pluralJours(n) {
  return `${n} jour${n > 1 ? 's' : ''}`;
}

// ── Status ────────────────────────────────────────────────────────────────────
function setStatus(msg, type = 'info') {
  statusEl.textContent = msg;
  statusEl.className = `status ${type}`;
}

function clearStatus() {
  statusEl.className = 'status hidden';
  statusEl.textContent = '';
}

// ── Mode toggles ──────────────────────────────────────────────────────────────
function getMode() {
  return [...modeRadios].find(r => r.checked)?.value ?? 'vivant';
}

function updateModeUI() {
  const mode = getMode();
  decesFields.classList.toggle('hidden', mode !== 'deces');
  futurFields.classList.toggle('hidden', mode !== 'futur');
}

modeRadios.forEach(r => r.addEventListener('change', updateModeUI));

decesAnneeOnly.addEventListener('change', () => {
  decesDateGroup.classList.toggle('hidden', decesAnneeOnly.checked);
  decesYearGroup.classList.toggle('hidden', !decesAnneeOnly.checked);
});

futurAnneeOnly.addEventListener('change', () => {
  futurDateGroup.classList.toggle('hidden', futurAnneeOnly.checked);
  futurYearGroup.classList.toggle('hidden', !futurAnneeOnly.checked);
});

// ── Validation client ─────────────────────────────────────────────────────────
function validate() {
  if (!RE_DATE.test(inputDate.value.trim())) {
    setStatus('Format de date de naissance invalide — attendu JJ-MM-AAAA', 'error');
    return false;
  }
  const mode = getMode();
  if (mode === 'deces') {
    const val = decesAnneeOnly.checked ? inputDecesAnnee.value.trim() : inputDeces.value.trim();
    if (!val) { setStatus('Veuillez saisir la date ou l\'année de décès', 'error'); return false; }
    if (decesAnneeOnly.checked && !RE_YEAR.test(val)) {
      setStatus('Format d\'année invalide — attendu AAAA', 'error'); return false;
    }
    if (!decesAnneeOnly.checked && !RE_DATE.test(val)) {
      setStatus('Format de date de décès invalide — attendu JJ-MM-AAAA', 'error'); return false;
    }
  }
  if (mode === 'futur') {
    const val = futurAnneeOnly.checked ? inputFuturAnnee.value.trim() : inputFutur.value.trim();
    if (!val) { setStatus('Veuillez saisir la date ou l\'année de référence', 'error'); return false; }
    if (futurAnneeOnly.checked && !RE_YEAR.test(val)) {
      setStatus('Format d\'année invalide — attendu AAAA', 'error'); return false;
    }
    if (!futurAnneeOnly.checked && !RE_DATE.test(val)) {
      setStatus('Format de date invalide — attendu JJ-MM-AAAA', 'error'); return false;
    }
  }
  return true;
}

// ── Submit ────────────────────────────────────────────────────────────────────
async function handleSubmit() {
  clearStatus();
  resultEl.classList.add('hidden');
  if (!validate()) return;

  btnCalc.disabled = true;
  setStatus('Calcul en cours…');

  const params = new URLSearchParams({ date: inputDate.value.trim() });
  const mode = getMode();
  if (mode === 'deces') {
    params.set('deces', decesAnneeOnly.checked ? inputDecesAnnee.value.trim() : inputDeces.value.trim());
  } else if (mode === 'futur') {
    params.set('futur', futurAnneeOnly.checked ? inputFuturAnnee.value.trim() : inputFutur.value.trim());
  }

  try {
    const resp = await fetch(`/api/calc?${params}`);
    const payload = await resp.json();
    if (!resp.ok) {
      setStatus(payload.error || 'Erreur serveur', 'error');
      return;
    }
    clearStatus();
    renderResult(payload);
  } catch (e) {
    setStatus('Erreur réseau : ' + e.message, 'error');
  } finally {
    btnCalc.disabled = false;
  }
}

btnCalc.addEventListener('click', handleSubmit);
[inputDate, inputDeces, inputDecesAnnee, inputFutur, inputFuturAnnee].forEach(el => {
  el.addEventListener('keydown', e => { if (e.key === 'Enter') handleSubmit(); });
});

// ── Renderers ─────────────────────────────────────────────────────────────────
function card(title, value, sub = '', extra = '') {
  return `<div class="info-card">
    <div class="card-title">${title}</div>
    <div class="card-value">${value}</div>
    ${sub ? `<div class="card-sub">${sub}</div>` : ''}
    ${extra ? `<div class="card-sub">${extra}</div>` : ''}
  </div>`;
}

function annivCard(title, value, jours = null) {
  const sub = jours !== null ? `dans ${pluralJours(jours)}` : '';
  return `<div class="info-card card-anniv">
    <div class="card-title">${title}</div>
    <div class="card-value">${value}</div>
    ${sub ? `<div class="card-sub">${sub}</div>` : ''}
  </div>`;
}

function noteBiss(flag) {
  return flag ? '<span class="note-biss"> → 01/03 (année non bissextile)</span>' : '';
}

function renderVivant(naissance, d) {
  let html = `<div class="info-cards">`;
  html += card('Âge actuel', `${d.age_actuel} ans`);
  if (d.est_anniversaire) {
    html += `<div class="info-card card-anniv">
      <div class="card-title">Anniversaire</div>
      <div class="card-value card-highlight">🎉 Joyeux anniversaire ! (${d.age_actuel} ans)</div>
    </div>`;
  } else {
    html += annivCard('Prochain anniversaire', formatDateFr(d.prochain_anniversaire), d.prochain_anniversaire_jours);
    html += card('Âge atteint', `${d.age_prochain} ans`);
  }
  html += `</div>`;
  return html;
}

function renderDeces(naissance, d) {
  let html = `<div class="info-cards">`;
  html += card('Date de décès', formatDateFr(d.date_deces));
  html += card('Âge au décès', `${d.age_deces} ans`);
  html += card('Âge aujourd\'hui', `${d.age_aurait} ans`, '(si vivant·e)');
  html += card(
    'Anniversaire dans l\'année du décès',
    formatDateFr(d.anniv_annee_deces) + noteBiss(d.anniv_annee_deces_note_bissextile)
  );
  html += annivCard('Prochain anniversaire de naissance', formatDateFr(d.prochain_anniv_naissance), d.prochain_anniv_naissance_jours);
  if (d.nb_anniv_depuis_deces > 0) {
    html += card('Anniversaires depuis le décès', `${d.nb_anniv_depuis_deces}`);
  }
  html += annivCard('Prochain anniversaire du décès', formatDateFr(d.prochain_anniv_deces), d.prochain_anniv_deces_jours);
  html += `</div>`;
  return html;
}

function renderDecesAnnee(naissance, d) {
  let html = `<div class="info-cards">`;
  html += card('Année de décès', `${d.annee_deces}`);
  html += card(
    'Âge au décès',
    `${d.age_deces_avant} ou ${d.age_deces_apres} ans`,
    `avant ou après le ${formatDateFr(d.anniv_annee_deces).split(' ')[0]}${noteBiss(d.anniv_annee_deces_note_bissextile)}`
  );
  html += card('Âge aujourd\'hui', `${d.age_aurait} ans`, '(si vivant·e)');
  html += card(
    'Anniversaire dans l\'année du décès',
    formatDateFr(d.anniv_annee_deces) + noteBiss(d.anniv_annee_deces_note_bissextile)
  );
  html += annivCard('Prochain anniversaire de naissance', formatDateFr(d.prochain_anniv_naissance), d.prochain_anniv_naissance_jours);
  if (d.nb_anniv_depuis_deces_approx > 0) {
    html += card('Anniversaires depuis le décès', `≈ ${d.nb_anniv_depuis_deces_approx}`, '(approximatif — date exacte inconnue)');
  }
  html += card('Prochain anniversaire du décès', `courant ${d.prochain_anniv_deces_annee}`, '(date exacte inconnue)');
  html += `</div>`;
  return html;
}

function renderFutur(naissance, d) {
  let html = `<div class="info-cards">`;
  html += card('Date de référence', formatDateFr(d.date_futur));
  html += card('Âge à cette date', `${d.age_a_futur} ans`);
  if (d.est_anniversaire) {
    html += `<div class="info-card card-anniv">
      <div class="card-title">Anniversaire</div>
      <div class="card-value card-highlight">🎂 Jour d'anniversaire ! (${d.age_a_futur} ans)</div>
    </div>`;
  } else {
    html += annivCard('Prochain anniversaire', formatDateFr(d.prochain_anniversaire), d.prochain_anniversaire_jours);
    html += card('Âge atteint', `${d.age_prochain} ans`);
  }
  html += `</div>`;
  return html;
}

function renderFuturAnnee(naissance, d) {
  let html = `<div class="info-cards">`;
  html += card('Année de référence', `${d.annee_futur}`);
  html += card(
    'Âge dans cette année',
    `${d.age_avant} ou ${d.age_apres} ans`,
    `avant ou après le ${formatDateFr(d.anniv_cette_annee).split(' ')[0]}${noteBiss(d.anniv_note_bissextile)}`
  );
  html += card(
    'Anniversaire dans cette année',
    formatDateFr(d.anniv_cette_annee) + noteBiss(d.anniv_note_bissextile)
  );
  html += `</div>`;
  return html;
}

function renderResult(payload) {
  const { naissance, mode, data } = payload;
  let html = `<div class="result-header">
    <div class="result-naissance">🎂 Date de naissance : ${formatDateFr(naissance)}</div>
  </div>`;

  switch (mode) {
    case 'vivant':      html += renderVivant(naissance, data);     break;
    case 'deces':       html += renderDeces(naissance, data);      break;
    case 'deces_annee': html += renderDecesAnnee(naissance, data); break;
    case 'futur':       html += renderFutur(naissance, data);      break;
    case 'futur_annee': html += renderFuturAnnee(naissance, data); break;
    default:
      html += `<p>Mode inconnu : ${mode}</p>`;
  }

  resultEl.innerHTML = html;
  resultEl.classList.remove('hidden');
}
