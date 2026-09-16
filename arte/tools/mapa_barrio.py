from PIL import Image, ImageDraw, ImageFont
import os, random
random.seed(11)

TILE = 8
MW, MH = 250, 180
MX, MY = 70, 200
W = MW*TILE + 140
H = MH*TILE + 200 + 340

BG=(18,26,22); INK=(12,18,14); CREAM=(246,239,220); GOLD=(217,178,76)
PINK=(242,166,195); VIOLET=(150,110,200); TEAL=(120,200,180)
ASPHALT=(78,82,80); ASPH_D=(64,68,66); SIDE=(176,170,152)
PLAZA=(198,184,150); PLAZA_D=(184,170,136)
GRASS=(86,126,78); GRASS_D=(72,110,66); GRASS_L=(102,142,88)
DIRT=(150,124,92); WATER=(70,116,140); WATER_D=(58,100,124)
ROOF_A=(168,96,74); ROOF_B=(150,146,132); ROOF_C=(128,118,104); ROOF_D=(146,110,88)
WALL=(206,196,174); TREE=(58,96,58); TREE_L=(78,122,72); TREE_BIG=(44,84,48)
TARP=[(196,110,110),(196,176,110),(110,150,180),(170,150,190),(200,190,160),(150,180,150)]

img = Image.new("RGB",(W,H),BG); d = ImageDraw.Draw(img)
def font(s,b=False):
    p=("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if b else
       "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
    return ImageFont.truetype(p,s) if os.path.exists(p) else ImageFont.load_default()
F_T1=font(48,True); F_SUB=font(21); F_LBL=font(16,True); F_S=font(15); F_TT=font(12); F_TAG=font(13,True)

def px(tx,ty): return (MX+tx*TILE, MY+ty*TILE)
def rect(tx,ty,tw,th,f,o=None,ow=1):
    a=px(tx,ty); b=px(tx+tw,ty+th); d.rectangle([a[0],a[1],b[0],b[1]],fill=f,outline=o,width=ow)
def ell(tx,ty,tw,th,f):
    a=px(tx,ty); b=px(tx+tw,ty+th); d.ellipse([a[0],a[1],b[0],b[1]],fill=f)
def checker(tx,ty,tw,th,c1,c2,st=4):
    for j in range(0,th,st):
        for i in range(0,tw,st):
            rect(tx+i,ty+j,min(st,tw-i),min(st,th-j), c1 if ((i//st)+(j//st))%2==0 else c2)

# ============ BASE ============
rect(0,0,MW,MH,GRASS_D)

# ============ CALLES ============
def road_h(x,w,y,h):
    rect(x,y,w,h,ASPHALT); rect(x,y-3,w,3,SIDE); rect(x,y+h,w,3,SIDE)
    for i in range(x,x+w,8): rect(i,y+h//2,4,1,(150,150,140))
def road_v(x,y,h,w):
    rect(x,y,w,h,ASPHALT); rect(x-3,y,3,h,SIDE); rect(x+w,y,3,h,SIDE)
    for j in range(y,y+h,8): rect(x+w//2,j,1,4,(150,150,140))

# ============ BANDA 1 · ZONA ALTA (y 0-56) ============
rect(0,0,MW,56,GRASS_L)
for y in (10,24,38,50): road_h(6,232,y,4)
for x in (26,58,90,122,154,186): road_v(x,0,56,4)

def bldg(tx,ty,tw,th,roof,shadow=True):
    if shadow: rect(tx+1,ty+1,tw,th,(42,54,46))
    rect(tx,ty,tw,th,roof); rect(tx,ty,tw,2,WALL)
    if tw>=6: rect(tx+tw-3,ty+2,2,2,(178,178,176))     # tanque de agua
    if tw>=8: rect(tx+2,ty+2,2,1,(160,160,158))        # AC

for ry,rh in [(2,6),(16,6),(30,6),(44,4)]:
    x=8
    while x < 236:
        if random.random()<0.16:                      # patio interno / baldío
            gw=random.choice([6,8])
            if x+gw<236:
                checker(x,ry,gw,rh,GRASS,GRASS_D,3)
                ell(x+1,ry+1,3,3,TREE)
            x+=gw+4; continue
        w=random.choice([9,11,13]); hh=rh+random.choice([0,0,2])
        if x+w>236: break
        bldg(x,ry,w,hh,[ROOF_C,ROOF_B,ROOF_A,ROOF_D][random.randint(0,3)])
        x+=w+random.choice([3,4,5])

# --- EL MIRADOR ---
bldg(198,12,14,20,ROOF_C); bldg(228,12,14,20,ROOF_C)
rect(214,14,13,20,(186,182,172))                       # plataforma
rect(214,14,13,2,(120,116,108))
for i in range(0,13,2): rect(214+i,33,1,2,(112,108,100))   # baranda
for j in range(9):                                          # escalera oculta
    rect(217,35+j,7,1,(170,164,152) if j%2==0 else (152,146,136))
rect(216,44,9,10,(96,120,92))
d.rectangle([px(214,12)[0]-4,px(214,12)[1]-4,px(227,34)[0]+4,px(227,34)[1]+4],outline=GOLD,width=3)

# barranca
rect(0,56,MW,4,(120,104,80))
for i in range(0,MW,4): rect(i,56,2,4,(102,86,66))
for i in range(0,MW,16): rect(i,58,3,3,(88,74,58))

# ============ BANDA 2 · MEDIA LADERA (y 62-118) ============
road_h(0,MW,60,4)
road_h(0,MW,118,4)
road_v(122,60,62,4)
road_v(62,64,54,3)

# --- RESIDENCIAL (x 0-118) ---
def house(tx,ty,tw,th,roof):
    rect(tx+1,ty+1,tw,th,(48,66,52)); rect(tx,ty,tw,th,roof); rect(tx,ty+th-2,tw,2,WALL)
def block(bx,by,bw,bh):
    checker(bx,by,bw,bh,GRASS,GRASS_D,5)
    y=by+2
    while y+8<=by+bh:
        x=bx+2
        while x+10<=bx+bw:
            house(x,y,9,6,[ROOF_A,ROOF_B,ROOF_C,ROOF_A,ROOF_D][random.randint(0,4)])
            x+=12
        y+=10

block(4,66,54,48); block(68,66,48,48)
# CASA TORRES destacada
d.rectangle([px(6,68)[0]-4,px(6,68)[1]-4,px(15,74)[0]+4,px(15,74)[1]+4],outline=GOLD,width=3)
rect(6,68,9,6,(176,104,80)); rect(6,73,9,1,WALL)
rect(6,75,9,5,GRASS)                                    # patio
# arboles de vereda
for x in range(6,118,9):
    ell(x,116,4,4,TREE); rect(x,120,3,1,(120,100,74))
    ell(x,62,3,3,TREE)

# --- PARQUE RIBEREÑO (x 128-250) ---
rect(128,64,108,52,GRASS)
checker(128,64,108,52,GRASS,GRASS_L,6)
rect(132,88,96,3,DIRT)                                  # sendero principal
for i in range(132,228,4): rect(i,88,2,3,(162,136,102))
rect(160,66,3,48,DIRT); rect(200,70,3,44,DIRT)
# canal
rect(238,60,10,60,(160,156,146))
rect(240,60,6,60,WATER)
for j in range(60,120,3): rect(240,j,6,1,WATER_D)
rect(238,84,10,4,(150,144,132))                          # puente
# sauces
for i,(x,y,s) in enumerate([(134,68,7),(150,72,6),(168,66,7),(186,70,6),(206,68,7),(222,72,6),
                            (138,98,6),(156,102,7),(176,96,6),(196,100,7),(214,98,6),(228,104,6),
                            (144,84,5),(190,86,5)]):
    ell(x,y,s,s,TREE_L if i%2 else TREE)
# SAUCE VIEJO — grieta al Reves
ell(224,108,10,10,TREE_BIG); ell(227,111,4,4,VIOLET)
# bancos
for x,y in [(140,86),(164,86),(188,86),(212,86),(150,94),(180,94),(206,94)]:
    rect(x,y,4,2,(120,104,80))

# ============ BANDA 3 · CENTRO (y 122-180) ============
road_h(0,MW,150,4)
road_v(78,122,58,4)
road_v(170,122,58,4)
road_v(38,150,30,3)

# --- PLAZA MAYOR (x 84-166) ---
rect(84,124,82,50,PLAZA)
checker(84,124,82,50,PLAZA,PLAZA_D,5)
for i in range(0,25):                                    # senderos diagonales
    rect(84+i*1,124+i,3,1,(212,200,168)); rect(165-i,124+i,3,1,(212,200,168))
rect(84,146,82,3,(212,200,168))
# EL ARBOL
TX,TY=112,136
ell(TX-3,TY-3,28,28,(30,60,36))
ell(TX-1,TY-1,24,24,(38,72,42))
ell(TX+1,TY+1,20,20,TREE_BIG)
ell(TX+4,TY+4,13,13,TREE)
ell(TX+7,TY+7,7,7,TREE_L)
rect(TX+9,TY+9,4,4,(96,74,52))
for a in [(-4,9),(23,10),(9,-4),(10,23),(-2,18),(21,3),(3,21),(18,-2)]:
    rect(TX+a[0],TY+a[1],5,2,(120,100,74))
# fuente seca
ell(140,156,13,13,(188,180,164)); ell(144,160,5,5,(150,144,130))
for x,y in [(90,130),(90,166),(156,130),(156,166),(100,170),(148,128),(120,168)]:
    rect(x,y,5,2,(96,124,90))
for x in [88,96,152,160]: ell(x,126,4,4,TREE)

# --- CALLE PRINCIPAL (x 0-74) ---
for ry,rh in [(124,10),(138,9),(156,10),(170,8)]:
    x=2
    lim = 60 if ry==156 else 74
    while x+11<=lim:
        bldg(x,ry,random.choice([9,11,12]),rh,[ROOF_A,ROOF_C,ROOF_B,ROOF_D][random.randint(0,3)])
        x+=14
# KIOSCO DE CHINO (esquina)
rect(62,154,12,9,(190,150,90)); rect(61,163,14,2,(224,194,124))
rect(64,156,3,2,(120,100,74))
d.rectangle([px(62,154)[0]-4,px(62,154)[1]-4,px(74,165)[0]+4,px(74,165)[1]+4],outline=TEAL,width=3)
# callejon del 1er Eco
rect(26,134,4,8,ASPH_D)
for x in range(4,74,10):
    ell(x,146,4,4,TREE); rect(x-1,150,3,1,(120,100,74))

# --- MERCADO VIEJO (x 174-250) ---
rect(174,150,74,30,(170,110,92))
checker(174,150,74,30,(170,110,92),(158,100,84),4)
for r,yy in enumerate([152,160,168,176]):
    for c in range(9):
        x=176+c*8
        if x+7>246: break
        rect(x,yy,7,6,TARP[(r+c)%len(TARP)]); rect(x,yy,7,1,(88,78,68))
for i,(x,y,w,h) in enumerate([(174,132,16,12),(194,132,14,12),(212,132,16,12),(232,132,14,12)]):
    bldg(x,y,w,h,[ROOF_A,ROOF_C][i%2])
# SOTANO
rect(240,172,8,7,(58,52,46)); rect(242,174,4,4,(38,34,30))

# ============ CABLES ============
for y in (59,121,149):
    a=px(0,y); b=px(MW,y); d.line([a[0],a[1],b[0],b[1]],fill=(48,52,50),width=1)
for x in (78,170):
    a=px(x,122); b=px(x,180); d.line([a[0],a[1],b[0],b[1]],fill=(48,52,50),width=1)

# ============ GRIETAS AL REVES ============
def crack(pts,w=3):
    d.line([px(x,y) for x,y in pts],fill=VIOLET,width=w,joint="curve")
crack([(122,126),(118,134),(124,142),(119,150),(125,160),(121,172)])
crack([(226,110),(231,116),(226,120)])
crack([(242,170),(238,176),(244,179)])
crack([(210,20),(205,30),(212,40),(207,52)])
crack([(60,60),(56,68),(62,76)])

# ============ MARCADORES ============
def marker(tx,ty,color,label,side="r"):
    x,y=px(tx,ty); tw=d.textlength(label,font=F_TAG)
    if side=="r":
        d.rectangle([x+11,y-10,x+11+tw+12,y+10],fill=INK)
        d.text((x+17,y),label,font=F_TAG,fill=color,anchor="lm")
    else:
        d.rectangle([x-11-tw-12,y-10,x-11,y+10],fill=INK)
        d.text((x-17,y),label,font=F_TAG,fill=color,anchor="rm")
    d.ellipse([x-8,y-8,x+8,y+8],fill=color,outline=INK,width=2)

for tx,ty,l,s in [(10,80,"S1 Graciela","r"),(146,162,"S2 vinilo","r"),(48,132,"S3 Marta","r"),
                  (186,78,"S4 parque","r"),(240,166,"S5 sótano","l"),(206,158,"S6*","l"),
                  (150,100,"S7 Revés","r"),(214,46,"S9 escalón","l")]:
    marker(tx,ty,PINK,l,s)
for tx,ty,l,s in [(8,78,"A0","l"),(142,158,"A2","l"),(180,150,"A3","r"),(196,90,"A4","r")]:
    marker(tx,ty,GOLD,l,s)
marker(244,178,VIOLET,"JEFE I","l")
marker(220,10,VIOLET,"JEFE III","l")
marker(228,113,VIOLET,"grieta","r")

# ============ ETIQUETAS ============
def zlabel(tx,ty,n,name):
    x,y=px(tx,ty); tw=d.textlength(name,font=F_LBL)
    d.rectangle([x,y,x+tw+34,y+28],fill=INK)
    d.ellipse([x+6,y+6,x+22,y+22],fill=GOLD)
    d.text((x+14,y+14),n,font=F_TT,fill=INK,anchor="mm")
    d.text((x+30,y+7),name,font=F_LBL,fill=CREAM)

zlabel(2,2,"5","ZONA ALTA")
zlabel(196,2,"7","EL MIRADOR")
zlabel(2,64,"0","RESIDENCIAL / CASA TORRES")
zlabel(128,64,"4","PARQUE RIBEREÑO")
zlabel(84,124,"2","PLAZA MAYOR")
zlabel(2,174,"1","CALLE PRINCIPAL")
zlabel(174,144,"3","MERCADO VIEJO")

# ============ GRILLA ============
for i in range(0,MW+1,25):
    a=px(i,0); b=px(i,MH); d.line([a[0],a[1],b[0],b[1]],fill=(44,56,48),width=1)
    d.text((a[0],MY-18),str(i),font=F_TT,fill=(120,140,122),anchor="ma")
for j in range(0,MH+1,20):
    a=px(0,j); b=px(MW,j); d.line([a[0],a[1],b[0],b[1]],fill=(44,56,48),width=1)
    d.text((MX-12,a[1]),str(j),font=F_TT,fill=(120,140,122),anchor="rm")
d.rectangle([px(0,0)[0],px(0,0)[1],px(MW,MH)[0],px(MW,MH)[1]],outline=GOLD,width=3)

# ============ HEADER ============
d.rectangle([0,0,W,158],fill=INK)
d.text((W//2,32),"BARRIO SAUCO — MAQUETA v2",font=F_T1,fill=GOLD,anchor="ma")
d.text((W//2,90),"250×180 tiles de 32px  ·  ≈8000×5760 px de mundo  ·  blockout para TileMapLayers en Godot",
       font=F_SUB,fill=(123,181,131),anchor="ma")
d.text((W//2,122),"El Revés se construye aparte, en su propio set de escenas (~200×150 tiles)",
       font=F_S,fill=(150,175,152),anchor="ma")

# ============ LEYENDA ============
LY = MY + MH*TILE + 40
d.rounded_rectangle([70,LY,W-70,LY+250],radius=12,fill=(26,38,30),outline=GOLD,width=3)
d.text((100,LY+16),"REFERENCIA DE ZONAS Y TAMAÑOS",font=F_LBL,fill=GOLD)

c1=[("Zona 5 · Zona Alta","x 0-250 · y 0-56   —  calles angostas, edificios 40s"),
    ("Zona 7 · Mirador","x 198-242 · y 12-54  —  plataforma + escalera oculta"),
    ("Zona 0 · Residencial","x 0-118 · y 64-118  —  Casa Torres en recuadro dorado"),
    ("Zona 4 · Parque","x 128-248 · y 64-118  —  sauce viejo = 1ª grieta")]
c2=[("Zona 2 · Plaza Mayor","x 84-166 · y 124-174  —  el árbol es el foco del mapa"),
    ("Zona 1 · Calle Principal","x 0-76 · y 124-180  —  kiosco de Chino en turquesa"),
    ("Zona 3 · Mercado Viejo","x 174-248 · y 132-180  —  sótano abajo a la derecha"),
    ("Marcadores","rosa = señales · dorado = anclajes · violeta = grietas y jefes")]
yy=LY+52
for k,v in c1:
    d.text((100,yy),k,font=F_TAG,fill=CREAM); d.text((300,yy),v,font=F_S,fill=(190,206,190)); yy+=34
yy=LY+52
for k,v in c2:
    d.text((W//2+60,yy),k,font=F_TAG,fill=CREAM); d.text((W//2+280,yy),v,font=F_S,fill=(190,206,190)); yy+=34
d.text((W//2,LY+218),"Cada zona es su propia escena .tscn conectada por puertas. La maqueta define posición y proporción, no el arte final.",
       font=F_S,fill=(150,175,152),anchor="ma")

img.save("SENALES_maqueta_mapa_v2.png")
print("ok",img.size)
