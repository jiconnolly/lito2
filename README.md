# El libro del club — Centro Atlético Lito

Sitio estático, sin build de Node ni dependencias. Se publica tal cual desde
GitHub Pages y más adelante puede migrar a Cloudflare Workers.

La web está armada como un **tomo encuadernado de 1917**: la portada es la tapa
de cuero con el escudo grabado, y cada sección es un capítulo del libro. La
apertura es CSS 3D, no video: el escudo es el PNG del manual y nunca se
deforma, como exige el capítulo 07 del brandbook.

Identidad visual según el **Manual de Marca, edición 2026 (v1.0)**: paleta,
tipografías y tono de voz salen de ahí. El hueso del manual (#F4EFE6) hace de
papel y el azul profundo de cuero. La única adición al sistema tipográfico es
**EB Garamond**, para la prosa larga; los datos, tablas y formularios siguen en
Manrope, y los titulares en Oswald, como manda el manual.

## Estructura

```
index.html          La tapa: escudo, apertura del libro e índice de capítulos
club.html           Capítulo I — historia, sede, camiseta, comisión, identidad
plantel.html        Capítulo II — plantel, cuerpo técnico y formativas
fixture.html        Capítulo III — partidos, resultados y tabla
noticias.html       Capítulo IV — listado de noticias
socios.html         Capítulo V — cuotas y alta de socio
contacto.html       Capítulo VI — contacto, prensa y uso de marca

assets/css/main.css Hoja de estilos única
assets/js/main.js   Apertura del libro, menú, partidos, tabla, plantel y noticias
assets/img/         Escudo, favicon, imagen para redes y fotos
assets/img/texturas Papel y cuero generados (procedurales, se repiten en mosaico)
data/*.json         Datos editables
worker/api.js       Worker de Cloudflare (todavía sin publicar)
build.py            Regenera las siete páginas desde plantillas compartidas
```

Las páginas comparten cabecera y pie. **Para cambiar el menú, el pie, los textos
o los metadatos hay que editar `build.py` y correr `python3 build.py`**, no los
HTML sueltos: el script los sobreescribe.

## Actualizar datos

| Qué | Dónde |
| --- | --- |
| Tabla de posiciones | `data/tabla.json` |
| Próximos partidos y resultados | `data/partidos.json` |
| Plantel y cuerpo técnico | `data/plantel.json` — los jugadores sin `nombre` se muestran como "a confirmar" |
| Noticias | `data/noticias.json` |

Los archivos con `"ejemplo": true` muestran un aviso visible en el sitio
("datos de ejemplo"). Al cargar la información real hay que sacar esa clave.

## Antes de publicar

- [ ] Reemplazar las fotos de `assets/img/fotos/` (son placeholders de marca).
- [ ] Cargar dirección de la sede, cancha, teléfono y horarios en `build.py`
      (páginas `club.html` y `contacto.html`). El manual de marca indica
      Av. Carlos María Ramírez s/n — confirmar cuál corresponde.
- [ ] Cargar la comisión directiva y los hitos de la historia.
- [ ] Confirmar los importes de las cuotas con tesorería.
- [ ] Cargar plantel, fixture y tabla reales; sacar `"ejemplo": true`.
- [ ] Confirmar los usuarios de Instagram, X y Facebook del pie.
- [ ] Poner `NOINDEX = False` en `build.py` y regenerar: hasta entonces todas
      las páginas van con `noindex, nofollow`.

## Formularios

Los formularios de socios y contacto todavía no envían nada: muestran un aviso
con la dirección de correo. Para activarlos hay que publicar el Worker.

## Pasar a datos en vivo y formularios reales

1. `wrangler kv namespace create DATOS` y `wrangler kv namespace create ENVIOS`
2. `wrangler deploy` con `worker/api.js`
3. En `assets/js/main.js`, poner `ORIGEN_VIVO = '/api'`

El Worker sirve `tabla` y `partidos` desde KV y guarda los envíos de los
formularios, sin exponer claves ni correos en el HTML.

## La apertura del libro

La tapa se abre con `transform: rotateY()`. Detalles que conviene no romper:

- **El estado por defecto es "abierto".** Sin JavaScript, con
  `prefers-reduced-motion` o si falla algo, el índice se lee igual. El JS agrega
  la clase `cerrado` para armar la ceremonia.
- **Una vez por visita.** Al abrir queda anotado en `sessionStorage`
  (`lito:libro`); si el hincha vuelve en la misma sesión entra directo al
  índice. Siempre hay un botón para saltearla.
- **El índice son enlaces reales**, no botones de JavaScript: funcionan con
  teclado, con el buscador y con el botón "atrás".

## Reglas de marca que el sitio respeta

- El escudo no se estira, no se rota, no cambia de color ni lleva efectos.
- Área de protección: una unidad X (1/12 del ancho) libre alrededor del escudo.
- Tamaño mínimo en pantalla: 32 px (16 px para favicon).
- Paleta: azul `#1C2C6B`, rojo `#D12C3E`, oro `#D4A85A`, hueso `#F4EFE6`.
  Proporción de referencia: 55 azul · 25 hueso · 12 rojo · 8 oro.
- Tipografías: Oswald (display), Manrope (texto), JetBrains Mono (etiquetas).
- Tono: frases cortas, una idea por pieza, datos al pie en mono, sin emoji.

Consultas de marca y archivos vectoriales: marca@calito.uy

## Ver el sitio localmente

```
python3 -m http.server 8000
```

Y abrir http://localhost:8000
