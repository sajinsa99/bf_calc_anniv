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
const chkDeces        = document.getElementById('chk-deces');
const chkFutur        = document.getElementById('chk-futur');
const chkAge          = document.getElementById('chk-age');
const ageFields       = document.getElementById('age-fields');
const inputAge        = document.getElementById('input-age');

// ── Helpers ───────────────────────────────────────────────────────────────────
const RE_YEAR = /^\d{4}$/;

// Convertit YYYY-MM-DD (valeur native d'un input type=date) en JJ-MM-AAAA
function isoToFr(isoDate) {
  const [y, m, d] = isoDate.split('-');
  return `${d}-${m}-${y}`;
}

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

// ── Checkbox toggles ──────────────────────────────────────────────────────────
function updateModeUI() {
  decesFields.classList.toggle('hidden', !chkDeces.checked);
  futurFields.classList.toggle('hidden', !chkFutur.checked);
  ageFields.classList.toggle('hidden', !chkAge.checked);
}

chkDeces.addEventListener('change', updateModeUI);
chkFutur.addEventListener('change', updateModeUI);
chkAge.addEventListener('change', updateModeUI);

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
  if (!inputDate.value) {
    setStatus('Veuillez sélectionner une date de naissance', 'error');
    return false;
  }
  if (chkDeces.checked) {
    if (decesAnneeOnly.checked) {
      if (!RE_YEAR.test(inputDecesAnnee.value.trim())) {
        setStatus('Format d\'année invalide — attendu AAAA', 'error'); return false;
      }
    } else if (!inputDeces.value) {
      setStatus('Veuillez sélectionner une date de décès', 'error'); return false;
    }
  }
  if (chkFutur.checked) {
    if (futurAnneeOnly.checked) {
      if (!RE_YEAR.test(inputFuturAnnee.value.trim())) {
        setStatus('Format d\'année invalide — attendu AAAA', 'error'); return false;
      }
    } else if (!inputFutur.value) {
      setStatus('Veuillez sélectionner une date de référence', 'error'); return false;
    }
  }
  if (chkAge.checked) {
    const v = parseInt(inputAge.value, 10);
    if (isNaN(v) || v < 0 || v > 150) {
      setStatus('Âge invalide — entier entre 0 et 150', 'error'); return false;
    }
  }
  return true;
}

// ── API calls ─────────────────────────────────────────────────────────────────
async function fetchCalc(extraParams) {
  const params = new URLSearchParams({ date: isoToFr(inputDate.value), ...extraParams });
  const resp = await fetch(`api/calc?${params}`);
  const payload = await resp.json();
  if (!resp.ok) throw new Error(payload.error || 'Erreur serveur');
  return payload;
}

// ── Submit ────────────────────────────────────────────────────────────────────
async function handleSubmit() {
  clearStatus();
  resultEl.classList.add('hidden');
  if (!validate()) return;

  btnCalc.disabled = true;
  setStatus('Calcul en cours…');

  const requests = [];

  // Toujours calculer le mode vivant
  requests.push(fetchCalc({}));

  if (chkDeces.checked) {
    const val = decesAnneeOnly.checked ? inputDecesAnnee.value.trim() : isoToFr(inputDeces.value);
    requests.push(fetchCalc({ deces: val }));
  }

  if (chkFutur.checked) {
    const val = futurAnneeOnly.checked ? inputFuturAnnee.value.trim() : isoToFr(inputFutur.value);
    requests.push(fetchCalc({ futur: val }));
  }

  try {
    const results = await Promise.all(requests);
    clearStatus();
    const ageResult = chkAge.checked ? calcAge(inputDate.value, parseInt(inputAge.value, 10)) : null;
    renderAllResults(results, ageResult);
  } catch (e) {
    setStatus(e.message, 'error');
  } finally {
    btnCalc.disabled = false;
  }
}

btnCalc.addEventListener('click', handleSubmit);
[inputDecesAnnee, inputFuturAnnee].forEach(el => {
  el.addEventListener('keydown', e => { if (e.key === 'Enter') handleSubmit(); });
});

const btnReset = document.getElementById('btn-reset');
btnReset.addEventListener('click', () => {
  inputDate.value = '';
  inputDeces.value = '';
  inputDecesAnnee.value = '';
  inputFutur.value = '';
  inputFuturAnnee.value = '';
  chkDeces.checked = false;
  chkFutur.checked = false;
  chkAge.checked = false;
  decesAnneeOnly.checked = false;
  futurAnneeOnly.checked = false;
  inputAge.value = '';
  updateModeUI();
  decesDateGroup.classList.remove('hidden');
  decesYearGroup.classList.add('hidden');
  futurDateGroup.classList.remove('hidden');
  futurYearGroup.classList.add('hidden');
  clearStatus();
  resultEl.classList.add('hidden');
  resultEl.innerHTML = '';
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
  html += card('Prochain anniversaire du décès', `courant ${d.prochain_anniv_deces_annee}`, '(date exacte inconnue)', `d'ici le 31/12/${d.prochain_anniv_deces_annee}`);
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

function renderOneResult(payload) {
  const { naissance, mode, data } = payload;
  let html = '';
  switch (mode) {
    case 'vivant':      html += renderVivant(naissance, data);     break;
    case 'deces':       html += renderDeces(naissance, data);      break;
    case 'deces_annee': html += renderDecesAnnee(naissance, data); break;
    case 'futur':       html += renderFutur(naissance, data);      break;
    case 'futur_annee': html += renderFuturAnnee(naissance, data); break;
    default:
      html += `<p>Mode inconnu : ${mode}</p>`;
  }
  return html;
}

const MODE_LABELS = {
  vivant:      'Aujourd\'hui',
  deces:       'Décès',
  deces_annee: 'Décès (année)',
  futur:       'Date future',
  futur_annee: 'Date future (année)',
};

function calcAge(naissanceIso, age) {
  const [y, m, d] = naissanceIso.split('-').map(Number);
  const annee = y + age;
  // Vérifier si l'anniversaire exact tombe le 29/02 et si annee n'est pas bissextile
  const estFev29 = m === 2 && d === 29;
  const bissextile = annee % 4 === 0 && (annee % 100 !== 0 || annee % 400 === 0);
  const annivIso = estFev29 && !bissextile
    ? `${annee}-03-01`
    : `${annee}-${String(m).padStart(2,'0')}-${String(d).padStart(2,'0')}`;
  return { age, annee, annivIso, noteNonBissextile: estFev29 && !bissextile };
}

function renderAge(ageResult) {
  const { age, annee, annivIso, noteNonBissextile } = ageResult;
  let html = `<div class="info-cards">`;
  html += card('Âge demandé', `${age} ans`);
  html += card('Année', `${annee}`);
  html += card(
    `Anniversaire des ${age} ans`,
    formatDateFr(annivIso) + (noteNonBissextile ? noteBiss(true) : '')
  );
  html += `</div>`;
  return html;
}

function renderAllResults(payloads, ageResult = null) {
  const naissance = payloads[0].naissance;
  const multiSection = payloads.length > 1 || ageResult !== null;

  let html = `<div class="result-header">
    <div class="result-naissance">🎂 Date de naissance : ${formatDateFr(naissance)}</div>
  </div>`;

  for (const payload of payloads) {
    if (multiSection) {
      html += `<div class="result-section-title">${MODE_LABELS[payload.mode] ?? payload.mode}</div>`;
    }
    html += renderOneResult(payload);
  }

  if (ageResult !== null) {
    if (multiSection) {
      html += `<div class="result-section-title">Âge</div>`;
    }
    html += renderAge(ageResult);
  }

  resultEl.innerHTML = html;
  resultEl.classList.remove('hidden');
}
