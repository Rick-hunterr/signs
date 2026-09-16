from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1700, 2200
BG        = (18, 26, 22)
INK       = (12, 18, 14)
CREAM     = (246, 239, 220)
GOLD      = (217, 178, 76)
PINK      = (242, 166, 195)
VIOLET    = (150, 110, 200)
FOREST_D  = (30, 63, 44)
FOREST_M  = (60, 107, 72)
FOREST_L  = (123, 181, 131)
BARK      = (74, 50, 34)
SKY       = (44, 82, 56)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

def font(sz, bold=False):
    paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold
        else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for p in paths:
        if os.path.exists(p):
            return ImageFont.truetype(p, sz)
    return ImageFont.load_default()

F_TITLE = font(58, True)
F_SUB   = font(26)
F_ZONE  = font(32, True)
F_BODY  = font(20)
F_SMALL = font(17)
F_TINY  = font(15)
F_TAG   = font(16, True)

def text(xy, s, f, fill=CREAM, anchor="la"):
    d.text(xy, s, font=f, fill=fill, anchor=anchor)

def panel(x, y, w, h, fill, border=INK, bw=4, r=14):
    d.rounded_rectangle([x, y, x+w, y+h], radius=r, fill=fill, outline=border, width=bw)

# ---------- HEADER ----------
d.rectangle([0, 0, W, 150], fill=INK)
text((W//2, 48), "BARRIO SAUCO", F_TITLE, GOLD, "ma")
text((W//2, 108), "Mapa de zonas, conexiones y puntos clave  ·  SEÑALES v3.0", F_SUB, FOREST_L, "ma")

# ---------- ELEVATION BANDS ----------
bands = [
    (190,  520, "ZONA ALTA", "edificios viejos · calles angostas · +3° más fresco", (26, 52, 38)),
    (740, 1120, "MEDIA LADERA", "residencial · parque ribereño", (34, 66, 46)),
    (1340, 1720, "CENTRO PLANO", "plaza · mercado · comercios", (42, 78, 54)),
]
for y0, y1, name, desc, col in bands:
    d.rectangle([60, y0, W-60, y1], fill=col)
    text((78, y0+12), name, F_TAG, GOLD)
    text((78, y0+34), desc, F_TINY, (150, 180, 155))

# ---------- ZONE BOXES ----------
# (x, y, w, h, num, name, color, lines)
zones = [
    (760, 200, 380, 190, "7", "EL MIRADOR", BARK, [
        "Señal 9 (flecha ↑)",
        "Jefe final: Miedo al Decir",
        "Anclaje 6",
        "La declaración · Acto V",
    ]),
    (180, 420, 400, 210, "5", "ZONA ALTA", FOREST_D, [
        "Don Mario · Rosa (florería)",
        "Firma: CARMEN SANTELLAN 1994",
        "Taller de Hernán (Acto IV)",
        "Zona más afectada post-Umbral",
    ]),
    (1180, 760, 400, 210, "4", "PARQUE RIBEREÑO", FOREST_M, [
        "Señal 4 · Anclaje 4",
        "Sauce de dos colores → 1ª grieta",
        "Sombra Errante (incendio, 40 años)",
        "Sin daño de sol · los patos no se van",
    ]),
    (180, 780, 400, 190, "0", "CASA TORRES", (58, 44, 30), [
        "Bautista · Natalia · Darío",
        "Anclaje 0 (siempre activo)",
        "Guardado manual · +5 Ánimo/min",
        "Heladera: dibujo cambia por acto",
    ]),
    (660, 1030, 400, 210, "2", "PLAZA MAYOR", (52, 92, 62), [
        "★ EL UMBRAL (fin Acto I)",
        "Señal 2 (vinilo) · Anclaje 2",
        "Leo y Vale · Valentina · Ernesto",
        "Grieta central post-Umbral",
    ]),
    (180, 1380, 420, 230, "1", "CALLE PRINCIPAL", FOREST_M, [
        "Kiosco de Chino → ZONA NEUTRAL",
        "Señal 3 (edificio de Marta)",
        "1er Eco (callejón) · gato del 847",
        "Almacén (Interludio II)",
        "MS-09: Chino de noche",
    ]),
    (1140, 1380, 420, 230, "3", "MERCADO VIEJO", (78, 60, 40), [
        "Doña Elsa · Sr. Ariel · Lucía",
        "Anclaje 3 · Señal 6 (opcional)",
        "SÓTANO → Jefe I: El Abandono",
        "Diario de Doña Carmen",
        "MS-03: la radio · Agujetas",
    ]),
]

zone_centers = {}
for x, y, w, h, num, name, col, lines in zones:
    panel(x, y, w, h, col)
    # number badge
    d.ellipse([x+14, y+14, x+58, y+58], fill=GOLD, outline=INK, width=3)
    text((x+36, y+36), num, F_ZONE, INK, "mm")
    text((x+72, y+24), name, F_ZONE, CREAM)
    yy = y + 72
    for ln in lines:
        text((x+22, yy), "· " + ln, F_SMALL, (222, 232, 220))
        yy += 27
    zone_centers[num] = (x + w//2, y + h//2, x, y, w, h)

# ---------- EL REVES (side panel) ----------
rx, ry, rw, rh = 1140, 200, 440, 480
d.rounded_rectangle([rx, ry, rx+rw, ry+rh], radius=14, fill=(40, 26, 62), outline=VIOLET, width=5)
text((rx+24, ry+22), "ZONA 6", F_TAG, VIOLET)
text((rx+24, ry+48), "EL REVÉS", F_ZONE, (215, 190, 250))
sub = [
    "Dimensión espejo · suelo translúcido",
    "cielo violeta→negro, tiempo no lineal",
    "",
    "SUB-ZONAS",
    "· Revés de Plaza Mayor (abierto)",
    "· Revés del Mercado (laberíntico)",
    "· Revés del Parque (agua arriba)",
    "· Revés Zona Alta (tiempo inestable)",
    "",
    "EL TELAR DE DOÑA CARMEN",
    "· Núcleo · conecta todos los Anclajes",
    "· Señal 7 · Anclaje 5",
    "· Jefe II: El Olvido",
    "· 1er encuentro con Pablo",
    "",
    "GUARDIANES",
    "Tejedor Ciego · Centinela de Piedra",
    "Pájaros de Tinta · Memoria de Agua",
]
yy = ry + 96
for s in sub:
    if s in ("SUB-ZONAS", "EL TELAR DE DOÑA CARMEN", "GUARDIANES"):
        text((rx+24, yy), s, F_TAG, GOLD)
    else:
        text((rx+24, yy), s, F_TINY, (198, 185, 220))
    yy += 21

# ---------- CONNECTIONS ----------
def conn(a, b, color=FOREST_L, w=5, dashed=False, label=None):
    ax, ay = a; bx, by = b
    if dashed:
        steps = 26
        for i in range(steps):
            if i % 2: continue
            t0 = i/steps; t1 = (i+1)/steps
            d.line([ax+(bx-ax)*t0, ay+(by-ay)*t0, ax+(bx-ax)*t1, ay+(by-ay)*t1], fill=color, width=w)
    else:
        d.line([ax, ay, bx, by], fill=color, width=w)
    if label:
        mx, my = (ax+bx)//2, (ay+by)//2
        tw = d.textlength(label, font=F_TINY)
        d.rectangle([mx-tw//2-8, my-13, mx+tw//2+8, my+13], fill=INK)
        text((mx, my), label, F_TINY, CREAM, "mm")

def edge(num, side):
    cx, cy, x, y, w, h = zone_centers[num]
    return {
        "top":    (cx, y),
        "bottom": (cx, y+h),
        "left":   (x, cy),
        "right":  (x+w, cy),
    }[side]

# Casa <-> Calle
conn(edge("0","bottom"), (380, 1380), FOREST_L, 5, False, "puerta")

# Calle <-> Plaza
conn(edge("1","right"), edge("2","bottom"), FOREST_L, 5, False, "norte")
# Calle -> Mercado
conn((600, 1495), (1140, 1495), FOREST_L, 5, False, "callejón")
# Calle -> Zona Alta (waypoint por la izquierda, evita Casa Torres)
conn(edge("1","left"), (120, 1495), FOREST_L, 5)
conn((120, 1495), (120, 700), FOREST_L, 5, False, "calle empinada")
conn((120, 700), edge("5","left"), FOREST_L, 5)
# Plaza <-> Parque
conn(edge("2","right"), edge("4","bottom"), FOREST_L, 5, False, "pasaje peatonal")
# Parque -> Zona Alta
conn(edge("4","left"), edge("5","right"), FOREST_L, 5, False, "sendero")
# Zona Alta -> Mirador
conn(edge("5","top"), edge("7","left"), GOLD, 6, False, "escalera oculta")

# Grietas al Reves (dashed violet)
for num, side in [("2","top"), ("3","top"), ("4","top"), ("5","right")]:
    conn(edge(num, side), (rx, ry+rh-60), VIOLET, 4, True)
gl = "- - -  grietas al Revés (post-Umbral)"
glw = d.textlength(gl, font=F_TINY)
d.rectangle([rx+rw-glw-16, ry+rh+10, rx+rw, ry+rh+34], fill=BG)
text((rx+rw-glw-8, ry+rh+14), gl, F_TINY, VIOLET)

# ---------- LEGEND ----------
ly = 1700
panel(180, ly, 1380, 200, (26, 38, 30), GOLD, 3)
text((208, ly+18), "REFERENCIAS", F_TAG, GOLD)

items = [
    (PINK,   "Señales de Pablo (9)", "1 Graciela · 2 Plaza · 3 Marta · 4 Parque · 5 Sótano · 6 Mercado* · 7 Revés · 8 Revés* · 9 Mirador"),
    (GOLD,   "Anclajes (7)",         "0 Cuarto · 1 Graciela · 2 Fuente · 3 Mercado · 4 Río · 5 Grieta · 6 Mirador"),
    (VIOLET, "Jefes (3)",            "I Abandono (sótano, Acto II) · II Olvido (Revés, Acto III) · III Miedo al Decir (Mirador, Acto IV)"),
]
yy = ly + 52
for col, title, desc in items:
    d.ellipse([212, yy+4, 232, yy+24], fill=col, outline=INK, width=2)
    text((246, yy+2), title, F_TAG, col)
    text((246, yy+26), desc, F_TINY, (200, 214, 200))
    yy += 48

text((W//2, ly+218), "* opcionales   ·   Tiles 32×32 px   ·   Mundo normal ≈ 120×80 tiles   ·   Base móvil 360×640 portrait",
     F_SMALL, (140, 170, 145), "ma")

# footer
d.rectangle([0, H-56, W, H], fill=INK)
text((W//2, H-28), "SEÑALES — El Umbral del Barrio  ·  Bit Hunter Dev", F_SMALL, FOREST_L, "mm")

img.save("SENALES_mapa_barrio.png")
print("mapa ok")
