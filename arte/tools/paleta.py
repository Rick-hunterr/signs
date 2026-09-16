from PIL import Image, ImageDraw, ImageFont
import os

W,H = 1500, 2050
BG=(18,26,22); INK=(12,18,14); CREAM=(246,239,220); GOLD=(217,178,76)
img=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(img)

def font(s,b=False):
    p=("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if b else
       "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
    return ImageFont.truetype(p,s) if os.path.exists(p) else ImageFont.load_default()
F_T1=font(46,True); F_SUB=font(20); F_H=font(22,True); F_L=font(15,True); F_S=font(13); F_M=font(12)

def hexs(c): return "#%02X%02X%02X" % c

GRUPOS = [
 ("PIEL Y PERSONAJES", "para Uma, Pablo y NPCs", [
   ("piel Uma clara",(247,217,196)),("piel Uma sombra",(226,186,164)),
   ("piel Pablo",(201,138,91)),("piel Pablo sombra",(172,112,72)),
   ("pelo oscuro",(36,23,18)),("pelo brillo",(64,44,36)),
   ("rosa cachete",(242,166,195)),("rosa agujetas",(232,132,172)),
 ]),
 ("BARRIO — MATERIALES", "revoque, chapa, ladrillo, cemento", [
   ("revoque crema",(206,196,174)),("revoque sombra",(180,170,150)),
   ("revoque celeste",(168,190,196)),("revoque terracota",(196,140,110)),
   ("ladrillo",(168,96,74)),("ladrillo sombra",(140,76,58)),
   ("chapa",(150,146,132)),("cemento",(128,118,104)),
   ("cemento claro",(186,182,172)),("madera",(120,100,74)),
   ("reja / hierro",(72,72,70)),("cable",(48,52,50)),
 ]),
 ("SUELOS", "asfalto, vereda, baldosa, tierra", [
   ("asfalto",(78,82,80)),("asfalto sombra",(64,68,66)),
   ("vereda",(176,170,152)),("vereda gastada",(160,154,138)),
   ("baldosa plaza",(198,184,150)),("baldosa sombra",(184,170,136)),
   ("baldosa roja mercado",(170,110,92)),("tierra sendero",(150,124,92)),
 ]),
 ("VEGETACIÓN Y AGUA", "árboles, pasto, canal", [
   ("pasto",(86,126,78)),("pasto claro",(102,142,88)),("pasto sombra",(72,110,66)),
   ("copa árbol",(58,96,58)),("copa clara",(78,122,72)),("copa oscura",(44,84,48)),
   ("agua canal",(70,116,140)),("agua sombra",(58,100,124)),
 ]),
 ("TOLDOS DEL MERCADO", "lonas descoloridas — usar de a pares", [
   ("lona roja",(196,110,110)),("lona amarilla",(196,176,110)),
   ("lona azul",(110,150,180)),("lona lila",(170,150,190)),
   ("lona crema",(200,190,160)),("lona verde",(150,180,150)),
 ]),
 ("EL REVÉS", "dimensión espejo — paleta fría y luminosa", [
   ("suelo Revés",(48,36,78)),("suelo sombra",(40,30,66)),("suelo claro",(60,46,94)),
   ("borde luminoso",(120,90,190)),("violeta grieta",(150,110,200)),
   ("violeta claro",(190,158,235)),("vacío",(20,16,34)),
   ("fantasma",(74,60,110)),("fantasma claro",(94,78,136)),
   ("hilo del Telar",(226,206,140)),("núcleo Telar",(250,238,180)),
   ("agua invertida",(60,90,140)),("vegetación Revés",(44,80,66)),
 ]),
 ("UI E INTERFAZ", "cuadros de diálogo, HUD, cuaderno", [
   ("pergamino",(240,228,196)),("pergamino sombra",(220,206,172)),
   ("tinta",(36,23,18)),("dorado UI",(217,178,76)),
   ("crema UI",(246,239,220)),("verde UI",(60,107,72)),
   ("negro UI",(12,18,14)),("gris deshabilitado",(120,124,120)),
 ]),
 ("ESTADOS Y FEEDBACK", "Ánimo, daño, señales", [
   ("Ánimo alto",(123,181,131)),("Ánimo medio",(226,196,110)),
   ("Ánimo bajo",(226,160,90)),("Ánimo crítico",(198,96,88)),
   ("señal de Pablo",(242,166,195)),("anclaje",(217,178,76)),
   ("zona neutral",(120,200,180)),("peligro",(210,90,90)),
 ]),
]

# ---- HEADER ----
d.rectangle([0,0,W,150],fill=INK)
d.text((W//2,34),"PALETA MAESTRA",font=F_T1,fill=GOLD,anchor="ma")
d.text((W//2,92),"SEÑALES — El Umbral del Barrio  ·  paleta cerrada  ·  usar SOLO estos colores",
       font=F_SUB,fill=(123,181,131),anchor="ma")

y = 186
SW = 130          # ancho de swatch
SH = 74           # alto de swatch
GAP = 12

for titulo, sub, colores in GRUPOS:
    d.text((70,y),titulo,font=F_H,fill=GOLD)
    d.text((70+d.textlength(titulo,font=F_H)+20,y+6),sub,font=F_S,fill=(140,165,142))
    y += 38
    x = 70
    for nombre,c in colores:
        if x+SW > W-60:
            x = 70; y += SH+46
        d.rectangle([x,y,x+SW,y+SH],fill=c,outline=INK,width=2)
        # etiqueta
        d.text((x+SW//2,y+SH+8),nombre,font=F_M,fill=(200,214,200),anchor="ma")
        d.text((x+SW//2,y+SH+24),hexs(c),font=F_S,fill=(140,165,142),anchor="ma")
        x += SW+GAP
    y += SH+58

# ---- REGLAS ----
d.rounded_rectangle([70,y,W-60,y+250],radius=12,fill=(26,38,30),outline=GOLD,width=3)
d.text((100,y+18),"REGLAS DE USO",font=F_L,fill=GOLD)
reglas = [
 "1.  Paleta cerrada. Si un color no está acá, no entra al juego. Esto es lo que da unidad visual.",
 "2.  Máximo 4 tonos por objeto: base, sombra, luz y línea. Nada de degradados suaves.",
 "3.  Sin anti-aliasing. Los bordes son duros. Pixel art de verdad, no imagen escalada.",
 "4.  El barrio usa la paleta cálida (crema, terracota, verde polvoriento). El Revés usa la fría (violeta, azul).",
 "5.  Nunca mezclar las dos paletas, EXCEPTO en el Acto IV, donde es el efecto buscado.",
 "6.  El rosa de las señales aparece solo en las señales. Es el color más escaso y por eso se nota.",
 "7.  El dorado del Telar y los Anclajes nunca se usa como decoración: siempre significa algo.",
]
yy = y+52
for r in reglas:
    d.text((100,yy),r,font=F_S,fill=(190,206,190)); yy += 26

img.save("SENALES_paleta.png")
print("ok",img.size)
