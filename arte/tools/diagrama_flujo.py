from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1700, 2500
BG       = (18, 26, 22)
INK      = (12, 18, 14)
CREAM    = (246, 239, 220)
GOLD     = (217, 178, 76)
PINK     = (242, 166, 195)
VIOLET   = (150, 110, 200)
FOREST_D = (30, 63, 44)
FOREST_M = (60, 107, 72)
FOREST_L = (123, 181, 131)
BLUE     = (140, 190, 210)
RED      = (198, 96, 88)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

def font(sz, bold=False):
    p = ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold
         else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
    return ImageFont.truetype(p, sz) if os.path.exists(p) else ImageFont.load_default()

F_TITLE = font(54, True)
F_SUB   = font(24)
F_ACT   = font(30, True)
F_H     = font(20, True)
F_B     = font(18)
F_S     = font(16)
F_T     = font(14)

def text(xy, s, f, fill=CREAM, anchor="la"):
    d.text(xy, s, font=f, fill=fill, anchor=anchor)

# HEADER
d.rectangle([0, 0, W, 148], fill=INK)
text((W//2, 44), "FLUJO NARRATIVO", F_TITLE, GOLD, "ma")
text((W//2, 104), "Los cinco actos · Hilo A (Uma) e Hilo B (Pablo) · SEÑALES v3.0", F_SUB, FOREST_L, "ma")

# Column headers
COL_A_X, COL_A_W = 120, 900
COL_B_X, COL_B_W = 1110, 480

d.rounded_rectangle([COL_A_X, 168, COL_A_X+COL_A_W, 218], radius=8, fill=FOREST_D, outline=INK, width=3)
text((COL_A_X+COL_A_W//2, 193), "HILO A — UMA  ·  campaña principal", F_H, CREAM, "mm")
d.rounded_rectangle([COL_B_X, 168, COL_B_X+COL_B_W, 218], radius=8, fill=(58, 40, 74), outline=VIOLET, width=3)
text((COL_B_X+COL_B_W//2, 193), "HILO B — PABLO  ·  interludios", F_H, (220, 200, 245), "mm")

# ---------------- ACT BLOCKS ----------------
acts = [
    {
        "y": 250, "h": 300, "col": (44, 70, 52),
        "tag": "PRÓLOGO", "time": "15–25 min", "sub": "El Martes de Febrero",
        "beats": [
            ("Ventilador. El juego abre sin menú.", None),
            ("Casa Torres: Bautista, Natalia, Darío.", None),
            ("Darío pide investigar 3 objetos raros.", None),
            ('"No te pido que resuelvas. Te pido que preguntes."', "quote"),
        ],
        "inter": ("I", "El papel doblado tres veces",
                  ["Cuarto de Pablo · 4×3 tiles",
                   "Escribe la señal 1 · la rompe 2 veces",
                   "DECISIÓN: Romperlo / Dejarlo así",
                   "→ mismo resultado, distinto matiz"]),
    },
    {
        "y": 580, "h": 400, "col": (52, 84, 60),
        "tag": "ACTO I", "time": "60–75 min", "sub": "El Barrio de Siempre",
        "beats": [
            ("Graciela → SEÑAL 1 · tutorial Resonancia", "signal"),
            ("Don Pepe → Fernet → SEÑAL 2", "signal"),
            ("Marta → SEÑAL 3 · pista del método", "signal"),
            ("Primer Eco Menor (callejón)", None),
            ("★ EL UMBRAL — cae el árbol", "big"),
            ("VISIÓN DE CLASE (irrevocable)", "choice"),
        ],
        "inter": ("II", "Cinco cuadras",
                  ["Calle · 10×3 tiles",
                   "Ve a Uma de lejos con Marta",
                   "DECISIÓN: Cruzar / Seguir derecho",
                   "→ compra fósforos. No fuma."]),
    },
    {
        "y": 1010, "h": 430, "col": (46, 76, 56),
        "tag": "ACTO II", "time": "80–100 min", "sub": "El Barrio Roto",
        "beats": [
            ("Barrio post-Umbral · llamada de Darío", None),
            ("SEÑAL 4 · 1ª incursión al Revés (5 min)", "signal"),
            ("Mercado Viejo · Doña Elsa · MS-03 radio", None),
            ("JEFE I — El Abandono (sótano)", "boss"),
            ("Diario de Carmen · SEÑAL 5 · SEÑAL 6*", "signal"),
            ("Ve a Pablo de espaldas · Leo lo nombra", "key"),
        ],
        "inter": ("III + IV", "Hernán · La entrevista",
                  ["III — Cocina 4×3 · cena en silencio",
                   '"Ojalá no heredes también lo mío."',
                   "IV — Balcón · llama el estudio",
                   "El reloj empieza a correr"]),
    },
    {
        "y": 1470, "h": 380, "col": (40, 66, 50),
        "tag": "ACTO III", "time": "70–90 min", "sub": "El Revés",
        "beats": [
            ("Entrada completa al Revés", None),
            ("SEÑAL 7 · Resonantes · SEÑAL 8*", "signal"),
            ("EL TELAR — lore completo de Carmen", "key"),
            ("JEFE II — El Olvido", "boss"),
            ("1er ENCUENTRO CON PABLO", "big"),
            ('"Sabés dónde encontrarme."', "quote"),
        ],
        "inter": ("V", "Tres semanas",
                  ["Azotea 5×4 · la ve resolver un Eco",
                   '"Se está quedando sin necesitar"',
                   "Escribe la señal 9 de un tirón",
                   "→ tarda 3 semanas en entregarla"]),
    },
    {
        "y": 1880, "h": 380, "col": (58, 46, 46),
        "tag": "ACTO IV", "time": "50–65 min", "sub": "La Fractura",
        "beats": [
            ("Barrio deteriorado · Darío pide ayuda", None),
            ("4 VACIADOS — solo Resonancia", "warn"),
            ("Marta liberada → info clave de Pablo", "key"),
            ("MP-12: Pablo confiesa la Regla 3", "big"),
            ("Escena de Hernán (opcional) → entrevista", "key"),
            ("SEÑAL 9 · JEFE III — Miedo al Decir", "boss"),
        ],
        "inter": None,
    },
]

def beat_color(kind):
    return {
        "signal": PINK, "boss": RED, "key": GOLD,
        "big": GOLD, "choice": BLUE, "quote": FOREST_L, "warn": (226, 160, 90),
    }.get(kind, CREAM)

# auto-ajuste de alto y reflow vertical
cy = 250
for a in acts:
    a["y"] = cy
    a["h"] = max(78 + 40*len(a["beats"]) + 18,
                 (82 + 26*len(a["inter"][2]) + 40) if a["inter"] else 0)
    cy = a["y"] + a["h"] + 46

for a in acts:
    y, h = a["y"], a["h"]
    # Act panel
    d.rounded_rectangle([COL_A_X, y, COL_A_X+COL_A_W, y+h], radius=12, fill=a["col"], outline=INK, width=4)
    # tag bar
    d.rounded_rectangle([COL_A_X, y, COL_A_X+COL_A_W, y+56], radius=12, fill=INK)
    d.rectangle([COL_A_X, y+40, COL_A_X+COL_A_W, y+56], fill=INK)
    text((COL_A_X+22, y+14), a["tag"], F_ACT, GOLD)
    text((COL_A_X+230, y+22), a["sub"], F_B, CREAM)
    text((COL_A_X+COL_A_W-22, y+22), a["time"], F_S, FOREST_L, "ra")

    yy = y + 78
    for label, kind in a["beats"]:
        col = beat_color(kind)
        if kind in ("big", "boss"):
            d.rounded_rectangle([COL_A_X+18, yy-4, COL_A_X+COL_A_W-18, yy+30], radius=6,
                                fill=(28, 40, 32), outline=col, width=2)
            text((COL_A_X+34, yy+3), label, F_H, col)
        else:
            d.ellipse([COL_A_X+26, yy+7, COL_A_X+38, yy+19], fill=col)
            f = F_B
            text((COL_A_X+52, yy+3), label, f, col if kind else CREAM)
        yy += 40

    # Interlude box
    if a["inter"]:
        num, name, lines = a["inter"]
        ih = 82 + 26*len(lines)
        iy = y + (h - ih)//2
        d.rounded_rectangle([COL_B_X, iy, COL_B_X+COL_B_W, iy+ih], radius=12,
                            fill=(48, 32, 64), outline=VIOLET, width=3)
        text((COL_B_X+18, iy+12), f"INTERLUDIO {num}", F_S, VIOLET)
        text((COL_B_X+18, iy+34), name, F_H, (226, 208, 250))
        ly2 = iy + 62
        for ln in lines:
            text((COL_B_X+18, ly2), "· " + ln, F_T, (196, 182, 220))
            ly2 += 26
        # connector
        d.line([COL_A_X+COL_A_W, y+h//2, COL_B_X, iy+ih//2], fill=VIOLET, width=3)
        d.ellipse([COL_B_X-8, iy+ih//2-8, COL_B_X+8, iy+ih//2+8], fill=VIOLET)

    # vertical flow arrow
    if a is not acts[-1]:
        ax = COL_A_X + COL_A_W//2
        d.line([ax, y+h, ax, y+h+30], fill=GOLD, width=5)
        d.polygon([(ax-11, y+h+30), (ax+11, y+h+30), (ax, y+h+46)], fill=GOLD)

# ---------------- ACT V / FINALES ----------------
last = acts[-1]
fy = last["y"] + last["h"] + 60
ax = COL_A_X + COL_A_W//2
d.line([ax, fy-56, ax, fy-16], fill=GOLD, width=5)
d.polygon([(ax-11, fy-16), (ax+11, fy-16), (ax, fy)], fill=GOLD)

d.rounded_rectangle([120, fy, W-120, fy+150], radius=12, fill=(66, 52, 40), outline=GOLD, width=4)
text((146, fy+14), "ACTO V — La Señal Más Clara", F_ACT, GOLD)
text((W-146, fy+22), "25–35 min", F_S, CREAM, "ra")

finals = [
    (GOLD,   "FINAL COMPLETO — “Sí”", "7+ NPCs · 6+ señales · Umbral cerrado"),
    (BLUE,   "FINAL SILENCIO",        "cualquier condición · se sientan juntos"),
    (RED,    "FINAL “Mañana”",        "pocos vínculos · Vaciados dañados"),
]
fx = 152
for col, name, cond in finals:
    d.rounded_rectangle([fx, fy+62, fx+460, fy+130], radius=8, fill=(30, 38, 30), outline=col, width=2)
    text((fx+16, fy+72), name, F_H, col)
    text((fx+16, fy+98), cond, F_T, (200, 210, 200))
    fx += 486

# LEGEND
lg = [(PINK, "señal"), (RED, "jefe"), (GOLD, "hito clave"),
      (BLUE, "decisión"), ((226,160,90), "cuidado"), (VIOLET, "interludio Pablo")]
ly3 = fy + 190
lx = 130
for col, name in lg:
    d.ellipse([lx, ly3+2, lx+14, ly3+16], fill=col)
    text((lx+22, ly3), name, F_T, (170, 190, 172))
    lx += int(d.textlength(name, font=F_T)) + 60

img = img.crop((0, 0, W, ly3 + 60))
img.save("SENALES_flujo_narrativo.png")
print("flujo ok")
