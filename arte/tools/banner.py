from PIL import Image, ImageDraw, ImageFont
import os, math, random
random.seed(3)

W,H = 1280, 420
INK=(12,18,14); CREAM=(246,239,220); GOLD=(217,178,76)
PINK=(242,166,195); VIOLET=(150,110,200)
SKY_T=(28,52,38); SKY_B=(62,98,66)
FOREST_D=(30,63,44); FOREST_M=(60,107,72)
ROOF_A=(168,96,74); ROOF_C=(128,118,104); WALL=(206,196,174)
TREE_BIG=(44,84,48); TREE=(58,96,58)

img=Image.new("RGB",(W,H),SKY_T); d=ImageDraw.Draw(img)

def font(s,b=False):
    p=("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if b else
       "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
    return ImageFont.truetype(p,s) if os.path.exists(p) else ImageFont.load_default()

# ── cielo: azul-verde arriba, dorado al horizonte, verde abajo ──
def mix(a,b,t): return tuple(int(a[i]+(b[i]-a[i])*t) for i in range(3))
TOP=(26,48,40); MID=(196,150,86); LOW=(52,84,58)
for y in range(H):
    t=y/H
    if t<0.55:
        col=mix(TOP,MID, (t/0.55)**1.6)
    else:
        col=mix(MID,LOW, ((t-0.55)/0.45)**0.7)
    d.line([0,y,W,y],fill=col)

# ── sol bajo ──
d.ellipse([1000,140,1105,245],fill=(238,198,128))

# ── siluetas del barrio, tres capas de profundidad ──
def skyline(y0, color, seed, alto_min, alto_max, ancho_min, ancho_max):
    random.seed(seed)
    x=-20
    while x<W+40:
        w=random.randint(ancho_min,ancho_max)
        h=random.randint(alto_min,alto_max)
        d.rectangle([x,y0-h,x+w,H],fill=color)
        # tanque de agua ocasional
        if random.random()<0.35:
            d.rectangle([x+w-18,y0-h-14,x+w-6,y0-h],fill=color)
        # ventanas encendidas
        for i in range(2):
            if random.random()<0.5:
                vx=x+8+i*18; vy=y0-h+14
                if vx+8<x+w:
                    d.rectangle([vx,vy,vx+7,vy+9],fill=(226,196,120))
        x+=w+random.randint(4,12)

skyline(330, (46,74,54), 1, 30, 70, 40, 80)
skyline(368, (34,58,42), 7, 45, 100, 50, 95)
skyline(410, (20,36,28), 11, 60, 120, 60, 110)

# ── el árbol de la plaza, silueta central ──
cx=235
TR=(16,28,20)
d.rectangle([cx-13,250,cx+13,420],fill=TR)
d.ellipse([cx-104,146,cx+104,282],fill=TR)
d.ellipse([cx-74,112,cx+62,222],fill=TR)
d.ellipse([cx-30,96,cx+90,196],fill=TR)
for a,l in ((-1,64),(1,58),(-1,34),(1,38)):
    d.line([cx,412,cx+a*l,420],fill=TR,width=11)

# ── cables cruzando ──
for y0,y1 in [(150,168),(196,182)]:
    d.line([0,y0,W,y1],fill=(18,26,20),width=2)

# ── la señal rosa: el único punto de color cálido ──
sx,sy=cx+128,214
d.polygon([(sx,sy),(sx+34,sy-7),(sx+37,sy+24),(sx+3,sy+31)],fill=PINK)
d.line([(sx+2,sy+2),(sx+35,sy+22)],fill=(212,128,164),width=2)

# ── barras de título ──
top=Image.new("RGB",(W,90),INK)
img.paste(top,(0,0))
bot=Image.new("RGB",(W,70),INK)
img.paste(bot,(0,H-70))

# ── tipografía ──
d.text((W//2,22),"SEÑALES",font=font(64,True),fill=GOLD,anchor="ma")
d.text((W//2,H-58),"EL UMBRAL DEL BARRIO",font=font(26,True),fill=CREAM,anchor="ma")
d.text((W//2,H-26),"Action-RPG narrativo · Godot 4 · Bit Hunter Dev",font=font(15),fill=(123,181,131),anchor="ma")

img.save("banner.png")
print("ok",img.size)
