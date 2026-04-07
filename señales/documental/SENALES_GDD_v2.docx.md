**S E Ñ A L E S**

**El Umbral del Barrio**

Game Design Document — Versión 2.0 (Edición Expandida)

*Un juego sobre las señales que alguien deja cuando no sabe cómo decirlo.*

| Motor / Plataforma | Godot 4.x — Android (portrait, soporte landscape opcional) |
| :---- | :---- |
| **Género** | RPG narrativo de exploración \+ Action-RPG post-Umbral — Pixel Art |
| **Tiles** | 32×32 px. Personajes 16×32 (exteriores), 16×24 (interiores) |
| **Perspectiva** | Top-down 2D exterior / 2.5D lateral en interiores y El Revés |
| **Duración** | 5–9 horas (completo) / 3–4 horas (historia principal) |
| **Sistema de guardado** | Anclajes \+ Autoguardado. Sin Game Over permanente. |
| **Clasificación** | T (Teen) / \+13 — violencia fantástica, contenido emocional |
| **Idioma** | Español rioplatense |
| **Equipo mínimo** | 1 programador · 1 artista pixel · 1 escritor · 1 músico |

# **ÍNDICE**

* 1\. Nombre y Concepto

* 2\. El Mundo — Diseño General

* 3\. El Umbral — El Evento que lo Cambia Todo

* 4\. Sistema de Clases y Poderes

* 5\. Sistema de Combate Detallado

* 6\. Enemigos y Criaturas

* 7\. Sistema de Muerte y Resurrección (Anclajes)

* 8\. Sistema de Ánimo y Progresión

* 9\. Sistema de Inventario y Equipamiento

* 10\. Sistema de Decisiones y Finales

* 11\. HISTORIA COMPLETA — Los Cinco Actos

* 12\. Flujo del Juego Paso a Paso

* 13\. Desarrollo de Personajes

* 14\. Pablo Daniel Santellan — Perfil Completo

* 15\. Mundo y Zonas

* 16\. Diseño de Mapas

* 17\. Misiones Principales y Secundarias

* 18\. Todos los Diálogos Importantes

* 19\. Eventos Clave

* 20\. Construcción Emocional de la Declaración Final

* 21\. Dirección Artística

* 22\. UI / UX

* 23\. Música y Diseño Sonoro

* 24\. Sistema de Guardado

* 25\. Apéndices Técnicos (Godot)

# **1\. NOMBRE Y CONCEPTO**

## **Título: SEÑALES — El Umbral del Barrio**

El título principal, SEÑALES, opera como en la versión anterior: es el lenguaje con que alguien que no sabe hablar directo elige comunicarse. El subtítulo, El Umbral del Barrio, introduce la segunda capa del juego: una fractura entre el mundo cotidiano y una dimensión paralela que emerge de la acumulación de años de soledad colectiva.

| SEÑALES | El rastro de objetos que alguien dejó para Uma. El idioma privado de quien la conoce mejor de lo que ella sabe. La forma en que una declaración se construye antes de pronunciarse. |
| :---- | :---- |
| **El Umbral** | La fractura dimensional que abre el segundo acto. El momento en que el barrio 'se dobla' y la realidad cotidiana coexiste con lo fantástico. |
| **El Barrio** | No es un escenario genérico: es el mundo emocional de Uma, externalizado. Cuando el barrio se rompe, Uma también se rompe. Cuando sana, ella también. |

## **Propuesta de Valor**

SEÑALES combina la intimidad emocional de un walking simulator narrativo con el gameplay de un action-RPG de exploración. La primera mitad del juego se siente como un slice-of-life de verano argentino. La segunda mitad agrega dimensiones fantásticas que sirven como metáfora amplificada de los conflictos emocionales reales. El núcleo nunca cambia: hay una persona que dejó suficientes señales para que Uma, si presta atención, llegue al lugar correcto y escuche lo que nunca se dijo en voz alta.

# **2\. EL MUNDO — DISEÑO GENERAL**

## **Barrio Sauco — La Base**

El juego transcurre en Barrio Sauco, un barrio ficticio de una ciudad argentina mediana durante el mes de febrero. Es el tipo de lugar donde los árboles son más viejos que los edificios, donde el kiosquero sabe cómo te llamás aunque seas cliente de tres meses, y donde las tardes de verano tienen una calidad de luz que los que viven ahí rara vez aprecian porque es todo lo que conocen.

Geográficamente, Sauco tiene tres niveles de elevación: el centro plano (la Plaza Mayor, el mercado, las calles comerciales), la media ladera (barrio residencial tranquilo, el parque ribereño) y la zona alta (edificios más viejos, calles más angostas, el Mirador). Esta topografía se vuelve crucial después del Umbral.

## **El Revés — La Dimensión Paralela**

El Revés es la contracara dimensional de Barrio Sauco. Existió siempre, como la sombra emocional del barrio: un espacio donde las memorias no resueltas, los vínculos rotos y las emociones ignoradas tomaron forma física. Durante décadas, estuvo contenido. Pero la acumulación de soledad colectiva, impulsada y amplificada por El Vacío, debilitó el umbral hasta que se rompió.

| Cómo se ve | El Revés es el barrio reconocible pero invertido en tono: las calles son de material traslúcido que brilla desde abajo, los edificios tienen sus fachadas normales pero sus interiores contienen versiones distorsionadas del pasado. El cielo es un gradiente de violeta a negro con estrellas que se mueven despacio. |
| :---- | :---- |
| **Tiempo** | En El Revés el tiempo es no-lineal. Pueden verse versiones del pasado del barrio superpuestas al presente. |
| **Habitantes** | Los denizens de El Revés son: Resonantes (seres de energía pura, no maliciosos), Guardianes del Revés (criaturas territoriales, neutrales), Ecos (fragmentos del Vacío), y las Memorias (fantasmas de personas que tuvieron un vínculo muy fuerte con el barrio). |
| **Acceso** | Post-Umbral, hay grietas en varios puntos del barrio que permiten cruzar. Antes del Umbral, solo quienes tienen Visión de Resonancia pueden percibirlo. |

## **La Dualidad del Mundo**

Después del Umbral, el juego se desarrolla en ambas capas simultáneamente. Hay zonas que existen solo en el Barrio, zonas que existen solo en El Revés, y zonas superpuestas donde ambas capas son visibles y navegables. Esta dualidad permite que la narrativa use la fantasía como amplificador emocional: los conflictos personales de los NPCs se materializan en El Revés como criaturas o fenómenos que Uma debe resolver.

# **3\. EL UMBRAL — EL EVENTO QUE LO CAMBIA TODO**

## **3.1 Qué es el Umbral**

El Umbral es el nombre que los denizens de El Revés dan a la fractura dimensional que ocurre en el centro exacto del Acto I. Es el momento en que el barrio se dobla. El detonante inmediato es la destrucción del último Anclaje Natural del barrio — un árbol viejo en la Plaza Mayor cuyas raíces servían como punto de sutura entre las dos dimensiones. El árbol muere por causas aparentemente naturales (una plaga) pero en realidad El Vacío llevaba años socavando sus raíces desde El Revés.

## **3.2 La Secuencia del Umbral**

Uma está en Plaza Mayor cuando el árbol colapsa. El juego pausa el movimiento libre. La secuencia es cinemática:

**NARRACIÓN (texto en pantalla, tipografía fragmentada):**

El árbol cae sin ruido.

Eso es lo primero que Uma nota: que un árbol tan grande no debería caer sin ruido.

Después, el cielo.

No cambia de color. Se dobla. Como papel.

El suelo de la plaza se parte en líneas de luz violeta. Las grietas se abren hacia todos lados. El ambiente sonoro cae a silencio total por 3 segundos. Luego una onda de presión sale del centro — los NPCs caen, las palomas vuelan en espiral — y el mundo vuelve a ser visible, pero ahora diferente.

| Qué cambia visualmente | El cielo alterna entre el azul del día y un violeta nocturno según la zona. Algunos edificios muestran superposición de su versión del Revés. Las sombras van en más de una dirección. |
| :---- | :---- |
| **Qué cambia** **jugablemente** | Aparecen grietas navegables. Los Ecos Menores se vuelven más agresivos. Nuevas criaturas emergen. El mapa se expande con zonas del Revés. Los NPCs con poder latente lo manifiestan. |
| **Qué cambia** **narrativamiente** | El padre de Uma (Darío) activa protocolo de investigación oficial. La misión de Uma se vuelve urgente. Pablo, hasta ahora invisible, empieza a ser perceptible incluso para quienes no tienen poderes. |

## **3.3 La Visión de Clase**

Justo después de recuperarse del golpe de la onda, Uma se queda inconsciente 20 segundos reales. Durante ese tiempo se produce la VISIÓN DE CLASE: uma entra en un espacio vacío de tono blanco donde tres figuras de luz le ofrecen un camino. Es la única decisión irrevocable del juego.

| CLASE | DESCRIPCIÓN | JUSTIFICACIÓN NARRATIVA |
| :---- | :---- | :---- |
| MAGA (Tejedora) | Usa Magia de Vínculo — proyectiles de energía emocional, escudos de resonancia, habilidades de sanación. Alta movilidad, daño desde distancia. Mejor árbol de diálogo con NPCs y criaturas. | Uma siempre sintió las emociones de los demás con intensidad inusual. Su poder manifiesta esa empatía como fuerza física. La abuela de Pablo (Doña Carmen, Tejedora) la reconoce en El Revés: 'Sos de los nuestros.' |
| GUERRERA (Anclada) | Usa Técnica de Anclaje — combate cuerpo a cuerpo, escudos físicos, golpes de tierra. Alta defensa, daño en área. Puede crear barreras que protegen NPCs. | Uma canalizó siempre su empatía hacia acción directa — se mete en situaciones difíciles en vez de observarlas. Su poder es estabilizador: ancla las cosas donde deben estar. |
| RESONANTE (Cantora) | Usa Magia de Sonido — ataques de onda sonora, canciones que afectan criaturas de formas únicas, habilidad de comunicar sin palabras con los Ecos. | Uma tiene una relación inconsciente con la música — las canciones la mueven de maneras que no entiende del todo. Al Resonar, esa sensibilidad se vuelve literal: sus palabras tienen peso físico. |

Cada clase tiene exactamente las mismas opciones narrativas. Las diferencias son puramente jugables: tipo de ataque, habilidades disponibles y cómo algunos NPCs reaccionan al poder de Uma. Ninguna clase bloquea misiones ni cambia el final.

# **4\. SISTEMA DE CLASES Y PODERES**

## **4.1 Justificación Narrativa de los Poderes**

Los poderes en SEÑALES no son arbitrarios. Existen porque El Umbral desbloqueó una capa de la realidad que siempre estuvo ahí. No todas las personas tienen poderes post-Umbral: solo quienes ya tenían un vínculo emocional inusualmente intenso con el barrio o con otras personas. Los poderes son, en todos los casos, una amplificación de algo que ya estaba.

| Uma Torres | Su empatía extraordinaria se convierte en poder activo. Ver sección de clase. |
| :---- | :---- |
| **Pablo D. Santellan** | Visión de Resonancia — ve las huellas emocionales en lugares y objetos. Pre-existía al Umbral. Se amplifica post-Umbral: ahora puede navegar El Revés conscientemente. |
| **Graciela** | Memoria Corporal — puede ver el pasado de los objetos que toca. Se activa post-Umbral sin que ella lo busque. |
| **Don Pepe** | Escucha Profunda — puede escuchar conversaciones del pasado en los lugares donde ocurrieron. Le aterra. |
| **Darío Torres** | Sin poder — pero con entrenamiento policial y conocimiento del barrio, es igualmente eficaz como soporte táctico. |
| **El Vacío** | No es un poder: es una presencia. Existe desde antes que el barrio. Ve la sección de Antagonista. |

## **4.2 Árbol de Habilidades por Clase**

### **MAGA (Tejedora)**

| NIVEL | HABILIDAD | DESCRIPCIÓN |
| :---- | :---- | :---- |
| 1 — Base | Hilo de Vínculo | Proyectil de energía rosa. Daño básico. Velocidad media. |
| 2 — Acto II | Escudo de Resonancia | Barrera circular. Absorbe 2 golpes. Costo: 15% energía. |
| 3 — Acto II | Sanación de Vínculo | Restaura 20 Ánimo. Funciona en NPCs también. Costo: 10% energía. |
| 4 — Acto III | Red de Hilos | Múltiples proyectiles en abanico. Costo: 20% energía. |
| 5 — Acto IV | Tejido Mayor | Paraliza enemigos 3 seg con red de energía. Costo: 40% energía. |
| Ultimate | Resonancia Total | Uma libera toda su energía en un pulso que disuelve todos los Ecos en pantalla. 60 seg de recarga. |

### **GUERRERA (Anclada)**

| NIVEL | HABILIDAD | DESCRIPCIÓN |
| :---- | :---- | :---- |
| 1 — Base | Golpe de Anclaje | Melee directo. Alto daño, corto alcance. |
| 2 — Acto II | Barrera de Tierra | Muro físico protege a Uma y NPCs cercanos. Dura 8 seg. |
| 3 — Acto II | Salto de Impacto | Uma salta y cae con impacto que aturde enemigos en área. |
| 4 — Acto III | Cadena de Anclaje | Golpe que encadena hasta 3 enemigos, incapacitándolos brevemente. |
| 5 — Acto IV | Fortaleza | Uma se vuelve inmune a daño 5 seg y su siguiente golpe hace daño triple. |
| Ultimate | Terremoto Menor | Sacudida de área que derriba a todos los enemigos en pantalla. 60 seg de recarga. |

### **RESONANTE (Cantora)**

| NIVEL | HABILIDAD | DESCRIPCIÓN |
| :---- | :---- | :---- |
| 1 — Base | Nota Aguda | Onda sonora de alcance medio. Daño y aturde brevemente. |
| 2 — Acto II | Canción de Calma | Detiene a los Ecos Menores sin dañarlos. Permite diálogo inmediato. |
| 3 — Acto II | Escudo Armónico | Barrera de sonido que refleja proyectiles menores. |
| 4 — Acto III | Disonancia | Daño masivo sonoro en área. Especialmente efectivo en El Revés. |
| 5 — Acto IV | Coro | Uma invoca eco de su propia voz como aliado temporal en combate. |
| Ultimate | La Canción del Barrio | Uma canta una melodía que restaura Ánimo de todos los aliados en pantalla y paraliza enemigos. 60 seg. |

# **5\. SISTEMA DE COMBATE DETALLADO**

## **5.1 Filosofía de Combate**

El combate de SEÑALES tiene dos modos que coexisten según el tipo de enemigo:

| Combate de Resonancia (pre-Umbral y Ecos) | Sistema de empatía activa: Uma escucha al Eco, identifica su dolor y elige la respuesta correcta. No hay daño físico, pero el error tiene costo de Ánimo. |
| :---- | :---- |
| **Combate Activo** **(post-Umbral)** | Acción en tiempo real con mecánicas ARPG simplificadas. Movimiento libre, ataque básico siempre disponible, habilidades según clase con cooldown. El tono nunca es gore: las criaturas se disuelven, los Vaciados se liberan. |

## **5.2 Mecánicas de Combate Activo**

| Ataque básico | Tap en enemigo cercano (si tiene touchscreen) o botón A cuando el enemigo está en rango. Daño bajo, sin cooldown. Animación específica por clase. |
| :---- | :---- |
| **Habilidades** | Botones B, Y, X en la zona derecha de la pantalla. Cooldown individual de cada habilidad. Indicador visual de recarga. |
| **Esquiva** | Swipe en cualquier dirección \= esquiva rápida. 0.8 seg de invencibilidad. Uma puede esquivar infinitas veces pero cansa (si esquiva 4+ veces seguidas, el movimiento se enlentece levemente 2 seg). |
| **Barra de Energía** | Uma tiene 100 puntos de energía que se consumen con habilidades. Se recarga 5 puntos por segundo en combate, 15 puntos por segundo fuera de combate. |
| **Finisher de Conexión** | Cuando un enemigo llega al 20% de HP, aparece una opción de 'Conexión Final' (ícono de mano). Si Uma la usa en vez de atacar, el enemigo se disuelve más rápido y deja mejor recompensa. |

## **5.3 Sistema de Combate de Resonancia**

Este sistema se usa exclusivamente con Ecos y Vaciados. Permanece del diseño original pero expandido:

| Fase 1 — Escuchar (10 seg) | El enemigo emite fragmentos de texto/audio. Uma puede elegir 'escuchar' (inmóvil, sin ser atacada) o ignorarlo. Si escucha: gana pista sobre la respuesta correcta. Si ignora: combate estándar. |
| :---- | :---- |
| **Fase 2 — Responder (3 opciones)** | Uma elige una de tres respuestas. Las opciones varían según clase (Maga tiene opción de empatía extra, Guerrera tiene opción de firmeza, Resonante tiene opción de cantar). La respuesta correcta es siempre la más específica al dolor del Eco. |
| **Fase 3 — Resolución** | Correcto x2/3 → Eco se disuelve, deja Fragmento de Memoria, Uma gana Ánimo. Correcto x1/3 → Eco se retira sin Fragmento. Incorrecto → Eco contraataca. |

## **5.4 Estado de Combate — UI**

Durante el combate activo, el HUD mínimo expande levemente:

* Barra de HP del enemigo aparece sobre su cabeza (no numérica — visual)

* Barra de energía de Uma aparece bajo su sprite

* Indicadores de cooldown de habilidades en la zona inferior derecha

* Si hay un NPC aliado, su barra de HP aparece en la esquina superior izquierda

# **6\. ENEMIGOS Y CRIATURAS**

## **6.1 Clasificación General**

| TIPO | ORIGEN | SISTEMA DE DERROTA |
| :---- | :---- | :---- |
| Ecos Menores | Fragmentos del Vacío. Pre-Umbral. | Resonancia (diálogo) |
| Ecos Mayores | Fragmentos del Vacío más densos. Post-Umbral. | Combate \+ Resonancia final |
| Sombras Errantes | Memorias sin resolver del Barrio. | Combate activo. No-letales. |
| Vaciados | NPCs temporalmente poseídos por El Vacío. | Solo Resonancia. No deben ser dañados físicamente. |
| Guardianes del Revés | Criaturas antiguas de El Revés. Neutrales hasta que se les molesta. | Combate activo o Negociación (Maga/Resonante tienen opción) |
| Fragmentos del Vacío | Manifestaciones grandes del antagonista. Son los jefes. | Combate \+ fase final de Resonancia |
| El Vacío | El antagonista central. | Secuencia narrativa especial |

## **6.2 Ecos Menores**

| Apariencia | Figura humanoide de niebla gris. Altura 1/3 de Uma. Movimiento lento y errático. Emite un sonido como respiración entrecortada. |
| :---- | :---- |
| **Comportamiento** | Deambula solo. Se acerca a Uma si la ve. Si la toca: \-10 Ánimo. No ataca con intención, solo busca contacto. |
| **Historia** | Cada Eco Menor es un fragmento de una emoción específica: hay Ecos de soledad, de miedo al abandono, de ira no expresada. Su texto en el sistema de Resonancia revela cuál. |
| **Resolución** | 2 respuestas correctas de 3\. Al disolverse emite un sonido suave y deja un Fragmento de Memoria y a veces un ingrediente de comida. |

## **6.3 Ecos Mayores**

| Apariencia | Figura de 2x Uma de alto. Forma vagamente humana pero distorsionada. Un ojo de luz dorada. Movimiento fluido, inquietante. |
| :---- | :---- |
| **Comportamiento** | Ataca activamente. Proyecta pulsos de energía oscura (daño \-15 por golpe). Puede crear copias menores de sí mismo (1-3 Ecos Menores como escudos). |
| **Mecánica especial** | Inmune a ataques físicos básicos hasta reducir HP al 30%. Una vez al 30%, se inmoviliza y pide Resonancia (fase de diálogo). Si Uma falla Resonancia: Eco Mayor se recupera al 50% HP. |
| **Resolución** | HP a 0 \+ Resonancia exitosa. Deja Fragmento de Memoria Mayor (historia larga), un objeto de equipamiento y \+25 Ánimo. |

## **6.4 Sombras Errantes**

| Apariencia | Silueta negra bidimensional de figura humana del pasado (vestimenta desactualizada). No tiene cara. Sus bordes tiemblan. |
| :---- | :---- |
| **Comportamiento** | Patrulla un área pequeña. Si Uma entra a su radio: la persigue. Ataque de toque (-12 Ánimo). Se puede dispersar con ataques normales pero reaparece al minuto si Uma no resolvió el conflicto del área. |
| **Historia** | Cada Sombra está ligada a un evento del pasado del barrio. Resolverla permanentemente requiere encontrar el 'ancla' del evento (un objeto o NPC relacionado) y usarla en el área. |
| **Lore** | Son distintas a los Ecos: las Sombras no vienen del Vacío. Son ecos de personas reales que tuvieron emociones muy intensas en ese lugar. |

## **6.5 Vaciados**

| Apariencia | NPCs normales pero con ojos completamente blancos y movimiento en zigzag. Una marca oscura en el cuello (la mano del Vacío). |
| :---- | :---- |
| **Comportamiento** | Agresivos. Atacan a Uma física y verbalmente (los Vaciados dicen cosas crueles que son las dudas internas de la persona poseída). Daño: \-20 por golpe. Alta velocidad. |
| **Mecánica CRÍTICA** | Atacar a un Vaciado con habilidades físicas aumenta el control del Vacío sobre él. Solo el combate de Resonancia los libera. Si Uma los golpea: reciben daño de verdad y eso daña la relación con ese NPC permanentemente. Esto está señalizado claramente. |
| **Resolución** | Solo Resonancia: Uma escucha lo que el Vacío usa contra esa persona y le da la respuesta contraria — el recuerdo, el vínculo, la razón para seguir. Al liberarse, el NPC colapsa, Uma puede ayudarlo a levantarse, y la relación sube al nivel máximo. |

## **6.6 Guardianes del Revés**

| Tipos | Hay 4 tipos de Guardianes. Cada uno cuida una zona de El Revés. |
| :---- | :---- |
| **El Tejedor Ciego** | Araña gigante de hilos de luz. Guarda el núcleo de El Revés. Hostil si Uma no tiene el 'Hilo de Paso' (objeto de misión). |
| **El Centinela de Piedra** | Figura de roca con corazón de fuego violeta. Guarda el acceso a la Sala del Vacío. No puede vencerse en combate — solo con la Clave de Resonancia. |
| **Los Pájaros de Tinta** | Bandada de criaturas de tinta negra que vuelan en formación. Confunden a Uma cambiando el diseño del nivel. Se calman con la habilidad de Resonante o con un item específico. |
| **La Memoria de Agua** | Figura fluida de agua de color azul. Custodia un evento del pasado importante. No ataca si Uma lleva la señal de Mateo... de Pablo. Reacciona a los objetos de Doña Carmen. |

## **6.7 Jefes — Fragmentos del Vacío**

### **FRAGMENTO I — 'El Abandono' (Jefe del Acto II)**

| Apariencia | Una figura gigante (5x Uma) hecha de cuartos vacíos superpuestos. Cada cuarto visible en su cuerpo es la habitación de alguien que se fue sin despedirse. |
| :---- | :---- |
| **Arena** | El sótano del Mercado Viejo, invadido por El Revés. |
| **Fases** | Fase 1: proyecta objetos personales como proyectiles. Fase 2: divide el arena en 4 cuartos oscuros, Uma debe moverse entre ellos. Fase 3 (Resonancia): Uma escucha a quién abandonó a quién y le responde. |
| **Resolución narrativa** | El Fragmento del Abandono se disuelve cuando Uma lo llama por el nombre de la emoción específica y le ofrece un recuerdo de regreso. |
| **Recompensa** | Habilidad de nivel 3\. Acceso al sótano completo. Fragmento de Memoria Mayor que revela parte del pasado de Doña Carmen. |

### **FRAGMENTO II — 'El Olvido' (Jefe del Acto III)**

| Apariencia | Una figura que cambia de forma según lo que Uma más teme olvidar (adaptativa según las señales que haya encontrado). |
| :---- | :---- |
| **Arena** | El Revés completo — el espacio es infinito y sin paredes. |
| **Mecánica especial** | Cada vez que El Olvido toca algo en el arena, ese objeto desaparece del mapa permanentemente (objetos decorativos, no mecánicos). El jugador siente la pérdida visualmente. |
| **Resolución narrativa** | Uma debe usar todas las señales de Pablo que tiene en el inventario como proyectiles de Resonancia. Cada señal ilumina un fragmento del Fragmento hasta disolverlo. |
| **Recompensa** | Habilidad de nivel 4\. Pablo aparece en El Revés por primera vez visible y habla brevemente con Uma. |

### **FRAGMENTO III — 'El Miedo al Decir' (Jefe final, Acto IV)**

| Apariencia | La forma de El Vacío más cercana a humana: una silueta que alterna entre ser Uma y ser otra persona (Pablo, aunque Uma no lo sabe todavía). Cada vez que ataca, dice una frase que Uma pensó pero nunca dijo. |
| :---- | :---- |
| **Arena** | El Mirador, invadido por El Revés. El fondo muestra el barrio desde arriba. |
| **Mecánica especial** | Cada ataque del Fragmento usa las dudas de Uma: 'nadie quiere escucharte', 'es demasiado tarde', 'se va a ir'. Estas frases aparecen en pantalla con tipografía grande. Uma puede contraatacarlas con fragmentos de los diálogos de sus NPCs (ataques especiales que se desbloquean al tener relaciones altas). |
| **Resolución narrativa** | El Fragmento se disuelve solo cuando Uma usa la última señal de Pablo — no como arma, sino como escudo. La señal actúa como barrera de resonancia que El Miedo no puede penetrar. |
| **Recompensa** | El Umbral se estabiliza. Pablo puede cruzar de regreso al Barrio. La secuencia de la declaración comienza. |

# **7\. SISTEMA DE MUERTE Y RESURRECCIÓN — LOS ANCLAJES**

## **7.1 Concepto**

Uma puede morir en combate. Cuando su Ánimo llega a 0 por daño de combate (no de sol — el sol solo la debilita), Uma colapsa. La pantalla hace un fundido suave a blanco. Uma se desintegra en partículas de luz. Este es el único momento visualmente 'dramático' — pero no aterrador. Las partículas de luz flotan hacia abajo, hacia la tierra, como si el barrio la estuviera absorbiendo.

## **7.2 Justificación Narrativa**

Las señales que Pablo dejó repartidas por el barrio no son solo mensajes: cada una cargaba, sin que él lo supiera conscientemente, un fragmento de su Visión de Resonancia. Al colocarlas, Pablo imprimió en esos puntos del barrio una conexión emocional extraordinariamente densa. Estas conexiones funcionan como cuerdas invisibles que anclan el ser de Uma al lugar cuando ella 'se suelta' por el golpe.

En términos del lore: Doña Carmen, la abuela de Pablo, diseñó este sistema hace décadas como protección para 'las que caminan con los ojos abiertos' — personas con empatía extraordinaria que son naturalmente vulnerables en El Revés. El poder de Pablo, heredado de ella, lo replicó instintivamente al dejar cada señal.

Uma lo descubre en el Acto III en un Fragmento de Memoria Mayor: encuentra el diario de Doña Carmen en El Revés. La última entrada dice: 'Si lo heredó bien, sus señales van a cuidar a quien las siga.' Uma lo lee. Monólogo interno:

*"No sé si reírme o llorar. Alguien que no me conoce me está cuidando a través de su nieto. El universo tiene muy malos modales."*

## **7.3 Los Anclajes — Puntos de Resurrección**

Los Anclajes son ubicaciones específicas del barrio que tienen una densidad emocional alta. Algunos son naturales (existían antes del Umbral), otros se activan cuando Uma establece una conexión profunda con el lugar o el NPC relacionado.

| ANCLAJE | UBICACIÓN | CÓMO SE ACTIVA |
| :---- | :---- | :---- |
| Anclaje 0 — La Mesita de Noche | Cuarto de Uma, Casa Torres | Siempre activo. El primer Anclaje. |
| Anclaje 1 — El Banco de Graciela | Tienda de objetos viejos | Activado al completar la misión de Graciela (nivel 2). |
| Anclaje 2 — La Fuente Seca | Plaza Mayor, centro | Activado al recoger el disco de vinilo del Acto I. |
| Anclaje 3 — El Escalón del Mercado | Entrada al Mercado Viejo | Activado al conocer a Doña Elsa (primera conversación). |
| Anclaje 4 — El Banco del Río | Parque Ribereño | Activado al esperar 3 minutos en el banco (evento contemplativo). |
| Anclaje 5 — La Grieta Principal | Centro de El Revés | Activado al completar el jefe del Acto II. |
| Anclaje 6 — El Escalón del Mirador | Pie de la escalera del Mirador | Activado automáticamente al llegar. No puede desactivarse. |

## **7.4 La Experiencia de Muerte y Regreso**

Cuando Uma muere:

* Pantalla fundida a blanco suave (0.5 segundos)

* Las partículas de Uma flotan hacia el suelo

* El ambiente sonoro cae a silencio

* Una voz muy suave (el eco de la voz de Doña Carmen) dice una sola frase cada vez. Hay 8 frases distintas que rotan aleatoriamente

* Fundido de regreso desde el último Anclaje activado. Uma aparece sentada, se levanta

* Ánimo se restaura al 30%

* Los enemigos del área se regeneran si estaban en combate activo

Frases de Doña Carmen al morir:

*'Todavía no, querida.'*

*'El barrio te aguarda.'*

*'Volvé. Siempre volvé.'*

*'Eso no era tu momento.'*

*'Levantate. Hay más por hacer.'*

*'Te lo dije: las que caminan con los ojos abiertos no se van así nomás.'*

*'Un poco más, nomás.'*

*'El hilo no se cortó. Seguí.'*

## **7.5 Diálogos Post-Muerte de Uma**

El monólogo interno de Uma cambia según cuántas veces murió:

| MUERTES | MONÓLOGO DE UMA AL REGRESAR | TONO |
| :---- | :---- | :---- |
| 1ª vez | '¿Qué fue eso? Estoy... estoy en el Anclaje. Bien. Ok. Bien.' (pausa) 'BIEN.' | Confusión, adrenalina |
| 2ª vez | 'Otra vez. Ok. No me muero de verdad. O sí. No sé. El barrio me escupe de vuelta, supongo. Gracias, barrio.' | Procesando |
| 3ª vez | 'La tercera vez ya no me asusta. Ya sé que vuelvo. Lo que no sé es si eso me hace más valiente o más inconsciente.' | Sarcasmo cómodo |
| 4ª+ vez | 'Seis siete, Doña Carmen, te debo una.' / 'Cuarto intento. Me voy a acordar de esto.' | Normalización |

# **8\. SISTEMA DE ÁNIMO Y PROGRESIÓN**

## **8.1 El Ánimo — Revisado**

El medidor de Ánimo (0–100) representa el estado emocional y físico de Uma. Post-Umbral también funciona como barra de HP en combate. La pérdida por combate es más rápida que la pérdida por exploración, pero la recuperación también lo es.

| 100–70 — Conectada | Uma en su mejor estado. Comentarios irónicos y agudos. Acceso a todas las opciones de diálogo. Colores del sprite más vivos. |
| :---- | :---- |
| **69–40 — Regular** | Sprite levemente más apagado. Diálogos más cortos. Uma dice cosas como 'tá. tá.' o 'qué largo está quedando el día'. Algunas opciones valientes se grisan. |
| **39–15 — Al límite** | Movimiento 15% más lento. Comentarios de cansancio genuino. 'Me quiero sentar un segundo, juro.' / 'Ok. Esta vez sí me quemo.' La barra parpadea levemente. |
| **14–1 — Crítico** | Sprite con efecto de distorsión suave. Uma dice 'no' a muchas cosas. Una sola habilidad disponible. |
| **0 — Resurrección** | Muerte. Ver sección 7\. No hay Game Over permanente. |

## **8.2 Progresión — Las Resonancias**

Uma no sube de nivel de forma numérica. Progresa a través de RESONANCIAS desbloquedas al completar arcos emocionales de NPCs y hitos narrativos:

| RESONANCIA | CÓMO SE DESBLOQUEA | EFECTO |
| :---- | :---- | :---- |
| Presencia | Completar arco de Graciela | Uma puede quedarse junto a NPCs solos sin hablar y su presencia los calma. Reduce frecuencia de Vaciados en el área cercana. |
| Lectura | Completar arco de Don Pepe | Uma puede 'leer' objetos para revelar capas profundas de lore e historia. Desvela secretos de El Revés. |
| Voz Firme | Resolver 5 Ecos por Resonancia | Uma puede completar Resonancias con 1 respuesta correcta de 3 (en vez de 2). Algunos Ecos se disuelven solo con su presencia. |
| Memoria Viva | Completar el Mercado Viejo | Los Fragmentos de Memoria se vuelven interactivos. Uma puede 'entrar' brevemente en la memoria. |
| La Señal | Recoger 7/9 señales de Pablo | Uma siente la dirección de la próxima señal. Destello suave en el minimapa. |
| Tejido Compartido | Completar el arco de Pablo en El Revés | Sinergía con Pablo: cuando Pablo está cerca en El Revés, Uma gana \+20 Ánimo pasivo. |

# **9\. SISTEMA DE INVENTARIO Y EQUIPAMIENTO**

## **9.1 La Mochila de Uma — Slots**

| Señales de Pablo (9 total) | Sección especial del cuaderno. No ocupan slot normal. Son el núcleo narrativo y también munición especial en el jefe del Acto IV. |
| :---- | :---- |
| **Equipamiento (3 slots)** | Ítems que modifican stats de Uma. Ver sección de equipamiento. |
| **Consumibles (4 slots)** | Comida, pociones de El Revés. Restauran Ánimo. |
| **Objetos Clave (3 slots)** | Objetos necesarios para misiones. Se usan y desaparecen. |
| **Fragmentos de Memoria (sin límite)** | Van al cuaderno. No ocupan slots normales. |
| **Permanentes (sin slot)** | Protector solar, auriculares, cuaderno. Siempre con Uma. |

## **9.2 Equipamiento**

| ÍTEM | DÓNDE SE CONSIGUE | EFECTO |
| :---- | :---- | :---- |
| Cordones Rosa | Tienda de Graciela (post-arco) | La historia de los cordones como talismán. \+15 Ánimo máximo. Referencia a Agujetas. |
| Guante de Resonancia | El Revés, tras jefe del Acto II | Reduce cooldown de habilidades en 15%. |
| Anteojos de Memoria | Doña Elsa, post-misión radio | Permite ver Sombras Errantes antes de que aparezcan (aviso de 3 seg). |
| Cinta del Barrio | Don Mario (NPC post-Umbral) | \+10 Ánimo máximo. Reduce penalización del sol a la mitad. |
| Hilo de Doña Carmen | El Revés, Sala de la Memoria | Solo disponible en segunda mitad. \+25% daño de Resonancia. Permite entrar en El Revés sin grieta cercana. |
| Nota de Héctor | Siempre disponible | El papá de Uma le deja una nota que Uma lleva. \+5 recuperación de Ánimo pasiva por minuto. |

## **9.3 Consumibles**

| ÍTEM | FUENTE | RESTAURA ÁNIMO |
| :---- | :---- | :---- |
| Medialunas | Kiosco de Chino, 10 pesos | 25 |
| Chipá | Doña Elsa, mercado | 20 |
| Mate (termo) | Casa Torres al inicio. Recargable en kioscos | 15 cada vez (3 usos por recarga) |
| Alfajor | Kiosco | 30 |
| Agua con gas | Kiosco | 10 (pero Uma dice 'es lo peor pero funciona') |
| Esencia de Resonancia | Criaturas de El Revés al disolverse | 40 (no disponible pre-Umbral) |
| Fruta de El Revés | Árboles de El Revés (recolectable) | 50 (Uma: 'No sé si esto es comible pero está deliciosa') |

# **10\. SISTEMA DE DECISIONES Y FINALES**

## **10.1 Decisiones que Importan**

| Elección de Clase (irrevocable) | La única decisión mecánica permanente. No cambia la historia ni el final, solo el estilo de juego. |
| :---- | :---- |
| **Árbol de Diálogos con NPCs** | Múltiples opciones por conversación. La opción más empática siempre desbloquea más historia. Nunca hay una elección que arruine permanentemente una relación, aunque algunas la retrasen. |
| **Señales opcionales** **(señales 6, 7, 8\)** | 3 de las 9 señales de Pablo están en zonas extra difíciles. Encontrarlas enriquece la declaración final con frases más específicas. |
| **Cómo resolver Vaciados** | Si Uma ataca a un Vaciado con poder físico, lo libera pero la relación baja permanentemente. Esto afecta qué NPCs aparecen en el Mirador al final. |
| **La Respuesta Final** | Las 3 opciones de respuesta de Uma a Pablo al final. Ver sección 10.3. |

## **10.2 Variables de Profundidad Narrativa**

El juego rastrea flags de:

* NPCs conectados (máx 12): cuántos aparecen en el fondo del Mirador

* Señales encontradas (máx 9): qué dice la declaración de Pablo

* Vaciados liberados sin daño (máx 4): tono emocional del Acto V

* Fragmentos de Memoria recolectados (máx 18): profundidad del cuaderno

* Veces que Uma murió: líneas opcionales de diálogo de Pablo en el final

## **10.3 Los Tres Finales**

### **FINAL COMPLETO — 'Sí' (Requiere 7+ NPCs, 6+ señales, Umbral cerrado)**

Uma responde de forma directa. El Mirador es el punto más alto del barrio. Desde ahí se ve Barrio Sauco reconstruido: algunas zonas todavía tienen el brillo violeta del Revés mezclado con la luz del atardecer — no es feo, es simplemente diferente. Los NPCs con los que Uma conectó aparecen en sus lugares habituales en el barrio de abajo, haciendo sus cosas. Todo sigue. Pero Uma está acá, arriba, y Pablo está a su lado, y la declaración ya fue.

La pantalla final: el cuaderno de Uma, abierto a la última página. Están todas las señales pegadas, con la declaración completa. En la página de enfrente, con letra de Uma: 'Seis siete.' Y una fecha.

### **FINAL SILENCIO (Cualquier condición)**

Uma no dice nada. Se sienta a su lado en la baranda. Pablo tampoco habla. La cámara se aleja lentamente. La pantalla oscurece en 20 segundos. El cuaderno final muestra solo la última señal, la más importante.

### **FINAL 'Mañana' (Pocos vínculos / menos señales / Uma dañó Vaciados)**

Uma dice que necesita tiempo. Pablo asiente sin dramatismo. 'Está bien. Sabés dónde encontrarme.' Se van juntos caminando de vuelta al barrio por caminos separados. La pantalla final muestra el cuaderno con una página nueva en blanco y el título: 'Señal pendiente.' Abajo, la fecha de hoy.

# **11\. HISTORIA COMPLETA — LOS CINCO ACTOS**

## **PRÓLOGO — El Martes de Febrero**

Uma Torres tiene 18 años, vive con su familia en Barrio Sauco y hace exactamente lo que siente ganas de hacer cada día, que a veces es mucho y a veces no es nada. Esta mañana en particular estaba escuchando música con el ventilador puesto y mirando cómo giraba el ventilador cuando su padre, Darío, entró al cuarto con la cara de 'necesito un favor'.

Tres vecinos reportaron haber encontrado objetos extraños: un origami de papel rosa en el patio de Graciela, un cassette sin etiqueta en la puerta de Don Pepe, y un portarretrato vacío con un cordón enroscado en la ventana de la maestra Marta. Nada amenazante. Pero extraño. Darío tiene turno en la comisaría y no puede investigarlo. Uma tiene el día libre. Darío deja plata para el kiosco.

Uma toma el mate que hizo Natalia, se despide de Bautista (que está construyendo lo que dice ser un auto de bomberos con bloques pero parece claramente una nave espacial), y sale. El sol está fuerte. Uma ya se puso tres veces el protector solar.

## **ACTO I — El Barrio de Siempre**

El primer acto transcurre en un Barrio Sauco completamente normal: calor de febrero, vecinos conocidos, la radio de Chino desde el kiosco, el gato de nadie que duerme en el umbral del número 847\. Uma recorre el barrio haciendo preguntas, conociendo historias, encontrando la primera señal (un origami rosa que Graciela tiene en el mostrador) y después la segunda y la tercera. Los objetos no son amenazantes; los que los recibieron no están asustados sino confundidos — y, en el caso de Graciela y Don Pepe, levemente emocionados aunque no lo admitan.

A medida que Uma avanza, aparecen los primeros Ecos: figuras grises en esquinas, bajo galerías, cerca de lugares que llevan tiempo abandonados. El sistema de Resonancia se presenta aquí: Uma aprende que los Ecos no son peligrosos si uno los escucha. El primer Eco que resuelve Uma es el del callejón detrás del almacén: una figura que repite fragmentos de una conversación que no llegó a tener.

En el transcurso del Acto I, Uma encuentra señales número 1, 2 y 3\. La señal 1 simplemente dice: 'Siempre te fijás en lo que los demás no ven.' Uma la lee, la dobla y la guarda. Monólogo interno: 'Quién escribe estas cosas. Quién las deja.' El juego no responde. Todavía.

Al final del Acto I, Uma está en Plaza Mayor cuando el árbol colapsa. El Umbral se abre.

## **ACTO II — El Barrio Roto**

El Barrio Sauco post-Umbral no es irreconocible, pero tampoco es el mismo. Las calles de siempre tienen ahora grietas de luz violeta en el suelo. El cielo alterna entre el azul del día y un violeta nocturno según la hora. Algunos edificios tienen sus fachadas normales pero sus sombras tienen formas equivocadas. Los Ecos Menores son más activos. Aparecen las primeras Sombras Errantes.

Uma, recién despertar de la visión de clase, tiene que navegar este nuevo mundo mientras trata de entender qué pasó. Darío la llama por teléfono y le dice que la situación en el barrio es seria: hay personas asustadas, algunas desaparecieron brevemente y reaparecieron en estado de shock, otras están 'raras' (los primeros Vaciados). Le pide a Uma que tenga cuidado pero también que siga — porque Uma tiene algo que otros no tienen. Darío no lo llama poder. Lo llama 'lo tuyo'.

El Acto II expande el mapa con las primeras grietas hacia El Revés. Uma puede entrar a El Revés brevemente en el Parque Ribereño (una zona donde la dimensión es especialmente delgada) y descubrir que el lugar es perturbador pero no hostil. Hay criaturas que la miran curiosas. Un Guardián del Revés la ignora si no lo ataca.

Las señales 4, 5 y 6 se encuentran en este acto. La señal 5 es la que dice: 'Me gusta cómo prestás atención a las cosas que los demás no ven.' Uma se detiene. El Fragmento del Abandono es el jefe del Acto II. Tras derrotarlo y acceder al sótano del Mercado, Uma encuentra el diario de Doña Carmen, que la lleva a la siguiente capa de la historia.

El Acto II termina cuando Uma conoce brevemente a Pablo. No de frente: lo ve de espaldas, cruzando una grieta hacia El Revés. Un NPC (Leo, el adolescente de la plaza) lo menciona después: 'Ese es Mateo... quiero decir Pablo. Pablo Santellan. Vive acá cerca. Es raro pero buena onda.'

## **ACTO III — El Revés**

Uma entra de lleno en El Revés para seguir las señales. Las señales 7 y 8 están en esta dimensión — colocadas por Pablo en sus incursiones anteriores. El Revés tiene su propia lógica: el tiempo se dobla, los lugares del barrio son reconocibles pero distorsionados, las emociones tienen peso físico.

En el centro de El Revés, Uma encuentra El Telar de Doña Carmen: una estructura de hilos de luz que conecta todos los Anclajes del barrio. Aquí entiende completamente el sistema de resurrección y la historia de Pablo. Aquí también encuentra a los Resonantes — seres de El Revés que son básicamente la versión amplificada de las emociones positivas del barrio — y puede hablar con ellos.

El jefe del Acto III es El Fragmento del Olvido. La batalla es larga y visualmente impresionante. Cuando El Fragmento cae, Pablo aparece en El Revés por primera vez visible y reconocible. El encuentro es breve:

**Pablo:**

*(de pie a 10 metros, en El Revés, mirando a Uma como si no pudiera creer que esté acá)*

Uma.

**Uma:**

*(lo mira. Primer plano de su cara.)*

Vos sos el que deja las señales.

**Pablo:**

*(asiente. Pausa larga.)*

¿Las seguiste todas?

**Uma:**

Todavía me faltan dos.

*(pausa)*

¿Podemos hablar cuando salga de acá?

**Pablo:**

*(una sonrisa pequeña que claramente está tratando de no ser grande.)*

Sabés dónde encontrarme.

Pablo desaparece. Uma sale de El Revés. Acto IV.

## **ACTO IV — La Fractura**

El Vacío tiene suficiente fuerza para empezar a manifestarse en el Barrio mismo — no solo a través de Ecos y Vaciados, sino como presencia. El Barrio Sauco se deteriora visualmente: las grietas se hacen más anchas, algunos NPCs están asustados, las zonas más afectadas huelen a silencio (Uma lo describe así).

Darío coordina una respuesta civil en la plaza pero la situación se sale de lo que un policía puede manejar. Uma es la única que puede llegar al núcleo del problema porque tiene las señales de Pablo como mapa implícito.

La señal 9 — la última — lleva a Uma al Mirador. Al llegar, el lugar está invadido por El Revés: el piso es de luz y el cielo es negro. El Fragmento del Miedo al Decir es el jefe. La batalla más difícil del juego, diseñada como una confrontación de Uma con sus propias dudas.

Cuando el Fragmento se disuelve (usando la última señal de Pablo como escudo), El Umbral comienza a estabilizarse. La dimensiones se separan lentamente. El cielo del Mirador se vuelve naranja y rosa: es el atardecer real, el primero que Uma ve con los ojos limpios desde que todo empezó.

## **ACTO V — La Señal Más Clara**

El barrio respira. Las grietas se cierran lentamente — no todas; algunas quedarán, convertidas en cicatrices luminosas que serán, con el tiempo, parte del paisaje de Barrio Sauco. Los NPCs salen de sus casas. Los que estaban Vaciados están bien. Fernet el gato apareció solo.

Pablo sube al Mirador.

Tiene el papel en la mano — el último, el que escribió de un solo golpe una tarde en su departamento — y está nervioso de una manera que Uma, que nota esas cosas, puede ver desde que asoma la cabeza sobre el último escalón.

Lo que pase después es cosa del jugador.

# **12\. FLUJO COMPLETO DEL JUEGO — PASO A PASO**

## **PRÓLOGO (15–25 min)**

* Tutorial de movimiento y exploración en la casa. Bautista como guía natural.

* Conversación con Natalia en la cocina (protector solar \= equipamiento permanente).

* Conversación con Darío: la misión. Uma acepta.

* Salida. El barrio se presenta. Sol intenso. Uma ya está protestando por el sol.

* Primer NPC libre: Chino en el kiosco. Tutorial de diálogo y compra de consumibles.

## **ACTO I (45–60 min)**

* Visita a Graciela → Primera señal (origami rosa). Tutorial de Resonancia con el primer Eco Menor.

* Visita a Don Pepe → Misión de Fernet el gato → Segunda señal (cassette). Don Pepe menciona a 'alguien que conoce a todos los que están solos en el barrio'.

* Visita a Marta → Tercera señal (portarretrato). Marta no sabe nada del autor pero describe con precisión cómo llegó: apareció de noche, sin ruido.

* Exploración libre: NPCs secundarios, Ecos Menores por el barrio, objetos de lore.

* EL UMBRAL. Secuencia cinemática. Uma inconsciente.

* VISIÓN DE CLASE. El jugador elige. Uma despierta con su poder activo.

* Primer combate post-Umbral: dos Ecos Menores que emergieron cerca.

* Fin del Acto I.

## **ACTO II (60–80 min)**

* Barrio post-Umbral: reconocimiento. Uma habla con Darío por teléfono.

* Señal 4: en el Parque Ribereño, pegada a un árbol que sobrevivió el Umbral.

* Primera incursión a El Revés desde el Parque. 5 minutos. Regreso.

* Misión del Mercado Viejo: Doña Elsa \+ la radio \+ misión de la foto de Graciela.

* Jefe del Acto II: El Fragmento del Abandono en el sótano del Mercado.

* Post-jefe: diario de Doña Carmen. Comprensión del sistema de Anclajes.

* Señal 5 (la clave narrativa): 'Me gusta cómo prestás atención...'. La sección Para Uma se desbloquea.

* Señal 6 (opcional): zona difícil, parte alta del Mercado Viejo.

* Uma ve a Pablo de espaldas cruzando una grieta. Leo lo nombra.

* Momento de Bautista: Uma vuelve a casa brevemente. Escena cómica y emotiva.

* Fin del Acto II.

## **ACTO III (50–70 min)**

* Entrada completa a El Revés. El barrio desde adentro.

* Señal 7: en El Revés, en el equivalente dimensional de la Plaza Mayor.

* Encuentro con los Resonantes. Información sobre El Vacío y su origen.

* El Telar de Doña Carmen: comprensión completa del lore de los Anclajes y Pablo.

* Señal 8 (opcional): zona oculta del Revés, acceso difícil.

* Jefe del Acto III: El Fragmento del Olvido.

* Post-jefe: primer encuentro breve con Pablo. Ver diálogo en sección 18\.

* Uma regresa al barrio. Todo el mundo sabe lo que se viene.

* Fin del Acto III.

## **ACTO IV (40–50 min)**

* El Barrio deteriorado. Darío necesita a Uma. Darío no pide ayuda fácilmente.

* Resolución de Vaciados: 4 NPCs que fueron poseídos. Uma los libera por Resonancia.

* Señal 9: en el escalón del Mirador. Solo una flecha dibujada. Apunta arriba.

* El Mirador invadido por El Revés. La batalla más larga y difícil.

* Jefe del Acto IV: El Fragmento del Miedo al Decir. Ver sección 6 para detalle.

* El Umbral se estabiliza. El barrio respira.

* Transición al Acto V.

## **ACTO V (20–30 min)**

* El barrio se calma. Escenas cortas de NPCs recuperándose.

* Una puede hacer un recorrido opcional por todas las zonas (NPCs con diálogos de cierre).

* Pablo sube al Mirador.

* La secuencia final: el papel, la lectura, las tres opciones de respuesta.

* Cierre según elección.

* Pantalla final: el cuaderno.

# **13\. DESARROLLO DE PERSONAJES**

## **13.1 UMA TORRES — Arco Completo**

| Edad | 18 años |
| :---- | :---- |
| **Apariencia** | Tez muy clara (se quema fácil, mucho protector solar). Pelo lacio oscuro con mechones lacios que el calor alborota. Ojos claros. Ropa cómoda: musculosa, pantalón cargo, zapatillas desgastadas. Mochila gastada. El olor de la ropa le importa un montón. |
| **Personalidad** | Empática de forma activa — no solo siente lo que otros sienten sino que hace algo al respecto. Observadora: nota detalles que otros pasan. Dice lo que piensa con filtro mínimo: 'seis siete', 'juro que', 'ngl', 'no cap', 'la putísima madre' cuando se golpea un dedo. Irreverente pero cariñosa. |
| **Lo que la define** | Se para a hablar con cualquiera que se vea solo. No porque sea su deber — sino porque genuinamente quiere saber. Eso la hizo conocida sin que ella lo haya buscado. |
| **Lo que evita** | El sol directo. Las situaciones donde tiene que explicar qué va a hacer con su vida. Que le digan qué sentir. |
| **Arco narrativo** | Uma empieza el juego sin brújula propia — se mueve por el pedido del padre. A medida que conecta con el barrio y luego navega El Revés, descubre que su empatía no es solo un rasgo de personalidad: es su fuerza real. El Vacío intenta usar sus dudas como arma. Pero las conexiones que construyó son más fuertes. Al final, Uma no es 'curada' de nada — es reconocida. Por el barrio. Por sus aliados. Y por una persona específica. |

## **13.2 BAUTISTA TORRES — El Hermano de 5 Años**

| Edad | 5 años. Pronto 6\. Él lo menciona constantemente. |
| :---- | :---- |
| **Apariencia** | Pelo revuelto, remera con algún animal que le gusta esta semana, descalzo adentro de casa. Siempre tiene algo en la mano: bloques, lápices, un snack. |
| **Historia** | Bautista creció mirando a Uma con adoración sin filtro. Para él, Uma es simplemente Uma: la que sabe cosas raras, la que siempre para cuando él le habla, la que a veces lo lleva a la plaza y le deja elegir el helado primero. No entiende nada de lo que pasa en el juego y eso lo hace extraordinariamente útil narrativamente. |
| **Función narrativa** | Bautista dice verdades sin saber que son verdades. Sus observaciones son inocentes pero afiladas. Es el ancla emocional de Uma cuando todo lo demás se complica. Su presencia en el juego — breve pero consistente — recuerda que hay una vida normal esperando. |
| **Mecánica especial** | La burbuja de Bautista al llegar a Ánimo 0 siempre sube el Ánimo a 15 automáticamente. Sus frases son siempre diferentes y siempre raras. Uma las responde con cariño exasperado. |

## **13.3 DARÍO TORRES — El Padre**

| Edad | 37 años |
| :---- | :---- |
| **Apariencia** | Alto, complexión sólida de quien estuvo activo toda su vida. Cara seria de trabajo que se parte en expresión de papá cuando está con sus hijos. |
| **Historia** | Darío lleva 14 años en la policía. Conoce Barrio Sauco como la palma de su mano — no solo los nombres de las calles sino quiénes viven dónde, qué pasó en qué esquina, qué familias tienen historia. Es precisamente eso lo que lo hace saber que los objetos misteriosos son de alguien que también conoce muy bien el barrio. |
| **Subtexto** | Darío sabe quién es Pablo Santellan. Lo conoció en el contexto del barrio, sabe lo que Pablo siente por Uma, y discretamente la mandó a investigar porque quería que Uma lo descubriera sola. Nunca lo dice directamente. Cuando Uma lo confronta al final del Acto III, él sonríe y dice: 'Eso que encontraste vos, no te lo puede dar nadie más.' |
| **Arco narrativo** | Darío es la autoridad que confía en Uma desde el principio — no porque deba, sino porque la conoce. Post-Umbral, está fuera de su elemento por primera vez en su carrera. Necesitar a Uma activamente (en vez de ayudarla) es un hito emocional para ambos. |

## **13.4 NATALIA — La Madre**

| Edad | 38 años |
| :---- | :---- |
| **Rol** | Diseñadora desde casa (ropa, ilustración, según el juego de rol de cada día). Su cuarto tiene una mesa de trabajo permanente llena de telas y bocetos. |
| **Función narrativa** | Natalia es el ancla emocional de la casa. No pregunta demasiado, no juzga, pero siempre tiene algo listo: mate, comida, un 'cómo estás' que espera respuesta real. Sus diálogos son breves pero pesados en tono positivo. |
| **Post-Umbral** | Natalia permanece en casa con Bautista. Uma la visita brevemente en cada acto. En el Acto IV, Natalia le dice: 'Siempre supe que el barrio te iba a necesitar. No lo dije antes para no asustarte.' |

## **13.5 NPCs Principales — Arcos Resumidos**

| NPC | HISTORIA PERSONAL | ARCO EN EL JUEGO |
| :---- | :---- | :---- |
| GRACIELA (70) Tienda de objetos viejos | Viuda hace 3 años. El primer aniversario de la muerte de su marido lo pasó sola porque sus hijos están en otras ciudades. Fue ese día que encontró el portarretrato con el cordón rosa. | Arco de 3 conversaciones: del silencio educado a la memoria viva. Post-Umbral: su Memoria Corporal activa le permite ver el pasado de objetos. Ayuda a Uma en El Revés como 'lector de objetos'. Resonancia: Presencia. |
| DON PEPE (62) Jubilado, vive solo | Ex músico amateur. Tocó en una banda de tango hace 30 años. Cuando la banda se disolvió, dejó de tocar. El cassette que recibió suena como su propia música, pero mejor. | Arco de la misión de Fernet \+ 2 conversaciones. Post-Umbral: su Escucha Profunda lo aterra pero Uma lo ayuda a aceptarlo. Al final puede escuchar la conversación que su banda tuvo el día que se disolvió y entender que nadie quería irse realmente. |
| CHINO (28) Kiosquero | Carlos, pero todo el mundo lo llama Chino desde chico. Vende de todo, sabe de todo, opina de todo. Soltero, vive con su mamá en el departamento encima del kiosco. | Hub de información del mundo. Vende consumibles. Post-Umbral: el kiosco es un refugio declarado (zona neutral donde los Ecos no entran). Sus chistes malos se vuelven el alivio cómico del Acto IV. |
| LEO y VALE (17) Adolescentes de la plaza | Novios desde hace 8 meses. Leo quiere estudiar arte. Vale todavía no sabe. Pasan los días en el banco de la plaza porque en sus casas no hay lugar tranquilo. | Son la pista involuntaria sobre Pablo. Post-Umbral: Leo desarrolla la habilidad de dibujar El Revés con precisión fotográfica aunque nunca fue. Sus dibujos son un mapa alternativo del juego. |
| MARTA (45) Maestra | Su alumno favorito se cambió de escuela hace un mes. Marta sigue viniendo a la plaza a las 6 de la tarde porque era cuando caminaban juntos hacia sus casas. | Post-Umbral: Marta es la primera que Uma libera de una posesión del Vacío (Vaciada). Al liberarla, Marta dice la cosa más importante sobre Pablo que Uma escucha antes del final. |
| DOÑA ELSA (58) Puesto en el Mercado | Vende especias, hierbas, algunas cosas raras. Lleva 25 años en el mismo puesto. Conoció a Doña Carmen, la abuela de Pablo, cuando ambas eran jóvenes. | Tiene información clave sobre Doña Carmen y el origen de El Revés. Su radio, cuando se sintoniza bien, toca Agujetas de Color de Rosa. Post-Umbral: su puesto en el Mercado se convierte en punto de comercio de ítems del Revés. |

# **14\. PABLO DANIEL SANTELLAN — PERFIL COMPLETO**

| Nombre completo | Pablo Daniel Santellan |
| :---- | :---- |
| **Edad** | 24 años |
| **Apariencia** | Altura media, complexión normal. Pelo oscuro corto pero algo desaliñado — del tipo que se hace solo. Ojos oscuros con tendencia a mirar dos segundos más de lo normal en los lugares. Siempre tiene algo en la mano o en el bolsillo: un papel doblado a medias, un lapicero sin tapa, una piedra pequeña que encontró en la calle y que le pareció de forma interesante. Camina rápido cuando está nervioso y muy despacio cuando está cómodo. No hay velocidad media. |
| **Ocupación** | Estudiante de arquitectura (5.° año, casi terminado). Trabaja part-time en un estudio de diseño haciendo renders. Vive solo en un departamento de un ambiente a cinco cuadras del barrio de Uma — lo consiguió hace un año con sus primeros ahorros. |
| **Personalidad** | Observador hasta el punto de que los demás lo creen callado. Habla cuando tiene algo que decir. Lo que dice tiende a ser preciso. Se ríe fácil si algo le resulta genuinamente gracioso pero nunca finge la risa. Tiene una relación intensa con los lugares — puede entrar a un edificio y saber en 30 segundos qué sintió la gente que lo construyó. |

## **14.1 Historia Personal**

Pablo creció en Barrio Sauco. Su madre se fue cuando él tenía 9 años — no de forma dramática: simplemente se fue a vivir a otra ciudad con su nueva pareja y las visitas se fueron espaciando hasta que se volvieron tarjetas en fechas importantes. Su padre, Hernán, trabajó siempre como mecánico y lo crio bien pero con la clase de silencio que los hombres de esa generación usaban como lenguaje. Pablo aprendió a leer el mundo a través de sus objetos y sus espacios porque las personas de su vida usaban poco las palabras.

Su abuela, Doña Carmen Santellan, era la excepción. Carmen era de los que hablan exactamente lo que necesitás escuchar — sin adornos ni rodeos, pero con una precisión que hacía que la cosa más directa sonara como un regalo. Murió cuando Pablo tenía 10 años. Era una Tejedora: alguien con la capacidad de sentir y tejer los vínculos emocionales entre personas y lugares. Pablo no lo sabía en esos términos. Lo que sabía es que la abuela Carmen siempre supo cosas.

El poder de Pablo — su Visión de Resonancia — se activó de forma involuntaria cuando tenía 16 años, en el momento más conflictivo entre su madre y su padre: pudo ver literalmente los hilos que los conectaban cortándose. Fue aterrador. Tardó dos años en entender que no era una alucinación sino una capacidad. Tardó dos más en poder controlarlo lo suficiente para no verse paralizado en lugares con mucha carga emocional.

En ese proceso descubrió algo sobre El Revés — no su nombre ni su naturaleza exacta, pero sí su presencia: cuando su poder estaba activo en ciertos lugares del barrio, podía ver el otro lado como un sueño superpuesto. Creyó durante mucho tiempo que era algo propio, raro, suyo. No supo que era un fenómeno real compartido hasta el Umbral.

## **14.2 Su Relación con Uma — Cómo Empezó**

Pablo conoce a Uma de verla en el barrio desde hace años — no de forma activa, sino de esa manera en que los barrios chicos crean una familiaridad de fondo. La empezó a notar en serio hace ocho meses, cuando la vio en Plaza Mayor parar frente a un Eco Menor (que en ese momento solo él podía ver) y hacer exactamente lo que el Eco necesitaba sin saber que el Eco existía: se detuvo, lo miró al espacio donde estaba, y no se movió durante 30 segundos. El Eco se dispersó.

Uma no sabía lo que había hecho. Pablo sí.

A partir de ahí la observó con la atención cuidadosa que pone en los lugares que le importan. Fue acumulando detalles: cómo dobla los papeles cuando está nerviosa (siempre para el mismo lado), que se pone el protector solar incluso cuando está nublado porque 'nunca se sabe', que dice 'seis siete' cuando algo la sorprende de verdad y lo dice en serio, que siempre para a hablar con alguien que está solo.

Cuando quiso decirle lo que sentía, no sabía cómo. Las palabras directas le parecían demasiado pequeñas. Y entonces se le ocurrió que Uma era la persona que seguía señales — que notaba las cosas que los demás ignoraban. Así que decidió dejar señales. Nueve. Una por cada cosa que sabía de ella que la hacía ser Uma.

## **14.3 Lo que Pablo Sabe que Uma No Sabe**

* Que es el autor de todas las señales. Uma lo descubre gradualmente.

* Que su poder de Visión de Resonancia fue lo que le permitió colocar cada señal en el lugar exacto donde Uma la iba a encontrar.

* Que las señales, al ser colocadas con su poder activo, crearon los Anclajes que protegen a Uma en El Revés.

* Que Doña Carmen lo 'preparó' para esto sin que él lo supiera: las historias que le contaba de niño eran instrucciones disfrazadas.

* Que la última señal — la novena, la del Mirador — la escribió de un golpe una tarde y después tardó tres semanas en animarse a dejarla.

## **14.4 Pablo en El Revés — Su Rol**

Pablo navegó El Revés desde mucho antes del Umbral, sin entender completamente lo que era. Lo que sí entendía es que era 'el lugar donde las cosas que no se dicen tienen forma'. Al abrirse el Umbral, su capacidad de navegar El Revés se amplificó: puede cruzar sin grieta, puede ver los Resonantes como criaturas en vez de sombras difusas, puede detectar dónde El Vacío presiona con más fuerza.

Durante los Actos II y III, Pablo opera en paralelo a Uma en El Revés: resolviendo algunos obstáculos antes de que Uma llegue, dejando el camino parcialmente despejado. Uma ve las consecuencias de su paso (Ecos que ya fueron resueltos, Guardianes que están calmados) antes de verlo a él.

En el Acto III, después del jefe, se ven por primera vez cara a cara en El Revés. El encuentro es breve y exactamente tan extraño y contenido como dos personas que se conocen de fondo pero nunca hablaron directamente.

## **14.5 El Papel Final — La Declaración**

Pablo escribió el papel final a mano. Tiene tachones porque empezó varias veces. La versión final dice lo que siempre dijo la primera vez que lo intentó, pero sin los rodeos.

La declaración base (presente incluso con el mínimo de señales encontradas):

*"Uma: Llevo meses siguiéndote sin que lo supieras. No de una forma rara — de la forma en que se sigue a alguien que hace cosas que te importan. Vi cómo parás frente a la gente sola. Cómo anotás cosas en el cuaderno. Cómo te peleás con el sol. Vi cómo lo que vos hacés sin pensarlo cambia el estado de los que te rodean. No sé si te lo dijo alguien antes. Me parece que no. Yo sí te lo digo: sos exactamente lo que sos, y eso es lo mejor que vi en mucho tiempo."*

Si Uma encontró 6+ señales, se agregan los fragmentos específicos (protector solar, el 'seis siete', cómo dobla los papeles). Si encontró las 9, la última frase es:

*"'Hoy te pregunto directo: ¿querés que sigamos siendo esto, pero con nombre?'"*

# **15\. MUNDO Y ZONAS — DESCRIPCIÓN DETALLADA**

## **ZONA 0 — Casa Torres**

| Descripción | Departamento de planta baja con patio trasero. 4 ambientes. Techos altos, baldosas antiguas, ventiladores de techo que hacen ruido. La casa huele a ropa lavada y mate. |
| :---- | :---- |
| **Cuarto de Uma** | Cama, estante con 18 discos (todos inspeccionables), ventana con persiana, escritorio con cuaderno abierto, foto de sus padres en la mesita. Después del Umbral, la ventana muestra El Revés superpuesto al patio. |
| **Living** | Bautista y sus construcciones. Televisión que nadie mira pero nadie apaga. Una planta grande que se cae regularmente y nadie sabe cómo sobrevive. |
| **Cocina** | Natalia. El mate. Una radio pequeña que a veces toca canciones de los 80s. La nota de Darío imantada en la heladera. |
| **Patio** | Macetas de Natalia. Una silla plástica. Ropa colgada. Post-Umbral: las plantas del patio florecen de noche con colores del Revés. Una pequeña grieta en la pared del fondo. |
| **Función** | Punto de regreso siempre disponible. Anclaje 0\. Guardar manual. Recuperación de Ánimo (+5 por minuto en casa). |

## **ZONA 1 — Barrio Inmediato / Calle Principal**

| Descripción | La cuadra de Uma y las tres siguientes. Árboles grandes con raíces que rompen las veredas. Edificios de 3-4 pisos mezclados con casas. El kiosco de Chino en la esquina estratégica. |
| :---- | :---- |
| **Puntos de interés** | Kiosco de Chino (hub de info y consumibles), Callejón del primer Eco, árbol con raíces expuestas (objeto de lore), buzón que no funciona, Señal 3 en la fachada del edificio de Marta. |
| **Post-Umbral** | Las raíces del árbol grande emiten un leve brillo violeta — una de ellas es en realidad la raíz de El Telar. Hay un Eco Mayor caminando por el callejón (antes eran solo Menores). El Kiosco de Chino tiene una barrera protectora natural (zona neutral). |

## **ZONA 2 — Plaza Mayor**

| Descripción | Hub central del barrio. Árbol viejo en el centro (caído post-Umbral), fuente seca de mármol, galería cubierta lateral, varios bancos. La Plaza Mayor es donde ocurren los eventos centrales del juego. |
| :---- | :---- |
| **Pre-Umbral** | Árbol vivo. NPCs en sus lugares. La fuente seca tiene el disco de vinilo en el borde (Señal 2). Valentina leyendo. Ernesto mirando el espacio de las palomas. |
| **El Umbral** | El árbol colapsa. Grieta principal se abre. Secuencia cinemática. |
| **Post-Umbral** | El árbol caído es ahora un Anclaje Natural (Anclaje 2\) cubierto de flores del Revés. La grieta en el centro permite acceso directo a El Revés. Los NPCs se reubicaron — algunos están en la galería, algunos no vuelven hasta después del Acto III. |
| **Secretos** | En la base del árbol caído hay una cavidad. Dentro: un papel viejo con letra de Doña Carmen. Una pista de hace 30 años sobre lo que iba a pasar. |

## **ZONA 3 — Mercado Viejo**

| Descripción | Mercado de barrio con historia. Puestos cubiertos con lonas multicolores, olor a pasto y especias, suelo de baldosas rojas. Lleva 40 años en el mismo lugar. Varios puestos llevan 20 de esos 40 años con la misma dueña. |
| :---- | :---- |
| **NPCs** | Doña Elsa (especias y cosas raras), el señor Ariel (frutas, muy callado), Lucía (ropa usada, 16 años, trabaja con su madre). |
| **Misiones** | MS-02 (foto de Graciela en el sótano), MS-03 (la radio de Doña Elsa), MS-05 (llave del sótano con Eco). |
| **El Sótano** | Acceso bloqueado por un Eco Mayor inicial. Al resolver: espacio grande, lleno de cajas de objetos olvidados. El diario de Doña Carmen está acá. Señal 6 (opcional) en el fondo del sótano. |
| **Post-Umbral** | Doña Elsa empieza a vender ítems del Revés sin entender exactamente qué son. Lucía tiene un don natural para calmar a los Ecos que descubre sola — minor NPC que se vuelve importante. |

## **ZONA 4 — Parque Ribereño**

| Descripción | Parque largo junto a un canal pequeño. Árboles de sauce que dan sombra todo el día. Banco junto al agua. Patos que están ahí sin pedirle permiso a nadie. Luz filtrada todo el tiempo — zona de descanso mecánico y visual. |
| :---- | :---- |
| **Función** | Uma pierde 0 Ánimo por sol en esta zona (sombra natural constante). El banco del río es un Anclaje (Acto IV). Zona de la Sombra Errante grande (evento del pasado del barrio: el incendio del antiguo mercado, hace 40 años). |
| **Post-Umbral** | El canal tiene ahora reflejos del Revés que no corresponden al cielo real. Los patos no se van — son los únicos animales aparentemente inmunes a El Umbral. Uma lo nota. Monólogo: 'Los patos tienen resuelto algo que nosotros no.' |
| **Primera grieta** | La primera grieta navegable para El Revés está en el sauce más viejo del parque, al fondo. El árbol tiene la corteza de dos colores: natural y violeta. |

## **ZONA 5 — La Zona Alta**

| Descripción | La parte más elevada del barrio. Escaleras, callecitas angostas, edificios de los años 40 que tienen la clase de resistencia discreta que da el tiempo. La luz llega más inclinada acá. La temperatura es 2-3 grados más fresca que abajo. |
| :---- | :---- |
| **NPCs** | Don Mario (jubilado en el banco de la vereda), Rosa (florería, tiene un Eco Menor atrapado entre sus plantas que no puede resolver sola). |
| **Secretos** | En la pared de un edificio, con letra de ciudad vieja, está el nombre 'CARMEN SANTELLAN' y una fecha de hace 30 años. Es la firma de Doña Carmen en uno de sus trabajos de Tejido. |
| **Post-Umbral** | La Zona Alta es la más afectada por El Umbral: algunas partes de las calles son directamente de El Revés sin grieta necesaria. Se puede caminar sobre luz violeta que es el suelo de la dimensión espejo. Los edificios muestran sus versiones del Revés superpuestas casi completamente. |

## **ZONA 6 — El Revés (Dimensión Paralela)**

| Descripción | El Revés es el barrio visto desde adentro de las emociones que lo construyeron. El suelo es translúcido y brilla desde abajo. Los edificios tienen sus fachadas normales pero sus interiores contienen versiones del pasado. El cielo es gradiente de violeta a negro con constelaciones en movimiento. |
| :---- | :---- |
| **Sub-zonas** | El Revés de la Plaza Mayor (más grande y abierto), El Revés del Mercado (laberíntico), El Revés del Parque (más fluido, agua arriba), El Revés de la Zona Alta (más angosto, tiempo más inestable). |
| **El Telar de Doña Carmen** | Estructura central del Revés: una cúpula de hilos de luz que conecta todos los Anclajes. Es el núcleo del sistema de resurrección. Aquí está el diario completo de Carmen y la Memoria de Agua (Guardiana). |
| **Hazards** | Zonas de tiempo inestable (Uma puede ver versiones del pasado superpuestas y confundirse), áreas del Fragmento del Olvido que borran detalles visuales, territorios de los Guardianes. |
| **Temperatura emocional** | El Revés amplifica las emociones: si Uma llega con Ánimo bajo, el Revés es visualmente más oscuro y los enemigos más agresivos. Si llega con Ánimo alto, el Revés es más luminoso y algunos Guardianes son más permisivos. |

## **ZONA 7 — El Mirador**

| Descripción | Acceso por escalera entre dos edificios de la Zona Alta. Plataforma de cemento con baranda de hierro que mira al oeste. Desde acá se ve todo Barrio Sauco. En día limpio, se ve hasta el centro de la ciudad. |
| :---- | :---- |
| **Pre-Umbral** | Tranquilo. Señal 9 en el escalón. Pablo arriba. |
| **Post-Umbral (Acto IV)** | El Mirador es la arena del jefe final. El suelo y las paredes son del Revés. El barrio de abajo visible desde la baranda está parcialmente invadido por el violeta del Umbral. |
| **Post-batalla** | El Mirador se normaliza pero conserva algo del Revés: la baranda tiene ahora un hilo de luz violeta enroscado que hace que el lugar se vea diferente pero más hermoso. El atardecer desde acá es el más bello del juego. |
| **El papel** | Está en el bolsillo de Pablo. Siempre estuvo ahí. |

# **16\. DISEÑO DE MAPAS**

## **16.1 Principios**

* Tiles 32×32 px. Resolución base para móvil: 360×640 (portrait). El mapa completo es aproximadamente 120×80 tiles en el mundo normal.

* Top-down en exteriores (ángulo 3/4 clásico de RPG). Lateral 2.5D en interiores y El Revés.

* Cada pantalla de juego cabe en la pantalla del dispositivo sin scroll horizontal. El scroll es solo vertical o diagonal según zona.

* Regla de diseño: toda zona tiene al menos 3 elementos interactivos no-mecánicos (objetos de lore, graffitis, detalles de fondo) por pantalla.

## **16.2 Conectividad del Mapa**

| Casa Torres | ↔ Calle Principal (puerta de entrada / portón de patio) |
| :---- | :---- |
| **Calle Principal** | ↔ Casa Torres / ↔ Plaza Mayor (norte) / → Mercado Viejo (callejón) / → Zona Alta (calle empinada) |
| **Plaza Mayor** | ↔ Calle Principal / ↔ Parque Ribereño (pasaje peatonal) / Grieta del Revés (centro, post-Umbral) |
| **Mercado Viejo** | ← Calle Principal / ↔ Sótano (post-misión) / Grieta del Revés (trastienda, post-Umbral) |
| **Parque Ribereño** | ← Plaza Mayor / → Zona Alta (sendero) / Grieta del Revés (sauce viejo, Acto II) |
| **Zona Alta** | ← Calle Principal / ← Parque Ribereño / → Mirador (escalera oculta) / Zona directa del Revés (post-Umbral) |
| **El Revés** | Acceso desde grietas. Sub-zonas conectadas entre sí por Pasajes de Resonancia (requieren energía). |
| **El Mirador** | ← Zona Alta / fin de juego |

## **16.3 Eventos de Mapa Post-Umbral**

El mapa cambia visualmente después del Umbral de las siguientes formas:

* Las grietas de luz violeta aparecen en el suelo de todas las zonas exteriores — decorativas, no dañinas

* Algunos edificios muestran su versión del Revés superpuesta (efecto de parallax visual)

* El árbol de Plaza Mayor está caído y cubierto de flores del Revés

* El Mirador es accesible desde el Acto IV (antes hay una barrera visual — una nube de energía oscura que bloquea la escalera)

* En El Revés, las sub-zonas se conectan según el progreso narrativo — no todos los pasillos están abiertos al inicio

# **17\. MISIONES PRINCIPALES Y SECUNDARIAS — COMPLETAS**

## **MISIONES PRINCIPALES**

| ID | MISIÓN | DETALLE |  |
| :---- | :---- | :---- | :---- |
| MP-01 Prólogo | El Encargo | Darío le pide investigar los 3 objetos. Objetivos: hablar con Graciela, Don Pepe, Marta. Desbloquea: cuaderno activo, mapa del barrio, Anclaje 1\. |  |
| MP-02 Acto I | Las Señales | Recoger señales 1, 2 y 3 mientras sigue el rastro de los vecinos. El jugador aprende el sistema de Resonancia y recolección. Desbloquea: Plaza Mayor completa, Parque Ribereño. |  |
| MP-03 Acto I | El Árbol | No es una misión que Uma acepta — simplemente ocurre cuando llega a Plaza Mayor. La cinemática del Umbral, la visión de clase, el despertar del poder. Desbloquea: todo el sistema post-Umbral. |  |
| MP-04 Acto II | El Barrio Roto | Navegar el nuevo barrio. Encontrar señal 4\. Primera incursión a El Revés. Resolver 3 Ecos post-Umbral. Desbloquea: Mercado Viejo completo, grietas de El Revés. |  |
| MP-05 Acto II | El Sótano | Ingresar al sótano del Mercado. Enfrentar el Fragmento del Abandono. Encontrar el diario de Doña Carmen. Desbloquea: comprensión de los Anclajes, Resonancia 4\. |  |
| MP-06 Acto III | El Revés | Entrada completa a El Revés. Señal 7\. El Telar de Doña Carmen. Enfrentar el Fragmento del Olvido. Primer encuentro cara a cara con Pablo. Desbloquea: Zona Alta completa, habilidades de nivel 4\. |  |
| MP-07 Acto IV | Los Vaciados | Liberar a los 4 NPCs Vaciados (Marta, Ariel, Hernán —el padre de Pablo—, Leo). Solo por Resonancia. Desbloquea: narrativa de Pablo, apertura del camino al Mirador. |  |
| MP-08 Acto IV | El Umbral Final | Señal 9 en el Mirador. El Fragmento del Miedo al Decir. Estabilizar el Umbral usando la última señal como escudo. Desbloquea: Acto V, regreso de Pablo. |  |
| MP-09 Acto V | La Señal Más Clara | Pablo sube al Mirador. El papel. La respuesta. El cierre. |  |

## **MISIONES SECUNDARIAS**

| ID | MISIÓN | DETALLE Y RECOMPENSA |
| :---- | :---- | :---- |
| MS-01 | Fernet el Gato | Fernet se escondió en el Mercado durante el Umbral. Uma lo encuentra (Eco menor lo asustó). Mini-puzzle de Resonancia con el gato. RECOMPENSA: Cassette (ítem de lore) \+ Don Pepe como aliado narrativo \+ Anclaje 1\. |
| MS-02 | La Foto de Graciela | La foto del marido de Graciela está en el sótano del Mercado (encadenada con MS-05). RECOMPENSA: Resonancia 1 (Presencia) \+ historia completa de Graciela \+ equipamiento Cordones Rosa. |
| MS-03 | La Radio de Doña Elsa | La radio de Elsa no sintoniza bien. Uma la ajusta. Cuando sintoniza: suena una canción que hace llorar a Elsa de felicidad. RECOMPENSA: Señal extra oculta \+ lore de Doña Carmen \+ acceso a venta de ítems del Revés. |
| MS-04 | El Dibujo de Leo | Leo quiere hacer un retrato de Vale. No sabe qué la define. Uma lo ayuda entendiendo a Vale mejor. RECOMPENSA: Relación con Leo/Vale al máximo \+ Leo empieza a dibujar mapas del Revés \+ pista directa sobre Pablo. |
| MS-05 | La Llave del Sótano | La llave está en el Mercado, con un Eco Mayor que la 'guarda' sin querer. Uma debe resolverlo. RECOMPENSA: Acceso al sótano \+ posibilita MS-02. |
| MS-06 | La Tarde con Bautista | Opcional (Acto II): Uma lleva a Bautista a la Plaza Mayor. Secuencia de 10 minutos. Bautista hace amistad con 3 NPCs en el tiempo que Uma tardó horas. RECOMPENSA: \+30 Ánimo, una señal extra de Pablo que aparece en el banco mientras Uma mira a Bautista. |
| MS-07 | Contemplación del Río | Opcional (Acto II): Uma se sienta en el banco del río 3 minutos reales sin input. El Eco grande del Parque se disuelve solo. RECOMPENSA: Anclaje 4 activado \+ Fragmento de Memoria Mayor del incendio del mercado viejo. |
| MS-08 | La Historia de Don Mario | Don Mario tiene algo que decirle a alguien antes de que sea demasiado tarde. Uma lo ayuda a descubrir quién es esa persona (árbol de diálogo \+ investigación). RECOMPENSA: Ítem de equipamiento Cinta del Barrio \+ narrativa de lore del barrio de hace 30 años. |
| MS-09 | Las Memorias de Doña Carmen | En El Revés, Uma puede recoger 5 páginas del diario de Doña Carmen repartidas por el Revés. Si las reúne todas: puede hablar con la Memoria de Agua (la guardiana que custodia el pasado de Carmen) y recibir el ítem Hilo de Doña Carmen. RECOMPENSA: Mejor equipamiento del juego \+ narrativa completa del pasado de Pablo. |
| MS-10 | El Padre de Pablo | Hernán Santellan (padre de Pablo) es uno de los Vaciados del Acto IV. Liberarlo requiere más pasos que los demás: Uma necesita encontrar un objeto específico de Pablo en El Revés para usar en la Resonancia. RECOMPENSA: Hernán le da información crucial sobre Pablo \+ el Acto V tiene un diálogo extra donde Hernán le agradece a Uma. |

# **18\. TODOS LOS DIÁLOGOS IMPORTANTES**

## **18.1 — PRÓLOGO: Darío y Uma**

**Darío:**

*(sentado en la mesa del comedor, carpeta abierta, cara de trabajo)*

Tengo un favor.

**Uma:**

¿Cuánto de qué?

**Darío:**

Tiempo. Nada más.

*(le explica de los tres objetos. Pausa.)*

No es urgente. Pero es raro. Y vos sos mejor que yo para hablar con la gente.

**Uma:**

*(mira el techo un segundo)*

Seis siete. Ok.

*(pausa)*

¿Hay plata para el kiosco o solo el favor?

**Darío:**

*(levantándose, saca billetes del bolsillo sin contar)*

Para el kiosco y para lo que haga falta. (pausa) Uma.

*(Uma lo mira.)*

Tenés ojo para las cosas que los demás no ven. Ya lo sabés. Usalo.

**Uma:**

*(monólogo interno)*

'Ojo para las cosas que los demás no ven.' Papá dice estas cosas como si fueran normales.

Supongo que para él sí lo son.

## **18.2 — ACTO I: Uma y Graciela (Primera Conversación)**

**Graciela:**

*(levanta la vista del mostrador cuando Uma entra)*

Uma. Hacía tiempo. ¿Cómo está tu mamá?

**Uma:**

Bien, cosiendo algo, como siempre. (pausa) Doña Graciela, mi papá me mandó a preguntar por unos objetos raros que encontraron algunos vecinos.

**Graciela:**

*(sin sorpresa)*

El portarretrato.

*(lo saca del mostrador. Es un marco de madera vacío con un cordón rosa enroscado adentro.)*

Apareció en mi patio hace diez días. A la mañana. No lo puse ahí yo.

**Uma:**

¿Sabe quién lo dejó?

**Graciela:**

*(pausa. Lo mira.)*

No. Pero sé cuándo fue. (pausa) Ese día fue el primer aniversario de la muerte de Pedro.

*(Uma espera. Graciela continúa.)*

Alguien sabía eso y dejó algo igual. No amenazante. Solo... (busca la palabra) ...presente.

**Uma:**

*(monólogo interno)*

El primer aniversario de la muerte de alguien. Y alguien dejó algo justo ese día.

Eso no es coincidencia.

## **18.3 — ACTO I: Uma y Graciela (Nivel 2 — Los Cordones Rosa)**

**Graciela:**

*(después de la misión de la foto)*

*(saca una caja de madera de debajo del mostrador)*

Acá hay algo que tenés que ver.

**Uma:**

*(se acerca)*

*(ve, entre otras cosas, un par de cordones rosas muy gastados)*

**Graciela:**

Tenía 17 años. Usaba siempre esos cordones. Color rosa chillón.

*(pausa)*

Pedro no sabía cómo hablarme. Era de los que callan porque no encuentran las palabras justas.

Un día me dejó un cassette en el buzón. Sin nombre. Sin nada. Adentro había una sola canción. Sobre una chica con cordones rosas que él veía todos los días y que no sabía cómo decirle lo que sentía.

**Uma:**

¿Y cómo supiste que era él?

**Graciela:**

Porque era demasiado específico para ser de alguien que no me conocía bien. (pausa)

Los que realmente te ven dejan cosas específicas. No genéricas.

*(mira a Uma directo)*

¿Entendés lo que te digo?

**Uma:**

*(monólogo interno)*

Específico. Como 'siempre te fijás en lo que los demás no ven.'

Como el origami en el patio exacto de Graciela el día exacto del aniversario.

Seis siete.

## **18.4 — ACTO I: Uma y Don Pepe (El Cassette)**

**Don Pepe:**

*(mientras toma mate en el escalón, después de que Uma le devuelve a Fernet)*

¿Sabés lo que más extraño de ser joven?

**Uma:**

La energía, digo yo.

**Don Pepe:**

No. La costumbre de guardar cosas. Cartas, cassettes, fotos. Ahora todo se borra solo.

*(pausa)*

Alguien me dejó esto hace diez días. (le muestra el cassette) No sé quién. No tiene nombre.

**Uma:**

¿Lo escuchó?

**Don Pepe:**

Sí. Suena a música que yo haría. Pero mejor. (pausa) Como si alguien escuchó lo que yo quería hacer y lo hizo.

**Uma:**

¿Asusta eso?

**Don Pepe:**

*(piensa un segundo)*

No. Me da envidia. (ríe un poco) Pero del bueno.

*(pausa. Mira al espacio.)*

Alguien todavía deja cassettes. Eso me parece bien.

## **18.5 — ACTO I: Uma y Bautista (Antes de Salir)**

**Bautista:**

*(sin levantar la vista, construyendo)*

¿Adónde vas?

**Uma:**

A investigar una cosa para papá.

**Bautista:**

*(pausa de construcción)*

¿Vas a encontrar algo tuyo?

**Uma:**

¿Cómo?

**Bautista:**

A veces uno sale y encuentra algo suyo que no sabía que se había ido. (sigue construyendo)

Igual traeme un alfajor si pasás por el kiosco.

**Uma:**

*(monólogo interno)*

Tiene cinco años.

Cinco y medio.

'Cinco y seis meses, Uma, que es casi seis.'

Ok, Bau. Ok.

## **18.6 — POST-UMBRAL: Darío y Uma (El Teléfono)**

**Darío:**

*(por teléfono, voz calmada pero tensa)*

¿Estás bien?

**Uma:**

*(monólogo: 'Puedo hablar, así que sí.')*

Sí. ¿Qué pasó exactamente?

**Darío:**

No lo sé todavía. Algo en la plaza. Hay personas en shock, una grieta en el suelo, el cielo no está bien.

*(pausa)*

Uma. Tenés ese... lo tuyo. ¿Lo sentís?

**Uma:**

*(mira su mano. El poder de la clase que eligió está activo — leve brillo.)*

*(al teléfono) Sí.*

**Darío:**

Entonces seguí. Yo lo veo desde acá pero no puedo ir adonde vos podés ir.

*(pausa larga)*

Cuidate. Y Uma — el que deja esas señales. No es el problema. Al contrario.

**Uma:**

*(corta. Mira el teléfono. Después mira el barrio.)*

*(monólogo interno)*

No es el problema. Al contrario.

Ok, papá. Tan discreto como siempre.

## **18.7 — ACTO II: Uma y Leo/Vale (La Pista)**

**Vale:**

*(a Leo, sin notar que Uma está cerca)*

Tu amigo Pablo es medio raro, ¿eh?

**Leo:**

No es raro. Es de los que piensan antes de hablar.

*(pausa)*

Que eso tarde mucho no lo hace raro.

**Vale:**

Ya sé. Pero lleva meses pensando y nunca dice nada.

**Leo:**

*(mira el dibujo que está haciendo, casualmente de la Plaza Mayor)*

Ya va a hablar. Solo necesita el momento.

*(pausa)*

O que alguien llegue al lugar correcto.

(Uma escucha esto de fondo, sin que Leo o Vale la noten. No es un diálogo que Uma 'activa'. Pasa automáticamente si está en el rango.)

**Uma:**

*(monólogo interno)*

El momento correcto.

*(mira la señal 5 que tiene en el cuaderno. La que dice 'me gusta cómo prestás atención.')*

...

Seis. Siete.

## **18.8 — ACTO II: Uma y Marta (Post-Vaciada)**

(Marta acaba de ser liberada de la posesión del Vacío. Está en el suelo, Uma la ayudó a levantarse. Marta llora sin dramatismo, como quien llora de alivio.)

**Marta:**

Gracias.

*(pausa)*

Había algo dentro de mí que usaba mis miedos. Pero también vi... vi otras cosas.

**Uma:**

¿Qué viste?

**Marta:**

Vi que alguien te está cuidando. No de arriba — de costado. Como cuando alguien camina del mismo lado de la vereda sin que vos lo veas.

*(mira a Uma)*

¿Lo sabés?

**Uma:**

*(pausa)*

Empiezo a saber.

## **18.9 — ACTO III: El Telar — Doña Carmen (Memoria en El Revés)**

(Uma toca el diario de Doña Carmen en El Telar. Una proyección de la memoria de Carmen aparece — no es un fantasma, es un eco de memoria, como una grabación de luz. Carmen habla sin mirarla, mirando su propio trabajo.)

**Doña Carmen:**

*(voz suave, acento del barrio de hace décadas)*

Los anclajes no son lugares. Son puntos donde alguien dejó algo de sí mismo.

*(teje un hilo invisible)*

Los mejores anclajes los hacen sin querer. El que deja algo por amor sin saber que lo está dejando — ese teje más fuerte que cualquier Tejedora entrenada.

**Uma:**

*(no puede hablar con ella — es una memoria. Pero escucha.)*

**Doña Carmen:**

*(pausa. Como si la sintiera.)*

Si lo heredó bien, mi nieto va a haber tejido sin saber que tejía.

*(una pausa larga)*

Y la que siguió sus señales va a ser la más protegida del barrio.

*(el eco empieza a difuminarse)*

Cuidenlo los dos. Los dos necesitan que los cuiden.

**Uma:**

*(monólogo interno)*

La abuela de Pablo.

*(mira sus manos, donde las señales de sus Anclajes brillan levemente)*

Seis siete, señora Carmen. Seis siete.

## **18.10 — ACTO III: Primer Encuentro con Pablo (Post-Jefe)**

**Pablo:**

*(de pie a 10 metros, en El Revés, mirando a Uma)*

Uma.

**Uma:**

*(un segundo de silencio)*

Vos sos el que deja las señales.

**Pablo:**

*(asiente. Sin prisa.)*

¿Las seguiste todas?

**Uma:**

Todavía me faltan dos.

*(pausa. Lo mira fijo.)*

¿Cómo sabías dónde dejarlas?

**Pablo:**

*(una pausa antes de responder)*

Sé dónde van a estar las cosas. A veces. Los lugares que tienen algo importante.

*(mira al suelo de El Revés)*

Cada señal la puse donde podía sentir que era el lugar correcto.

**Uma:**

¿Y la última?

**Pablo:**

*(pausa más larga)*

La última la puse donde tengo que estar yo para decirte el resto.

**Uma:**

*(lo mira un segundo. No dice nada. Después:)*

¿Podemos hablar cuando salga de acá?

**Pablo:**

*(una sonrisa pequeña que claramente está tratando de no ser grande)*

Sabés dónde encontrarme.

**Uma:**

*(monólogo interno, mientras Pablo desaparece en El Revés)*

Sé dónde va a estar. Y sé cómo se llama.

*(pausa)*

Pablo.

*(pausa)*

Ok. Ok, barrio. Entendí.

## **18.11 — ACTO IV: Darío y Uma (La Revelación)**

**Uma:**

Papá.

*(llega a casa entre Acto III y IV. Darío está en el sillón.)*

¿Sabés quién deja las señales?

**Darío:**

*(apaga el audio del televisor pero sigue mirándolo)*

*(pausa larga)*

Sé quién es.

**Uma:**

¿Y no me dijiste nada?

**Darío:**

*(pausa)*

Por eso.

**Uma:**

*(lo mira. Silencio.)*

¿Cuánto sabés?

**Darío:**

Lo suficiente para mandarte a recorrer el barrio.

*(pausa)*

Lo que encontraste vos, Uma — no te lo puede dar nadie más.

*(pausa)*

El barrio lo hizo por vos. Él lo hizo por vos. Ahora falta que lo hagas vos.

**Uma:**

*(pausa larga. Después ríe levemente, sin querer.)*

*(monólogo interno: 'Tan sutil como siempre, papá.')*

Ok.

## **18.12 — ACTO V: Pablo y Uma — El Mirador**

(Pablo está en el Mirador, de espaldas a la baranda, mirando hacia las escaleras. Sabe que Uma va a subir. Cuando ella aparece, se gira.)

**Pablo:**

*(voz normal, sin drama en el tono, aunque la postura lo delata)*

Hola.

**Uma:**

*(lo mira. Ve el papel en su mano.)*

Hola.

*(pausa)*

Llevás un rato acá.

**Pablo:**

Un rato. (pausa) ¿Seguiste todas?

**Uma:**

Las nueve.

**Pablo:**

*(asiente. Un segundo.)*

Sé que es raro. No te voy a pedir disculpas por cómo lo hice porque sé que vos ibas a seguir las señales — eso es lo que hacés.

*(pausa)*

Y quería que las siguieras.

**Uma:**

*(sin moverse)*

¿Por qué señales y no... hablarlo?

**Pablo:**

Porque las palabras directas me parecían demasiado pequeñas para lo que quería decirte.

*(pausa)*

Las señales podían ser exactas. Podía dejar acá lo que sé de vos, no lo que se me ocurre cuando estoy nervioso y hablo rápido.

**Uma:**

*(monólogo interno)*

Específico. Como dijo Graciela. El que te ve de verdad deja cosas específicas.

**Pablo:**

*(le da el papel)*

Acá está la última.

(Uma lo lee. La pantalla muestra el papel completo — la declaración según las señales que el jugador encontró. Siempre termina con la misma última frase. Cuando Uma termina de leer, el juego presenta las tres opciones de respuesta.)

### **OPCIÓN A — 'Sí'**

**Uma:**

*(dobla el papel con cuidado, para el mismo lado de siempre)*

*(lo mira)*

Seis siete.

*(pausa)*

Sí.

**Pablo:**

*(pausa. Después ríe — no la sonrisa contenida de antes, una real.)*

¿Seis siete es sí?

**Uma:**

Seis siete es cuando algo me sorprende en serio. Ya lo sabés. Lo escribiste.

**Pablo:**

*(asiente)*

Lo sé.

### **OPCIÓN B — Silencio**

**Uma:**

*(no dice nada. Se sienta en la baranda, a su lado. Mira el barrio.)*

**Pablo:**

*(tampoco dice nada. Se queda.)*

*(El tiempo pasa. La cámara se aleja lentamente.)*

**Uma:**

*(monólogo final — solo en esta variante)*

'El silencio que no incomoda es el más honesto que existe.'

### **OPCIÓN C — 'Mañana'**

**Uma:**

*(pausa larga)*

Necesito tiempo.

*(lo mira)*

No es no. Es que necesito tiempo para entender qué es.

**Pablo:**

*(asiente. Sin presión.)*

Está bien.

*(pausa)*

Sabés dónde encontrarme.

**Uma:**

*(monólogo interno)*

Ya sé dónde encontrarlo.

Eso ya es algo.

# **19\. EVENTOS CLAVE**

## **19.1 — La Historia de los Cordones (La Referencia a Agujetas)**

Graciela le cuenta a Uma la historia del cassette que le dejó Pedro. La canción que suena en ese cassette — audible brevemente si Uma lo examina en el cuaderno después de hablar con Graciela, como música que llega a través de las paredes — es una versión diegética de la melodía de Agujetas de Color de Rosa. No se nombra la canción ni el artista. La conexión es para quienes la conocen.

Tres capas de integración:

* NARRATIVA: Los cordones rosas de Graciela son el objeto-símbolo de la historia. Pedro le dejó una canción sobre una chica con cordones rosas. El objeto persiste como equipamiento.

* DIEGÉTICA: La radio de Doña Elsa, cuando Uma la sintoniza bien (MS-03), toca 4 segundos de la canción antes de que Elsa cambie. Si Uma dice '¡No, esa\!': Elsa dice 'Ay, es viejísima. Mi marido la bailaba.' Sin más.

* MUSICAL: La progresión armónica de Agujetas está citada en el tema musical del Mercado Viejo. Es una referencia para oídos educados.

## **19.2 — El Umbral (La Fractura en Plaza Mayor)**

La secuencia del Umbral es el evento visual más importante del juego. El árbol colapsa en silencio. El suelo de la plaza se parte en líneas de luz violeta. Uma colapsa. La visión de clase. El despertar. Ver sección 3 para detalle completo.

## **19.3 — La Burbuja de Bautista (La Mecánica Emotiva)**

Cuando el Ánimo de Uma llega a 0 en combate, en vez de una pantalla de Game Over aparece la burbuja de pensamiento de Bautista. Él está haciendo algo ridículo — construyendo algo, dibujando algo, preguntándole a Natalia algo absurdo — y lo que dice siempre tiene la cualidad de ser simultáneamente disparatado y exactamente lo que Uma necesita escuchar. Sube el Ánimo a 15 automáticamente.

| N.° | FRASE DE BAUTISTA | CONTEXTO |
| :---- | :---- | :---- |
| 1 | 'Uma, ¿los pulpos pueden soñar? Porque yo soñé con uno y era muy feliz.' | Primera muerte |
| 2 | 'Uma, el auto de bomberos que hice tiene ahora cuatro pisos. Eso es imposible pero funciona.' | Segunda muerte |
| 3 | 'Uma, papá dice que si vas a salvar el barrio te compra medialunas. Son cuatro si ganás y dos si perdés.' | Tercera muerte |
| 4 | 'Uma, ¿qué pasa si ganás algo que no sabías que podías ganar?' | Cuarta muerte (casi filosófico) |
| 5+ | 'Uma. El barrio te necesita. Yo también. Pero el barrio más.' | Quintas muertes en adelante |

## **19.4 — La Entrada al Revés (El Sauce del Parque)**

La primera grieta navegable hacia El Revés está en el árbol más viejo del Parque Ribereño. Uma llega ahí por la misión MP-04. El cruce es voluntario: hay un destello en la corteza que Uma puede tocar para cruzar. El juego advierte: 'El Revés puede ser confuso. Tu último Anclaje guardado es el tuyo más cercano.' Confirmación con dos toques.

La primera vez que Uma entra a El Revés y vuelve, el monólogo es:

*"Ok. El otro lado del barrio se ve desde adentro. No sé si eso me alegra o me asusta. Ambos. Los dos juntos."*

## **19.5 — El Encuentro con Hernán (Padre de Pablo)**

Hernán Santellan es uno de los Vaciados del Acto IV. Uma no sabe que es el padre de Pablo hasta que, al liberarlo, Hernán dice 'mi hijo va a estar contento de saber que fue vos.' Uma pregunta qué quiere decir. Hernán dice que Pablo es terco como sus viejos y que llevaba meses tratando de encontrar el momento. Uma no dice nada. Hernán se va a buscar a Pablo.

Este evento es uno de los más emocionalmente cargados del Acto IV — no por lo que se dice sino por lo que Uma entiende que significa.

# **20\. CONSTRUCCIÓN EMOCIONAL DE LA DECLARACIÓN FINAL**

## **20.1 — La Arquitectura**

La declaración de Pablo no sorprende. No puede sorprender: el juego construyó su lógica emocional desde la primera señal. Lo que hace el Acto V no es revelar algo inesperado — es dar nombre a algo que el jugador ya sabe. Esa es la diferencia entre un giro dramático y una resolución emocional. SEÑALES apunta a la segunda.

| PILAR | QUÉ CONSTRUYE | DÓNDE OCURRE |
| :---- | :---- | :---- |
| Especificidad | Las señales son demasiado exactas para ser genéricas. El protector solar. El 'seis siete'. Cómo dobla los papeles. El jugador aprende que hay alguien que conoce a Uma de verdad, no de ideal. | Señales 1–9, distribuidas en todos los actos |
| El Espejo de Graciela | La historia de los cordones rosa enseña al jugador el patrón antes que a Uma: quien te ve de verdad deja cosas específicas. Esta conversación es la llave para entender todo lo demás. | Acto I — conversación nivel 2 con Graciela |
| El Silencio de Darío | Darío sabe y no dice. Eso es una validación estructural: el padre de Uma, que la conoce, no lo detiene. Al contrario. | Actos I y IV |
| Las Historias Paralelas | Graciela/Pedro. Don Pepe/su banda. Ernesto/su mujer. Cada arco de NPC es una versión distinta de la misma pregunta: ¿vale la pena dejar algo para alguien que quizás no lo va a entender de inmediato? | Actos I y II |
| La Abuela Carmen | Doña Carmen le habla a Uma desde el pasado sin saberlo. La protección que Pablo construyó sin querer — los Anclajes — es la prueba más material de lo que siente. | Acto III — El Telar |
| El Fragmento del Miedo al Decir | El último jefe usa las dudas de Uma como arma. Al derrotarlo, Uma ya venció lo que podría haber bloqueado su respuesta. | Acto IV — El Mirador |
| La Simplicidad del Final | Pablo no llega en un momento grandioso. Llega cuando todo terminó. El mundo no espera a nadie — el barrio sigue. Y en ese silencio tranquilo, lo que se dice es exactamente suficiente. | Acto V |

## **20.2 — Las Señales Como Retrato**

Las nueve señales, leídas en orden, son un retrato de Uma escrito por alguien que la observó sin su permiso — y que, sin embargo, lo hizo de la forma más respetuosa posible: sin distorsionar, sin idealizar, solo viendo.

| SEÑAL | FRASE | LO QUE REVELA DE UMA |
| :---- | :---- | :---- |
| 1 (Zona 1 — Graciela) | 'Siempre te fijás en lo que los demás no ven.' | Su forma de moverse por el mundo |
| 2 (Zona 1 — Plaza) | 'Hablás con los que están solos. Eso no es pequeño.' | Su empatía activa |
| 3 (Zona 2 — Marta) | 'Salís con protector aunque esté nublado. Por las dudas. Me gusta eso.' | Su cuidado consigo misma \+ el detalle del sol |
| 4 (Zona 3 — Parque) | 'Decís lo que pensás aunque no sea lo que esperan escuchar.' | Su honestidad sin filtro |
| 5 (Zona 3 — Plaza post-Umbral) | 'Me gusta cómo prestás atención a las cosas que los demás no ven.' | La señal que rompe el anonimato — Uma sabe que está dirigida a ella |
| 6 (Opcional — Sótano) | 'Doblás los papeles siempre para el mismo lado. Me parece que no lo sabés.' | El detalle más íntimo. La observación más cuidadosa. |
| 7 (El Revés — Plaza) | 'Le encontrás algo a cada persona que conocés.' | Su mirada hacia los demás |
| 8 (Opcional — El Revés profundo) | 'Seis siete. Lo decís cuando algo te sorprende en serio. No lo fingís.' | Su forma de expresar asombro genuino |
| 9 (Mirador) | 'Hoy te pregunto directo: ¿querés que sigamos siendo esto, pero con nombre?' | La declaración directa. Lo que todas las anteriores construyeron. |

## **20.3 — Por Qué Funciona (Sin Spoiler en el Juego)**

La declaración funciona porque el jugador la recibe al mismo tiempo que Uma. No hay 'giro': hay construcción. Cada conversación con cada NPC fue una pieza. Cada señal encontrada fue un centímetro más de comprensión. El final no es una sorpresa — es la consecuencia natural de haber prestado atención. Que es exactamente lo que hace Uma. Que es exactamente lo que hace Pablo con Uma. Que es exactamente lo que el juego le pide al jugador que haga con el barrio.

Es una estructura de espejo: el jugador, al seguir las señales, replicó lo que Pablo hizo. Y en ese momento de entendimiento — cuando el papel llega — el jugador siente lo que Uma siente porque lo vivió junto a ella.

# **21\. DIRECCIÓN ARTÍSTICA**

## **21.1 Estilo Visual**

SEÑALES usa pixel art con tiles 32×32. La influencia visual combina los RPGs de GBA tardíos (Mother 3, Golden Sun) con juegos modernos de tono íntimo (Celeste, Undertale, A Short Hike). El pixel art no es minimalista: tiene detalle, sombras suaves pintadas a mano y animaciones expressivas de 6–8 frames.

| Personajes | Sprites de 16×32. Uma tiene animaciones de: caminar (8 frames), correr (6), ataque por clase (8 únicos), usar habilidad (6), hablar (4), sentarse (2 frames idle), herida (4). Las expresiones faciales son grandes y legibles. |
| :---- | :---- |
| **Fondos exteriores** | Tiles con variaciones de 3 tilesets por superficie (pasto, asfalto, vereda). Las fachadas de edificios tienen grietas, manchas y carteles específicos de barrio. Sin el efecto alfombra. |
| **El Revés** | Visual completamente diferente: fondo oscuro con luz interna, todo brilla levemente desde abajo, los tiles son de cristal y energía. Las mismas formas del barrio pero invertidas en tono. |
| **Iluminación** | Sistema de capas: sombra de árboles/edificios (tile de transparencia), luz ambiental según hora narrativa, efectos de poderes y señales. |

## **21.2 Paleta de Colores**

| Barrio — Mañana (Acto I) | Amarillo cálido, naranja suave, verde hierba, azul cielo. Saturación \+15%. Contraste alto del sol. |
| :---- | :---- |
| **Barrio — Post-Umbral (Actos II–IV)** | Misma base pero con venas violeta en el suelo y el cielo alterno. Saturación base. Las grietas brillan \#7B2D8B. |
| **El Revés** | Violeta profundo (\#2C1654), negro con estrellas móviles, luz desde abajo en azul claro (\#87CEEB difuminado). Los personajes brillan con sus colores correspondientes. |
| **El Mirador — Final** | Atardecer: naranja (\#E8863A), rosa (\#C87DA6), violeta de El Revés integrado (\#7B2D8B). El cielo gradiente más hermoso del juego. |
| **Señales y Pablo** | Rosa antiguo (\#C87DA6) para todos los objetos de Pablo. Estrella dorada (\#F4C430). Papel crema (\#FFF5DC). |
| **Ecos** | Gris niebla (\#B0B8C1), azul desteñido para los Mayores. El Vacío: negro sin textura, como agujero visual. |

# **22\. UI / UX**

## **22.1 HUD**

| Esquina superior izquierda | Corazón pixelado (Ánimo). Barra circular bajo el corazón: Energía para habilidades (post-Umbral). Ícono de Anclaje activo (miniatura del lugar) debajo. |
| :---- | :---- |
| **Esquina superior derecha** | Contador de señales (◆ X/9). Ícono de hora narrativa. |
| **Sin minimapa en pantalla** | El mapa solo existe en el cuaderno. Esto mantiene la inmersión. |
| **Zona inferior — Combate** | Aparece solo en combate: barra de HP de enemigo, botones de habilidades (B, Y, X) con cooldown visual, botón de esquiva. |

## **22.2 El Cuaderno**

| Mapa | Dibujado a mano (boceto pixel). Zonas exploradas en color, inexploradas en silueta. |
| :---- | :---- |
| **Señales** | Papeles doblados que Uma abre. La sección 'Para Uma' se desbloquea en el Acto II. |
| **Personas** | Bocetos de Uma de cada NPC conocido \+ nota breve. |
| **Fragmentos** | Fragmentos de Memoria con sus historias completas. |
| **Bocetos** | Los dibujos que Uma hace durante momentos contemplativos. |

## **22.3 Controles (Android — Touch)**

| Movimiento | Joystick virtual en zona izquierda de pantalla. Funciona con input en cualquier parte de la mitad izquierda. |
| :---- | :---- |
| **Interactuar / Ataque básico** | Botón A en zona derecha. En exploración: interactúa con NPCs y objetos. En combate: ataque básico en dirección del joystick. |
| **Habilidades** | Botones B (habilidad 1), Y (habilidad 2), X (habilidad 3\) en triángulo en zona inferior derecha. |
| **Esquiva** | Swipe en cualquier dirección. |
| **Cuaderno** | Botón central inferior. Accesible siempre excepto en combate. |
| **Mirada Atenta** | Mantener A sin moverse 2 segundos: resalta interactivos ocultos. |
| **Pausa / Menú** | Botón en esquina superior derecha. |

# **23\. MÚSICA Y DISEÑO SONORO**

## **23.1 Estilo General**

La música de SEÑALES combina chiptune con elementos de bossa nova, folklore argentino y ambient electrónico. Hay tres 'eras' musicales: el barrio normal (cálido, orgánico), el barrio post-Umbral (el mismo tema base pero con síntesis electrónica superpuesta) y El Revés (ambient profundo, casi sin percusión).

## **23.2 Temas por Zona**

| Casa Torres | Piano suave \+ bajo muted. Tempo lento. 'Mañana de verano adentro de casa.' |
| :---- | :---- |
| **Calle Principal** | Guitarra acústica \+ marimba. Ritmo suave, 4/4. El kiosco tiene una radio que suma un fragmento de pop argentino diegético. |
| **Plaza Mayor** | Acuerdos de bandoneón \+ marimba \+ guitarra. El hub tiene el tema más 'lleno' del barrio. |
| **Mercado Viejo** | Bandoneón solo. Melancólico, lento. El tema más nostálgico del juego. |
| **Parque Ribereño** | Solo ambiental: agua, viento. La música está casi ausente — solo un tono drone muy suave. |
| **El Revés** | Sintetizador ambient. Bajo profundo. Sin melodía reconocible — solo texturas. Los Resonantes emiten armónicos cuando Uma está cerca. |
| **El Mirador (Final)** | Los primeros 20 segundos: silencio total excepto el viento. Luego, el leitmotiv completo del juego (el tema de las señales) con todos los instrumentos juntos. |
| **Combate post-Umbral** | El tema de la zona continúa pero se agrega percusión sintética y el tempo sube. No hay 'música de batalla' separada — el mundo y el combate son continuos. |

## **23.3 El Leitmotiv de las Señales**

Hay una melodía de 12 notas que es el leitmotiv del juego. Aparece fragmentada cada vez que Uma recoge una señal de Pablo. La señal 1 da las primeras 2 notas. Cada señal agrega más. Cuando Uma llega al Mirador, la melodía está completa y suena entera por primera vez durante la lectura del papel.

## **23.4 Integración de Agujetas de Color de Rosa**

* NARRATIVA: Los cordones rosas de Graciela. La historia de Pedro y el cassette. El arco emocional completo.

* DIEGÉTICA 1: El cassette de Don Pepe, si Uma lo examina en el cuaderno, emite 3-4 segundos de la melodía apenas reconocible.

* DIEGÉTICA 2: La radio de Doña Elsa (misión MS-03) toca 4 segundos de la canción antes de que Elsa la cambie.

* MUSICAL: La progresión de acordes del tema del Mercado Viejo cita el centro armónico de Agujetas, reinterpretado en chiptune-bandoneón.

* ARMÓNICA: El leitmotiv de las señales comparte la tonalidad y el tempo de Agujetas — hermanos musicales.

## **23.5 Diseño Sonoro — Principios**

* Cada tipo de enemigo tiene su firma sonora distinta: los Ecos Menores suenan como respiración entrecortada, los Mayores como un acorde sostenido que no resuelve, las Sombras como pasos en cerámica rota, los Vaciados como la voz de la persona distorsionada.

* Los Anclajes emiten un pulso sonoro muy suave cuando Uma está cerca — un recordatorio de que están activos.

* Los silencios están diseñados: 3 segundos antes del Umbral, 8 segundos antes de que Pablo hable en el Mirador, 5 segundos después de que Uma lee el papel.

* Bautista tiene un jingle de 3 notas que suena cada vez que aparece su burbuja. Instantáneamente reconocible.

# **24\. SISTEMA DE GUARDADO**

| Guardado Manual | En cualquier Anclaje. Animación de Uma sentándose y abriendo el cuaderno. Muestra: hora narrativa, misiones activas, señales recolectadas. |
| :---- | :---- |
| **Autoguardado** | Al completar misiones principales, al recoger señales, al entrar a zona nueva, cada 3 minutos de juego activo. |
| **3 Slots** | Nombre \+ hora narrativa \+ % exploración \+ señales. Permiten distinguir partidas fácilmente. |
| **Guardado pre-Final** | Autoguardado al pie del Mirador. El juego indica que puede volver para explorar los tres finales. |
| **New Game+** | Cuaderno de la partida anterior. NPCs tienen una línea extra. Pablo cruza una calle en el Acto I — de espaldas. Uma puede llamarlo. Él dice: 'Todavía no.' El juego guiña. |

# **25\. APÉNDICES TÉCNICOS — GODOT 4**

## **25.1 Estructura de Escenas**

| Main.tscn | Node principal: World \+ SystemLayer (UI, Save, Audio, GameFlags) |
| :---- | :---- |
| **Zones/** | Zone0\_Casa · Zone1\_Calle · Zone2\_Plaza · Zone3\_Mercado · Zone4\_Parque · Zone5\_ZonaAlta · Zone6\_Revez · Zone7\_Mirador |
| **Characters/** | Uma.tscn · Pablo.tscn · NPCBase.tscn · EcoBase.tscn · EcoMayor.tscn · SombraErrante.tscn · Vaciado.tscn · Jefe1-3.tscn |
| **UI/** | HUD.tscn · Cuaderno.tscn · DialogoBox.tscn · MonologoInterno.tscn · ClaseSelector.tscn · AnclajeFade.tscn |
| **Systems/** | GameFlags.gd (Autoload) · SaveManager.gd (Autoload) · AudioManager.gd (Autoload) · DialogueManager.gd (Autoload) · WeatherController.gd |

## **25.2 GameFlags.gd — Singleton Principal**

El singleton GameFlags.gd es el sistema de memoria central. Persiste entre escenas y se serializa en el sistema de guardado. Contiene todos los flags booleanos, contadores y estados del juego.

Estructura de flags críticos:

* clase\_elegida: String ('maga' | 'guerrera' | 'resonante')

* umbral\_ocurrido: bool

* senales\_encontradas: Array\[int\] (IDs de señales 1–9)

* npcs\_conectados: Dictionary (nombre → nivel\_relacion: int 0–3)

* npcs\_vaciados\_liberados: Array\[String\]

* anclajes\_activos: Array\[int\]

* resonancias\_desbloqueadas: Array\[String\]

* muertes\_uma: int

* respuesta\_pablo: String ('si' | 'silencio' | 'manana' | '')

* fragmentos\_memoria: Array\[int\]

## **25.3 Sistema de Combate — Nodos**

| CombatManager.gd | Controla el estado de combate: activo/inactivo, lista de enemigos en rango, turno de habilidades. Se activa cuando un enemigo entra en el rango de combate de Uma. |
| :---- | :---- |
| **ResonanciaManager.gd** | Maneja el sistema de Resonancia (diálogo de combate). Carga las respuestas según el tipo de Eco. Evalúa las opciones del jugador. Aplica consecuencias. |
| **EnemyBase.gd** | Clase base para todos los enemigos. Contiene: HP, estado (idle/patrol/chase/resonance/dead), referencias a sus datos de Resonancia. |
| **BossBase.gd** | Hereda de EnemyBase. Agrega: fases de combate, trigger de Resonancia final, recompensas. |

## **25.4 Resolución y Escalado**

Resolución base: 360×640 (portrait). El ViewportContainer escala al dispositivo manteniendo aspect ratio. La UI usa Control nodes con anchors dinámicos. El joystick virtual y los botones de acción tienen áreas táctiles de mínimo 80×80 px para comodidad en pantalla táctil.

## **25.5 Preguntas que el Juego Deja Sin Responder**

*(Intencionalmente.)*

* ¿Cuánto tiempo lleva Pablo siguiendo a Uma? (Se infiere. No se dice.)

* ¿El Umbral puede volver a abrirse? (Las grietas cicatrices sugieren que sí. El juego no lo confirma.)

* ¿Fernet el gato era ya viejo? (Don Pepe dice 'viejo para sus años'. Eso es todo.)

* ¿Doña Carmen sigue en El Revés como presencia activa? (El Telar la recuerda. Eso quizás es suficiente.)

* ¿Qué pasó con la banda de tango de Don Pepe? (Cuando escucha el cassette completo en el Acto III, llora. Eso es la respuesta.)

* ¿Qué responde Uma en el Final Silencio? (Nada. Eso también es una respuesta.)

*— SEÑALES: EL UMBRAL DEL BARRIO — GDD v2.0 — Fin del documento —*