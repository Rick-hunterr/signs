from PIL import Image, ImageDraw, ImageFont
import os, random, math
random.seed(23)

TILE = 8
MW, MH = 200, 150
MX, MY = 70, 210
W = MW*TILE + 140
H = MH*TILE + 210 + 350

BG=(14,12,24); INK=(8,6,16); CREAM=(238,232,246); GOLD=(217,178,76)
PINK=(242,166,195); VIOLET=(150,110,200); VIOLET_L=(190,158,235); TEAL=(120,200,180)
FLOOR=(48,36,78); FLOOR_D=(40,30,66); FLOOR_L=(60,46,94)
GLOW=(96,70,150); EDGE=(120,90,190)
GHOST=(74,60,110); GHOST_L=(94,78,136)
WATER=(60,90,140); THREAD=(226,206,140)
RED=(198,96,88); AMBER=(226,160,90)

img=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(img)
def font(s,b=False):
    p=("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if b else
       "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
    return ImageFont.truetype(p,s) if os.path.exists(p) else ImageFont.load_default()
F_T1=font(48,True); F_SUB=font(21); F_LBL=font(16,True); F_S=font(15); F_TT=font(12); F_TAG=font(13,True)

def px(tx,ty): return (MX+tx*TILE, MY+ty*TILE)
def rect(tx,ty,tw,th,f,o=None,ow=1):
    a=px(tx,ty); b=px(tx+tw,ty+th); d.rectangle([a[0],a[1],b[0],b[1]],fill=f,outline=o,width=ow)
def ell(tx,ty,tw,th,f,o=None,ow=1):
    a=px(tx,ty); b=px(tx+tw,ty+th); d.ellipse([a[0],a[1],b[0],b[1]],fill=f,outline=o,width=ow)
def line(pts,f,w=2):
    d.line([px(x,y) for x,y in pts],fill=f,width=w,joint="curve")
def checker(tx,ty,tw,th,c1,c2,st=4):
    for j in range(0,th,st):
        for i in range(0,tw,st):
            rect(tx+i,ty+j,min(st,tw-i),min(st,th-j), c1 if ((i//st)+(j//st))%2==0 else c2)

# ================= VACÍO DE FONDO =================
rect(0,0,MW,MH,(22,18,38))
for _ in range(260):                       # constelaciones
    x=random.randint(0,MW-1); y=random.randint(0,MH-1)
    c=random.choice([(120,110,170),(150,140,200),(90,84,130)])
    rect(x,y,1,1,c)

# ================= PLATAFORMAS FLOTANTES =================
def platform(tx,ty,tw,th,tone=0):
    base=[FLOOR,FLOOR_D,FLOOR_L][tone%3]
    rect(tx+1,ty+1,tw,th,(18,14,32))             # sombra/vacío debajo
    checker(tx,ty,tw,th,base,FLOOR_D if tone%2==0 else FLOOR_L,5)
    # borde luminoso
    rect(tx,ty,tw,1,EDGE); rect(tx,ty+th-1,tw,1,EDGE)
    rect(tx,ty,1,th,EDGE); rect(tx+tw-1,ty,1,th,EDGE)

def ghost_bldg(tx,ty,tw,th,solid=False):
    rect(tx,ty,tw,th,GHOST_L if solid else GHOST)
    rect(tx,ty,tw,1,VIOLET_L)
    for i in range(1,tw-1,3):                    # ventanas encendidas
        if random.random()<.55: rect(tx+i,ty+2,1,1,(214,190,120))

# ---- SUB-ZONA A · REVÉS DE PLAZA MAYOR (centro-izq, abierto) ----
platform(10,44,74,60,0)
# árbol invertido: copa hundida abajo, raíces abiertas hacia arriba
ell(36,80,22,18,(34,26,58)); ell(39,83,16,12,(28,22,50))
rect(46,68,3,13,(96,80,60))                      # tronco vertical
for a in range(200,341,20):                      # raíces hacia el cielo
    r=math.radians(a)
    line([(47,68),(47+math.cos(r)*15,68+math.sin(r)*15)],(130,110,180),2)
    line([(47+math.cos(r)*15,68+math.sin(r)*15),
          (47+math.cos(r)*20,68+math.sin(r)*20)],(100,84,146),1)
ell(43,84,9,7,VIOLET)
for x,y in [(14,48),(26,48),(58,48),(72,48),(14,96),(30,96),(60,96),(74,96)]:
    ghost_bldg(x,y,9,6)
line([(10,74),(84,74)],(70,56,110),1); line([(47,44),(47,104)],(70,56,110),1)

# ---- SUB-ZONA B · REVÉS DEL MERCADO (abajo-der, laberíntico) ----
platform(104,92,80,52,1)
random.seed(5)
for i in range(11):                              # muros del laberinto
    if i%2==0:
        x=108+i*6; rect(x,96,2,random.choice([16,24,32]),GHOST_L)
    else:
        y=98+i*4; rect(108,y,random.choice([20,34,46]),2,GHOST_L)
for x,y in [(112,100),(140,112),(166,104),(126,132),(158,134)]:
    rect(x,y,5,4,(96,60,60)); rect(x,y,5,1,AMBER)   # puestos fantasma
# el sótano espejado
rect(172,132,10,9,(30,22,44),VIOLET,2); rect(175,135,4,4,(16,12,26))

# ---- SUB-ZONA C · REVÉS DEL PARQUE (arriba-der, agua invertida) ----
platform(108,14,78,58,2)
rect(108,14,78,10,WATER)                          # agua ARRIBA
for j in range(14,24,2): rect(108,j,78,1,(48,74,120))
for i in range(112,184,7):                        # gotas cayendo hacia arriba
    line([(i,30),(i,24)],(90,130,180),1)
for x,y,s in [(116,34,9),(134,40,8),(152,32,9),(170,42,8),(124,54,8),(146,58,9),(166,56,8)]:
    ell(x,y,s,s,(44,80,66))                       # sauces sumergidos
    line([(x+s//2,y),(x+s//2,y-6)],(70,110,90),1)
ell(170,60,10,10,(38,70,58)); ell(173,63,4,4,VIOLET)   # espejo del sauce viejo

# ---- SUB-ZONA D · REVÉS DE ZONA ALTA (izq-arriba, tiempo inestable) ----
platform(8,8,76,28,1)
for i,(x,y,w,h) in enumerate([(12,12,10,7),(26,10,9,9),(39,13,11,6),(54,11,9,8),(68,12,10,7)]):
    ghost_bldg(x,y,w,h,solid=(i%2==0))
    if i%2:                                       # copia desfasada = tiempo inestable
        d.rectangle([px(x+2,y+2)[0],px(x+2,y+2)[1],px(x+w+2,y+h+2)[0],px(x+w+2,y+h+2)[1]],
                    outline=(110,90,160),width=1)
line([(8,24),(84,24)],(80,64,124),1)

# ================= EL TELAR (centro) =================
CX,CY,CR=94,58,26
platform(78,42,34,34,2)
ell(CX-CR//2,CY-CR//2,CR,CR,(30,24,54))
ell(CX-CR//2+3,CY-CR//2+3,CR-6,CR-6,(40,32,70))
for a in range(0,360,15):
    r=math.radians(a)
    line([(CX,CY),(CX+math.cos(r)*(CR//2+2),CY+math.sin(r)*(CR//2+2))],THREAD,1)
for rad in (6,9,12):
    ell(CX-rad,CY-rad,rad*2,rad*2,None if True else None)
    d.ellipse([px(CX-rad,CY-rad)[0],px(CX-rad,CY-rad)[1],px(CX+rad,CY+rad)[0],px(CX+rad,CY+rad)[1]],
              outline=THREAD,width=1)
ell(CX-3,CY-3,6,6,(250,238,180))

# hilos del Telar hacia cada anclaje/sub-zona
for tx,ty in [(47,79),(146,44),(144,118),(46,20),(178,64),(120,136)]:
    line([(CX,CY),(tx,ty)],(150,132,90),1)

# ================= PASAJES DE RESONANCIA =================
def bridge(pts):
    line(pts,(70,56,110),5); line(pts,VIOLET,2)
bridge([(84,74),(94,66)])          # Plaza  -> Telar
bridge([(94,50),(108,40)])         # Telar  -> Parque
bridge([(104,72),(112,92)])        # Telar  -> Mercado
bridge([(84,30),(94,50)])          # ZAlta  -> Telar
bridge([(84,20),(108,20)])         # ZAlta  -> Parque (alto)

# ================= GRIETAS DE ENTRADA (desde el mundo real) =================
def portal(tx,ty,label,side="r"):
    ell(tx-3,ty-3,7,7,(30,24,52))
    ell(tx-2,ty-2,5,5,VIOLET)
    ell(tx-1,ty-1,3,3,(220,200,250))
    x,y=px(tx,ty); tw=d.textlength(label,font=F_TT)
    if side=="r":
        d.rectangle([x+10,y-9,x+10+tw+10,y+9],fill=INK)
        d.text((x+15,y),label,font=F_TT,fill=VIOLET_L,anchor="lm")
    else:
        d.rectangle([x-10-tw-10,y-9,x-10,y+9],fill=INK)
        d.text((x-15,y),label,font=F_TT,fill=VIOLET_L,anchor="rm")

portal(47,104,"← grieta Plaza Mayor","r")
portal(178,66,"← sauce viejo (Acto II)","l")
portal(176,140,"← sótano Mercado","l")
portal(46,10,"← Zona Alta (sin grieta)","r")

# ================= MARCADORES =================
def marker(tx,ty,color,label,side="r"):
    x,y=px(tx,ty); tw=d.textlength(label,font=F_TAG)
    if side=="r":
        d.rectangle([x+11,y-10,x+11+tw+12,y+10],fill=INK)
        d.text((x+17,y),label,font=F_TAG,fill=color,anchor="lm")
    else:
        d.rectangle([x-11-tw-12,y-10,x-11,y+10],fill=INK)
        d.text((x-17,y),label,font=F_TAG,fill=color,anchor="rm")
    d.ellipse([x-8,y-8,x+8,y+8],fill=color,outline=INK,width=2)

marker(CX,CY-20,GOLD,"EL TELAR · diario de Carmen","r")
marker(CX+11,CY+14,GOLD,"A5 anclaje","r")
marker(66,52,PINK,"S7 señal","l")
marker(150,120,PINK,"S8* señal","l")
marker(24,96,RED,"JEFE II · El Olvido","r")
marker(60,110,TEAL,"1er encuentro con Pablo","r")

# guardianes
def guard(tx,ty,label,side="r"):
    x,y=px(tx,ty); tw=d.textlength(label,font=F_TT)
    d.polygon([(x,y-9),(x+9,y),(x,y+9),(x-9,y)],fill=AMBER,outline=INK)
    if side=="r":
        d.rectangle([x+12,y-9,x+12+tw+10,y+9],fill=INK); d.text((x+17,y),label,font=F_TT,fill=AMBER,anchor="lm")
    else:
        d.rectangle([x-12-tw-10,y-9,x-12,y+9],fill=INK); d.text((x-17,y),label,font=F_TT,fill=AMBER,anchor="rm")

guard(116,72,"Tejedor Ciego","r")
guard(150,100,"Centinela de Piedra","l")
guard(140,26,"Pájaros de Tinta","r")
guard(178,52,"Memoria de Agua","l")

# ================= ETIQUETAS DE SUB-ZONA =================
def zlabel(tx,ty,letra,name):
    x,y=px(tx,ty); tw=d.textlength(name,font=F_LBL)
    d.rectangle([x,y,x+tw+34,y+28],fill=INK)
    d.ellipse([x+6,y+6,x+22,y+22],fill=VIOLET)
    d.text((x+14,y+14),letra,font=F_TT,fill=INK,anchor="mm")
    d.text((x+30,y+7),name,font=F_LBL,fill=CREAM)

zlabel(8,0,"D","REVÉS ZONA ALTA · tiempo inestable")
zlabel(108,4,"C","REVÉS DEL PARQUE · agua arriba")
zlabel(10,36,"A","REVÉS DE PLAZA MAYOR · abierto")
zlabel(104,84,"B","REVÉS DEL MERCADO · laberíntico")

# ================= GRILLA =================
for i in range(0,MW+1,25):
    a=px(i,0); b=px(i,MH); d.line([a[0],a[1],b[0],b[1]],fill=(40,34,62),width=1)
    d.text((a[0],MY-18),str(i),font=F_TT,fill=(130,118,170),anchor="ma")
for j in range(0,MH+1,25):
    a=px(0,j); b=px(MW,j); d.line([a[0],a[1],b[0],b[1]],fill=(40,34,62),width=1)
    d.text((MX-12,a[1]),str(j),font=F_TT,fill=(130,118,170),anchor="rm")
d.rectangle([px(0,0)[0],px(0,0)[1],px(MW,MH)[0],px(MW,MH)[1]],outline=VIOLET,width=3)

# ================= HEADER =================
d.rectangle([0,0,W,168],fill=INK)
d.text((W//2,30),"EL REVÉS — MAQUETA",font=F_T1,fill=VIOLET_L,anchor="ma")
d.text((W//2,88),"200×150 tiles de 32px  ·  dimensión espejo  ·  SEÑALES v3.0",font=F_SUB,fill=(150,130,200),anchor="ma")
d.text((W//2,122),"Las sub-zonas son islas flotantes sobre el vacío, unidas por Pasajes de Resonancia (cuestan energía).",
       font=F_S,fill=(130,116,170),anchor="ma")
d.text((W//2,146),"La geografía es reconocible pero está mal: el árbol tiene las raíces al cielo y el agua del canal corre por arriba.",
       font=F_S,fill=(130,116,170),anchor="ma")

# ================= LEYENDA =================
LY=MY+MH*TILE+40
d.rounded_rectangle([70,LY,W-70,LY+270],radius=12,fill=(26,20,44),outline=VIOLET,width=3)
d.text((100,LY+16),"CÓMO LEER ESTA MAQUETA",font=F_LBL,fill=VIOLET_L)

c1=[("Suelo","translúcido, brilla desde abajo · borde luminoso = límite de plataforma"),
    ("Fuera del borde","EL VACÍO. Caer = muerte + resurrección en anclaje"),
    ("Pasajes violeta","Pasajes de Resonancia entre sub-zonas · consumen energía"),
    ("Hilos dorados","el Telar conecta todos los Anclajes del barrio real")]
c2=[("Portales","grietas de entrada desde el mundo real (Actos II-III)"),
    ("Rombo ámbar","los 4 Guardianes · neutrales hasta que se los molesta"),
    ("Rosa","señales 7 y 8*  ·  Dorado: Telar y Anclaje 5"),
    ("Temperatura","Ánimo bajo = más oscuro y hostil · Ánimo alto = más luminoso")]
yy=LY+52
for k,v in c1:
    d.text((100,yy),k,font=F_TAG,fill=CREAM); d.text((270,yy),v,font=F_S,fill=(180,168,210)); yy+=34
yy=LY+52
for k,v in c2:
    d.text((W//2+40,yy),k,font=F_TAG,fill=CREAM); d.text((W//2+210,yy),v,font=F_S,fill=(180,168,210)); yy+=34
d.text((W//2,LY+228),"Regla de diseño: cada sub-zona espeja una zona real. Si algo no existe arriba, no existe acá.",
       font=F_S,fill=(140,126,180),anchor="ma")

img.save("SENALES_maqueta_reves.png")
print("ok",img.size)
