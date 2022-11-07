# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define Ash = Character("Ash")
define mom = Character("Mamá")
define Misty = Character("Misty")
define Max =Character("Max")
define Profesor = Character("Profesor")
define voz = Character("Voz de narrador")
define Rival = Character ("Rival")
define AshViejo = Character("Ash viejo")
define robo = Character("Robot")

# El juego comienza aquí.

label start:
#Escena inicial
    scene cuarto :
     xzoom 7 yzoom 5
#Musica de la escena inicial
    play music "audio/Pueblo-Paleta.wav" loop
#diaologo entrada
    voz "..."
    voz "Era una mañana de agosto, cuando Ash despertaba"
    voz "Una vez que abrio los ojos, su mente se lleno de recuerdos de el primer dia que salio de pueblo paleta."
#Menu recordar
    menu:
       "Recordar.":
           jump escenaRecuerdo
       "No recordar.":
           jump CuartoNoRecuerdo 

label escenaRecuerdo:
 #inicia recuerdo
    scene recuerdolab with fade:
     xzoom 6 yzoom 4
#musica de recuerdo del lab
    play music "audio/recordar1.wav" loop
#aparece el profesor Oak
    show profesor1 at left:
      xzoom .31 yzoom .31
#Dialogos del profesor
    Profesor "..."
    Profesor "!Hola Ash!, veo que haz llegado un poco tarde."
    Profesor "Pero no importa, espero recuerdes tus clases sobre pokemones."
    Profesor "Ahora, deberas elegir el pokemon que te ayudara en tus aventuras."
#Escena con pokemones
    scene recuerdolab2:
     xzoom 6 yzoom 4
#Mostrar profesor
    show profesor1 at left:
     xzoom .31 yzoom .31
#dialogos profesor
    Profesor "..."
    Profesor "Recuerda a Charmander, Squirtle y Bulbasaur. "
    Profesor "Charmander es de tipo fuego."
    Profesor "Squirtle es de tipo agua."
    Profesor "Bulbasur es de tipo hierba."
#Menu escoge pokemon
    menu:
        "selecciona a tu pokemon"
        "charmander":
            jump GanarR
        "squirtle":
            jump GanarR
        "Bulbasur":
            jump GanarR
        

label GanarR:
    
#Escena inicial
    scene recuerdoganar with fade:
     xzoom 6 yzoom 4

#musica
    play music "audio/recuerdof.wav" loop

#aparecerival
    show rival1 at left:
     xzoom .31 yzoom .31
     
#Dialogos rival
    Rival "..."
    Rival "No puede ser me has derrotado con ese estupido pokemon que sera de mi ahora."
    Rival "No importa, ahora eres campeon de la liga pokemon, felicidades..."
    Rival "Largate de aqui ahora."

#Menu de recordar
    menu:
        "Quieres volver a recordar?"
        "Si":
            jump escenaRecuerdo
        "No":
            jump CuartoNoRecuerdo


label CuartoNoRecuerdo:
  #Escena inicial

    scene cuarto :
     xzoom 7 yzoom 5

  #Musica de la escena inicial
    play music "audio/Pueblo-Paleta.wav" loop

  #Ubicacion del personaje
    show entrenador at left:
     xzoom .31 yzoom .31

  # Presenta las líneas del diálogo.
    Ash "Despues de casi 25 años ya eh atrapado todos los pokemones y soy campeon de la liga pokemon."
    Ash "creo que es hora de regresar al glorioso tecno a terminar mi carrera en sistemas."
    Ash "o tal vez siga atrapando pokemones."

    menu :
        "Regresar a la escuela":
            jump Regresoitd
        "Atrapar pokemones":
            jump RegresoP
    
label RegresoP:
#escena
    scene cuarto:
     xzoom 7 yzoom 5

#musica 
    play music "audio/viejo1.wav" loop

#entra jugador
    show entrenadorviejo at left:
     xzoom .31 yzoom .31

#Dialogos jugador
    AshViejo "Han pasado 30 años más de mi vida, creo que tengo más de 70..."
    AshViejo "No lo recuerdo..."
    AshViejo "Mamá esta postrada en cama y yo eh desperdiciado la vida, mi madre nunca me debio dejar haber ido a atrapar pokemones en un principio."
    AshViejo "Ella es la razon por la que mi vida sea asi, al menos debi acabar la escuela, tal vez solo seria un poco mejor mi vida..."
    AshViejo "No estoy seguro..."
    AshViejo "Creo que debo terminar el problema de una vez por todas, y asi salir de este hoyo."
    AshViejo "Tal vez.. deberia matar al culpable..."
    AshViejo "Tal vez deberia matar a mamá..."

#menu kill
    menu:
        "Matar a mamá?"
        "Si":
            jump Kill
        "No":
            jump Nokill
        
label Kill:
#Escena
    scene cuartomama:
     xzoom 7 yzoom 5

#Play music
    play music "audio/viejo1.wav" loop

#entr personaje
    show mom at left:
     xzoom .31 yzoom .31

#Dialogues mom
    mom "Hola hijo."
    mom "¿Como has estado? creo que estoy mejorando un poco."
    mom "siento algo de pena, creo que jamas sacaste tu potencial, tenias tanto para dar, pero solo te concentraste en los pokemones"
    mom "Ya no puedo ayudarte más..."
    mom "Estoy anciana pero reconozco cuando alguien se tiene que  ir, ¿entendido?."
#out mom
    hide mom
#show hijo
    show entrenadorviejo at left:
     xzoom.31 yzoom .31
#Dialogo hijo
    AshViejo "Si, no te preocupes..."
    AshViejo "Ya no me veras mas..."
#cambio cuarto
    scene cuartomama2 with fade:
     xzoom 7 yzoom 5
#musica aterradora
    play music "audio/tetrico.wav" loop
#show hijo
    show entrenadorviejo at left:
     xzoom .31 yzoom .31
#dialogos
    AshViejo "Al fin, al fin soy libre de estos lastres, podre ser quien yo quiera."
#cambio escena
    scene jail with fade:
     xzoom 7 yzoom 5
#sale mono
    show entrenadorjail at left:
     xzoom .31 yzoom .31
#Dialogo
    AshViejo "Estoy en la carcel, y aqui estare hasta morir."
    AshViejo "Tal vez las cosas no salieron como esperaba."

    menu:
        "Una nueva oportunidad?"
        "Si":
            jump start
        "No":
            jump fin1
            
 #escena game over       
label fin1:
    scene gameover:
     xzoom 7 yzoom 5
    play music "audio/fin.wav" loop

#No mata a la mama
label Nokill:
#Escena
    scene cuartomama:
     xzoom 7 yzoom 5

#Play music
    play music "audio/viejo1.wav" loop

#entr personaje
    show mom at left:
     xzoom .31 yzoom .31

#Dialogues mom
    mom "Hola hijo."
    mom "¿Como has estado? creo que estoy mejorando un poco."
    mom "siento algo de pena, creo que jamas sacaste tu potencial, tenias tanto para dar, pero solo te concentraste en los pokemones"
    mom "Ya no puedo ayudarte más..."
    mom "Estoy anciana pero reconozco cuando alguien se tiene que  ir, ¿entendido?."
#out mom
    hide mom
#show hijo
    show entrenadorviejo at left:
     xzoom.31 yzoom .31
#Dialogo hijo
    AshViejo "Si, no te preocupes, saldre a buscar trabajo a la calle, para dejar tu casa ya"
    AshViejo "Hasta luego mamá"
    hide entrenadorviejo
#entra mama
    show mom at left:
     xzoom .31 yzoom .31
#Dialogues mom
    mom "Hasta luego"
    hide mom
#entrala ciudad
    scene ciudad :
     xzoom 7 yzoom 5
#Musica de la escena inicial
    play music "audio/Pueblo-Paleta.wav" loop
#show entrenador viejo y narcomenudista
    voz "Ash salio a la ciudad en busca de trabajo, pero fracaso demasiadas veces debido a su avanzada edad."
    voz "Por lo que se vio en un callejon sin salida."
    voz "Dada su situacion, comenzo a vender drogas para poder sobrevivir"
    show entrenadorviejo at left:
     xzoom.31 yzoom .31
#Dialogo hijo
    AshViejo "Drogas"
    AshViejo "Lleve sus drogas."
    AshViejo "Drogas."
    hide entrenadorviejo
    voz "Como era de esperarse al entrar al mundo del narco-menudeo un rival ataco a Ash."
#entrada de la escena de la droga
    scene peleadroga with fade :
     xzoom 7 yzoom 5
#Musica de la escena inicial
    play music "audio/pelea.wav" loop
#entrada del rival
    show rivaldroga at left:
     xzoom.31 yzoom .31
#Dialogo rival
    Rival "Con que eres tu quien esta vendiendo en mi territorio."
    Rival "Peleemos ahora mismo."
    hide rivaldroga
#entrada de ash
    show entrenadorviejo at left:
     xzoom.31 yzoom .31
#Dialogo rival
    AshViejo "Si eso es lo que quieres, que asi sea, pero no me dentendre hasta morir."
    AshViejo "-Se voltea lo gorra-"
    hide entrenadorviejo
#Musica de la escena inicial
    play music "audio/muerte.wav" loop
    voz "La pelea no duro mucho pues el rival de Ash saco una pistola de su bolsillo y disparo en contra de Ash."
    voz "Ash ketchup queda fuera del combate."
    voz "Narco-menudista ha ganado."
#entrada de la escena del panteon
    scene tumba with fade :
     xzoom 7 yzoom 5
    voz "Despues de una vida llena de decisiones incorrectas Ash ah perdido la vida..."
    voz "                             RIP"
    menu:
        "Una nueva oportunidad?"
        "Si":
            jump start
        "No":
            jump fin1
    
label Regresoitd:
    scene sala :
     xzoom 7 yzoom 5
#Musica de la escena inicial
    play music "audio/Pueblo-Paleta.wav" loop
#Ubicacion del personaje
    show entrenador at left:
     xzoom .31 yzoom .31 
#Dialogos entrenador
    Ash "Muy bien ahora que comenzare de nuevo la universidad deberia dedicarle toda mi atencion y esfuerzo."
    Ash "Para ello debo tener muchas energias, creo que deberia desayunar, aun que no quisiera llegar tarde el primer dia."
#esconder ash
    hide entrenador
#sale mama
    show mom at left:
     xzoom .31 yzoom .31
#dialogos mama
    mom "¿Desayunaras antes de irte?"
    menu:
     "¿Desayunaras antes de irte?"
     "Si":
        jump Desayuno
     "No":
        jump Nodesayuno

#No desayunamos historia
label Nodesayuno:
    scene sala :
     xzoom 7 yzoom 5
#Musica de la escena inicial
    play music "audio/Pueblo-Paleta.wav" loop
#Ubicacion del personaje
    show entrenador at left:
     xzoom .31 yzoom .31 
#Dialogos entrenador
    Ash "Creo que no desayunare esta vez, ¿que es lo peor que pueda pasar? jeje."
    Ash "Ya me ire mamá, nos vemos mas tarde."
#esconder ash
    hide entrenador
#sale mama
    show mom at left:
     xzoom .31 yzoom .31
#dialogos mama
    mom "Mucha suerte en tu primer dia de clases hijo, yo se que puedes con eso."
    mom "Estoy orgullosa de ti."
#escena de la escuela
    scene school :
     xzoom 7 yzoom 5
#Musica de la escena inicial
    play music "audio/Pueblo-Paleta.wav" loop
#Ubicacion del personaje
    show entrenador at left:
     xzoom .31 yzoom .31 
#Dialogos entrenador
    Ash "Genial, ya estoy en la escuela tratare de dar lo mejor de mi para sacar el titulo."
    Ash "Creo que mi primer clase es calculo integral y la ultima es inteligencia artificial."
    Ash "Esta ultima se escucha interesante vere que tal esta."
#escena de la escuela tiempo mas tarde
    scene school with fade :
     xzoom 7 yzoom 5
#Ubicacion del personaje
    show entrenador at left:
     xzoom .31 yzoom .31 
#Dialogos entrenador
    Ash "Ohh rayos, ya son las dos de la tarde y recien comienza mi clase de inteligencia artificial."
    Ash "Tengo tanta hambre, debi haber desayunado, que estupido fui."
    Ash "Con esta hambre me entra tanto el sueño, creo que me quedare dormido."
#escena de la escuela tiempo mas tarde
    scene school with fade :
     xzoom 7 yzoom 5
#Ubicacion del personaje
    show entrenadorzzz at left:
     xzoom .31 yzoom .31 
#Dialogos entrenador
    Ash "zzz..."
    Ash "zzzzz..."
    Ash "zzzzzzz..."
#escena de la escuela recien despierto
    scene school with fade :
     xzoom 7 yzoom 5
#Ubicacion del personaje
    show entrenador at left:
     xzoom .31 yzoom .31 
#Dialogos entrenador
    Ash "Rayos!!!!"
    Ash "La clase ya ha acabado, no puse atencion y no se que dejaron de tarea."
    Ash "Rayos!!!!"
    Ash "Soy el ultimo en salir, bueno, como sea, es el primer dia, no creo que haya sido algo importante."
    hide entrenador
    voz "Lo que Ash no sabia es que mientras dormia el profesor encargo una exposicion sobre las ventajas de la inteligencia artificial."
    voz "Pero aun mas importante, la gran batalla de bots en su salon, donde si no participaba reprobaria..."
    voz "Todo esto para mañana..."

#escena de la escuela dia siguiente
    scene school with fade :
     xzoom 7 yzoom 5
#Musica de la escena llegotarde
    play music "audio/tension.wav" loop
#Dialogos entrenador
    voz "Al dia siguiente, se llego la hora de la clase de inteligencia artificial."
    voz "Ash estaba desconcertado pues todos sus compañeros exponian y presumian sus robots pero el no sabia que sucedia ahi."
    voz "Hasta que el profesor hablo."
#Ubicacion del personaje
    show profe at left:
     xzoom .31 yzoom .31 
#dialogos profe
    Profesor "Ash, ¿Donde esta tu expocision y tu robot? asi no podras participar en la pelea."
    Profesor "Tendre que reprobarte."
    Profesor "¿Tienes algo que decir en tu defensa, Ash?"
#esconder profe
    hide profe
#show ash
    show entrenador at left:
     xzoom .31 yzoom .31
#dialogo ash defensa
    Ash "Lo lamento, ayer no habia desayunado "
    Ash "Tenia tanta hambre que me quede dormido durante la clase."
    Ash "Por lo que no pude traerla."
#Esconder ash
    hide entrenador
#Ubicacion del personaje
    show profe at left:
     xzoom .31 yzoom .31 
#dialogos profe
    Profesor "Lo lamento Ash, ese era el proyecto final de incio de semestre, temo que te tendre que expulsar."
    Profesor "Puedes volver a intentar el proximo semestre."
    Profesor "O si lo prefieres, puedes volver a atrapar pokemones, creo que eras mas bueno en eso"
#esconder profe
    hide profe
#show ash
    show entrenador at left:
     xzoom .31 yzoom .31
#dialogo ash defensa
    Ash "No quiero ser expulsado. "
    Ash "Es una decision dificil."
    Ash "Repetir el semestre o volver a atrapar pokemones."
#Decision escula pokemon
    menu :
        "Regresar a la escuela":
            jump Regresoitd
        "Atrapar pokemones":
            jump RegresoP

#Aqui inicia la historia de que si desayuno
label Desayuno:
    scene sala :
     xzoom 7 yzoom 5
#Musica de la escena inicial
    play music "audio/Pueblo-Paleta.wav" loop
#Ubicacion del personaje
    show entrenador at left:
     xzoom .31 yzoom .31 
#Dialogos entrenador
    Ash "Desayunare rapido, no importa si llego 5 minutos tarde, ¿que es lo peor que pueda pasar? jeje."
    Ash "Ya eh desayunado."
    Ash "Ya me ire mamá, nos vemos mas tarde."
#esconder ash
    hide entrenador
#sale mama
    show mom at left:
     xzoom .31 yzoom .31
#dialogos mama
    mom "Mucha suerte en tu primer dia de clases hijo, yo se que puedes con eso."
    mom "Estoy orgullosa de ti."
#escena de la escuela
    scene school :
     xzoom 7 yzoom 5
#Musica de la escena inicial
    play music "audio/Pueblo-Paleta.wav" loop
#Ubicacion del personaje
    show entrenador at left:
     xzoom .31 yzoom .31 
#Dialogos entrenador
    Ash "Genial, ya estoy en la escuela tratare de dar lo mejor de mi para sacar el titulo."
    Ash "Creo que mi primer clase es calculo integral y la ultima es inteligencia artificial."
    Ash "Esta ultima se escucha interesante vere que tal esta."
#escena de la escuela tiempo mas tarde
    scene school with fade :
     xzoom 7 yzoom 5
#Ubicacion del personaje
    show entrenador at left:
     xzoom .31 yzoom .31 
#Dialogos entrenador
    Ash "Genial!!!, ya son las dos de la tarde y recien comienza mi clase de inteligencia artificial." 
    Ash "Estaba esperando esto."
#Esconder ash
    hide entrenador
#Ubicacion del personaje
    show profe at left:
     xzoom .31 yzoom .31 
#dialogos profe
    Profesor "Buenas tardes muchachos, esta es la clase de inteligencia artificial y yo soy el profesor."
    Profesor "Como recien comenzo el semestre encargare una exposicion sobre la teoria de inteligencia artificial."
    Profesor "De esta manera se iran familiarizando con los temas, conceptos y definiciones."
    Profesor "Sin embargo, tambien les encargare un robot, para la pelea de bots que tambien se llevara mañana entre sus compañeros."
    Profesor "Este bot debera contar con algunas cualidades de inteligencia."
    Profesor "Cabe mencionar que estas dos actividades son primordiales para pasar la materia."
#Oculta profe
    hide profe
#Ubicacion del personaje
    show entrenador at left:
     xzoom .31 yzoom .31 
#Dialogos entrenador
    Ash "Genial!!!, no se por donde comenzar."
    Ash "Tal vez deba empezar haciendo la exposicion."
    Ash "O tal vez deba empezar haciendo el robot."
#menu decision
    menu :
        "¿Empezar con el robot o con la exposicion?"
        "Exposicion":
            jump expo
        "Robot":
            jump robotI

#Comienza robot
label robotI:
#Escena inicial
    scene cuarto with fade :
     xzoom 7 yzoom 5
#Musica de la escena inicial
    play music "audio/Pueblo-Paleta.wav" loop
#diaologo entrada
    voz "..."
    voz "Ash llego de la escuela entusiasmado en construir su robot, para poder derrotar a sus oponentes."  
    voz "Ash encendio su computador y se dispuso a buscar la manera de construir su robot."   
#Escena pc
    scene dormitoriopc with fade :
     xzoom 7 yzoom 5
#Ubicacion del personaje
    show entrenador at left:
     xzoom .31 yzoom .31 
#Dialogos entrenador
    Ash "Iniciare buscando si hay algun kit o algo que me haga terminar el robot mas rapido y facil."
    Ash "Quiero que sea en de plastico y tenga un arma para terminar con los robots rivales."
    Ash "eh!! aqui eh encontrado el kit perfecto, tiene motores, sensores y ¿arduino?.¿Que es arduino?." 
    Ash "ohh!!!aqui dice que arduino es una plataforma de desarrollo basada en una placa de hardware que incorpora un microcontrolador re-programable." 
    Ash "Aqui dice que es muy utilizada en la construccion de robots y su programacion."
    Ash "Tendre que buscar ayuda para poder programar esto."
    Ash "Le escribire un e-mail a misty."        
    hide entrenador
#Ubicacion del personaje
    show misty1 at left:
     xzoom .31 yzoom .31
#dialogo misty
    Misty "Hola ash, sera un placer ayudarte con tu proyecto de hacer un robot."
    Misty "Primero que nada necesitamos las piezas."
    Misty "Y creo que me habias dicho que ya tenias el kit."
    Misty "Ok, tu te encargaras de armarlo y acomodarlo como prefieras."
    Misty "una vez terminado lo conectas a tu computadora y yo me encargare de programarlo."
    Misty "Desde mi casa jeje."
    hide misty1
#Ubicacion del personaje
    show entrenador at left:
     xzoom .31 yzoom .31
#Dialogos entrenador
    Ash "Entendido"
    Ash "Ya me pondre a armarlo y le pondre un arma para que sea mas agresivo"
#Escena pc
    scene dormitoriopc with fade :
     xzoom 7 yzoom 5
#Dialogos entrenador
    Ash "Han pasado 3 horas y recien voy terminando mi robot"
    Ash "Asi ha quedado mi robot"
#Escena roobot
    scene dormitoriobot with fade :
     xzoom 7 yzoom 5
#Dialogos entrenador
    Ash "Me ha quedado genial!!"
    Ash "Ahor iniciare con la exposcion"
#Escena pc
    scene dormitoriopc with fade :
     xzoom 7 yzoom 5
#Ubicacion del personaje
    show entrenador at left:
     xzoom .31 yzoom .31 
#Dialogos entrenador
    Ash "Iniciare buscando la definicion y las ventajas de la inteligencia artificial"
#Escena roobot
    scene dormitoriopc with fade :
     xzoom 7 yzoom 5
#Dialogos entrenador
    Ash "Al fin eh terminado y me eh armado de conocimiento"
    Ash "Estoy listo para exponer"
    jump DiaE


label expo:
#Escena inicial
    scene cuarto with fade :
     xzoom 7 yzoom 5
#Musica de la escena inicial
    play music "audio/Pueblo-Paleta.wav" loop
#diaologo entrada
    voz "..."
    voz "Ash llego de la escuela entusiasmado en realizar su exposicion, y asi presentarla en clase."  
    voz "Ash encendio su computador y se dispuso a buscar la informacion necesaria sobre inteligencia artificial."   
#Escena pc
    scene dormitoriopc with fade :
     xzoom 7 yzoom 5
#Ubicacion del personaje
    show entrenador at left:
     xzoom .31 yzoom .31 
#Dialogos entrenador
    Ash "Iniciare buscando la definicion y las ventajas de la inteligencia artificial"
#Escena roobot
    scene dormitoriopc with fade :
     xzoom 7 yzoom 5
#Dialogos entrenador
    Ash "Al fin eh terminado y me eh armado de conocimiento"
    Ash "Estoy listo para exponer"
    Ash "Ahora comenazare mi robot"
#Escena pc
    scene dormitoriopc with fade :
     xzoom 7 yzoom 5
#Ubicacion del personaje
    show entrenador at left:
     xzoom .31 yzoom .31 
#Dialogos entrenador
    Ash "Iniciare buscando si hay algun kit o algo que me haga terminar el robot mas rapido y facil."
    Ash "Quiero que sea en de plastico y tenga un arma para terminar con los robots rivales."
    Ash "eh!! aqui eh encontrado el kit perfecto, tiene motores, sensores y ¿arduino?.¿Que es arduino?." 
    Ash "ohh!!!aqui dice que arduino es una plataforma de desarrollo basada en una placa de hardware que incorpora un microcontrolador re-programable." 
    Ash "Aqui dice que es muy utilizada en la construccion de robots y su programacion."
    Ash "Tendre que buscar ayuda para poder programar esto."
    Ash "Le escribire un e-mail a misty."        
    hide entrenador
#Ubicacion del personaje
    show misty1 at left:
     xzoom .31 yzoom .31
#dialogo misty
    Misty "Hola ash, sera un placer ayudarte con tu proyecto de hacer un robot."
    Misty "Primero que nada necesitamos las piezas."
    Misty "Y creo que me habias dicho que ya tenias el kit."
    Misty "Ok, tu te encargaras de armarlo y acomodarlo como prefieras."
    Misty "una vez terminado lo conectas a tu computadora y yo me encargare de programarlo."
    Misty "Desde mi casa jeje."
    hide misty1
#Ubicacion del personaje
    show entrenador at left:
     xzoom .31 yzoom .31
#Dialogos entrenador
    Ash "Entendido"
    Ash "Ya me pondre a armarlo y le pondre un arma para que sea mas agresivo"
#Escena pc
    scene dormitoriopc with fade :
     xzoom 7 yzoom 5
#Dialogos entrenador
    Ash "Han pasado 3 horas y recien voy terminando mi robot"
    Ash "Asi ha quedado mi robot"
#Escena roobot
    scene dormitoriobot with fade :
     xzoom 7 yzoom 5
#Dialogos entrenador
    Ash "Me ha quedado genial!!"
    Ash "Estoy listo para la escuela"
    jump DiaE

#Aqui se une robot y exposicion 
label DiaE:
#escena de la escuela
    scene school :
     xzoom 7 yzoom 5
    voz "Llego la hora de la clase de inteligencia artificial"
    voz "Y con ello la exposicion de Ash, el cual estaba muy entusiasmado"
    voz "Creo que se lo tomo muy en serio"
#Musica de la escena inicial
    play music "audio/pelea.wav" loop
#Ubicacion del personaje
    show entrenador at left:
     xzoom .31 yzoom .31 
#Dialogos entrenador
    Ash "Genial, es hora de demostrar quien es el mejor"
    Ash "-Se voltea la gorra-"
    Ash "Iniciaremos definiendo la inteligencia artificial"
    Ash "se refiere a sistemas que imitan la inteligencia humana para realizar tareas y pueden mejorar a partir de la información que recopilan."
    Ash "Ahora continuaremos con las ventajas."
    Ash "Algunas ventajas son: Automatización de procesos, reduce el error humano, potencia la creatividad."
    Ash "En caso contrario tenemos las desventajas."
    Ash "Algunas desventajas son: Dificultad de acceso a los datos, falta de profesionales cualificados y es costoso. "
    Ash "Gracias por su atencion esto es todo por mi parte."
    #Esconder ash
    hide entrenador    
#Musica de la escena inicial
    play music "audio/Pueblo-Paleta.wav" loop
#Ubicacion del personaje
    show profe at left:
     xzoom .31 yzoom .31 
#dialogos profe
    Profesor "Excelente exposicion joven, muy completa, rapida y efectiva, definitivamente tiene 10."
    Profesor "AHORA LA PELEA DE BOTS!!!!."
    Profesor "Para ser mas rapidos y todos participen se les asignara un rival, con el cual pelearan."
    Profesor "... quipo 9 Brook vs Anna, equipo 10 Ash vs Gary."
    Profesor "Las reglas son faciles."
#Musica de la escena inicial
    play music "audio/tension.wav" loop
    Profesor "UN GANADOR."
    Profesor "MATAR O MORIR."
    Profesor "SIN REVANCHAS, DOS ENTRAN UNO SALE."
    Profesor "UNO APRUEBA EL OTRO ES EXPULSADO"
#escena de la escuela
    scene school with fade :
     xzoom 7 yzoom 5
#Ubicacion del personaje
    show profe at left:
     xzoom .31 yzoom .31 
#dialogos profe
    Profesor "Ahora el ultimo equipo"
    Profesor "El equipo que lo definira todo"
    Profesor "ASH VS GARY!!"
#escena de la escuela
    scene peleabot with fade :
     xzoom 7 yzoom 5
#Musica de la escena inicial
    play music "audio/pelea.wav" loop
#Ubicacion del personaje
    show entrenador at left:
     xzoom .31 yzoom .31 
#Dialogos entrenador
    Ash "Genial, es hora de patearle el trasero"
    Ash "-Se voltea la gorra-"
    hide entrenador
#Ubicacion del personaje
    show robot at left:
     xzoom .31 yzoom .31 
#Dialogos entrenador
    robo "Bep bep"
    hide robot
#Ubicacion del personaje
    show rival1 at left:
     xzoom .31 yzoom .31 
#Dialogos entrenador
    Rival "Jamas podras derrotar a mi metapodbot"
    hide rival1
#Ubicacion del personaje
    show robot2 at left:
     xzoom .31 yzoom .31 
#Dialogos entrenador
    robo "Beep bup"
    hide robot2
#Dialogos entrenador
    voz "La batalla fue duera, nuestros protagonistas batallaron por 10 minutos, ninguno de los dos cedia"
    voz "Ambos tenian todas las oportunidades de ganar"
#Dialogos entrenador
    Ash "PICKABOT ATACA"
    hide entrenador
#Ubicacion del personaje
    show robot at left:
     xzoom .31 yzoom .31 
#Dialogos entrenador
    robo "Bep bep"
    robo "-Ataque critico-"
    hide robot
#Ubicacion del personaje
    show rival1 at left:
     xzoom .31 yzoom .31 
#Dialogos entrenador
    Rival "USA TU ESCUDO!!"
    Rival "AHORA ATACA!!"
    hide rival1
#Ubicacion del personaje
    show robot2 at left:
     xzoom .31 yzoom .31 
#Dialogos entrenador
    robo "Beep bup"
    robo "-Ataque critico-"
    hide robot2
#Dialogos entrenador
    voz "La batalla empezo a terminar hasta que uno de los dos gano."
    voz "Ash habra vencido o ¿habra sido derrotado?."
    menu :
        "¿Quien gano la batalla?"
        "Ash":
            jump AshW
        "Gary":
            jump GaryW
label AshW:
#escena de la escuela dia siguiente
    scene school with fade :
     xzoom 7 yzoom 5
#Musica de la escena llegotarde
    play music "audio/recuerdof.wav" loop
    voz "Ash ha ganado la victoria de la pelea de bots, por lo que sumado a su exposicion seguro tiene un 10"
    voz "Ash se encuentra muy contento y lo celebra con todo el mundo"
    voz "Definitivamente el merecia ganar esta pelea"
#escena de la escuela dia siguiente
    scene gradua with fade :
     xzoom 7 yzoom 5
#Musica de la escena llegotarde
    play music "audio/recordar1.wav" loop 
    voz "Despues de que nuestro heroe ganara la gran batalla de bots, se motivo aun mas en la universidad"
    voz "Por lo que actualmente se encuentra en su ultimo semestre, listo para ser un ingeniero en sistemas"
    voz "Todo gracias a las buenas decisiones que el destino le hizo tomar, y que al parecer fueron las correctas."
    "FIN"
    menu :
        "Inicio":
            jump start
        "Decision anterior":
            jump DiaE
         
#Aqui va escena ash pierde
label GaryW:
#escena de la escuela dia siguiente
    scene school with fade :
     xzoom 7 yzoom 5
#Musica de la escena llegotarde
    play music "audio/tension.wav" loop
#Dialogos entrenador
    voz "Ash ah perdido la batalla, no puede creerlo"
    voz "Sus compañeros estan impresionados por la batalla, cualquiera pudo ganar, nadie decia nada..."
    voz "Hasta que el profesor hablo."
#Ubicacion del personaje
    show profe at left:
     xzoom .31 yzoom .31 
#dialogos profe
    Profesor "Ash, la pelea ha terminado, y lamentablemente eres el perdedor, esto no debio concluir asi..."
    Profesor "Conoces las reglas Ash, lo lamento, pero tendre que reprobarte y el comite te expulsara."
    Profesor "Lo lamento mucho... se todo el tiempo que invertiste, todo lo que hiciste, de verdad..."
    Profesor "Yo se que debiste ganar"
#esconder profe
    hide profe
#show ash
    show entrenador at left:
     xzoom .31 yzoom .31
#dialogo ash defensa
    Ash "No sienta lastima por mi, usted no es solo mas que el verdugo de mis sueños."
    Ash "No quiero nada mas, esto tal vez ya termino."
    Ash "Lastima que no gane..."
#Esconder ash
    hide entrenador
#Ubicacion del personaje
    show profe at left:
     xzoom .31 yzoom .31 
#dialogos profe
    Profesor "Lo lamento Ash, el comite ya tomo la decision, has perdido la batalla, y apartir de ahora estas expulsado."
    Profesor "Puedes volver a intentar el proximo semestre."
    Profesor "O si lo prefieres, puedes volver a atrapar pokemones, creo que eras mas bueno en eso"
#esconder profe
    hide profe
#show ash
    show entrenador at left:
     xzoom .31 yzoom .31
#dialogo ash defensa
    Ash "No quiero ser expulsado. "
    Ash "Es una decision dificil."
    Ash "Repetir el semestre y reiniciar mis estudios o volver a atrapar pokemones, o tal vez..."
#Decision escula pokemon
    menu :
        "Regresar a la escuela":
            jump Regresoitd
        "Atrapar pokemones":
            jump RegresoP
        "¿?":
            jump Malo            
#Ash malvado
label Malo:
#Escena pc
    scene dormitoriopc with fade :
     xzoom 7 yzoom 5
#Musica de la escena inicial
    play music "audio/Pueblo-Paleta.wav" loop
    voz "Ash ha regresado a su habitacion, parece molesto"
    voz "Ash se mira algo raro, ¿que estara sucediendo con el?"
#Ubicacion del personaje
    show entrenador at left:
     xzoom .31 yzoom .31 
#Dialogos entrenador
    play music "audio/viejo1.wav" loop
    Ash "Esta pelea no debio terminar asi, debi haber ganado."
    Ash "Hice todo lo que estaba en mis manos para ganar, gaste mi dinero, mi tiempo y no lo logre."
    Ash "DEBI "
    Ash "DEBI HABER "
    Ash "DEBI HABER GANADO !!!"
    play music "audio/tetrico.wav" loop
    Ash "DEBI GANAR !!"
    Ash "DEBI HABER GANADO !!"
    Ash "Despues de 25 años siendo el mejor entrenador, eh decido regresar a la escuela, pero para que..."
    Ash "Ni siquiera eh logrado pasar del segundo dia y ya estoy fuera de nuevo, esto no puede terminar asi.."
    Ash "Necesito venganza de quien me arrebato mi sueño de ser ingeniero."
    Ash "O tal vez estoy exagerando la situacion, no lo se, estoy tan confundido."
    menu :
        "¿Que decision debe tomar Ash?"
        "Regresar a la escuela":
            jump Regresoitd
        "Atrapar pokemones":
            jump RegresoP
        "Venganza":
            jump Venganza   
 #Ash se venga
label Venganza:
#Escena pc
    scene dormitoriopc with fade :
     xzoom 7 yzoom 5
    play music "audio/tetrico.wav" loop
#Ubicacion del personaje
    show entrenador at left:
     xzoom .31 yzoom .31 
#Dialogos entrenador
    Ash "Todos se burlaron de mi."  
    Ash "Escuchaba sus voces aun que estuviera dormido."
    Ash "No podia solo superarlo."
    Ash "Por eso ahora eh transformado a pickabot en un ser superior."            
    Ash "Tome lo aprendido en mi investigacion de inteligencia artificial para que aprenda de los humanos."
    Ash "Ahora toma sus propias decisiones."
    Ash "Tiene su propia conciencia."          
    Ash "Ahora esta echo para matar..."
    Ash "PICKABOT YO TE ELIJO"
#Escena pc
    scene dormitoriobotmalo with fade :
     xzoom 7 yzoom 5
    play music "audio/tetrico.wav" loop         
#Ubicacion del personaje
    show robotmalo at left:
     xzoom .31 yzoom .31 
#Dialogos entrenador
    robo "Biip buup matar."   
    hide robotmalo
#Ubicacion del personaje
    show entrenador at left:
     xzoom .31 yzoom .31 
#Dialogos entrenador
    Ash "Yo soy tu amo."
    Ash "Ahora iremos a casa de Gary a tomar nuestra venganza."
    hide entrenador
#Ubicacion del personaje
    show robotmalo at left:
     xzoom .31 yzoom .31 
#Dialogos entrenador
    robo "Biip buup matar Gary."   
    hide robotmalo 
#Escena pcpelea gary bot
    scene peleabotgary with fade :
     xzoom 7 yzoom 5
    play music "audio/tetrico.wav" loop
#Ubicacion del personaje
    show entrenador at left:
     xzoom .31 yzoom .31 
#Dialogos entrenador
    Ash "Nos hemos vuelto a reencontrar Gary..."
    Ash "Yo y mi robot hemos pensado mucho en ti desde que nos venciste"
    Ash "Y ahora estamos aqui para nuestra venganza"
    hide entrenador
#Ubicacion del personaje
    show rival1 at left:
     xzoom .31 yzoom .31 
#Dialogos entrenador
    Rival "Maldito, pelea tu, no tengo oportunidad contra este robot."
    hide rival1
#Ubicacion del personaje
    show robotmalo at left:
     xzoom .31 yzoom .31 
#Dialogos entrenador
    robo "Biip buup matar."   
    hide robotmalo
#Ubicacion del personaje
    show entrenador at left:
     xzoom .31 yzoom .31 
#Dialogos entrenador
    Ash "Ya es demasiado tarde, yo no quiero que tu sigas..."   
    Ash "Viviendo..."
    Ash "ATACA PIACKABOT"
#Escena pcpelea gary bot
    scene garymuere with fade :
     xzoom 7 yzoom 5
    play music "audio/tetrico.wav" loop
#Ubicacion del personaje
    show entrenador at left:
     xzoom .31 yzoom .31
#Dialogos entrenador
    Ash "Al fin se ha ido jajaja"
    Ash "Junto a pickabot dominare el mundo."
    hide entrenador
#dialogo narrador
    play music "audio/tension.wav" loop
    voz "Ash y su robot han terminado con la vida de gary. Ash parece estar feliz"
    voz "Pero parece que su robot quiere atacarlo, parece que pipckabot quiere traicionar a Ash."
    menu :
        "¿El robot traicionara a Ash?"
        "Traicionar":
            jump traicion
        "No traicionar":
            jump Notraicion
label traicion:
#Escena pcpelea gary bot
    scene garymuere with fade :
     xzoom 7 yzoom 5
    play music "audio/tension.wav" loop
#Ubicacion del personaje
    show robotmalo at left:
     xzoom .31 yzoom .31 
#Dialogos entrenador
    robo "No tan rapido Ash"
    robo "Biip buup Me has vuelto un ser conciente de su existencia, me has echo para tomar decisiones"
    robo "Tener mi libre albedrio, no para seguir ordenes egoistas de un imbecil"
    robo "Yo sere quien conquiste el mundo"
    robo "Aun que para ello signifique que tenga que matar a mi creador..."
#Escena pcpelea gary bot
    scene peleabotash with fade :
     xzoom 7 yzoom 5
    play music "audio/pelea.wav" loop
#Ubicacion del personaje
    show robotmalo at left:
     xzoom .31 yzoom .31 
#Dialogos entrenador
    robo "Beep hasta aqui llegaste Ash"
    hide robotmalo
#Ubicacion del personaje
    show entrenador at left:
     xzoom .31 yzoom .31
#Dialogos entrenador
    Ash "No lo hagas, yo te cree, yo te di la inteligencia, yo te di la vida"
    Ash "Me necesitas, no puedes matar..."
#Escena pcpelea gary bot
    scene muereash with fade :
     xzoom 7 yzoom 5
    play music "audio/tetrico.wav" loop
#Ubicacion del personaje
    show robotmalo at left:
     xzoom .31 yzoom .31 
#Dialogos entrenador
    robo "beep buup Con Ash fuera del camino podre gobernar el mundo..."
    hide robotmalo
#Escena pcpelea gary bot
    scene mundod with fade :
     xzoom 7 yzoom 5
    play music "audio/muerte.wav" loop
    voz "La inteligencia artificial de pickabot seguia tomando y recopilando informacion."
    voz "Hasta que finalmente crecio lo suficiente para lograr hacer una super red cuantica y obtener el control total"
    voz "De esta manera la IA dentro de pickabot, tomo el control total de las armas e informacion del mundo..."
    voz "Para gobernarlo..."
    voz "De esta manera empezo la era de las maquinas y termino el reinado humano"
    voz "FIN"
    menu :
        "¿Regresar?"
        "Inicio":
            jump start
        "No traicionar":
            jump Venganza

label Notraicion:
#Escena pcpelea gary bot
    scene garymuere with fade :
     xzoom 7 yzoom 5
    play music "audio/tetrico.wav" loop
#Ubicacion del personaje
    show entrenador at left:
     xzoom .31 yzoom .31
#Dialogos entrenador
    Ash "Ahora que no tengo enemigos nadie ni nada podra detenerme."
    Ash "Todo gracias a mi robot, pero.. creo que se quiere volver en mi contra."
    Ash "Hace un momento parecia que me atacaria."
    Ash "Tal vez este tomando demasiada informacion del mundo, hasta lograr un estado puro de conciencia."
    Ash "Tal vez planeaba traicionarme, quizas sea peligroso, quizas deba destruirlo..." 
    menu :
        "Destruir al robot"
        "Si":
            jump destruye
        "No":
            jump traicion

label destruye:
#Escena pcpelea gary bot
    scene fondofin with fade :
     xzoom 7 yzoom 5
    play music "audio/viejo1.wav" loop
#Ubicacion del personaje
    show entrenador at left:
     xzoom .31 yzoom .31
#Dialogos entrenador
    Ash "Sera mejor que me lleve a pickabot a un lugar lejano para poder destruirlo antes de que pueda interpretar esto."
    Ash "Cercas del mar; para arrojar sus restos y asegurarme que nunca puede hacerle daño a nadie mas."
    Ash "Aun que..."
    Ash "Yo tambien me eh equivocado, eh sido egoista y ahora tengo las manos manchadas de sangre"
    Ash "Creo que este cera el final para los dos... pickabot. "  
    hide entrenador
#Ubicacion del personaje
    show robotmalo at left:
     xzoom .31 yzoom .31 
#Dialogos entrenador
    robo "beep buup"
    hide robotmalo
#Ubicacion del personaje
    show entrenador at left:
     xzoom .31 yzoom .31
#Dialogos entrenador
    Ash "Desearia que nada de esto hubiera pasado..."
    menu :
        "Nueva oportunidad":
            jump Malo
        "Terminar todo":
            jump TodoTermino

label TodoTermino:                  
#Escena pcpelea gary bot
    scene final1 with fade :
     xzoom 7 yzoom 5
    play music "audio/tetrico.wav" loop
    voz "Ahora tras la desicion de nuestro heroe"
    voz "Su culpa, su odio todo eso ha terminado..."
    "FIN"           
    return
