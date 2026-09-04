/* ============================================================
   CENTRO ATLÉTICO LITO — comportamiento del sitio
   ============================================================ */

/* Origen de datos.
   Vacío = los JSON estáticos de /data (GitHub Pages).
   Cuando el Worker de Cloudflare esté publicado, poner acá su base
   (por ejemplo '/api') y el sitio pasa a datos en vivo sin tocar el HTML. */
const ORIGEN_VIVO = '';

const RUTAS = {
  tabla:    ORIGEN_VIVO ? ORIGEN_VIVO + '/tabla'    : 'data/tabla.json',
  partidos: ORIGEN_VIVO ? ORIGEN_VIVO + '/partidos' : 'data/partidos.json',
  plantel:  'data/plantel.json',
  noticias: 'data/noticias.json'
};

const CLUB = 'Lito';
const MESES = ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'set', 'oct', 'nov', 'dic'];
const DIAS = ['domingo', 'lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado'];

function leerFecha(iso) {
  const [a, m, d] = String(iso).split('-').map(Number);
  return new Date(a, m - 1, d);
}

function fechaCorta(iso) {
  const f = leerFecha(iso);
  return `${String(f.getDate()).padStart(2, '0')} ${MESES[f.getMonth()]} ${f.getFullYear()}`;
}

function fechaLarga(iso) {
  const f = leerFecha(iso);
  return `${DIAS[f.getDay()]} ${f.getDate()} de ${MESES[f.getMonth()]}`;
}

function esc(t) {
  return String(t == null ? '' : t).replace(/[&<>"']/g, c => (
    { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]
  ));
}

async function traer(ruta) {
  const r = await fetch(ruta, { cache: 'no-store' });
  if (!r.ok) throw new Error('No se pudo leer ' + ruta);
  return r.json();
}

function falla(destino, que) {
  destino.innerHTML = `<p class="error-datos">No se pudieron cargar ${esc(que)}. Recargá la página.</p>`;
}

/* ---------- Menú ---------- */

function menu() {
  const boton = document.querySelector('.menu-boton');
  const lista = document.querySelector('.menu');
  if (!boton || !lista) return;
  boton.addEventListener('click', () => {
    const abierto = lista.classList.toggle('abierto');
    boton.setAttribute('aria-expanded', String(abierto));
  });
}

/* ---------- La tapa del libro ----------
   Por defecto el libro está abierto: así se lee sin JS y con
   prefers-reduced-motion. Con JS y movimiento permitido, el libro aparece
   cerrado y perfilado cada vez que se entra a la portada. */
function libro() {
  const tomo = document.querySelector('[data-libro]');
  if (!tomo) return;

  const escena = tomo.closest('.escena');
  const camara = escena && escena.querySelector('[data-camara]');
  const quieto = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!quieto) {
    tomo.classList.add('cerrado');
    if (escena) escena.classList.add('lejos');
    if (camara) camara.classList.add('lejos');
  }

  const tapa = tomo.querySelector('.tapa');
  const apagarTapa = () => {
    if (!tapa) return;
    tapa.setAttribute('aria-hidden', 'true');
    tapa.tabIndex = -1;
  };

  const abrir = () => {
    if (!tomo.classList.contains('cerrado')) return;
    tomo.classList.remove('cerrado');
    if (escena) escena.classList.remove('lejos');
    if (camara) camara.classList.remove('lejos');
    apagarTapa();
    const primero = tomo.querySelector('.indice a');
    if (primero) setTimeout(() => primero.focus({ preventScroll: true }), 2600);
  };

  tomo.querySelectorAll('[data-abrir]').forEach(b => b.addEventListener('click', abrir));
  if (!tomo.classList.contains('cerrado')) apagarTapa();
}

/* ---------- Aviso de datos de ejemplo ---------- */

function avisoEjemplo(d) {
  if (!d.ejemplo) return;
  document.querySelectorAll('[data-aviso-ejemplo]').forEach(n => { n.hidden = false; });
}

/* ---------- Próximo partido y resultados ---------- */

function tarjetaPartido(p, claseExtra) {
  const marcador = p.golesLocal != null
    ? `<span class="partido-marcador">${p.golesLocal}–${p.golesVisitante}</span>`
    : '<span class="partido-vs">VS</span>';
  const pie = [
    p.hora ? `${fechaLarga(p.fecha)} · ${p.hora}` : fechaLarga(p.fecha),
    p.cancha || '',
    p.detalle || ''
  ].filter(Boolean).join(' · ');

  return `<article class="partido ${claseExtra || ''}">
      <p class="competencia">${esc(p.competencia || '')}</p>
      <div class="partido-equipos">
        <span class="partido-equipo">${esc(p.local)}</span>
        ${marcador}
        <span class="partido-equipo der">${esc(p.visitante)}</span>
      </div>
      <p class="partido-pie">${esc(pie)}</p>
    </article>`;
}

async function partidos() {
  const destinos = document.querySelectorAll('[data-partidos]');
  if (!destinos.length) return;
  let d;
  try {
    d = await traer(RUTAS.partidos);
  } catch (e) {
    destinos.forEach(x => falla(x, 'los partidos'));
    return;
  }

  avisoEjemplo(d);

  destinos.forEach(destino => {
    const modo = destino.dataset.partidos;

    if (modo === 'proximo') {
      const p = d.proximos && d.proximos[0];
      destino.innerHTML = p
        ? tarjetaPartido(p)
        : '<p class="cargando">Sin partidos programados.</p>';
      return;
    }

    if (modo === 'ultimo') {
      destino.innerHTML = d.ultimo
        ? tarjetaPartido(d.ultimo, 'partido--hueso')
        : '<p class="cargando">Sin resultados cargados.</p>';
      return;
    }

    if (modo === 'proximos') {
      destino.innerHTML = (d.proximos || []).map(p => `
        <article class="fila-partido ${p.condicion === 'local' ? 'local' : ''}">
          <p class="fecha">${esc(fechaCorta(p.fecha))}<br>${esc(p.hora || 'a confirmar')}</p>
          <p class="cruce">${esc(p.local)} <span class="partido-vs">vs</span> ${esc(p.visitante)}</p>
          <p class="dato">${esc(p.competencia || '')}<br>${esc(p.cancha || '')}</p>
        </article>`).join('') || '<p class="cargando">Sin partidos programados.</p>';
      return;
    }

    if (modo === 'resultados') {
      destino.innerHTML = (d.resultados || []).map(p => {
        const nuestro = p.local === CLUB ? p.golesLocal - p.golesVisitante : p.golesVisitante - p.golesLocal;
        const signo = nuestro > 0 ? 'G' : nuestro === 0 ? 'E' : 'P';
        return `<article class="fila-partido">
          <p class="fecha">${esc(fechaCorta(p.fecha))}<br>${esc(p.competencia || '')}</p>
          <p class="cruce">${esc(p.local)} <span class="partido-vs">${p.golesLocal}–${p.golesVisitante}</span> ${esc(p.visitante)}</p>
          <p class="dato"><span class="forma"><i class="${signo}">${signo}</i></span></p>
        </article>`;
      }).join('') || '<p class="cargando">Sin resultados cargados.</p>';
    }
  });
}

/* ---------- Tabla de posiciones ---------- */

function filaTabla(e, resumida) {
  const forma = (e.forma || []).map(r =>
    `<i class="${r}" title="${r === 'G' ? 'Ganó' : r === 'E' ? 'Empató' : 'Perdió'}">${r}</i>`).join('');
  const largas = resumida ? '' :
    `<td>${e.g}</td><td>${e.e}</td><td>${e.p}</td><td>${e.gf}</td><td>${e.gc}</td>`;

  return `<tr class="${e.esNosotros ? 'fila-nuestra' : ''}">
      <td>${e.pos}</td>
      <td>${esc(e.equipo)}</td>
      <td>${e.pj}</td>${largas}
      <td>${e.dg > 0 ? '+' : ''}${e.dg}</td>
      <td class="pts">${e.pts}</td>
      ${resumida ? '' : `<td><span class="forma">${forma}</span></td>`}
    </tr>`;
}

async function tabla() {
  const destinos = document.querySelectorAll('[data-tabla]');
  if (!destinos.length) return;

  let d;
  try {
    d = await traer(RUTAS.tabla);
  } catch (e) {
    destinos.forEach(x => falla(x, 'las posiciones'));
    return;
  }

  avisoEjemplo(d);

  destinos.forEach(destino => pintarTabla(destino, d));
}

function pintarTabla(destino, d) {
  const resumida = destino.dataset.tabla === 'resumida';

  const encabezados = resumida
    ? ['#', 'Equipo', 'PJ', 'DG', 'Pts']
    : ['#', 'Equipo', 'PJ', 'G', 'E', 'P', 'GF', 'GC', 'DG', 'Pts', 'Últimos 5'];

  const equipos = resumida
    ? d.equipos.slice(0, 6)
    : d.equipos;

  destino.innerHTML = `
    <div class="tabla-envoltorio">
      <table class="posiciones">
        <caption class="sr-only">Posiciones del ${esc(d.torneo)}</caption>
        <thead><tr>${encabezados.map(h => `<th scope="col">${h}</th>`).join('')}</tr></thead>
        <tbody>${equipos.map(e => filaTabla(e, resumida)).join('')}</tbody>
      </table>
    </div>
    <p class="aviso-formulario" style="margin-top:12px">${esc(d.torneo)} · fecha ${d.fecha_jugada} · actualizado ${esc(fechaCorta(d.actualizado))} · fuente ${esc(d.fuente || 'AUF')}</p>`;
}

/* ---------- Plantel ---------- */

async function plantel() {
  const destino = document.querySelector('[data-plantel]');
  if (!destino) return;

  let d;
  try {
    d = await traer(RUTAS.plantel);
  } catch (e) {
    falla(destino, 'el plantel');
    return;
  }

  const puestos = ['Arqueros', 'Defensas', 'Mediocampistas', 'Delanteros'];
  destino.innerHTML = puestos.map(puesto => {
    const grupo = d.jugadores.filter(j => j.puesto === puesto);
    if (!grupo.length) return '';
    return `<section class="grupo-plantel">
        <p class="cintilla">${esc(puesto)}</p>
        <div class="rejilla rejilla--3">
          ${grupo.map(j => `
            <article class="jugador ${j.nombre ? '' : 'jugador--vacante'}">
              <span class="numero">${j.numero != null ? j.numero : '—'}</span>
              <span>
                <span class="nombre">${esc(j.nombre || 'A confirmar')}</span><br>
                <span class="detalle">${esc(j.nacimiento || 'Ficha pendiente')}</span>
              </span>
            </article>`).join('')}
        </div>
      </section>`;
  }).join('');

  const ct = document.querySelector('[data-cuerpo-tecnico]');
  if (ct) {
    ct.innerHTML = d.cuerpoTecnico.map(m => `
      <div><dt>${esc(m.rol)}</dt><dd>${esc(m.nombre || 'A confirmar')}</dd></div>`).join('');
  }
}

/* ---------- Noticias ---------- */

async function noticias() {
  const destinos = document.querySelectorAll('[data-noticias]');
  if (!destinos.length) return;

  let d;
  try {
    d = await traer(RUTAS.noticias);
  } catch (e) {
    destinos.forEach(x => falla(x, 'las noticias'));
    return;
  }

  avisoEjemplo(d);

  destinos.forEach(destino => pintarNoticias(destino, d));
}

function pintarNoticias(destino, d) {
  const limite = Number(destino.dataset.noticias) || 0;
  const notas = limite ? d.notas.slice(0, limite) : d.notas;
  destino.innerHTML = notas.map(n => `
    <article class="noticia">
      <img src="${esc(n.imagen)}" alt="" loading="lazy" width="1000" height="640">
      <div class="noticia-cuerpo">
        <p class="fecha">${esc(fechaCorta(n.fecha))}</p>
        <h3>${n.enlace ? `<a href="${esc(n.enlace)}">${esc(n.titulo)}</a>` : esc(n.titulo)}</h3>
        <p>${esc(n.bajada)}</p>
        <p class="etiqueta">${esc(n.etiqueta || 'Club')}</p>
      </div>
    </article>`).join('');
}

/* ---------- Formularios (sin backend todavía) ---------- */

function formularios() {
  document.querySelectorAll('form[data-sin-backend]').forEach(f => {
    f.addEventListener('submit', ev => {
      ev.preventDefault();
      const aviso = f.querySelector('[data-respuesta]');
      if (aviso) {
        aviso.hidden = false;
        aviso.textContent = 'El formulario todavía no está conectado. Escribinos a ' + (f.dataset.sinBackend || 'info@calito.uy') + '.';
      }
    });
  });
}

/* ---------- Año en el pie ---------- */

function anio() {
  document.querySelectorAll('[data-anio]').forEach(n => { n.textContent = new Date().getFullYear(); });
}

libro();
menu();
anio();
formularios();
partidos();
tabla();
plantel();
noticias();
