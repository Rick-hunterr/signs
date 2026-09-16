from PIL import Image, ImageDraw, ImageFont
import os, random

# =====================================================================
#  SEÑALES — Hojas de zona
#  Una hoja por zona, al tamaño real de construcción en Godot.
#  Cada hoja trae: grilla numerada, capas, tiles interactuables y NPCs.
# =====================================================================

TILE = 16          # px por tile EN LA HOJA (no en el juego)

BG=(18,26,22); INK=(12,18,14); CREAM=(246,239,220); GOLD=(217,178,76)
PINK=(242,166,195); VIOLET=(150,110,200); TEAL=(120,200,180)
BLUE=(140,190,210); RED=(198,96,88); AMBER=(226,160,90)
ASPHALT=(78,82,80); ASPH_D=(64,68,66); SIDE=(176,170,152); SIDE_D=(160,154,138)
PLAZA=(198,184,150); PLAZA_D=(184,170,136)
GRASS=(86,126,78); GRASS_D=(72,110,66); GRASS_L=(102,142,88)
DIRT=(150,124,92); WATER=(70,116,140); WATER_D=(58,100,124)
ROOF_A=(168,96,74); ROOF_B=(150,146,132); ROOF_C=(128,118,104); ROOF_D=(146,110,88)
WALL=(206,196,174); WOOD=(120,100,74); TILEFLOOR=(170,110,92)
TREE=(58,96,58); TREE_L=(78,122,72); TREE_BIG=(44,84,48)
TARP=[(196,110,110),(196,176,110),(110,150,180),(170,150,190),(200,190,160),(150,180,150)]

def font(s,b=False):
    p=("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if b else
       "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
    return ImageFont.truetype(p,s) if os.path.exists(p) else ImageFont.load_default()
F_T1=font(38,True); F_SUB=font(19); F_LBL=font(15,True); F_S=font(14); F_TT=font(11); F_TAG=font(12,True)


class Sheet:
    """Una hoja de zona: mapa + grilla + tabla de interactuables."""
    def __init__(self, num, name, subtitle, mw, mh, n_items=0, n_npcs=0):
        self.num, self.name, self.sub = num, name, subtitle
        self.MW, self.MH = mw, mh
        self.MX, self.MY = 78, 190
        rows = max(n_items, n_npcs)
        self.table_h = 130 + rows*26
        self.W = max(mw*TILE + 150, 1320)
        self.H = mh*TILE + 190 + self.table_h + 60
        self.img = Image.new("RGB",(self.W,self.H),BG)
        self.d = ImageDraw.Draw(self.img)
        self.items = []   # (n, tx, ty, tipo, detalle)
        self.npcs  = []   # (letra, tx, ty, nombre, detalle)

    # ---- primitivas en coordenadas de TILE ----
    def px(self,tx,ty): return (self.MX+tx*TILE, self.MY+ty*TILE)
    def rect(self,tx,ty,tw,th,f,o=None,ow=1):
        a=self.px(tx,ty); b=self.px(tx+tw,ty+th)
        self.d.rectangle([a[0],a[1],b[0],b[1]],fill=f,outline=o,width=ow)
    def ell(self,tx,ty,tw,th,f,o=None,ow=1):
        a=self.px(tx,ty); b=self.px(tx+tw,ty+th)
        self.d.ellipse([a[0],a[1],b[0],b[1]],fill=f,outline=o,width=ow)
    def line(self,pts,f,w=2):
        self.d.line([self.px(x,y) for x,y in pts],fill=f,width=w,joint="curve")
    def checker(self,tx,ty,tw,th,c1,c2,st=2):
        for j in range(0,th,st):
            for i in range(0,tw,st):
                self.rect(tx+i,ty+j,min(st,tw-i),min(st,th-j),
                          c1 if ((i//st)+(j//st))%2==0 else c2)

    # ---- helpers de escenario ----
    def road_h(self,x,w,y,h,side=True):
        self.rect(x,y,w,h,ASPHALT)
        if side: self.rect(x,y-2,w,2,SIDE); self.rect(x,y+h,w,2,SIDE)
        for i in range(x,x+w,6): self.rect(i,y+h//2,3,1,(150,150,140))
    def road_v(self,x,y,h,w,side=True):
        self.rect(x,y,w,h,ASPHALT)
        if side: self.rect(x-2,y,2,h,SIDE); self.rect(x+w,y,2,h,SIDE)
        for j in range(y,y+h,6): self.rect(x+w//2,j,1,3,(150,150,140))
    def bldg(self,tx,ty,tw,th,roof,tank=True):
        self.rect(tx+1,ty+1,tw,th,(40,52,44))
        self.rect(tx,ty,tw,th,roof); self.rect(tx,ty,tw,1,WALL)
        if tank and tw>=5: self.rect(tx+tw-2,ty+1,1,1,(178,178,176))
    def tree(self,tx,ty,s=3,c=None):
        self.ell(tx,ty,s,s,c or TREE)

    # ---- marcadores ----
    def item(self,n,tx,ty,tipo,detalle):
        self.items.append((n,tx,ty,tipo,detalle))
        x,y=self.px(tx+0.5,ty+0.5)
        col={"dialogo":PINK,"puerta":TEAL,"senal":PINK,"zona_revers":VIOLET,
             "anclaje":GOLD,"item":AMBER,"jefe":RED}.get(tipo,CREAM)
        self.d.rectangle([x-11,y-11,x+11,y+11],fill=INK,outline=col,width=2)
        self.d.text((x,y),str(n),font=F_TAG,fill=col,anchor="mm")
    def npc(self,letra,tx,ty,nombre,detalle):
        self.npcs.append((letra,tx,ty,nombre,detalle))
        x,y=self.px(tx+0.5,ty+0.5)
        self.d.ellipse([x-11,y-11,x+11,y+11],fill=BLUE,outline=INK,width=2)
        self.d.text((x,y),letra,font=F_TAG,fill=INK,anchor="mm")
    def collision(self,tx,ty,tw,th):
        a=self.px(tx,ty); b=self.px(tx+tw,ty+th)
        self.d.rectangle([a[0],a[1],b[0],b[1]],outline=(210,90,90),width=2)

    # ---- render final ----
    def finish(self, notas=""):
        d=self.d
        # grilla cada 5 tiles
        for i in range(0,self.MW+1,5):
            a=self.px(i,0); b=self.px(i,self.MH)
            w = 2 if i%10==0 else 1
            c = (58,74,62) if i%10==0 else (40,52,44)
            d.line([a[0],a[1],b[0],b[1]],fill=c,width=w)
            if i%10==0: d.text((a[0],self.MY-16),str(i),font=F_TT,fill=(120,140,122),anchor="ma")
        for j in range(0,self.MH+1,5):
            a=self.px(0,j); b=self.px(self.MW,j)
            w = 2 if j%10==0 else 1
            c = (58,74,62) if j%10==0 else (40,52,44)
            d.line([a[0],a[1],b[0],b[1]],fill=c,width=w)
            if j%10==0: d.text((self.MX-10,a[1]),str(j),font=F_TT,fill=(120,140,122),anchor="rm")
        a=self.px(0,0); b=self.px(self.MW,self.MH)
        d.rectangle([a[0],a[1],b[0],b[1]],outline=GOLD,width=3)

        # header
        d.rectangle([0,0,self.W,150],fill=INK)
        d.ellipse([40,44,88,92],fill=GOLD)
        d.text((64,68),str(self.num),font=F_T1,fill=INK,anchor="mm")
        d.text((106,44),self.name,font=F_T1,fill=GOLD)
        d.text((108,94),self.sub,font=F_SUB,fill=(123,181,131))
        d.text((self.W-40,52),f"{self.MW}×{self.MH} tiles",font=F_LBL,fill=CREAM,anchor="ra")
        d.text((self.W-40,78),f"{self.MW*32}×{self.MH*32} px  ·  tile 32px",font=F_S,fill=(150,175,152),anchor="ra")
        d.text((self.W-40,102),"grilla cada 5 tiles · líneas gruesas cada 10",font=F_TT,fill=(120,140,122),anchor="ra")

        # tabla
        ty0 = self.MY + self.MH*TILE + 30
        d.rounded_rectangle([70,ty0,self.W-70,ty0+self.table_h-20],radius=10,
                            fill=(26,38,30),outline=GOLD,width=2)
        colx = 96
        d.text((colx,ty0+14),"TILES INTERACTUABLES",font=F_LBL,fill=GOLD)
        yy=ty0+44
        d.text((colx,yy),"#",font=F_TAG,fill=(140,165,142))
        d.text((colx+30,yy),"coord",font=F_TAG,fill=(140,165,142))
        d.text((colx+110,yy),"tipo",font=F_TAG,fill=(140,165,142))
        d.text((colx+210,yy),"detalle",font=F_TAG,fill=(140,165,142))
        yy+=22
        for n,tx,tyy,tipo,det in self.items:
            col={"dialogo":PINK,"puerta":TEAL,"senal":PINK,"zona_revers":VIOLET,
                 "anclaje":GOLD,"item":AMBER,"jefe":RED}.get(tipo,CREAM)
            d.text((colx,yy),str(n),font=F_S,fill=col)
            d.text((colx+30,yy),f"({tx},{tyy})",font=F_S,fill=(200,214,200))
            d.text((colx+110,yy),tipo,font=F_S,fill=col)
            d.text((colx+210,yy),det,font=F_S,fill=(190,206,190))
            yy+=26

        if self.npcs:
            cx2 = self.W//2 + 90
            d.text((cx2,ty0+14),"NPCs Y NODOS",font=F_LBL,fill=BLUE)
            yy=ty0+44
            d.text((cx2,yy),"·",font=F_TAG,fill=(140,165,142))
            d.text((cx2+30,yy),"coord",font=F_TAG,fill=(140,165,142))
            d.text((cx2+110,yy),"nombre",font=F_TAG,fill=(140,165,142))
            yy+=22
            for l,tx,tyy,nom,det in self.npcs:
                d.text((cx2,yy),l,font=F_S,fill=BLUE)
                d.text((cx2+30,yy),f"({tx},{tyy})",font=F_S,fill=(200,214,200))
                d.text((cx2+110,yy),nom,font=F_S,fill=CREAM)
                d.text((cx2+240,yy),det,font=F_S,fill=(190,206,190))
                yy+=26

        if notas:
            d.text((96,ty0+self.table_h-58),notas,font=F_S,fill=(150,175,152))

        fn=f"zona{self.num}_{self.name.lower().replace(' ','_').replace('ñ','n').replace('é','e').replace('á','a')}.png"
        self.img.save(fn)
        print("→",fn,self.img.size)


# =====================================================================
# ZONA 0 — CASA TORRES  (interior, 40×30)
# =====================================================================
def zona0():
    s=Sheet(0,"Casa Torres","interior · 4 ambientes + patio · Anclaje 0",40,30,7,3)
    s.rect(0,0,40,30,(30,42,34))
    # muros exteriores
    s.rect(2,2,34,24,(112,96,76))
    s.rect(3,3,32,22,(186,176,156))            # piso general
    # divisiones
    s.rect(15,3,1,12,(112,96,76))              # vertical arriba
    s.rect(3,14,13,1,(112,96,76))              # horizontal izq
    s.rect(16,14,19,1,(112,96,76))             # horizontal der
    s.rect(25,15,1,10,(112,96,76))
    # cuarto de Uma (arriba izq)
    s.checker(4,4,11,9,(176,166,146),(168,158,138),2)
    s.rect(4,4,4,6,(150,120,140)); s.rect(4,4,4,1,(190,160,180))   # cama
    s.rect(11,4,4,2,WOOD)                                          # escritorio
    s.rect(11,8,3,5,(140,120,96))                                  # estante discos
    s.rect(15,8,1,3,(120,170,200))                                 # ventana
    # living (arriba der)
    s.checker(17,4,17,9,(180,170,150),(172,162,142),2)
    s.rect(18,5,6,3,(120,100,120))                                 # sofá
    s.rect(28,5,4,2,(90,80,70))                                    # tv
    s.ell(25,9,3,3,TREE_L)                                         # planta
    # cocina (abajo izq)
    s.checker(4,16,11,8,(190,182,168),(182,174,160),2)
    s.rect(4,16,7,2,(160,150,140))                                 # mesada
    s.rect(12,16,3,3,(200,196,190))                                # heladera
    s.rect(6,20,5,3,WOOD)                                          # mesa
    # patio (abajo der)
    s.checker(27,16,8,8,GRASS,GRASS_D,2)
    s.rect(28,17,2,2,(150,100,80)); s.rect(31,19,2,2,(150,100,80)) # macetas
    s.rect(28,22,6,1,(180,180,175))                                # soga de ropa
    s.rect(34,20,1,3,VIOLET)                                       # grieta post-Umbral
    # puerta de calle
    s.rect(19,25,3,1,(120,170,140))

    s.collision(2,2,34,1); s.collision(2,25,34,1)
    s.collision(2,2,1,24); s.collision(35,2,1,24)

    s.item(1,4,4,"anclaje","Anclaje 0 — mesita de noche · guardado")
    s.item(2,11,8,"dialogo","estante de 18 discos · un comentario c/u")
    s.item(3,12,16,"dialogo","heladera · dibujo de Bauti cambia por acto")
    s.item(4,19,25,"puerta","→ Zona 1 Calle Principal")
    s.item(5,34,20,"zona_revers","grieta del patio (post-Umbral)")
    s.item(6,11,4,"item","cuaderno de Uma · permanente")
    s.item(7,4,16,"item","termo de mate · recargable")
    s.npc("B",20,6,"Bautista","burbujas de Ánimo 0")
    s.npc("N",7,17,"Natalia","cocina · entrega protector solar")
    s.npc("D",30,20,"Darío","patio · da la misión MP-01")
    s.finish("Recuperación pasiva +5 Ánimo/min en toda la zona. Guardado manual solo en el Anclaje 0.")

# =====================================================================
# ZONA 1 — CALLE PRINCIPAL  (60×40)
# =====================================================================
def zona1():
    random.seed(3)
    s=Sheet(1,"Calle Principal","4 cuadras · kiosco de Chino · zona neutral",60,40,8,4)
    s.rect(0,0,60,40,(64,90,60))
    s.road_h(0,60,18,5); s.road_h(0,60,34,4)
    s.road_v(28,0,40,4)
    # manzana norte izq
    for i,(x,y,w,h) in enumerate([(2,2,10,11),(14,2,9,11),(2,15,9,0)]):
        if h: s.bldg(x,y,w,h,[ROOF_A,ROOF_C,ROOF_B][i%3])
    s.bldg(2,2,10,11,ROOF_A); s.bldg(14,2,9,11,ROOF_C)
    # manzana norte der
    s.bldg(34,2,11,11,ROOF_B); s.bldg(47,2,11,11,ROOF_A)
    # manzana sur izq
    s.bldg(2,25,10,7,ROOF_C); s.bldg(14,25,9,7,ROOF_D)
    s.bldg(2,37,10,3,ROOF_A); s.bldg(14,37,9,3,ROOF_B)
    # manzana sur der — kiosco en la esquina
    s.rect(34,25,10,7,(190,150,90)); s.rect(33,32,12,1,(224,194,124))
    s.bldg(47,25,11,7,ROOF_C)
    s.bldg(34,37,11,3,ROOF_D); s.bldg(47,37,11,3,ROOF_A)
    # callejón del primer Eco
    s.rect(12,4,2,9,ASPH_D)
    # árboles con raíces que rompen la vereda
    for x in range(4,58,7):
        s.tree(x,15,3); s.rect(x,16,2,1,WOOD)
        s.tree(x,23,3)
    # cables
    s.line([(0,17),(60,17)],(48,52,50),1); s.line([(0,33),(60,33)],(48,52,50),1)
    # gato del 847
    s.ell(50,23,2,2,(200,170,120))
    # grieta post-Umbral
    s.line([(20,18),(18,24),(22,30)],VIOLET,3)

    for x,y,w,h in [(2,2,10,11),(14,2,9,11),(34,2,11,11),(47,2,11,11),
                    (2,25,10,7),(14,25,9,7),(34,25,10,7),(47,25,11,7)]:
        s.collision(x,y,w,h)

    s.item(1,34,25,"dialogo","KIOSCO DE CHINO · hub · ZONA NEUTRAL (Ecos no entran)")
    s.item(2,16,2,"senal","SEÑAL 3 · fachada del edificio de Marta")
    s.item(3,12,8,"dialogo","callejón · primer Eco Menor (tutorial Resonancia)")
    s.item(4,28,0,"puerta","→ Zona 2 Plaza Mayor (norte)")
    s.item(5,0,18,"puerta","→ Zona 0 Casa Torres (oeste)")
    s.item(6,59,34,"puerta","→ Zona 3 Mercado Viejo (callejón este)")
    s.item(7,28,39,"puerta","→ Zona 5 Zona Alta (calle empinada sur)")
    s.item(8,20,24,"zona_revers","grieta decorativa post-Umbral")
    s.npc("C",36,27,"Chino","kiosco · consumibles + info")
    s.npc("M",17,14,"Marta","balcón/vereda · Acto I")
    s.npc("A",50,14,"Almacenero","Interludio II de Pablo")
    s.npc("g",50,23,"gato del 847","acariciar 3 días → te sigue")
    s.finish("El kiosco es zona neutral: los Ecos no entran (Regla 2 del Vacío). El juego nunca lo explica.")

# =====================================================================
# ZONA 2 — PLAZA MAYOR  (70×50)
# =====================================================================
def zona2():
    s=Sheet(2,"Plaza Mayor","hub central · EL UMBRAL · Anclaje 2",70,50,8,5)
    s.rect(0,0,70,50,(70,96,64))
    s.road_h(0,70,2,4); s.road_h(0,70,44,4)
    s.road_v(2,2,46,4); s.road_v(64,2,46,4)
    # explanada
    s.rect(8,8,54,34,PLAZA); s.checker(8,8,54,34,PLAZA,PLAZA_D,3)
    # senderos diagonales
    for i in range(17):
        s.rect(8+i,8+i,2,1,(212,200,168)); s.rect(61-i,8+i,2,1,(212,200,168))
    s.rect(8,24,54,2,(212,200,168)); s.rect(34,8,2,34,(212,200,168))
    # EL ÁRBOL
    TX,TY=28,18
    s.ell(TX-2,TY-2,18,18,(38,72,42)); s.ell(TX,TY,14,14,TREE_BIG)
    s.ell(TX+3,TY+3,8,8,TREE); s.ell(TX+5,TY+5,4,4,TREE_L)
    s.rect(TX+6,TY+6,2,2,(96,74,52))
    for a in [(-3,6),(15,7),(6,-3),(7,15),(-1,12),(14,2)]:
        s.rect(TX+a[0],TY+a[1],3,1,WOOD)
    # fuente seca
    s.ell(46,28,8,8,(188,180,164)); s.ell(49,31,3,3,(150,144,130))
    # galería cubierta
    s.rect(8,38,54,4,(150,140,124))
    for x in range(9,62,6): s.rect(x,38,1,4,(120,110,96))
    # bancos
    for x,y in [(12,12),(12,34),(56,12),(56,34),(20,40),(44,6),(34,40)]:
        s.rect(x,y,3,1,(96,124,90))
    for x in [10,20,50,60]: s.tree(x,4,3)
    # grieta central post-Umbral
    s.line([(35,10),(33,18),(37,26),(34,34),(38,40)],VIOLET,3)

    s.item(1,28,18,"dialogo","EL ÁRBOL · cae en el Umbral · Anclaje 2 post-caída")
    s.item(2,46,28,"senal","SEÑAL 2 · disco de vinilo en el borde de la fuente")
    s.item(3,35,26,"zona_revers","GRIETA CENTRAL → El Revés (post-Umbral)")
    s.item(4,28,26,"item","cavidad en la base del árbol · papel de Doña Carmen")
    s.item(5,34,0,"puerta","→ Zona 4 Parque Ribereño (pasaje norte)")
    s.item(6,34,49,"puerta","→ Zona 1 Calle Principal (sur)")
    s.item(7,69,24,"puerta","→ Zona 5 Zona Alta (este)")
    s.item(8,20,40,"dialogo","galería cubierta · refugio de NPCs post-Umbral")
    s.npc("L",13,13,"Leo","banco · nombra a Pablo en Acto II")
    s.npc("V",16,13,"Vale","banco · escena espejo del Acto V")
    s.npc("Va",57,13,"Valentina","lee · cambia de libro por acto")
    s.npc("E",50,35,"Ernesto","mira el espacio de las palomas")
    s.npc("R",8,45,"regador","riega la vereda a las 18:00 SIEMPRE")
    s.finish("El Umbral: el árbol cae SIN RUIDO, 3 segundos de silencio absoluto (el único del juego).")

# =====================================================================
# ZONA 3 — MERCADO VIEJO  (60×45)
# =====================================================================
def zona3():
    s=Sheet(3,"Mercado Viejo","puestos cubiertos · sótano · Jefe I",60,45,8,4)
    s.rect(0,0,60,45,(70,90,66))
    s.road_h(0,60,2,4)
    # nave del mercado
    s.rect(4,8,52,30,TILEFLOOR); s.checker(4,8,52,30,TILEFLOOR,(158,100,84),3)
    # estructura + toldos
    for r,yy in enumerate([9,17,25,33]):
        for c in range(6):
            x=6+c*8
            s.rect(x,yy,6,5,TARP[(r+c)%len(TARP)]); s.rect(x,yy,6,1,(88,78,68))
            s.rect(x+1,yy+4,4,1,WOOD)
    # pasillos
    s.rect(4,14,52,2,(184,124,104)); s.rect(4,22,52,2,(184,124,104)); s.rect(4,30,52,2,(184,124,104))
    # acceso al sótano
    s.rect(50,39,7,5,(58,52,46),VIOLET,2)
    for j in range(4): s.rect(51,40+j,5,1,(70,62,54) if j%2 else (58,52,46))
    # edificios lindantes
    s.bldg(4,42,12,3,ROOF_A); s.bldg(20,42,12,3,ROOF_C); s.bldg(36,42,10,3,ROOF_B)
    s.line([(30,8),(28,16),(32,24),(29,32),(33,38)],VIOLET,3)
    s.collision(50,39,7,5)

    s.item(1,6,9,"dialogo","puesto de Doña Elsa · especias y cosas raras")
    s.item(2,7,10,"item","MS-03 · la radio · Agujetas de Color de Rosa")
    s.item(3,50,39,"puerta","→ SÓTANO · bloqueado por Eco Mayor (MS-05)")
    s.item(4,53,42,"jefe","JEFE I · El Fragmento del Abandono")
    s.item(5,54,41,"item","diario de Doña Carmen (sótano)")
    s.item(6,46,10,"senal","SEÑAL 6* (opcional) · parte alta del mercado")
    s.item(7,4,20,"anclaje","Anclaje 3 · escalón de entrada")
    s.item(8,30,0,"puerta","→ Zona 1 Calle Principal (callejón oeste)")
    s.npc("El",7,11,"Doña Elsa","especias · lore de Doña Carmen")
    s.npc("Ar",22,18,"Sr. Ariel","frutas · UNA sola línea, en el Acto V")
    s.npc("Lu",38,26,"Lucía","ropa usada · 16 años · calma Ecos sola")
    s.npc("Ec",50,37,"Eco Mayor","bloquea el sótano hasta MS-05")
    s.finish("El sótano guarda el diario de Carmen: ahí Uma entiende el sistema de Anclajes.")

# =====================================================================
# ZONA 4 — PARQUE RIBEREÑO  (90×50)
# =====================================================================
def zona4():
    random.seed(9)
    s=Sheet(4,"Parque Ribereno","canal · sauces · primera grieta navegable",90,50,7,3)
    s.rect(0,0,90,50,GRASS); s.checker(0,0,90,50,GRASS,GRASS_L,4)
    s.road_h(0,90,2,3)
    # senderos
    s.rect(4,24,72,2,DIRT)
    for i in range(4,76,3): s.rect(i,24,2,2,(162,136,102))
    s.rect(24,6,2,38,DIRT); s.rect(52,6,2,38,DIRT)
    # canal
    s.rect(78,4,10,44,(160,156,146)); s.rect(80,4,6,44,WATER)
    for j in range(4,48,3): s.rect(80,j,6,1,WATER_D)
    s.rect(78,22,10,3,(150,144,132))     # puente peatonal
    # sauces
    for x,y,ss in [(6,6,7),(16,10,6),(32,6,7),(42,11,6),(58,7,7),(68,12,6),
                   (8,32,6),(20,36,7),(36,30,6),(48,34,7),(62,32,6),(70,38,6),
                   (14,20,5),(44,20,5),(64,22,5)]:
        s.tree(x,y,ss,TREE_L if (x+y)%2 else TREE)
    # SAUCE VIEJO — grieta al Revés
    s.ell(70,42,8,8,TREE_BIG); s.ell(72,44,4,4,VIOLET)
    # banco del río (Anclaje 4)
    s.rect(74,26,4,2,WOOD)
    for x,y in [(10,22),(30,22),(50,22),(66,26),(18,28),(40,28)]:
        s.rect(x,y,3,1,(120,104,80))
    # patos
    for x,y in [(82,12),(83,16),(81,30),(84,34)]:
        s.ell(x,y,2,2,(230,220,200))

    s.item(1,70,42,"zona_revers","SAUCE VIEJO · primera grieta navegable (Acto II)")
    s.item(2,34,8,"senal","SEÑAL 4 · árbol que sobrevivió al Umbral")
    s.item(3,74,26,"anclaje","Anclaje 4 · banco del río (esperar 3 min)")
    s.item(4,20,30,"dialogo","Sombra Errante · incendio del viejo mercado (40 años)")
    s.item(5,0,24,"puerta","→ Zona 2 Plaza Mayor (pasaje oeste)")
    s.item(6,44,0,"puerta","→ Zona 5 Zona Alta (sendero norte)")
    s.item(7,82,14,"dialogo","MS-10 · los patos · lore del Revés")
    s.npc("Ro",12,14,"paseante","ambiental · rota por acto")
    s.npc("So",20,30,"Sombra Errante","combate no letal")
    s.npc("Pa",82,12,"patos","no se van post-Umbral")
    s.finish("Uma pierde 0 Ánimo por sol en toda esta zona. Es el punto de descanso mecánico del juego.")

# =====================================================================
# ZONA 5 — ZONA ALTA  (80×60)
# =====================================================================
def zona5():
    random.seed(4)
    s=Sheet(5,"Zona Alta","edificios 40s · taller de Hernán · acceso Mirador",80,60,8,4)
    s.rect(0,0,80,60,(96,132,84))
    for y in (10,26,42): s.road_h(2,76,y,3)
    for x in (18,38,58): s.road_v(x,0,60,3)
    # manzanas
    for ry,rh in [(2,7),(15,10),(31,10),(47,11)]:
        x=3
        while x<76:
            if random.random()<0.18:
                gw=random.choice([4,6])
                if x+gw<76: s.checker(x,ry,gw,rh,GRASS,GRASS_D,2); s.tree(x+1,ry+1,3)
                x+=gw+3; continue
            w=random.choice([6,8,10])
            if x+w>76: break
            s.bldg(x,ry,w,rh,[ROOF_C,ROOF_B,ROOF_A,ROOF_D][random.randint(0,3)])
            x+=w+3
    # escaleras entre niveles
    for j in range(6): s.rect(28,11+j,4,1,(170,164,152) if j%2==0 else (152,146,136))
    for j in range(6): s.rect(48,27+j,4,1,(170,164,152) if j%2==0 else (152,146,136))
    # taller de Hernán
    s.rect(62,47,14,11,(120,110,98)); s.rect(62,47,14,2,WALL)
    s.rect(64,56,4,2,(90,80,70))
    # firma de Carmen en la pared
    s.rect(4,33,8,1,(214,190,120))
    # escalera oculta al Mirador
    for j in range(8): s.rect(38,50+j,3,1,(178,172,160) if j%2==0 else (158,152,142))
    # zona directamente del Revés post-Umbral
    s.checker(60,10,16,12,(96,76,140),(84,66,124),3)
    s.line([(66,10),(62,16),(68,22)],VIOLET,3)

    s.item(1,4,33,"dialogo","firma en la pared: CARMEN SANTELLAN 1994")
    s.item(2,62,47,"puerta","→ TALLER DE HERNÁN (escena Acto IV)")
    s.item(3,38,57,"puerta","→ Zona 7 EL MIRADOR (escalera oculta)")
    s.item(4,20,20,"dialogo","florería de Rosa · Eco Menor entre las plantas (MS-04)")
    s.item(5,8,44,"dialogo","Don Mario · MS-08 · Cinta del Barrio")
    s.item(6,66,16,"zona_revers","suelo del Revés SIN grieta (post-Umbral)")
    s.item(7,38,0,"puerta","→ Zona 1 Calle Principal (norte)")
    s.item(8,0,42,"puerta","→ Zona 4 Parque Ribereño (sendero oeste)")
    s.npc("Ma",9,45,"Don Mario","banco de la vereda · recuerda a Carmen")
    s.npc("Ro",21,21,"Rosa","florería · no puede resolver su Eco sola")
    s.npc("He",68,52,"Hernán","taller · escena opcional del Acto IV")
    s.npc("Ec",22,22,"Eco Menor","entre las plantas de Rosa")
    s.finish("Zona más afectada post-Umbral: partes del suelo son directamente del Revés, sin grieta.")

# =====================================================================
# ZONA 7 — EL MIRADOR  (30×25)
# =====================================================================
def zona7():
    s=Sheet(7,"El Mirador","plataforma · Jefe III · la declaración",30,25,6,2)
    s.rect(0,0,30,25,(40,58,44))
    # edificios que flanquean
    s.bldg(0,0,9,20,ROOF_C); s.bldg(21,0,9,20,ROOF_C)
    s.collision(0,0,9,20); s.collision(21,0,9,20)
    # escalera de acceso
    for j in range(7):
        s.rect(12,18+j,6,1,(178,172,160) if j%2==0 else (158,152,142))
    # plataforma de cemento
    s.rect(10,3,10,15,(186,182,172)); s.checker(10,3,10,15,(186,182,172),(176,172,162),3)
    # baranda de hierro (oeste, mirando al barrio)
    for i in range(0,10,2): s.rect(10+i,2,1,1,(112,108,100))
    s.rect(10,2,10,1,(126,122,114))
    # el escalón de la señal 9
    s.rect(13,17,4,1,(200,196,186))
    # vista del barrio abajo (fuera de la plataforma)
    s.rect(0,21,30,4,(52,74,56))
    for x in range(1,29,3): s.rect(x,22,2,2,(70,92,70))
    # invasión del Revés en el Acto IV
    s.line([(15,3),(13,8),(17,13),(14,17)],VIOLET,3)
    s.checker(10,3,10,6,(96,76,140),(84,66,124),3)

    s.item(1,13,17,"senal","SEÑAL 9 · solo una flecha dibujada, apunta ARRIBA")
    s.item(2,15,18,"anclaje","Anclaje 6 · pie de la escalera · no se desactiva")
    s.item(3,15,8,"jefe","JEFE III · El Fragmento del Miedo al Decir")
    s.item(4,15,5,"dialogo","ACTO V · la declaración de Pablo")
    s.item(5,10,2,"dialogo","baranda · el atardecer más lindo del juego")
    s.item(6,15,24,"puerta","→ Zona 5 Zona Alta (bajar)")
    s.npc("P",16,6,"Pablo","sube con el papel en el bolsillo")
    s.npc("U",14,10,"Uma","posición de llegada")
    s.finish("Antes del Acto IV una barrera de energía oscura bloquea la escalera. El jefe se resuelve usando la señal como ESCUDO, no como arma.")


for f in (zona0,zona1,zona2,zona3,zona4,zona5,zona7):
    f()
print("\nlisto")
