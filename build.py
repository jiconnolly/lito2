# -*- coding: utf-8 -*-
"""Genera las páginas del sitio del Centro Atlético Lito desde plantillas compartidas.

Uso: python3 build.py

Las siete páginas comparten cabecera, pie y metadatos. Para cambiar el menú, el
pie o cualquier texto institucional hay que editar este archivo y volver a
correrlo: el script sobreescribe los HTML sueltos.
"""
import os

SITIO = "Centro Atlético Lito"
DOMINIO = "calito.uy"
BASE = os.path.dirname(os.path.abspath(__file__))

# Mientras el contenido no esté aprobado por el club, las páginas van con
# noindex. Poner en False y regenerar antes de publicar.
NOINDEX = True

PAGINAS_MENU = [
    ("index.html", "Inicio"),
    ("club.html", "El club"),
    ("plantel.html", "Plantel"),
    ("fixture.html", "Fixture y tabla"),
    ("noticias.html", "Noticias"),
    ("socios.html", "Hacete socio"),
    ("contacto.html", "Contacto"),
]


def cabecera(actual, titulo, descripcion):
    enlaces = "\n".join(
        '        <a href="{h}"{a}>{t}</a>'.format(
            h=h, t=t, a=' aria-current="page"' if h == actual else ""
        )
        for h, t in PAGINAS_MENU
    )
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
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@300;400;500;600;700&family=Manrope:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/main.css">
</head>
<body>
<a class="saltar" href="#contenido">Ir al contenido</a>

<header class="cabecera">
  <div class="marco cabecera-fila">
    <a class="marca" href="index.html">
      <img src="assets/img/escudo.png" alt="" width="720" height="981">
      <span class="marca-texto">Centro Atlético Lito
        <small>Montevideo · 1917</small>
      </span>
    </a>
    <button class="menu-boton" aria-expanded="false" aria-controls="menu-principal">Menú</button>
    <nav class="menu" id="menu-principal" aria-label="Principal">
{enlaces}
    </nav>
  </div>
</header>
<div class="filete"><i></i><i></i><i></i><i></i></div>

<main id="contenido">
"""


def pie():
    enlaces_club = "\n".join(
        f'          <li><a href="{h}">{t}</a></li>' for h, t in PAGINAS_MENU[1:5]
    )
    return f"""</main>

<footer class="pie">
  <div class="marco">
    <div class="pie-grilla">
      <div class="pie-escudo">
        <img src="assets/img/escudo.png" alt="" width="720" height="981" loading="lazy">
        <div>
          <strong>Centro Atlético Lito</strong><br>
          Arroyo Seco, Montevideo, Uruguay.<br>
          Fundado en 1917. Tercera División Profesional.
        </div>
      </div>
      <div>
        <h4>El club</h4>
        <ul>
{enlaces_club}
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
# Páginas
# ============================================================

def pagina_inicio():
    return """
<section class="portada">
  <div class="portada-fondo"></div>
  <div class="marco">
    <div class="portada-grilla">
      <div>
        <p class="cintilla">Centro Atlético Lito · Montevideo · desde 1917</p>
        <h1>Tercera,<br>con orgullo.</h1>
        <p class="plomo">Más de un siglo de barrio, balón y camiseta. Somos el club de Arroyo Seco: se juega, se trabaja y se vuelve a empezar cada domingo.</p>
        <div class="acciones">
          <a class="boton" href="socios.html">Hacete socio</a>
          <a class="boton boton--fantasma" href="fixture.html">Ver fixture</a>
        </div>
      </div>
      <div class="portada-escudo">
        <img src="assets/img/escudo.png" alt="Escudo del Centro Atlético Lito" width="720" height="981" fetchpriority="high">
      </div>
    </div>
  </div>
</section>

<section class="seccion--profundo tex-diagonal" style="padding:0">
  <div class="marco" style="padding:0">
    <div class="cifras">
      <div class="cifra"><strong>1917</strong><span>Año de fundación</span></div>
      <div class="cifra"><strong>Tercera</strong><span>División Profesional</span></div>
      <div class="cifra"><strong>Arroyo Seco</strong><span>Barrio · Montevideo</span></div>
      <div class="cifra"><strong>AUF</strong><span>Club afiliado</span></div>
    </div>
  </div>
</section>

<section class="seccion seccion--hueso">
  <div class="marco">
    <div class="encabezado-seccion">
      <div>
        <p class="cintilla">Agenda</p>
        <h2>Próximo partido</h2>
      </div>
      <a class="boton boton--fantasma" style="color:var(--azul)" href="fixture.html">Fixture completo</a>
    </div>
    <div class="rejilla rejilla--2">
      <div data-partidos="proximo"><p class="cargando">Cargando…</p></div>
      <div data-partidos="ultimo"><p class="cargando">Cargando…</p></div>
    </div>
""" + AVISO_EJEMPLO + """  </div>
</section>

<section class="seccion seccion--hueso-80">
  <div class="marco">
    <div class="encabezado-seccion">
      <div>
        <p class="cintilla">Tercera División Profesional</p>
        <h2>Cómo va la tabla</h2>
      </div>
      <a class="boton boton--fantasma" style="color:var(--azul)" href="fixture.html#tabla">Tabla completa</a>
    </div>
    <div data-tabla="resumida"><p class="cargando">Cargando…</p></div>
  </div>
</section>

<section class="seccion seccion--hueso">
  <div class="marco">
    <div class="encabezado-seccion">
      <div>
        <p class="cintilla">Últimas</p>
        <h2>Noticias del club</h2>
      </div>
      <a class="boton boton--fantasma" style="color:var(--azul)" href="noticias.html">Todas las noticias</a>
    </div>
    <div class="rejilla rejilla--3" data-noticias="3"><p class="cargando">Cargando…</p></div>
  </div>
</section>

<section class="franja-cierre">
  <div class="marco">
    <div>
      <h2>El club se sostiene con socios</h2>
      <p>Cuota mensual, entrada a la cancha y voz en la asamblea. Así se banca Lito.</p>
    </div>
    <a class="boton boton--oro" href="socios.html">Asociarme</a>
  </div>
</section>
"""


def pagina_club():
    return """
<section class="seccion seccion--profundo tex-diagonal">
  <div class="marco claro">
    <p class="cintilla">El club</p>
    <h1>Más de un siglo de barrio, balón y camiseta.</h1>
    <p class="plomo">Nacimos en 1917, cuando un puñado de vecinos se cansó de jugar en el potrero y decidió formar un club. Desde entonces compartimos una sola idea: el fútbol popular se sostiene con trabajo, identidad de barrio y memoria larga.</p>
  </div>
</section>

<section class="seccion seccion--hueso">
  <div class="marco">
    <div class="rejilla rejilla--2">
      <div>
        <p class="cintilla">Historia</p>
        <h2>De la vereda a la cancha</h2>
        <p>Lito es un club de barrio en el sentido más literal: se fundó entre vecinos, se sostuvo con vecinos y sigue jugando para ellos. La sede es punto de encuentro antes que oficina y la cancha, el lugar donde el club se explica solo.</p>
        <p>Las fechas y los hitos que siguen se completan con el archivo institucional. Lo que no cambia es el marco: 1917, Montevideo, fútbol de ascenso y una hinchada que llega temprano.</p>
        <ul class="cronologia">
          <li><b>1917</b><span><strong>Fundación.</strong> Un grupo de vecinos del barrio formaliza el club.</span></li>
          <li><b>1920s</b><span><strong>Primeros años.</strong> Consolidación de la sede y de las categorías juveniles. <em>Completar con el archivo.</em></span></li>
          <li><b>Hoy</b><span><strong>Tercera División Profesional.</strong> Primer equipo, formativas y actividad social todo el año.</span></li>
        </ul>
      </div>
      <div>
        <img src="assets/img/fotos/sede.jpg" alt="Sede y cancha del Centro Atlético Lito" width="1200" height="800" loading="lazy" style="border-radius:4px">
        <p class="aviso-formulario" style="margin-top:12px">Reemplazar por una foto real de la sede o la cancha.</p>
      </div>
    </div>
  </div>
</section>

<section class="seccion seccion--azul tex-diagonal">
  <div class="marco claro">
    <p class="cintilla">Sede y cancha</p>
    <h2>Dónde late el club</h2>
    <dl class="datos">
      <div><dt>Barrio</dt><dd>Arroyo Seco, Montevideo</dd></div>
      <div><dt>Dirección</dt><dd>A confirmar</dd></div>
      <div><dt>Cancha</dt><dd>A confirmar</dd></div>
      <div><dt>Días de actividad</dt><dd>A confirmar</dd></div>
      <div><dt>Afiliación</dt><dd>Asociación Uruguaya de Fútbol (AUF)</dd></div>
    </dl>
  </div>
</section>

<section class="seccion seccion--hueso-80">
  <div class="marco">
    <p class="cintilla">Indumentaria 2026</p>
    <h2>La camiseta es el escudo en movimiento</h2>
    <div class="rejilla rejilla--3" style="margin-top:28px">
      <article class="camiseta">
        <div class="muestra" style="background:var(--azul)"><i style="background:linear-gradient(90deg,transparent 42%,var(--rojo) 42% 58%,transparent 58%)"></i></div>
        <div class="pie">
          <h4>Titular</h4>
          <p class="detalle">Azul · banda central roja · local</p>
        </div>
      </article>
      <article class="camiseta">
        <div class="muestra" style="background:var(--hueso)"><i style="background:linear-gradient(90deg,transparent 88%,var(--rojo) 88%)"></i></div>
        <div class="pie">
          <h4>Suplente</h4>
          <p class="detalle">Hueso · vivo rojo en puño · visitante</p>
        </div>
      </article>
      <article class="camiseta">
        <div class="muestra" style="background:var(--oro)"><i style="background-image:repeating-linear-gradient(45deg,rgba(12,16,36,.22) 0 6px,transparent 6px 18px),repeating-linear-gradient(-45deg,rgba(12,16,36,.22) 0 6px,transparent 6px 18px)"></i></div>
        <div class="pie">
          <h4>Arquero</h4>
          <p class="detalle">Oro · tramado tinta · diferenciación</p>
        </div>
      </article>
    </div>
  </div>
</section>

<section class="seccion seccion--hueso">
  <div class="marco">
    <div class="rejilla rejilla--2">
      <div>
        <p class="cintilla">Institucional</p>
        <h2>Comisión directiva</h2>
        <p>La comisión se renueva en asamblea de socios. Cargar la nómina vigente y la fecha de la última asamblea.</p>
        <dl class="datos">
          <div><dt>Presidencia</dt><dd>A confirmar</dd></div>
          <div><dt>Vicepresidencia</dt><dd>A confirmar</dd></div>
          <div><dt>Secretaría</dt><dd>A confirmar</dd></div>
          <div><dt>Tesorería</dt><dd>A confirmar</dd></div>
          <div><dt>Vocales</dt><dd>A confirmar</dd></div>
        </dl>
      </div>
      <div>
        <p class="cintilla">Identidad</p>
        <h2>El escudo es la firma del club</h2>
        <p>Blasón con borde dorado, fondo azul, banderines rojos y la pelota como protagonista. El año de fundación lo ancla al tiempo; la estrella lo proyecta hacia adelante.</p>
        <div class="rejilla rejilla--4" style="margin-top:20px">
          <div class="tarjeta" style="background:var(--azul);color:var(--hueso);padding:16px"><span class="mono">Azul Lito</span><br><span class="mono" style="color:var(--oro)">#1C2C6B</span></div>
          <div class="tarjeta" style="background:var(--rojo);color:var(--hueso);padding:16px"><span class="mono">Rojo Lito</span><br><span class="mono">#D12C3E</span></div>
          <div class="tarjeta" style="background:var(--oro);color:var(--tinta);padding:16px"><span class="mono">Oro Lito</span><br><span class="mono">#D4A85A</span></div>
          <div class="tarjeta" style="background:var(--hueso-80);color:var(--tinta);padding:16px"><span class="mono">Hueso</span><br><span class="mono">#F4EFE6</span></div>
        </div>
        <p class="aviso-formulario" style="margin-top:14px">Uso de marca y archivos vectoriales: <a href="mailto:marca@calito.uy">marca@calito.uy</a></p>
      </div>
    </div>
  </div>
</section>
"""


def pagina_plantel():
    return """
<section class="seccion seccion--profundo tex-diagonal">
  <div class="marco claro">
    <p class="cintilla">Temporada 2026</p>
    <h1>Plantel</h1>
    <p class="plomo">Primer equipo del Centro Atlético Lito. Los puestos sin nombre están a confirmar.</p>
  </div>
</section>

<section class="seccion seccion--hueso">
  <div class="marco">
    <div data-plantel><p class="cargando">Cargando plantel…</p></div>
  </div>
</section>

<section class="seccion seccion--azul tex-diagonal">
  <div class="marco claro">
    <div class="rejilla rejilla--2">
      <div>
        <p class="cintilla">Cuerpo técnico</p>
        <h2>Quién dirige</h2>
        <dl class="datos" data-cuerpo-tecnico><div><dt>Cargando…</dt><dd></dd></div></dl>
      </div>
      <div>
        <img src="assets/img/fotos/plantel.jpg" alt="Plantel del Centro Atlético Lito" width="1200" height="800" loading="lazy" style="border-radius:4px">
      </div>
    </div>
  </div>
</section>

<section class="seccion seccion--hueso-80">
  <div class="marco">
    <p class="cintilla">Formativas</p>
    <h2>Las divisiones del club</h2>
    <p>Lito trabaja con categorías juveniles todo el año. Para sumarse hay que escribir al club con nombre, edad y categoría.</p>
    <div class="rejilla rejilla--3" style="margin-top:24px">
      <article class="tarjeta tarjeta--borde-oro"><h3>Juveniles</h3><p>Categorías y horarios a confirmar.</p></article>
      <article class="tarjeta tarjeta--borde-oro"><h3>Baby fútbol</h3><p>Categorías y horarios a confirmar.</p></article>
      <article class="tarjeta tarjeta--borde-oro"><h3>Pruebas de jugadores</h3><p>Fechas a confirmar. Consultas por <a href="contacto.html">contacto</a>.</p></article>
    </div>
  </div>
</section>
"""


def pagina_fixture():
    return """
<section class="seccion seccion--profundo tex-diagonal">
  <div class="marco claro">
    <p class="cintilla">Tercera División Profesional · 2026</p>
    <h1>Fixture y tabla</h1>
    <p class="plomo">Partidos, resultados y posiciones. Se actualiza después de cada fecha.</p>
  </div>
</section>

<section class="seccion seccion--hueso">
  <div class="marco">
""" + AVISO_EJEMPLO + """    <p class="cintilla">Próximo partido</p>
    <div data-partidos="proximo" style="margin-bottom:36px"><p class="cargando">Cargando…</p></div>

    <p class="cintilla">Próximas fechas</p>
    <div class="lista-partidos" data-partidos="proximos"><p class="cargando">Cargando…</p></div>
  </div>
</section>

<section class="seccion seccion--hueso-80">
  <div class="marco">
    <p class="cintilla">Resultados</p>
    <h2>Últimos partidos</h2>
    <div class="lista-partidos" data-partidos="resultados" style="margin-top:24px"><p class="cargando">Cargando…</p></div>
  </div>
</section>

<section class="seccion seccion--hueso" id="tabla">
  <div class="marco">
    <p class="cintilla">Posiciones</p>
    <h2>Tabla</h2>
    <div data-tabla="completa" style="margin-top:24px"><p class="cargando">Cargando…</p></div>
  </div>
</section>
"""


def pagina_noticias():
    return """
<section class="seccion seccion--profundo tex-diagonal">
  <div class="marco claro">
    <p class="cintilla">Comunicación oficial</p>
    <h1>Noticias</h1>
    <p class="plomo">Partes de prensa, anuncios y novedades del club.</p>
  </div>
</section>

<section class="seccion seccion--hueso">
  <div class="marco">
""" + AVISO_EJEMPLO + """    <div class="rejilla rejilla--3" data-noticias="0" style="margin-top:24px"><p class="cargando">Cargando…</p></div>
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
"""


def pagina_socios():
    return """
<section class="seccion seccion--profundo tex-diagonal">
  <div class="marco claro">
    <p class="cintilla">Socios y socias</p>
    <h1>El club se sostiene con vos.</h1>
    <p class="plomo">La cuota social paga la cancha, los viajes y las formativas. Ser socio de Lito es entrar a la cancha y tener voz en la asamblea.</p>
  </div>
</section>

<section class="seccion seccion--hueso" id="cuotas">
  <div class="marco">
    <p class="cintilla">Categorías</p>
    <h2>Cuotas</h2>
    <p class="aviso-formulario" style="margin:0 0 24px">Valores de referencia. Confirmar los importes vigentes con tesorería antes de publicar.</p>
    <div class="rejilla rejilla--3">
      <article class="tarjeta cuota">
        <h3>Adherente</h3>
        <p class="precio">$ 350<small>por mes · pesos uruguayos</small></p>
        <ul>
          <li>Carné de socio</li>
          <li>Entrada a partidos de local</li>
          <li>Novedades por correo</li>
        </ul>
      </article>
      <article class="tarjeta cuota cuota--destacada">
        <h3>Activo</h3>
        <p class="precio">$ 600<small>por mes · pesos uruguayos</small></p>
        <ul>
          <li>Todo lo del adherente</li>
          <li>Voz y voto en la asamblea</li>
          <li>Descuento en indumentaria</li>
        </ul>
      </article>
      <article class="tarjeta cuota">
        <h3>Vitalicio</h3>
        <p class="precio">$ 1.200<small>por mes · pesos uruguayos</small></p>
        <ul>
          <li>Todo lo del activo</li>
          <li>Invitación a actos institucionales</li>
          <li>Reconocimiento en la sede</li>
        </ul>
      </article>
    </div>
  </div>
</section>

<section class="seccion seccion--hueso-80">
  <div class="marco">
    <div class="rejilla rejilla--2">
      <div>
        <p class="cintilla">Alta de socio</p>
        <h2>Sumate</h2>
        <p>Completá el formulario y el club se comunica para cerrar el alta y la forma de pago.</p>
        <form class="formulario" data-sin-backend="marca@calito.uy">
          <div class="campo-doble">
            <div class="campo">
              <label for="nombre">Nombre y apellido</label>
              <input id="nombre" name="nombre" type="text" autocomplete="name" required>
            </div>
            <div class="campo">
              <label for="documento">Documento</label>
              <input id="documento" name="documento" type="text" inputmode="numeric" required>
            </div>
          </div>
          <div class="campo-doble">
            <div class="campo">
              <label for="correo">Correo</label>
              <input id="correo" name="correo" type="email" autocomplete="email" required>
            </div>
            <div class="campo">
              <label for="telefono">Teléfono</label>
              <input id="telefono" name="telefono" type="tel" autocomplete="tel">
            </div>
          </div>
          <div class="campo">
            <label for="categoria">Categoría</label>
            <select id="categoria" name="categoria">
              <option>Adherente</option>
              <option>Activo</option>
              <option>Vitalicio</option>
            </select>
          </div>
          <div class="campo">
            <label for="mensaje">Comentario</label>
            <textarea id="mensaje" name="mensaje"></textarea>
          </div>
          <button class="boton" type="submit">Enviar solicitud</button>
          <p class="aviso-formulario" data-respuesta hidden></p>
          <p class="aviso-formulario">Los datos se usan solo para gestionar el alta de socio.</p>
        </form>
      </div>
      <div>
        <img src="assets/img/fotos/hinchada.jpg" alt="Hinchada del Centro Atlético Lito" width="1200" height="800" loading="lazy" style="border-radius:4px">
        <div class="nota" style="margin-top:20px">
          El formulario todavía no está conectado a un backend. Ver README para publicar el Worker de Cloudflare.
        </div>
      </div>
    </div>
  </div>
</section>
"""


def pagina_contacto():
    return """
<section class="seccion seccion--profundo tex-diagonal">
  <div class="marco claro">
    <p class="cintilla">Contacto</p>
    <h1>Hablemos.</h1>
    <p class="plomo">Sede, prensa, formativas y uso de marca. Escribinos y te respondemos.</p>
  </div>
</section>

<section class="seccion seccion--hueso">
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
          <p>Para acreditaciones de prensa, fotos institucionales, archivos vectoriales del escudo o autorizaciones de uso de marca: <a href="mailto:marca@calito.uy">marca@calito.uy</a>.</p>
          <p class="aviso-formulario">El escudo no se estira, no se rota y no cambia de color fuera de paleta. Manual de marca, edición 2026.</p>
        </div>
      </div>
      <div>
        <p class="cintilla">Formulario</p>
        <h2>Escribinos</h2>
        <form class="formulario" data-sin-backend="marca@calito.uy">
          <div class="campo">
            <label for="c-nombre">Nombre</label>
            <input id="c-nombre" name="nombre" type="text" autocomplete="name" required>
          </div>
          <div class="campo">
            <label for="c-correo">Correo</label>
            <input id="c-correo" name="correo" type="email" autocomplete="email" required>
          </div>
          <div class="campo">
            <label for="c-motivo">Motivo</label>
            <select id="c-motivo" name="motivo">
              <option>Consulta general</option>
              <option>Socios</option>
              <option>Formativas</option>
              <option>Prensa</option>
              <option>Sponsors</option>
            </select>
          </div>
          <div class="campo">
            <label for="c-mensaje">Mensaje</label>
            <textarea id="c-mensaje" name="mensaje" required></textarea>
          </div>
          <button class="boton" type="submit">Enviar</button>
          <p class="aviso-formulario" data-respuesta hidden></p>
        </form>
      </div>
    </div>
  </div>
</section>
"""


PAGINAS = {
    "index.html": (
        "Inicio",
        "Sitio oficial del Centro Atlético Lito: fixture, plantel, noticias y socios. Montevideo, desde 1917.",
        pagina_inicio,
    ),
    "club.html": (
        "El club",
        "Historia, sede, camiseta y comisión directiva del Centro Atlético Lito, fundado en 1917 en Montevideo.",
        pagina_club,
    ),
    "plantel.html": (
        "Plantel",
        "Plantel y cuerpo técnico del Centro Atlético Lito, temporada 2026.",
        pagina_plantel,
    ),
    "fixture.html": (
        "Fixture y tabla",
        "Próximos partidos, resultados y tabla de posiciones del Centro Atlético Lito.",
        pagina_fixture,
    ),
    "noticias.html": (
        "Noticias",
        "Noticias, partes de prensa y anuncios del Centro Atlético Lito.",
        pagina_noticias,
    ),
    "socios.html": (
        "Hacete socio",
        "Categorías de socio, cuotas y alta en el Centro Atlético Lito.",
        pagina_socios,
    ),
    "contacto.html": (
        "Contacto",
        "Datos de contacto, prensa y uso de marca del Centro Atlético Lito.",
        pagina_contacto,
    ),
}


def main():
    for archivo, (titulo, descripcion, cuerpo) in PAGINAS.items():
        html = cabecera(archivo, titulo, descripcion) + cuerpo() + pie()
        with open(os.path.join(BASE, archivo), "w", encoding="utf-8") as f:
            f.write(html)
        print("escrito", archivo)


if __name__ == "__main__":
    main()
