# -*- coding: utf-8 -*-
"""Genera "el libro del club": el sitio del Centro Atlético Lito.

Uso: python3 build.py

La portada es la tapa de un tomo encuadernado; cada sección del sitio es un
capítulo de ese libro. Cabecera, colofón y metadatos se comparten desde acá:
para cambiar cualquier texto institucional hay que editar este archivo y volver
a correrlo, no los HTML sueltos, porque el script los sobreescribe.
"""
import os

SITIO = "Centro Atlético Lito"
DOMINIO = "calito.uy"
BASE = os.path.dirname(os.path.abspath(__file__))

# Mientras el contenido no esté aprobado por el club, las páginas van con
# noindex. Poner en False y regenerar antes de publicar.
NOINDEX = True

# Los capítulos del libro, en orden de lectura.
CAPITULOS = [
    ("club.html", "El club", "I", "Del Café Lito a la cancha"),
    ("plantel.html", "Plantel", "II", "Primer equipo y formativas"),
    ("fixture.html", "Fixture y tabla", "III", "Domingo a domingo"),
    ("noticias.html", "Noticias", "IV", "Partes de prensa"),
    ("socios.html", "Hacete socio", "V", "Cuotas y alta"),
    ("contacto.html", "Contacto", "VI", "Sede, prensa y marca"),
]


def encabezado_html(titulo, descripcion):
    robots = '<meta name="robots" content="noindex, nofollow">\n' if NOINDEX else ""
    return f"""<!DOCTYPE html>
<html lang="es-UY">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo} · {SITIO}</title>
<meta name="description" content="{descripcion}">
{robots}<meta property="og:title" content="{titulo} · {SITIO}">
<meta property="og:description" content="{descripcion}">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_UY">
<meta property="og:image" content="assets/img/og.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0F1A40">
<link rel="icon" href="assets/img/favicon.png">
<link rel="apple-touch-icon" href="assets/img/escudo-180.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@300;400;500;600;700&family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Pinyon+Script&family=Manrope:wght@400;500;600;700&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/main.css">
</head>
<body>
<a class="saltar" href="#contenido">Ir al contenido</a>
"""


def cabecera_hoja(actual):
    """Cornisa de las páginas interiores: escudo chico y los capítulos."""
    enlaces = '        <a href="index.html">Portada</a>\n'
    enlaces += "\n".join(
        '        <a href="{h}"{a}>{t}</a>'.format(
            h=h, t=t, a=' aria-current="page"' if h == actual else ""
        )
        for h, t, _, _ in CAPITULOS
    )
    return f"""
<header class="cabecera">
  <div class="marco cabecera-fila">
    <a class="marca" href="index.html">
      <img src="assets/img/escudo.png" alt="" width="720" height="879">
      <span class="marca-texto">Centro Atlético Lito
        <small>Montevideo · 1917</small>
      </span>
    </a>
    <button class="menu-boton" aria-expanded="false" aria-controls="menu-principal">Capítulos</button>
    <nav class="menu" id="menu-principal" aria-label="Capítulos del libro">
{enlaces}
    </nav>
  </div>
</header>

<main id="contenido" class="hoja">
"""


def portadilla(romano, titulo, bajada):
    return f"""<section class="portadilla">
  <div class="marco">
    <p class="romano-grande">Capítulo {romano}</p>
    <h1>{titulo}</h1>
    <p class="plomo">{bajada}</p>
    <div class="filete-cap"></div>
  </div>
</section>
"""


def folio(romano, titulo):
    return f"""<p class="folio"><i></i> {romano} · {titulo} · Centro Atlético Lito <i></i></p>
"""


def colofon():
    enlaces_capitulos = "\n".join(
        f'          <li><a href="{h}">{t}</a></li>' for h, t, _, _ in CAPITULOS[:4]
    )
    return f"""</main>

<footer class="pie">
  <div class="marco">
    <div class="pie-grilla">
      <div class="pie-escudo">
        <img src="assets/img/escudo.png" alt="" width="720" height="879" loading="lazy">
        <div>
          <strong>Centro Atlético Lito</strong><br>
          Arroyo Seco, Montevideo, Uruguay.<br>
          Fundado el 24 de julio de 1917.<br>
          Primera División Amateur · AUF.
        </div>
      </div>
      <div>
        <h4>Capítulos</h4>
        <ul>
{enlaces_capitulos}
        </ul>
      </div>
      <div>
        <h4>Hinchada</h4>
        <ul>
          <li><a href="socios.html">Hacete socio</a></li>
          <li><a href="socios.html#cuotas">Cuotas</a></li>
          <li><a href="contacto.html">Contacto</a></li>
          <li><a href="contacto.html#prensa">Prensa y marca</a></li>
        </ul>
      </div>
      <div>
        <h4>Seguinos</h4>
        <ul>
          <li><a href="https://instagram.com/calito.uy" rel="noopener">Instagram</a></li>
          <li><a href="https://x.com/calito_uy" rel="noopener">X</a></li>
          <li><a href="https://facebook.com/calito.uy" rel="noopener">Facebook</a></li>
          <li><a href="mailto:marca@{DOMINIO}">marca@{DOMINIO}</a></li>
        </ul>
      </div>
    </div>
    <div class="pie-legal">
      <span>© <span data-anio>2026</span> Centro Atlético Lito · {DOMINIO}</span>
      <span>Identidad visual según Manual de Marca, edición 2026</span>
    </div>
  </div>
</footer>

<script src="assets/js/main.js"></script>
</body>
</html>
"""


AVISO_EJEMPLO = """      <p class="nota" data-aviso-ejemplo hidden>
        Datos de ejemplo. Cargar la información oficial antes de publicar el sitio.
      </p>
"""


# ============================================================
# Portada: la tapa del libro
# ============================================================

def pagina_portada():
    indice = "\n".join(f"""        <li>
          <a href="{h}">
            <span class="romano">{r}</span>
            <span class="titulo">{t}</span>
            <span class="apunte">{a}</span>
          </a>
        </li>""" for h, t, r, a in CAPITULOS)

    return f"""
<div class="escena" data-escena>
  <button class="abrir-libro" type="button" data-abrir>Abrir el libro del club</button>
  <div class="camara" data-camara>
    <div class="tablero"></div>
    <div class="mesa">
      <div class="sombra"></div>
      <div class="libro" data-libro>

      <span class="cara-lomo" aria-hidden="true"></span>
      <span class="cara-cabeza" aria-hidden="true"></span>
      <span class="cara-canto" aria-hidden="true"></span>
      <div class="contratapa" aria-hidden="true"></div>

    <div class="hoja-indice">
      <h1>El libro del club</h1>
      <p class="sello">Centro Atlético Lito · Montevideo · 1917</p>
      <div class="regla"></div>
      <ul class="indice">
{indice}
      </ul>
      <p class="indice-pie">
        <span>Tomo del club · 2026</span>
        <a href="socios.html">Hacete socio</a>
      </p>
      <div class="marcas">
        <img src="assets/img/marcas/auf.png" alt="Asociación Uruguaya de Fútbol" width="111" height="180" loading="lazy">
        <img src="assets/img/marcas/mgr.png" alt="MGR Sport" width="342" height="110" loading="lazy">
        <img src="assets/img/marcas/enas.png" alt="ENAS" width="509" height="100" loading="lazy">
        <img src="assets/img/marcas/pinuccio.png" alt="Pinuccio Trattoria" width="279" height="130" loading="lazy">
      </div>
    </div>

    <div class="tapa">
      <span class="cara cara-frente" aria-hidden="true">
        <span class="grabado-arriba">Centro Atlético</span>
        <img class="escudo-tapa" src="assets/img/escudo-tapa.png" alt="Escudo del Centro Atlético Lito" width="760" height="911" fetchpriority="high">
        <span class="lema">Garra y Corazón</span>
        <span class="grabado-abajo">Montevideo · 1917</span>
      </span>
      <span class="cara cara-dorso">
        <div class="cancion">
          <p class="cancion-rotulo">Canción oficial</p>
          <div class="cancion-letra">
            <p><span class="inicial">L</span>ito querido,<br>
              cuadro invencible,<br>
              fuerte, aguerrido e irresistible.</p>
            <p>Siempre Centro Lito adelante,<br>
              triunfante, triunfante,<br>
              porque tiene garra y corazón,<br>
              campeón, campeón.</p>
            <p>Que proclaman tus parciales,<br>
              que son inmortales,<br>
              tu gloria y honor.</p>
          </div>
          <p class="cancion-pie">Centro Atlético Lito · Montevideo · 1917</p>
        </div>
      </span>
    </div>

    <div class="hoja-vuelta" aria-hidden="true"></div>

      </div>
    </div>
  </div>

  </div>
</div>
"""


# ============================================================
# Capítulos
# ============================================================

def cap_club():
    return portadilla("I", "El club", "Nacimos el 24 de julio de 1917 en un café de Arroyo Seco. Más de un siglo después seguimos siendo del barrio.") + """
<section class="seccion">
  <div class="marco">
    <div class="rejilla rejilla--2">
      <div class="prosa">
        <p class="cintilla">Historia</p>
        <h2>De la vereda a la cancha</h2>
        <p class="capitular">El nombre salió del mostrador. Manuel Semino era «Lito» para todo el barrio, y su café, en Agraciada y Santa Fe, era el punto de encuentro de Arroyo Seco. Cuando el 24 de julio de 1917 los que paraban ahí decidieron fundar el club, le pusieron el nombre del café.</p>
        <p>La primera camiseta fue azul eléctrico con vivos rojos y pantalón blanco, con el escudo sobre el pecho izquierdo. De ahí viene el apodo: la azulgrana de Arroyo Seco. La de hoy sigue esa línea: azul francia, cuello rojo y vivo rojo en las mangas.</p>
        <p>Afiliado a la AUF, ganó la Divisional Extra en 1919 y la Intermedia en 1920. Dos ascensos al hilo lo dejaron en el Campeonato Uruguayo de 1921, y ahí se mantuvo hasta 1928. Sus mejores temporadas fueron 1922 y 1923: quinto puesto.</p>
        <p>Por esta camiseta pasaron José Nasazzi y Héctor «el Manco» Castro, que debutaron en Lito, y también Pedro Cea. Los tres estuvieron después en las conquistas grandes de Uruguay, la del Mundial de 1930 incluida.</p>
        <p>Durante el cisma del fútbol uruguayo, Lito fue uno de los tres clubes que presentaron dos equipos en las competencias paralelas. Al de la AUF le decían el <em>Lito redondo</em>; al de la Federación, el <em>Lito cuadrado</em>. La diferencia estaba en la forma del escudo de cada camiseta.</p>
        <p>Cuando el fútbol se profesionalizó en 1932, el club siguió amateur y jugó en el ascenso hasta desaparecer de la competencia oficial cerca de 1947. Desde 1952 volvió a jugar en la Federación Uruguaya de Fútbol Amateur, impulsado por los hijos de Vicente Cappuccio: dos campeonatos y dos subcampeonatos. Dejó de competir en 1960.</p>
        <p>En 2022, impulsado por Rodolfo Neme, Lito volvió a las competencias oficiales de la AUF, setenta y cinco años después, en la Divisional D. En 2023 salió campeón —2 a 0 a Rincón de Carrasco en la final— y subió a la Primera División Amateur.</p>
      </div>
      <div>
        <figure class="foto-album" style="margin:0">
          <img src="assets/img/fotos/sede.jpg" alt="Sede y cancha del Centro Atlético Lito" width="1200" height="800" loading="lazy">
        </figure>
        <p class="epigrafe">Reemplazar por una foto real de la sede o la cancha.</p>
      </div>
    </div>

    <ul class="cronologia" style="margin-top:44px">
      <li><b>1917</b><span><strong>Fundación.</strong> El 24 de julio, en el Café Lito de Agraciada y Santa Fe.</span></li>
      <li><b>1919</b><span><strong>Divisional Extra.</strong> Primer título y primer ascenso.</span></li>
      <li><b>1920</b><span><strong>Divisional Intermedia.</strong> Segundo título al hilo y salto a Primera.</span></li>
      <li><b>1921</b><span><strong>Primera División.</strong> Debut en el Campeonato Uruguayo; se mantiene hasta 1928. Quinto en 1922 y en 1923.</span></li>
      <li><b>1932</b><span><strong>Llega el profesionalismo.</strong> Lito sigue amateur y juega en el ascenso.</span></li>
      <li><b>1947</b><span><strong>Se apaga.</strong> Desaparece de la competencia oficial.</span></li>
      <li><b>1952</b><span><strong>La Federación.</strong> Vuelve al amateurismo: dos campeonatos y dos subcampeonatos hasta 1960.</span></li>
      <li><b>2022</b><span><strong>El regreso.</strong> Setenta y cinco años después, de vuelta en la AUF, en la Divisional D.</span></li>
      <li><b>2023</b><span><strong>Campeón.</strong> Final ganada 2 a 0 y ascenso a la Primera División Amateur.</span></li>
    </ul>
  </div>
</section>

<section class="lamina">
  <div class="marco claro">
    <p class="cintilla">Sede y cancha</p>
    <h2>Dónde late el club</h2>
    <dl class="datos">
      <div><dt>Barrio</dt><dd>Arroyo Seco, Montevideo</dd></div>
      <div><dt>Apodo</dt><dd>La azulgrana de Arroyo Seco</dd></div>
      <div><dt>Fundación</dt><dd>24 de julio de 1917</dd></div>
      <div><dt>Categoría</dt><dd>Primera División Amateur</dd></div>
      <div><dt>Afiliación</dt><dd>Asociación Uruguaya de Fútbol (AUF)</dd></div>
      <div><dt>Dirección</dt><dd>A confirmar</dd></div>
      <div><dt>Cancha</dt><dd>A confirmar</dd></div>
    </dl>
  </div>
</section>

<section class="seccion">
  <div class="marco">
    <div class="rejilla rejilla--2">
      <div>
        <p class="cintilla">Palmarés</p>
        <h2>Lo ganado</h2>
        <ul class="cronologia">
          <li><b>2023</b><span><strong>Divisional D.</strong> Campeón.</span></li>
          <li><b>2022</b><span><strong>Divisional D.</strong> Campeón de la fase regular.</span></li>
          <li><b>1920</b><span><strong>Divisional Intermedia.</strong> Campeón.</span></li>
          <li><b>1919</b><span><strong>Divisional Extra.</strong> Campeón.</span></li>
        </ul>
        <p class="aviso-formulario" style="margin-top:14px">Más dos campeonatos y dos subcampeonatos de Primera División Amateur en la Federación, entre 1952 y 1960.</p>
      </div>
      <div>
        <p class="cintilla">En números</p>
        <h2>El paso por las divisionales</h2>
        <dl class="datos">
          <div><dt>Primera División</dt><dd>6 temporadas · 1921 a 1928</dd></div>
          <div><dt>Segunda División</dt><dd>12 temporadas · 1920 y 1929 a 1941</dd></div>
          <div><dt>Tercera División</dt><dd>8 temporadas · 1918-1919, 1942-1945 y desde 2024</dd></div>
          <div><dt>Cuarta División</dt><dd>3 temporadas · 1946 y 2022-2023</dd></div>
          <div><dt>Mejor puesto en Primera</dt><dd>Quinto, en 1922 y en 1923</dd></div>
          <div><dt>Registro en Primera</dt><dd>168 partidos: 53 ganados, 50 empatados, 65 perdidos</dd></div>
        </dl>
      </div>
    </div>
  </div>
</section>

<section class="seccion">
  <div class="marco">
    <p class="cintilla">Indumentaria</p>
    <h2>La camiseta es el escudo en movimiento</h2>
    <p class="prosa" style="margin-bottom:0">El conjunto oficial de local: camiseta azul francia con cuello rojo y vivo rojo en las mangas, y pantalón blanco con vivo rojo en el ruedo.</p>
    <div class="rejilla rejilla--3" style="margin-top:26px">
      <article class="camiseta">
        <div class="muestra" style="background:#1b3fa8"><i style="background:linear-gradient(180deg,var(--rojo) 0 7%,transparent 7% 26%,var(--rojo) 26% 30%,transparent 30%)"></i></div>
        <div class="rotulo"><h4>Camiseta</h4><p class="detalle">Azul francia · cuello y mangas con vivo rojo</p></div>
      </article>
      <article class="camiseta">
        <div class="muestra" style="background:var(--hueso)"><i style="background:linear-gradient(180deg,transparent 0 84%,var(--rojo) 84% 88%,transparent 88%)"></i></div>
        <div class="rotulo"><h4>Pantalón</h4><p class="detalle">Blanco · vivo rojo en el ruedo</p></div>
      </article>
      <article class="camiseta">
        <div class="muestra" style="background:linear-gradient(180deg,#1b3fa8 0 58%,var(--hueso) 58%)"><i style="background:linear-gradient(180deg,var(--rojo) 0 5%,transparent 5% 16%,var(--rojo) 16% 19%,transparent 19% 92%,var(--rojo) 92% 96%,transparent 96%)"></i></div>
        <div class="rotulo"><h4>Conjunto de local</h4><p class="detalle">El oficial · suplente y arquero a confirmar</p></div>
      </article>
    </div>
  </div>
</section>

<section class="seccion">
  <div class="marco">
    <div class="rejilla rejilla--2">
      <div>
        <p class="cintilla">Institucional</p>
        <h2>Comisión directiva</h2>
        <p class="prosa">La comisión se renueva en asamblea de socios. Cargar la nómina vigente y la fecha de la última asamblea.</p>
        <dl class="datos">
          <div><dt>Presidencia</dt><dd>Rodolfo Neme</dd></div>
          <div><dt>Vicepresidencia</dt><dd>A confirmar</dd></div>
          <div><dt>Secretaría</dt><dd>A confirmar</dd></div>
          <div><dt>Tesorería</dt><dd>A confirmar</dd></div>
          <div><dt>Vocales</dt><dd>A confirmar</dd></div>
        </dl>
      </div>
      <div>
        <p class="cintilla">Identidad</p>
        <h2>El escudo es la firma del club</h2>
        <p class="prosa">Blasón de cuarteles en rojo y azul, con las iniciales del club, la pelota al centro y el año de fundación al pie, todo dentro de un borde dorado. El azul y el rojo vienen de la primera camiseta, la de 1917.</p>
        <div class="rejilla rejilla--4" style="margin-top:18px">
          <div style="background:var(--azul);color:var(--hueso);padding:14px"><span class="mono">Azul Lito</span><br><span class="mono" style="color:var(--oro)">#1C2C6B</span></div>
          <div style="background:var(--rojo);color:var(--hueso);padding:14px"><span class="mono">Rojo Lito</span><br><span class="mono">#D12C3E</span></div>
          <div style="background:var(--oro);color:var(--tinta);padding:14px"><span class="mono">Oro Lito</span><br><span class="mono">#D4A85A</span></div>
          <div style="background:var(--hueso-80);color:var(--tinta);padding:14px"><span class="mono">Hueso</span><br><span class="mono">#F4EFE6</span></div>
        </div>
        <p class="aviso-formulario" style="margin-top:14px">Uso de marca y archivos vectoriales: <a href="mailto:marca@calito.uy">marca@calito.uy</a></p>
      </div>
    </div>
  </div>
</section>
""" + folio("I", "El club")


def cap_plantel():
    return portadilla("II", "Plantel", "Primer equipo del Centro Atlético Lito, temporada 2026. Los puestos sin nombre están a confirmar.") + """
<section class="seccion">
  <div class="marco">
    <div data-plantel><p class="cargando">Cargando plantel…</p></div>
  </div>
</section>

<section class="lamina">
  <div class="marco claro">
    <div class="rejilla rejilla--2">
      <div>
        <p class="cintilla">Cuerpo técnico</p>
        <h2>Quién dirige</h2>
        <dl class="datos" data-cuerpo-tecnico><div><dt>Cargando…</dt><dd></dd></div></dl>
      </div>
      <div>
        <figure class="foto-album" style="margin:0;background:rgba(244,239,230,.1)">
          <img src="assets/img/fotos/plantel.jpg" alt="Plantel del Centro Atlético Lito" width="1200" height="800" loading="lazy">
        </figure>
      </div>
    </div>
  </div>
</section>

<section class="seccion">
  <div class="marco">
    <p class="cintilla">Formativas</p>
    <h2>Las divisiones del club</h2>
    <p class="prosa">Lito trabaja con categorías juveniles todo el año. Para sumarse hay que escribir al club con nombre, edad y categoría.</p>
    <div class="rejilla rejilla--3" style="margin-top:26px">
      <article class="tarjeta tarjeta--borde-oro"><h3>Juveniles</h3><p>Categorías y horarios a confirmar.</p></article>
      <article class="tarjeta tarjeta--borde-oro"><h3>Baby fútbol</h3><p>Categorías y horarios a confirmar.</p></article>
      <article class="tarjeta tarjeta--borde-oro"><h3>Pruebas de jugadores</h3><p>Fechas a confirmar. Consultas por <a href="contacto.html">contacto</a>.</p></article>
    </div>
  </div>
</section>
""" + folio("II", "Plantel")


def cap_fixture():
    return portadilla("III", "Fixture y tabla", "Partidos, resultados y posiciones. Se actualiza después de cada fecha.") + """
<section class="seccion">
  <div class="marco">
""" + AVISO_EJEMPLO + """    <p class="cintilla" style="margin-top:26px">Próximo partido</p>
    <div class="rejilla rejilla--2">
      <div data-partidos="proximo"><p class="cargando">Cargando…</p></div>
      <div data-partidos="ultimo"><p class="cargando">Cargando…</p></div>
    </div>
  </div>
</section>

<section class="seccion">
  <div class="marco">
    <p class="cintilla">Próximas fechas</p>
    <div class="lista-partidos" data-partidos="proximos"><p class="cargando">Cargando…</p></div>
  </div>
</section>

<section class="seccion">
  <div class="marco">
    <p class="cintilla">Resultados</p>
    <h2>Últimos partidos</h2>
    <div class="lista-partidos" data-partidos="resultados" style="margin-top:22px"><p class="cargando">Cargando…</p></div>
  </div>
</section>

<section class="seccion" id="tabla">
  <div class="marco">
    <p class="cintilla">Posiciones</p>
    <h2>Tabla</h2>
    <div data-tabla="completa" style="margin-top:22px"><p class="cargando">Cargando…</p></div>
  </div>
</section>
""" + folio("III", "Fixture y tabla")


def cap_noticias():
    return portadilla("IV", "Noticias", "Partes de prensa, anuncios y novedades del club.") + """
<section class="seccion">
  <div class="marco">
""" + AVISO_EJEMPLO + """    <div class="rejilla rejilla--3" data-noticias="0" style="margin-top:26px"><p class="cargando">Cargando…</p></div>
  </div>
</section>

<section class="franja-cierre">
  <div class="marco">
    <div>
      <h2>¿Sos prensa?</h2>
      <p>Acreditaciones, fotos y uso de marca: marca@calito.uy</p>
    </div>
    <a class="boton boton--oro" href="contacto.html#prensa">Escribir al club</a>
  </div>
</section>
""" + folio("IV", "Noticias")


def cap_socios():
    return portadilla("V", "Hacete socio", "La cuota social paga la cancha, los viajes y las formativas. Ser socio de Lito es entrar a la cancha y tener voz en la asamblea.") + """
<section class="seccion" id="cuotas">
  <div class="marco">
    <p class="cintilla">Categorías</p>
    <h2>Cuotas</h2>
    <p class="aviso-formulario" style="margin:0 0 24px">Valores de referencia. Confirmar los importes vigentes con tesorería antes de publicar.</p>
    <div class="rejilla rejilla--3">
      <article class="tarjeta cuota">
        <h3>Adherente</h3>
        <p class="precio">$ 350<small>por mes · pesos uruguayos</small></p>
        <ul><li>Carné de socio</li><li>Entrada a partidos de local</li><li>Novedades por correo</li></ul>
      </article>
      <article class="tarjeta cuota cuota--destacada">
        <h3>Activo</h3>
        <p class="precio">$ 600<small>por mes · pesos uruguayos</small></p>
        <ul><li>Todo lo del adherente</li><li>Voz y voto en la asamblea</li><li>Descuento en indumentaria</li></ul>
      </article>
      <article class="tarjeta cuota">
        <h3>Vitalicio</h3>
        <p class="precio">$ 1.200<small>por mes · pesos uruguayos</small></p>
        <ul><li>Todo lo del activo</li><li>Invitación a actos institucionales</li><li>Reconocimiento en la sede</li></ul>
      </article>
    </div>
  </div>
</section>

<section class="seccion">
  <div class="marco">
    <div class="rejilla rejilla--2">
      <div>
        <p class="cintilla">Alta de socio</p>
        <h2>Sumate</h2>
        <p class="prosa">Completá el formulario y el club se comunica para cerrar el alta y la forma de pago.</p>
        <form class="formulario" data-sin-backend="marca@calito.uy">
          <div class="campo-doble">
            <div class="campo"><label for="nombre">Nombre y apellido</label><input id="nombre" name="nombre" type="text" autocomplete="name" required></div>
            <div class="campo"><label for="documento">Documento</label><input id="documento" name="documento" type="text" inputmode="numeric" required></div>
          </div>
          <div class="campo-doble">
            <div class="campo"><label for="correo">Correo</label><input id="correo" name="correo" type="email" autocomplete="email" required></div>
            <div class="campo"><label for="telefono">Teléfono</label><input id="telefono" name="telefono" type="tel" autocomplete="tel"></div>
          </div>
          <div class="campo">
            <label for="categoria">Categoría</label>
            <select id="categoria" name="categoria"><option>Adherente</option><option>Activo</option><option>Vitalicio</option></select>
          </div>
          <div class="campo"><label for="mensaje">Comentario</label><textarea id="mensaje" name="mensaje"></textarea></div>
          <button class="boton" type="submit">Enviar solicitud</button>
          <p class="aviso-formulario" data-respuesta hidden></p>
          <p class="aviso-formulario">Los datos se usan solo para gestionar el alta de socio.</p>
        </form>
      </div>
      <div>
        <figure class="foto-album" style="margin:0">
          <img src="assets/img/fotos/hinchada.jpg" alt="Hinchada del Centro Atlético Lito" width="1200" height="800" loading="lazy">
        </figure>
        <div class="nota" style="margin-top:20px">
          El formulario todavía no está conectado a un backend. Ver README para publicar el Worker de Cloudflare.
        </div>
      </div>
    </div>
  </div>
</section>
""" + folio("V", "Hacete socio")


def cap_contacto():
    return portadilla("VI", "Contacto", "Sede, prensa, formativas y uso de marca. Escribinos y te respondemos.") + """
<section class="seccion">
  <div class="marco">
    <div class="rejilla rejilla--2">
      <div>
        <p class="cintilla">Datos</p>
        <h2>Dónde encontrarnos</h2>
        <dl class="datos">
          <div><dt>Sede</dt><dd>Arroyo Seco, Montevideo, Uruguay<br><span class="mono">Dirección exacta a confirmar</span></dd></div>
          <div><dt>Correo</dt><dd><a href="mailto:marca@calito.uy">marca@calito.uy</a></dd></div>
          <div><dt>Teléfono</dt><dd>A confirmar</dd></div>
          <div><dt>Instagram</dt><dd><a href="https://instagram.com/calito.uy" rel="noopener">@calito.uy</a></dd></div>
          <div><dt>Horario de sede</dt><dd>A confirmar</dd></div>
        </dl>

        <div id="prensa" style="margin-top:36px">
          <p class="cintilla">Prensa y marca</p>
          <h3>Acreditaciones y archivos</h3>
          <p class="prosa">Para acreditaciones de prensa, fotos institucionales, archivos vectoriales del escudo o autorizaciones de uso de marca: <a href="mailto:marca@calito.uy">marca@calito.uy</a>.</p>
          <p class="aviso-formulario">El escudo no se estira, no se rota y no cambia de color fuera de paleta. Manual de marca, edición 2026.</p>
        </div>
      </div>
      <div>
        <p class="cintilla">Formulario</p>
        <h2>Escribinos</h2>
        <form class="formulario" data-sin-backend="marca@calito.uy">
          <div class="campo"><label for="c-nombre">Nombre</label><input id="c-nombre" name="nombre" type="text" autocomplete="name" required></div>
          <div class="campo"><label for="c-correo">Correo</label><input id="c-correo" name="correo" type="email" autocomplete="email" required></div>
          <div class="campo">
            <label for="c-motivo">Motivo</label>
            <select id="c-motivo" name="motivo"><option>Consulta general</option><option>Socios</option><option>Formativas</option><option>Prensa</option><option>Sponsors</option></select>
          </div>
          <div class="campo"><label for="c-mensaje">Mensaje</label><textarea id="c-mensaje" name="mensaje" required></textarea></div>
          <button class="boton" type="submit">Enviar</button>
          <p class="aviso-formulario" data-respuesta hidden></p>
        </form>
      </div>
    </div>
  </div>
</section>
""" + folio("VI", "Contacto")


CUERPOS = {
    "club.html": cap_club,
    "plantel.html": cap_plantel,
    "fixture.html": cap_fixture,
    "noticias.html": cap_noticias,
    "socios.html": cap_socios,
    "contacto.html": cap_contacto,
}

DESCRIPCIONES = {
    "club.html": "Historia, sede, camiseta y comisión directiva del Centro Atlético Lito, fundado en 1917 en Montevideo.",
    "plantel.html": "Plantel y cuerpo técnico del Centro Atlético Lito, temporada 2026.",
    "fixture.html": "Próximos partidos, resultados y tabla de posiciones del Centro Atlético Lito.",
    "noticias.html": "Noticias, partes de prensa y anuncios del Centro Atlético Lito.",
    "socios.html": "Categorías de socio, cuotas y alta en el Centro Atlético Lito.",
    "contacto.html": "Datos de contacto, prensa y uso de marca del Centro Atlético Lito.",
}


def main():
    # Portada: la tapa. Sin cornisa ni colofón, para no romper la ilusión.
    portada = (
        encabezado_html("El libro del club", "Sitio oficial del Centro Atlético Lito: historia, plantel, fixture, noticias y socios. Montevideo, desde 1917.")
        + pagina_portada()
        + '\n<script src="assets/js/main.js"></script>\n</body>\n</html>\n'
    )
    with open(os.path.join(BASE, "index.html"), "w", encoding="utf-8") as f:
        f.write(portada)
    print("escrito index.html")

    for archivo, titulo, _romano, _apunte in CAPITULOS:
        html = (
            encabezado_html(titulo, DESCRIPCIONES[archivo])
            + cabecera_hoja(archivo)
            + CUERPOS[archivo]()
            + colofon()
        )
        with open(os.path.join(BASE, archivo), "w", encoding="utf-8") as f:
            f.write(html)
        print("escrito", archivo)


if __name__ == "__main__":
    main()
