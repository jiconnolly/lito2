# El libro del club — Centro Atlético Lito

Sitio estático, sin build de Node ni dependencias. Se publica tal cual desde
GitHub Pages y más adelante puede migrar a Cloudflare Workers.

La web está armada como un **tomo encuadernado de 1917**, apoyado sobre la barra
del bar donde nació el club. Al tocar el escudo la toma se acerca, se endereza y
el libro se abre sobre el índice de capítulos. Todo es CSS 3D, no video: el
escudo es el PNG del manual y nunca se deforma, como exige el capítulo 07 del
brandbook.

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
assets/img/texturas Fondo de la portada, cuero de la tapa y papel de las hojas
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
- **Cerrado en cada visita.** Cada vez que se entra a la portada el libro
  aparece cerrado.
- **Sin carteles.** La portada no lleva ninguna indicación escrita: toda la
  escena abre el libro con un toque, en cualquier punto. La tapa sigue siendo un
  `<button>` con su etiqueta accesible, así que con teclado se llega con Tab y
  se abre con Enter.
- **Dos tiempos.** Primero el libro se endereza (1,05 s) y recién después gira
  la tapa (1,4 s, con 0,62 s de espera). Si se tocan esos tiempos en el CSS hay
  que mantener la espera de la tapa por encima de la duración del enderezado, o
  la tapa se abre mientras el libro todavía está de costado.
- **Es la cámara la que se mueve, no el libro.** Todo lo que se ve —el plano del
  fondo y el libro— vive dentro de `.camara`. Si se anima el libro por separado,
  el ojo lo lee como un objeto flotando sobre una postal.
- **Profundidad.** El fondo está en `translateZ(-520px)` con la escala que
  compensa la perspectiva a esa distancia: por eso el libro crece más rápido que
  el fondo al acercarse la toma. La sombra de contacto vive apenas detrás del
  libro (`translateZ(-12px)`).
- **Nada decorativo intercepta clicks.** Las caras del tomo y la hoja que se da
  vuelta llevan `pointer-events: none`, y el índice no lleva `translateZ`
  negativo: si se corre hacia atrás queda detrás del propio contenedor y sus
  enlaces dejan de recibir clicks.
- **El pasaje al capítulo.** Al elegir un capítulo se pasa una hoja, la cámara
  entra y un velo del color del papel toma la pantalla; el capítulo arranca con
  un fundido desde ese mismo color, así la costura entre las dos páginas no se
  ve. Si se cambia `--papel` hay que mirar que las dos puntas sigan coincidiendo.
- **El tomo tiene cuerpo.** `.cara-lomo`, `.cara-cabeza` y `.cara-canto` son
  caras reales rotadas 90°, y `--grosor` define el espesor. Al girar la toma se
  ve el canto de las hojas; el lomo con sus nervios queda del lado opuesto.
- **El índice son enlaces reales**, no botones de JavaScript: funcionan con
  teclado, con el buscador y con el botón "atrás".

## Las texturas

Tres fotografías sostienen la escena. Se cambian reemplazando el archivo, sin
tocar el CSS:

| Archivo | Dónde se usa | Cómo conviene que sea |
| --- | --- | --- |
| `fondo.jpg` | Fondo de la portada | Apaisada y oscura en los bordes, con una superficie clara donde apoyar el libro |
| `tapa.jpg` | Tapa y contratapa | Cuero fotografiado de frente, con su filete impreso. El escudo y las letras se componen encima en CSS |
| `lomo.jpg` | Lomo del tomo | Lomo con nervios, de frente y vertical; se recorta a `cover` sobre una cara de 58 px |
| `cuero.jpg` | (sin uso hoy) | Quedó de la etapa anterior; el troquel del escudo ya toma su grano de `tapa.jpg` |
| `papel.jpg` | Hojas y guarda | **Tiene que repetir sin costura**: se repite en mosaico de 520 px |

El papel del repositorio es un mosaico espejado y llevado al hueso del manual
(`#F4EFE6`), para que la trama no cante y el color siga siendo el de la marca.
Si se reemplaza por una foto cruda, el mosaico se va a notar.

**El filete de la tapa es rojo, y no venía así.** La fotografía original tenía
el filete dorado; se lo pasó a rojo Lito por matiz: se toma la máscara de los
amarillos con saturación (matiz 33°–68°, S > .26, V > .30), se les fija el
matiz del rojo del manual y se les conserva el valor, para que el gastado y los
raspones del oro original sigan leyéndose en el rojo. Las esquinas peladas del
cuero quedan fuera de la máscara por ser más anaranjadas y menos saturadas. Si
se cambia la foto de tapa hay que rehacer esa conversión.

**La tapa trae su propio filete.** Por eso `.cara-frente` no dibuja
ningún marco y el contenido va con `padding: 13% 14% 12.5%`, que es lo que lo
mantiene dentro del filete de la foto. Si se cambia la foto de tapa hay que
volver a medir ese padding contra el nuevo marco.

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
