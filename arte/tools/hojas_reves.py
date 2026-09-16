from PIL import Image, ImageDraw, ImageFont
import os, random, math

# =====================================================================
#  SEÑALES — Hojas de El Revés
#  Una hoja por sub-zona, al tamaño real de construcción en Godot.
#  Paleta y reglas propias: suelo translúcido, vacío alrededor.
# =====================================================================

TILE = 16

BG=(14,12,24); INK=(8,6,16); CREAM=(238,232,246); GOLD=(217,178,76)
PINK=(242,166,195); VIOLET=(150,110,200); VIOLET_L=(190,158,235); TEAL=(120,200,180)
BLUE=(140,190,210); RED=(198,96,88); AMBER=(226,160,90)
FLOOR=(48,36,78); FLOOR_D=(40,30,66); FLOOR_L=(60,46,94)
EDGE=(120,90,190); VOID=(20,16,34)
GHOST=(74,60,110); GHOST_L=(94,78,136)
WATER=(60,90,140); WATER_D=(48,74,118); THREAD=(226,206,140)
TREEV=(44,80,66); TREEV_L=(58,98,80)

def font(s,b=False):
    p=("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if b else
       "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
    return ImageFont.truetype(p,s) if os.path.exists(p) else ImageFont.load_default()
F_T1=font(38,True); F_SUB=font(19); F_LBL=font(15,True); F_S=font(14); F_TT=font(11); F_TAG=font(12,True)


class Sheet:
    def __init__(self, code, name, subtitle, mw, mh, n_items=0, n_npcs=0):
        self.code, self.name, self.sub = code, name, subtitle
        self.MW, self.MH = mw, mh
        self.MX, self.MY = 78, 190
        rows = max(n_items, n_npcs)
        self.table_h = 130 + rows*26
        self.W = max(mw*TILE + 150, 1320)
        self.H = mh*TILE + 190 + self.table_h + 60
        self.img = Image.new("RGB",(self.W,self.H),BG)
        self.d = ImageDraw.Draw(self.img)
        self.items=[]; self.npcs=[]

    def px(self,tx,ty): return (self.MX+tx*TILE, self.MY+ty*TILE)
    def rect(self,tx,ty,tw,th,f,o=None,ow=1):
        a=self.px(tx,ty); b=self.px(tx+tw,ty+th)
        self.d.rectangle([a[0],a[1],b[0],b[1]],fill=f,outline=o,width=ow)
    def ell(self,tx,ty,tw,th,f,o=None,ow=1):
        a=self.px(tx,ty); b=self.px(tx+tw,ty+th)
        self.d.ellipse([a[0],a[1],b[0],b[1]],fill=f,outline=o,width=ow)
    def line(self,pts,f,w=2):
        self.d.line([self.px(x,y) for x,y in pts],fill=f,width=w,joint="curve")
    def checker(self,tx,ty,tw,th,c1,c2,st=3):
        for j in range(0,th,st):
            for i in range(0,tw,st):
                self.rect(tx+i,ty+j,min(st,tw-i),min(st,th-j),
                          c1 if ((i//st)+(j//st))%2==0 else c2)

    # ---- helpers propios del Revés ----
    def void(self):
        """El vacío: fondo con constelaciones."""
        self.rect(0,0,self.MW,self.MH,VOID)
        random.seed(7)
        for _ in range(int(self.MW*self.MH*0.05)):
            x=random.randint(0,self.MW-1); y=random.randint(0,self.MH-1)
            self.rect(x,y,1,1,random.choice([(110,100,160),(140,130,190),(80,74,120)]))
    def platform(self,tx,ty,tw,th,tone=0):
        """Isla flotante con borde luminoso. Fuera del borde = caída."""
        self.rect(tx+1,ty+1,tw,th,(16,12,28))
        base=[FLOOR,FLOOR_D,FLOOR_L][tone%3]
        self.checker(tx,ty,tw,th,base,FLOOR_D if tone%2==0 else FLOOR_L,4)
        self.rect(tx,ty,tw,1,EDGE); self.rect(tx,ty+th-1,tw,1,EDGE)
        self.rect(tx,ty,1,th,EDGE); self.rect(tx+tw-1,ty,1,th,EDGE)
    def ghost(self,tx,ty,tw,th,solid=False,desfase=False):
        self.rect(tx,ty,tw,th,GHOST_L if solid else GHOST)
        self.rect(tx,ty,tw,1,VIOLET_L)
        for i in range(1,tw-1,3):
            if random.random()<.5: self.rect(tx+i,ty+2,1,1,(214,190,120))
        if desfase:
            a=self.px(tx+2,ty+2); b=self.px(tx+tw+2,ty+th+2)
            self.d.rectangle([a[0],a[1],b[0],b[1]],outline=(120,100,170),width=1)
    def bridge(self,pts):
        self.line(pts,(64,52,102),6); self.line(pts,VIOLET,2)

    # ---- marcadores ----
    def item(self,n,tx,ty,tipo,detalle):
        self.items.append((n,tx,ty,tipo,detalle))
        x,y=self.px(tx+0.5,ty+0.5)
        col={"dialogo":PINK,"portal":VIOLET,"senal":PINK,"anclaje":GOLD,
             "item":AMBER,"jefe":RED,"pasaje":TEAL,"hazard":RED}.get(tipo,CREAM)
        self.d.rectangle([x-11,y-11,x+11,y+11],fill=INK,outline=col,width=2)
        self.d.text((x,y),str(n),font=F_TAG,fill=col,anchor="mm")
    def npc(self,letra,tx,ty,nombre,detalle):
        self.npcs.append((letra,tx,ty,nombre,detalle))
        x,y=self.px(tx+0.5,ty+0.5)
        self.d.ellipse([x-11,y-11,x+11,y+11],fill=BLUE,outline=INK,width=2)
        self.d.text((x,y),letra,font=F_TAG,fill=INK,anchor="mm")
    def guard(self,letra,tx,ty,nombre,detalle):
        self.npcs.append((letra,tx,ty,nombre,detalle))
        x,y=self.px(tx+0.5,ty+0.5)
        self.d.polygon([(x,y-12),(x+12,y),(x,y+12),(x-12,y)],fill=AMBER,outline=INK)
        self.d.text((x,y),letra,font=F_TAG,fill=INK,anchor="mm")

    def finish(self, notas=""):
        d=self.d
        for i in range(0,self.MW+1,5):
            a=self.px(i,0); b=self.px(i,self.MH)
            w=2 if i%10==0 else 1; c=(56,46,86) if i%10==0 else (38,32,58)
            d.line([a[0],a[1],b[0],b[1]],fill=c,width=w)
            if i%10==0: d.text((a[0],self.MY-16),str(i),font=F_TT,fill=(130,118,170),anchor="ma")
        for j in range(0,self.MH+1,5):
            a=self.px(0,j); b=self.px(self.MW,j)
            w=2 if j%10==0 else 1; c=(56,46,86) if j%10==0 else (38,32,58)
            d.line([a[0],a[1],b[0],b[1]],fill=c,width=w)
            if j%10==0: d.text((self.MX-10,a[1]),str(j),font=F_TT,fill=(130,118,170),anchor="rm")
        a=self.px(0,0); b=self.px(self.MW,self.MH)
        d.rectangle([a[0],a[1],b[0],b[1]],outline=VIOLET,width=3)

        d.rectangle([0,0,self.W,150],fill=INK)
        d.ellipse([40,44,88,92],fill=VIOLET)
        d.text((64,68),self.code,font=F_T1,fill=INK,anchor="mm")
        d.text((106,44),self.name,font=F_T1,fill=VIOLET_L)
        d.text((108,94),self.sub,font=F_SUB,fill=(150,130,200))
        d.text((self.W-40,52),f"{self.MW}×{self.MH} tiles",font=F_LBL,fill=CREAM,anchor="ra")
        d.text((self.W-40,78),f"{self.MW*32}×{self.MH*32} px  ·  tile 32px",font=F_S,fill=(140,126,180),anchor="ra")
        d.text((self.W-40,102),"ZONA 6 · EL REVÉS",font=F_TT,fill=(120,108,160),anchor="ra")

        ty0=self.MY+self.MH*TILE+30
        d.rounded_rectangle([70,ty0,self.W-70,ty0+self.table_h-20],radius=10,
                            fill=(26,20,44),outline=VIOLET,width=2)
        colx=96
        d.text((colx,ty0+14),"TILES INTERACTUABLES",font=F_LBL,fill=VIOLET_L)
        yy=ty0+44
        for lbl,off in [("#",0),("coord",30),("tipo",110),("detalle",210)]:
            d.text((colx+off,yy),lbl,font=F_TAG,fill=(130,118,170))
        yy+=22
        for n,tx,tyy,tipo,det in self.items:
            col={"dialogo":PINK,"portal":VIOLET,"senal":PINK,"anclaje":GOLD,
                 "item":AMBER,"jefe":RED,"pasaje":TEAL,"hazard":RED}.get(tipo,CREAM)
            d.text((colx,yy),str(n),font=F_S,fill=col)
            d.text((colx+30,yy),f"({tx},{tyy})",font=F_S,fill=(190,180,220))
            d.text((colx+110,yy),tipo,font=F_S,fill=col)
            d.text((colx+210,yy),det,font=F_S,fill=(180,170,210))
            yy+=26
        if self.npcs:
            cx2=self.W//2+90
            d.text((cx2,ty0+14),"CRIATURAS Y NODOS",font=F_LBL,fill=BLUE)
            yy=ty0+44
            for lbl,off in [("·",0),("coord",30),("nombre",110)]:
                d.text((cx2+off,yy),lbl,font=F_TAG,fill=(130,118,170))
            yy+=22
            for l,tx,tyy,nom,det in self.npcs:
                d.text((cx2,yy),l,font=F_S,fill=BLUE)
                d.text((cx2+30,yy),f"({tx},{tyy})",font=F_S,fill=(190,180,220))
                d.text((cx2+110,yy),nom,font=F_S,fill=CREAM)
                d.text((cx2+250,yy),det,font=F_S,fill=(180,170,210))
                yy+=26
        if notas:
            d.text((96,ty0+self.table_h-58),notas,font=F_S,fill=(140,126,180))

        fn=f"reves_{self.code}_{self.name.lower().replace(' ','_').replace('é','e').replace('á','a')}.png"
        self.img.save(fn); print("→",fn,self.img.size)


# =====================================================================
# A — REVÉS DE PLAZA MAYOR  (60×50) · abierto · árbol invertido
# =====================================================================
def revesA():
    s=Sheet("A","Reves de Plaza Mayor","abierto · árbol invertido · Jefe II",60,50,7,4)
    s.void()
    s.platform(4,4,52,42,0)
    # explanada espejada
    s.checker(8,8,44,34,(54,42,86),(46,34,74),4)
    # ÁRBOL INVERTIDO: copa hundida, raíces al cielo
    TX,TY=26,26
    # copa hundida en el suelo (grande, es el árbol de la plaza)
    s.ell(TX-9,TY+1,20,14,(34,26,58))
    s.ell(TX-7,TY+3,16,10,(28,22,50))
    s.ell(TX-3,TY+5,8,5,VIOLET)
    # tronco corto, vertical
    s.rect(TX,TY-4,2,6,(96,80,60))
    # raíces abriéndose hacia el cielo
    for a in range(195,346,15):
        r=math.radians(a)
        s.line([(TX+1,TY-4),(TX+1+math.cos(r)*8,TY-4+math.sin(r)*8)],(130,110,180),2)
        s.line([(TX+1+math.cos(r)*8,TY-4+math.sin(r)*8),
                (TX+1+math.cos(r)*12,TY-4+math.sin(r)*12)],(100,84,146),1)
    # fuente espejada: llena, pero de luz
    s.ell(40,32,8,8,(60,48,96)); s.ell(43,35,3,3,(200,180,240))
    # edificios fantasma en el perímetro
    for x,y in [(8,8),(18,8),(38,8),(48,8),(8,38),(20,38),(40,38),(48,38)]:
        s.ghost(x,y,7,4)
    # senderos de luz
    s.line([(8,25),(52,25)],(84,68,130),1); s.line([(30,8),(30,42)],(84,68,130),1)
    # pasajes de resonancia
    s.bridge([(56,20),(60,16)])
    s.bridge([(30,46),(30,50)])

    s.item(1,26,26,"jefe","JEFE II · El Fragmento del Olvido (arena sin paredes)")
    s.item(2,14,22,"senal","SEÑAL 7 · al pie del árbol invertido")
    s.item(3,30,48,"portal","← grieta central Plaza Mayor (mundo real)")
    s.item(4,58,17,"pasaje","→ EL TELAR (Pasaje de Resonancia · cuesta energía)")
    s.item(5,40,32,"dialogo","fuente de luz · Resonante explica la Regla 1")
    s.item(6,34,36,"dialogo","1er ENCUENTRO CON PABLO (post-jefe)")
    s.item(7,0,25,"hazard","BORDE · caer al vacío = muerte + Anclaje")
    s.npc("R1",42,33,"Resonante","Regla 1: no puede crear, solo vaciar")
    s.npc("R2",12,30,"Resonante","cuenta la historia de Don Pepe")
    s.npc("Ol",26,26,"El Olvido","borra objetos del mapa al tocarlos")
    s.npc("P",34,36,"Pablo","aparece al caer el Fragmento")
    s.finish("El Olvido borra objetos decorativos del mapa PERMANENTEMENTE. Se derrota usando las señales como proyectiles.")

# =====================================================================
# B — REVÉS DEL MERCADO  (55×45) · laberíntico
# =====================================================================
def revesB():
    random.seed(5)
    s=Sheet("B","Reves del Mercado","laberíntico · puestos fantasma · sótano espejado",55,45,7,3)
    s.void()
    s.platform(3,3,49,39,1)
    # laberinto
    for i in range(9):
        if i%2==0:
            x=7+i*5
            if x<48: s.rect(x,7,2,random.choice([12,18,24]),GHOST_L)
        else:
            y=8+i*4
            if y<38: s.rect(7,y,random.choice([16,26,34]),2,GHOST_L)
    for i in range(5):
        s.rect(10+i*8,30,2,8,GHOST)
    # puestos fantasma
    for x,y in [(9,9),(22,14),(36,10),(16,26),(30,30),(42,22),(24,36)]:
        s.rect(x,y,4,3,(96,60,60)); s.rect(x,y,4,1,AMBER)
    # sótano espejado
    s.rect(44,34,7,6,(30,22,44),VIOLET,2)
    for j in range(4): s.rect(45,35+j,5,1,(44,34,62) if j%2 else (34,26,50))
    s.bridge([(3,20),(0,16)])

    s.item(1,44,34,"portal","← sótano del Mercado Viejo (mundo real)")
    s.item(2,30,30,"senal","SEÑAL 8* (opcional) · fondo del laberinto")
    s.item(3,1,17,"pasaje","→ EL TELAR (Pasaje de Resonancia)")
    s.item(4,22,14,"dialogo","puesto fantasma · Resonante · Regla 2")
    s.item(5,42,22,"item","Guante de Resonancia (−15% cooldown)")
    s.item(6,16,26,"hazard","territorio del Centinela de Piedra")
    s.item(7,9,9,"dialogo","Memoria · Doña Elsa joven con Carmen")
    s.guard("Ce",17,27,"Centinela de Piedra","NO se vence en combate · Clave de Resonancia")
    s.npc("R3",23,15,"Resonante","Regla 2: no entra donde algo fue dicho")
    s.npc("Me",10,10,"Memoria","fantasma de Elsa y Carmen jóvenes")
    s.finish("El laberinto cambia de disposición si los Pájaros de Tinta están activos en la sub-zona C.")

# =====================================================================
# C — REVÉS DEL PARQUE  (65×45) · agua arriba
# =====================================================================
def revesC():
    s=Sheet("C","Reves del Parque","agua invertida · sauces sumergidos · Memoria de Agua",65,45,7,3)
    s.void()
    s.platform(3,3,59,39,2)
    # EL AGUA VA ARRIBA (techo)
    s.rect(3,3,59,8,WATER)
    for j in range(3,11,2): s.rect(3,j,59,1,WATER_D)
    for i in range(6,60,5):                     # gotas cayendo HACIA ARRIBA
        s.line([(i,16),(i,11)],(90,130,180),1)
        s.rect(i,16,1,1,(150,190,220))
    # sauces sumergidos: crecen hacia abajo desde el agua
    for x,y,ss in [(8,14,6),(18,18,5),(30,13,6),(42,17,5),(52,14,6),
                   (12,28,5),(24,32,6),(38,28,5),(50,30,6)]:
        s.ell(x,y,ss,ss,TREEV_L if (x+y)%2 else TREEV)
        s.line([(x+ss//2,y),(x+ss//2,y-4)],(70,110,90),1)
    # sendero de luz
    s.line([(6,24),(58,24)],(84,68,130),2)
    # espejo del sauce viejo
    s.ell(50,34,8,8,(38,70,58)); s.ell(52,36,4,4,VIOLET)
    # banco espejado
    s.rect(30,24,4,2,(96,80,60))
    s.bridge([(3,24),(0,28)])
    s.bridge([(32,3),(32,0)])

    s.item(1,50,34,"portal","← sauce viejo del Parque (mundo real · Acto II)")
    s.item(2,30,24,"anclaje","Anclaje 5 alternativo · banco espejado")
    s.item(3,1,25,"pasaje","→ EL TELAR (Pasaje de Resonancia)")
    s.item(4,32,1,"pasaje","→ sub-zona D · Revés Zona Alta (pasaje alto)")
    s.item(5,20,8,"hazard","AGUA ARRIBA · tocarla invierte la gravedad 3s")
    s.item(6,42,17,"item","Fruta del Revés (+50 Ánimo)")
    s.item(7,12,28,"dialogo","Resonante · Regla 3: crece con lo que se le esconde")
    s.guard("MA",52,20,"Memoria de Agua","no ataca si Uma lleva una señal de Pablo")
    s.guard("PT",24,12,"Pájaros de Tinta","reconfiguran el laberinto de la sub-zona B")
    s.npc("R4",13,29,"Resonante","Regla 3 · la más importante del juego")
    s.finish("La Memoria de Agua custodia el recuerdo de Carmen tejiendo los Anclajes hace 30 años.")

# =====================================================================
# D — REVÉS DE ZONA ALTA  (60×35) · tiempo inestable
# =====================================================================
def revesD():
    random.seed(4)
    s=Sheet("D","Reves de Zona Alta","tiempo inestable · copias desfasadas",60,35,6,3)
    s.void()
    s.platform(3,3,54,29,1)
    # edificios con copia desfasada = dos momentos en el mismo lugar
    for i,(x,y,w,h) in enumerate([(6,6,8,7),(18,5,7,9),(29,7,9,6),(42,6,7,8),(50,8,6,6),
                                  (8,18,7,8),(20,20,8,6),(33,18,7,8),(45,20,8,6)]):
        s.ghost(x,y,w,h,solid=(i%2==0),desfase=(i%2==1))
    # calles angostas de luz
    s.line([(3,15),(57,15)],(84,68,130),1)
    s.line([(30,3),(30,32)],(84,68,130),1)
    # zonas de tiempo inestable (visualmente distintas)
    s.checker(38,24,16,7,(88,68,132),(76,58,118),3)
    s.checker(6,26,14,5,(88,68,132),(76,58,118),3)
    s.bridge([(30,32),(34,35)])
    s.bridge([(57,16),(60,20)])

    s.item(1,46,27,"hazard","TIEMPO INESTABLE · versiones del pasado superpuestas")
    s.item(2,12,28,"hazard","TIEMPO INESTABLE · segunda zona")
    s.item(3,32,34,"pasaje","→ EL TELAR (Pasaje de Resonancia)")
    s.item(4,58,18,"pasaje","→ sub-zona C · Revés del Parque")
    s.item(5,20,8,"item","Fragmento de Pablo 1/3 (MS-11) · interludio extendido")
    s.item(6,45,22,"dialogo","Memoria · Carmen firmando la pared en 1994")
    s.npc("Me",46,23,"Memoria de Carmen","la escena de la firma CARMEN SANTELLAN")
    s.npc("Gu",34,10,"Guardián menor","territorial · ignora si no se lo ataca")
    s.npc("R5",14,21,"Resonante","explica el tiempo inestable")
    s.finish("En zonas de tiempo inestable el jugador ve dos momentos a la vez. Es donde se ocultan los 3 Fragmentos de Pablo.")

# =====================================================================
# T — EL TELAR  (35×35) · núcleo
# =====================================================================
def revesT():
    s=Sheet("T","El Telar","núcleo · diario de Carmen · Anclaje 5",35,35,6,2)
    s.void()
    s.platform(4,4,27,27,2)
    CX,CY=17,17
    # cúpula de hilos
    s.ell(CX-11,CY-11,22,22,(30,24,54))
    s.ell(CX-9,CY-9,18,18,(40,32,70))
    for a in range(0,360,12):
        r=math.radians(a)
        s.line([(CX,CY),(CX+math.cos(r)*11,CY+math.sin(r)*11)],THREAD,1)
    for rad in (4,7,10):
        a=s.px(CX-rad,CY-rad); b=s.px(CX+rad,CY+rad)
        s.d.ellipse([a[0],a[1],b[0],b[1]],outline=THREAD,width=1)
    s.ell(CX-2,CY-2,4,4,(250,238,180))
    # atril del diario
    s.rect(CX-1,CY+12,3,2,(120,100,74))
    # hilos que salen hacia los anclajes del barrio real
    for a in range(0,360,45):
        r=math.radians(a)
        s.line([(CX+math.cos(r)*13,CY+math.sin(r)*13),
                (CX+math.cos(r)*17,CY+math.sin(r)*17)],(150,132,90),1)
    # 4 pasajes, uno por sub-zona
    s.bridge([(4,17),(0,17)]); s.bridge([(31,17),(35,17)])
    s.bridge([(17,4),(17,0)]); s.bridge([(17,31),(17,35)])

    s.item(1,17,29,"item","DIARIO DE DOÑA CARMEN · lore completo")
    s.item(2,17,17,"anclaje","Anclaje 5 · centro del Telar")
    s.item(3,2,17,"pasaje","→ sub-zona A · Revés de Plaza Mayor")
    s.item(4,32,17,"pasaje","→ sub-zona C · Revés del Parque")
    s.item(5,17,2,"pasaje","→ sub-zona D · Revés de Zona Alta")
    s.item(6,17,32,"pasaje","→ sub-zona B · Revés del Mercado")
    s.guard("TC",24,11,"Tejedor Ciego","hostil sin el Hilo de Paso")
    s.npc("Ca",17,20,"Memoria de Carmen","aparece al leer el diario")
    s.finish("Los hilos del Telar conectan TODOS los Anclajes del barrio real: es el sistema de resurrección de Uma.")


for f in (revesA,revesB,revesC,revesD,revesT):
    f()
print("\nlisto")
