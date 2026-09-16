from PIL import Image, ImageDraw, ImageFont
import os, math

# =====================================================================
#  SEÑALES — Hojas de los Interludios de Pablo (Hilo B)
#  Micro-segmentos jugables. Sin combate, sin HUD, sin Ánimo.
#  Una decisión real por escena. "Caminos distintos, mismo destino."
# =====================================================================

TILE = 34   # tiles grandes: son escenas chiquitas

BG=(20,18,30); INK=(10,9,18); CREAM=(240,234,244); GOLD=(217,178,76)
PINK=(242,166,195); VIOLET=(150,110,200); TEAL=(120,200,180)
BLUE=(140,190,210); AMBER=(226,160,90); RED=(198,96,88)
WALL=(112,96,84); FLOOR=(178,164,140); FLOOR_D=(166,152,128)
WOOD=(120,100,74); WOOD_D=(96,78,56)
NIGHT=(58,62,78); ASPHALT=(78,82,80); SIDE=(176,170,152)
SKY=(96,112,138); GRASS=(86,126,78)
PAPER=(240,228,196); GLASS=(150,180,196)

def font(s,b=False):
    p=("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if b else
       "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
    return ImageFont.truetype(p,s) if os.path.exists(p) else ImageFont.load_default()
F_T1=font(36,True); F_SUB=font(18); F_H=font(17,True); F_L=font(14,True); F_S=font(13); F_TT=font(11)


class Sheet:
    def __init__(self, num, name, sub, mw, mh, n_rows=0, n_guion=0):
        self.num,self.name,self.sub=num,name,sub
        self.MW,self.MH=mw,mh
        self.MX,self.MY=80,200
        self.panel_h = max(150 + n_rows*24, 190 + n_guion*22)
        self.W = max(mw*TILE+160, 1340)
        self.H = mh*TILE + 200 + self.panel_h + 60
        self.img=Image.new("RGB",(self.W,self.H),BG); self.d=ImageDraw.Draw(self.img)
        self.items=[]

    def px(self,tx,ty): return (self.MX+tx*TILE, self.MY+ty*TILE)
    def rect(self,tx,ty,tw,th,f,o=None,ow=1):
        a=self.px(tx,ty); b=self.px(tx+tw,ty+th)
        self.d.rectangle([a[0],a[1],b[0],b[1]],fill=f,outline=o,width=ow)
    def ell(self,tx,ty,tw,th,f):
        a=self.px(tx,ty); b=self.px(tx+tw,ty+th)
        self.d.ellipse([a[0],a[1],b[0],b[1]],fill=f)
    def line(self,pts,f,w=2):
        self.d.line([self.px(x,y) for x,y in pts],fill=f,width=w,joint="curve")
    def checker(self,tx,ty,tw,th,c1,c2,st=1):
        for j in range(0,th,st):
            for i in range(0,tw,st):
                self.rect(tx+i,ty+j,min(st,tw-i),min(st,th-j),
                          c1 if ((i//st)+(j//st))%2==0 else c2)

    def mark(self,n,tx,ty,tipo,det,col=None):
        self.items.append((n,tx,ty,tipo,det))
        x,y=self.px(tx+0.5,ty+0.5)
        c=col or {"decision":GOLD,"objeto":AMBER,"salida":TEAL,
                  "npc":BLUE,"trigger":PINK,"camara":VIOLET}.get(tipo,CREAM)
        self.d.rectangle([x-13,y-13,x+13,y+13],fill=INK,outline=c,width=2)
        self.d.text((x,y),str(n),font=F_L,fill=c,anchor="mm")

    def actor(self,letra,tx,ty,col=BLUE):
        x,y=self.px(tx+0.5,ty+0.5)
        self.d.ellipse([x-14,y-14,x+14,y+14],fill=col,outline=INK,width=2)
        self.d.text((x,y),letra,font=F_L,fill=INK,anchor="mm")

    def arrow(self,p0,p1,col=GOLD,label=None):
        a=self.px(*p0); b=self.px(*p1)
        self.d.line([a[0],a[1],b[0],b[1]],fill=col,width=3)
        ang=math.atan2(b[1]-a[1],b[0]-a[0])
        for s in (2.6,-2.6):
            self.d.line([b[0],b[1],b[0]+math.cos(ang+s)*12,b[1]+math.sin(ang+s)*12],fill=col,width=3)
        if label:
            mx,my=(a[0]+b[0])//2,(a[1]+b[1])//2
            tw=self.d.textlength(label,font=F_TT)
            self.d.rectangle([mx-tw//2-6,my-11,mx+tw//2+6,my+11],fill=INK)
            self.d.text((mx,my),label,font=F_TT,fill=col,anchor="mm")

    def finish(self, decision, ramas, guion, nota=""):
        d=self.d
        # grilla por tile
        for i in range(self.MW+1):
            a=self.px(i,0); b=self.px(i,self.MH)
            d.line([a[0],a[1],b[0],b[1]],fill=(44,40,62),width=1)
        for j in range(self.MH+1):
            a=self.px(0,j); b=self.px(self.MW,j)
            d.line([a[0],a[1],b[0],b[1]],fill=(44,40,62),width=1)
        for i in range(0,self.MW+1,5):
            a=self.px(i,0); d.text((a[0],self.MY-16),str(i),font=F_TT,fill=(130,124,160),anchor="ma")
        for j in range(0,self.MH+1,5):
            a=self.px(0,j); d.text((self.MX-10,a[1]),str(j),font=F_TT,fill=(130,124,160),anchor="rm")
        a=self.px(0,0); b=self.px(self.MW,self.MH)
        d.rectangle([a[0],a[1],b[0],b[1]],outline=VIOLET,width=3)

        # header
        d.rectangle([0,0,self.W,158],fill=INK)
        d.ellipse([40,46,96,102],fill=VIOLET)
        d.text((68,74),self.num,font=F_T1,fill=INK,anchor="mm")
        d.text((116,46),self.name,font=F_T1,fill=(214,190,245))
        d.text((118,96),self.sub,font=F_SUB,fill=(150,130,200))
        d.text((self.W-40,54),f"{self.MW}×{self.MH} tiles",font=F_L,fill=CREAM,anchor="ra")
        d.text((self.W-40,80),"HILO B · PABLO  ·  sin combate · sin HUD · sin Ánimo",font=F_S,fill=(140,126,180),anchor="ra")
        d.text((self.W-40,104),"una decisión · caminos distintos, mismo destino",font=F_TT,fill=(120,108,160),anchor="ra")

        # panel inferior
        py=self.MY+self.MH*TILE+30
        d.rounded_rectangle([70,py,self.W-70,py+self.panel_h-20],radius=10,
                            fill=(28,24,44),outline=VIOLET,width=2)
        # col izq: elementos
        d.text((100,py+14),"ELEMENTOS DE ESCENA",font=F_L,fill=(190,168,235))
        yy=py+42
        for n,tx,ty,tipo,det in self.items:
            c={"decision":GOLD,"objeto":AMBER,"salida":TEAL,
               "npc":BLUE,"trigger":PINK,"camara":VIOLET}.get(tipo,CREAM)
            d.text((100,yy),str(n),font=F_S,fill=c)
            d.text((124,yy),f"({tx},{ty})",font=F_S,fill=(190,182,215))
            d.text((196,yy),tipo,font=F_S,fill=c)
            d.text((280,yy),det,font=F_S,fill=(180,172,205))
            yy+=24
        # col der: decisión
        cx=self.W//2+70
        d.text((cx,py+14),"LA DECISIÓN",font=F_L,fill=GOLD)
        d.text((cx,py+42),decision,font=F_S,fill=CREAM)
        yy=py+70
        for r in ramas:
            d.text((cx,yy),"→ "+r,font=F_S,fill=(190,206,190)); yy+=24
        yy+=6
        d.text((cx,yy),"GUION",font=F_L,fill=(190,168,235)); yy+=24
        for g in guion:
            d.text((cx,yy),g,font=F_S,fill=(180,172,205)); yy+=22
        if nota:
            d.text((100,py+self.panel_h-52),nota,font=F_S,fill=(150,136,190))

        fn=f"interludio_{self.num}_{self.name.lower().replace(' ','_').replace('í','i').replace('é','e')}.png"
        self.img.save(fn); print("→",fn,self.img.size)


# =====================================================================
# I — EL PAPEL DOBLADO TRES VECES   (cuarto de Pablo · 8×7)
# =====================================================================
def i1():
    s=Sheet("I","El papel doblado tres veces","cierre del Prólogo · cuarto de Pablo",8,7,7,12)
    s.rect(0,0,8,7,(38,34,48))
    s.rect(1,1,6,5,WALL)
    s.checker(1,1,6,5,FLOOR,FLOOR_D,1)
    # escritorio
    s.rect(1,1,3,1,WOOD); s.rect(1,1,3,1,WOOD_D,None)
    s.rect(1,1,3,1,WOOD)
    s.rect(2,2,1,1,(60,54,46))            # silla
    s.rect(1,1,1,1,PAPER)                 # papel sobre el escritorio
    # ventana
    s.rect(6,2,1,2,GLASS)
    # cesto de basura
    s.ell(5,4,1,1,(90,86,80))
    # puerta
    s.rect(3,6,2,1,(140,120,96))
    # recorrido posible
    s.arrow((2.5,2.5),(5.5,4.5),AMBER,"tirar")
    s.arrow((2.5,2.5),(4,6),TEAL,"salir · única salida real")

    s.mark(1,1,1,"objeto","escritorio · escribir la señal (3 veces)")
    s.mark(2,5,4,"decision","cesto · Romperlo / Dejarlo así")
    s.mark(3,3,6,"salida","puerta · fin de escena (fade)")
    s.mark(4,6,2,"objeto","ventana · Pablo mira afuera si el jugador espera")
    s.mark(5,2,2,"npc","PABLO (posición inicial, sentado)")
    s.mark(6,4,6,"trigger","umbral · Pablo se queda 2 seg de más")
    s.mark(7,1,4,"objeto","cama sin hacer · inspeccionable, sin función")
    s.actor("P",2,2,VIOLET)

    s.finish(
        "Tocar el papel: ¿Romperlo o Dejarlo así?",
        ['Romperlo → lo rompe. "No. Así no."',
         'Dejarlo así → mira 3 seg, lo rompe igual.',
         'Se repite 2 veces. La 3ª vez sale por la puerta.'],
        ['PABLO: "Siempre te fijás en lo que',
         '        los demás no ven."',
         '(rompe)  "No. Así no."',
         '',
         'Al salir:',
         'PABLO: "Listo. Ya está. No lo pienses más."'],
        "El jugador ve el ORIGEN de la señal 1 antes de que Uma la encuentre. El tic de doblar para el mismo lado nace acá.")

# =====================================================================
# II — CINCO CUADRAS   (tira de calle · 14×5)
# =====================================================================
def i2():
    s=Sheet("II","Cinco cuadras","cierre del Acto I · calle · reusa tileset Zona 1",14,5,7,12)
    s.rect(0,0,14,5,GRASS)
    s.rect(0,2,14,2,ASPHALT)
    s.rect(0,1,14,1,SIDE); s.rect(0,4,14,1,SIDE)
    for i in range(0,14,3): s.rect(i,2,2,1,(150,150,140))
    # edificios de fondo
    for x,w in [(0,3),(4,3),(8,2),(11,3)]:
        s.rect(x,0,w,1,(150,120,96))
    # almacén de la esquina (destino)
    s.rect(11,0,3,1,(190,150,90)); s.rect(11,1,3,1,(224,194,124))
    # recorrido
    s.arrow((2.5,3.5),(6,3.5),CREAM,"camina")
    s.arrow((6,3.5),(6,1.5),AMBER,"cruzar")
    s.arrow((6,3.5),(12,3.5),TEAL,"seguir derecho")

    s.mark(1,2,3,"npc","PABLO (inicio) · camina hacia la derecha")
    s.mark(2,6,3,"decision","punto de decisión · Cruzar / Seguir derecho")
    s.mark(3,7,1,"npc","UMA + MARTA (fondo, no interactuables)")
    s.mark(4,8,1,"trigger","Uma se ríe fuerte → Pablo frena")
    s.mark(5,12,1,"salida","almacén · fin de escena")
    s.mark(6,0,3,"camara","cámara fija · sin scroll")
    s.mark(7,10,3,"objeto","kiosco de Chino de fondo · Pablo lo EVITA")
    s.actor("P",2,3,VIOLET); s.actor("U",7,1); s.actor("M",8,1)

    s.finish(
        "¿Cruzar la calle o Seguir derecho?",
        ['Cruzar → 2 pasos, la ve reírse, frena.',
         '   "No. Interrumpo algo."',
         'Seguir → ni gira la cabeza del todo.',
         '   "Ni lo pienses."'],
        ['ALMACENERO: "¿Te ayudo con algo?"',
         'PABLO: "Sí... eh. ¿Tenés fósforos?"',
         '',
         '(Pablo no fuma. Mira la caja como si',
         ' no supiera cómo llegó ahí.)'],
        "Entra al ALMACÉN, no al kiosco de Chino: evita también el hub social del barrio. Es deliberado.")

# =====================================================================
# III — LO QUE DIJO HERNÁN   (cocina · 7×6)
# =====================================================================
def i3():
    s=Sheet("III","Lo que dijo Hernan","mitad del Acto II · cocina de Hernán",7,6,7,13)
    s.rect(0,0,7,6,(34,32,42))
    s.rect(1,1,5,4,WALL); s.checker(1,1,5,4,(186,178,164),(176,168,154),1)
    # mesada y heladera
    s.rect(1,1,3,1,(160,150,140)); s.rect(5,1,1,1,(200,196,190))
    # mesa chica con dos sillas
    s.rect(2,3,3,1,WOOD)
    s.rect(2,2,1,1,(70,62,52)); s.rect(4,4,1,1,(70,62,52))
    # olla
    s.ell(3,3,1,1,(120,120,124))
    # lámpara colgante (única fuente de luz)
    s.ell(3,2,1,1,(226,206,140))
    s.rect(1,5,5,1,(28,26,36))

    s.mark(1,2,2,"npc","PABLO (silla izquierda)")
    s.mark(2,4,4,"npc","HERNÁN (silla derecha) · de perfil")
    s.mark(3,3,3,"decision","mesa · Preguntar / Comer en silencio")
    s.mark(4,3,3,"objeto","pan · gesto chico (acercar)")
    s.mark(5,1,1,"objeto","mesada · servir agua · gesto chico")
    s.mark(6,3,2,"camara","fundido final SOBRE PABLO, no sobre Hernán")
    s.mark(7,5,1,"objeto","heladera · nada pegado (contraste con Casa Torres)")
    s.actor("P",2,2,VIOLET); s.actor("H",4,4,AMBER)

    s.finish(
        "¿Preguntarle algo o Comer en silencio?",
        ['Preguntar → "¿Extrañás tocar la guitarra?"',
         '   HERNÁN: "Comé."',
         'Silencio → no pasa nada varios segundos.',
         '   El silencio ES el gameplay.'],
        ['HERNÁN: "Vos heredaste lo de tu abuela.',
         '  Lo de ver cosas que los demás no ven."',
         '  "Ojalá no heredes también lo mío."',
         'PABLO: "¿Lo tuyo qué es?"',
         'HERNÁN: "Quedarte con las cosas adentro',
         '  hasta que ya no importan."'],
        "Movimiento MUY acotado: 3 tiles útiles. La claustrofobia de la escena es intencional.")

# =====================================================================
# IV — LA ENTREVISTA   (monoambiente · 9×5)
# =====================================================================
def i4():
    s=Sheet("IV","La entrevista","cierre del Acto II · monoambiente de Pablo",9,5,7,13)
    s.rect(0,0,9,5,(30,30,42))
    # interior
    s.rect(1,1,5,3,WALL); s.checker(1,1,5,3,FLOOR,FLOOR_D,1)
    s.rect(1,1,2,1,WOOD)                    # escritorio
    s.rect(1,1,1,1,PAPER)                   # SEÑAL 9 a medio escribir
    s.rect(4,2,1,1,(150,120,140))           # cama
    # balcón
    s.rect(6,1,2,3,(150,146,132))
    for i in range(3): s.rect(8,1+i,1,1,(96,92,88))   # baranda
    s.rect(6,1,1,3,(120,116,108))                      # puerta ventana
    # ciudad de fondo
    s.rect(6,0,3,1,SKY)
    s.arrow((2,1.5),(7,2.5),TEAL,"salir al balcón")
    s.arrow((7,2.5),(2,1.5),AMBER,"volver adentro")

    s.mark(1,1,1,"objeto","ESCRITORIO · señal 9 a medio escribir")
    s.mark(2,2,2,"decision","posición ADENTRO · atender acá")
    s.mark(3,7,2,"decision","posición AFUERA · atender en el balcón")
    s.mark(4,6,2,"salida","puerta ventana · une las dos posiciones")
    s.mark(5,1,1,"camara","plano final: encuadre sobre el papel")
    s.mark(6,8,2,"objeto","baranda · vista de la otra ciudad (siembra)")
    s.mark(7,4,2,"objeto","cama · sin hacer, igual que el Interludio I")
    s.actor("P",2,2,VIOLET)

    s.finish(
        "¿Atender adentro o afuera?",
        ['Adentro → la cámara termina en el papel.',
         'Afuera → camina adentro y ÉL elige mirarlo.',
         'Mismo plano final, distinto camino.'],
        ['PABLO: "Sí, sigo interesado..."',
         '  "No, todavía no le avisé a nadie acá."',
         '  (pausa larga)',
         '  "Fin de mes está bien. Ahí les confirmo."',
         '(cuelga · mira el papel)',
         'PABLO: "Todavía no."'],
        "Acá arranca el reloj. El jugador sabe que Pablo se puede ir; Uma no se entera hasta el Acto IV.")

# =====================================================================
# V — TRES SEMANAS   (azotea + cuarto · 10×6)
# =====================================================================
def i5():
    s=Sheet("V","Tres semanas","antes del Acto III · azotea + cuarto",10,6,8,14)
    s.rect(0,0,10,6,(34,36,48))
    # AZOTEA (izquierda)
    s.rect(0,0,6,4,(150,146,132)); s.checker(0,0,6,4,(150,146,132),(140,136,124),1)
    for i in range(6): s.rect(i,4,1,1,(96,92,88))     # borde/parapeto
    s.rect(0,5,6,1,(58,74,58))                         # plaza abajo, lejos
    s.ell(2,5,1,1,(44,84,48))                          # el árbol visto desde arriba
    # CORTE + cuarto (derecha)
    s.rect(6,0,1,6,(20,18,28))                         # separador de escena
    s.rect(7,1,3,4,WALL); s.checker(7,1,3,4,FLOOR,FLOOR_D,1)
    s.rect(7,1,2,1,WOOD); s.rect(7,1,1,1,PAPER)        # escritorio + señal 9
    s.rect(9,2,1,2,GLASS)                              # ventana
    s.arrow((1.5,2.5),(1.5,4.5),AMBER,"acercarse al borde")
    s.arrow((8,3.5),(9,2.5),TEAL,"ventana ↔ escritorio")

    s.mark(1,1,2,"npc","PABLO (azotea, mirando abajo)")
    s.mark(2,1,4,"decision","borde · Acercarse / Quedarse en la sombra")
    s.mark(3,2,5,"trigger","UMA abajo · resuelve un Eco SOLA (no interactuable)")
    s.mark(4,4,1,"objeto","sombra del tanque · la opción 'quedarse atrás'")
    s.mark(5,6,0,"camara","CORTE DIRECTO al cuarto (sin fade)")
    s.mark(6,7,1,"objeto","escritorio · escribe la señal 9 de un tirón")
    s.mark(7,9,3,"objeto","ventana · camina ida y vuelta, sin decisión")
    s.mark(8,8,4,"salida","fin de escena · fade a Acto III")
    s.actor("P",1,2,VIOLET); s.actor("U",2,5)

    s.finish(
        "¿Acercarse al borde o Quedarse en la sombra?",
        ['Ambas terminan en la misma línea.',
         'El segundo tramo (cuarto) NO tiene decisión:',
         'un solo camino, escritorio ↔ ventana.'],
        ['PABLO (muy bajo): "Se está quedando sin',
         '  necesitar que le explique nada."',
         '— corte al cuarto —',
         'PABLO: "Bueno. Ahora o nunca, entonces."',
         '(escribe de un tirón · la dobla igual que siempre)',
         'PABLO: "Tres semanas para entregarla.',
         '  Un poco patético, pero bueno."'],
        "Único interludio con DOS escenarios. La señal 9 se escribe acá y tarda 3 semanas en llegar al Mirador.")


for f in (i1,i2,i3,i4,i5): f()
print("\nlisto")
