from datetime import datetime, timedelta
from random import randint

from otree.api import models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer, widgets

class Constants(BaseConstants):
    name_in_url = 'CapitulosPrueba'
    players_per_group = None
    max_number_random = 6
    extension_sounds = "mp3"
    names_chapters = [
        "Frankie llega al colegio",
        "Cuando un carajito también es un chino",
        "Es cuestión de respeto",
        "Un nuevo equipo de fútbol",
        "¡Nuevas Oportunidades!",
        "Doralba, ¿Futbolista?", 
        "¡La culpa no es de Frankie!",
        "¡Que vivan las uvas pasas!", 
        "¡Hoy por ti, Mañana por mi!",
        "¡Romeo Tik y Julieta tok!",
        "Brillan los ojitos",
        "Un juego, una oportunidad",
        "El barrio es de todos",  
        "Los panas", 
        "Sueños inesperados",
    ]
    num_rounds = len(names_chapters)  # Número de capítulos/audios
    respuestas_correctas_p1 = {
        'P1P3_ciudad': '2',
        'P1P4_carajito': '1',
        'P1P5_mama': '1',
    }


class Subsession(BaseSubsession):
    def creating_session(self):
        # Inicializa la lista de números usados si no existe
        if 'numeros_usados' not in self.session.vars:
            self.session.vars['numeros_usados'] = []

        if 'ronda_intermedia' not in self.session.vars:
            self.session.vars['ronda_intermedia'] = Constants.num_rounds // 2

        # Fecha de inicio experimento
        fecha_inicio = datetime(2024, 2, 8) # Año, mes, día

        # Obtener la fecha actual
        hoy = datetime.now()

        # Calcula los jueves pasados desde la fecha de inicio
        diferencia = (hoy - fecha_inicio).days
        jueves_pasados = 0
        for i in range(diferencia + 1):
            dia_actual = fecha_inicio + timedelta(days=i)
            if dia_actual.weekday() == 3:  # Jueves
                jueves_pasados += 1

        # Los primeros tres capítulos siempre están disponibles
        max_capitulos_disponibles = 3

        # Calcular cuántos capítulos deben estar disponibles
        if jueves_pasados > 0:
            cap_adicionales = 3 * (jueves_pasados - 1)  # -1 porque los primeros 3 ya están disponibles

            # Ajustar si el total excede el número de capítulos
            max_capitulos_disponibles += min(cap_adicionales, Constants.num_rounds - max_capitulos_disponibles)

        self.session.vars['max_capitulos_disponibles'] = max_capitulos_disponibles
class Group(BaseGroup):
    pass

class Player(BasePlayer):
    tiempos_reproduccion_json = models.LongStringField(blank=True)
    numero_aleatorio = models.IntegerField(initial=0)

    #### VARIABLES POSTAUDIO1
    numeros_aleatorios_p1 = models.StringField()
    contador_correctas_p1 = models.IntegerField(initial=0)
    P1P1_emocion_1 = models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5])
    P1P2_palabras = models.LongStringField(
        label="2. ¿De qué otra forma se les llama a los y las jóvenes en otras ciudades o países? Ej., En mi ciudad les llamamos sardinas.",
        blank=True  
    )

    P1P3_ciudad = models.StringField(
        label="3. ¿De qué ciudad es Frankie?",
        choices=[
            [1,"a. De Bogotá, Colombia"],
            [2,"b. De Valencia, Venezuela"],
            [3,"c. De Lima, Perú"],
        ],
        widget = widgets.RadioSelect
    )

    P1P4_carajito = models.StringField(
        label="4. ¿Qué es un Carajito?",
        choices=[
            [1,"a. Un Niño"],
            [2,"b. Un dulce tipico de Maracaibo"],
            [3,"c. Una bebida a base de café"],
        ],
        widget = widgets.RadioSelect
    )

    P1P5_mama = models.StringField(
        label="5. ¿Cómo se llama la mamá de Frankie?",
        choices=[
            [1,"a. Doralba"],
            [2,"b. Sandra"],
            [3,"c. Martha"],
        ],
        widget = widgets.RadioSelect
    )

    P1P6_gusto = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    P1P7_personajes = models.StringField(
        label="7. ¿Con cuál de los personajes te sientes identificado?",
        choices=[
            [1,"a. Pelusa"],
            [2,"b. Erika"],
            [3,"c. Frankie"],
            [4,"c. Ninguno"],
        ],
        widget = widgets.RadioSelect
    )

    P1P8_amigos = models.StringField(
        label="8. Si le mostrarás estos 3 primeros capítulos a alguno de tus amigos creerías que:",
        choices=[
            [1,"a. Le parecería interesante y seguiría escuchando los otros capítulos"],
            [2,"b. No le interesaría y no seguiría escuchando"],
            [3,"c. Le sería indiferente"],
        ],
        widget = widgets.RadioSelect
    )

    ####  VARIABLES POSTAUDIO2
    P2P1_emocion_2 = models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5])
    P2P2_jugar = models.StringField(
        label="¿Estas de acuerdo con que las chicas deberían jugar en el equipo con los chicos? ",
        choices=[
            [0,"No"],
            [1,"Si"],
        ],
        widget = widgets.RadioSelect
    )

    P2P3_capitan = models.StringField(
        label="3. ¿Quién es el/la capitán/a del equipo de fútbol del colegio?",
        choices=[
            [1,"a. Frankie"],
            [2,"b. Pelusa"],
            [3,"c. Erika"],
            [4,"d. El profesor de educación fisica"],
        ],
        widget = widgets.RadioSelect
    )

    P2P4_preocupados = models.StringField(
        label="4. ¿Por qué Frankie y su mamá están preocupados por su abuela?",
        choices=[
            [1,"a. Porque está de cumpleaños y no pueden estar con ella"],
            [2,"b. Porque se le acabó la medicina y no tiene dinero para comprarla"],
            [3,"c. Porque se va de viaje y no tiene quien la acompañe"],
        ],
        widget = widgets.RadioSelect
    )

    P2P5_futbol = models.StringField(
        label="5. ¿Quién es la persona que más sabe de fútbol en el colegio?",
        choices=[
            [1,"a. El profesor de educación física, Milton, porque el fútbol se le da muy bien."],
            [2,"b. Doralba, la mamá de Frankie, porque tiene una Licenciatura en Deportes."],
            [3,"c. La profesora Marcela, porque juega fútbol desde niña."],
        ],
        widget = widgets.RadioSelect
    )

    P2P6_proximos = models.StringField(
        label="6. ¿Qué crees que pasará en los próximos capítulos?",
        choices=[
            [1,"a. Que Doralba podrá ser entrenadora del equipo de fútbol del colegio"],
            [2,"b. Que Doralba no podrá homologar su título"],
            [3,"c. Que expulsarán a Doralba por querer hacer cosas diferentes a su trabajo"],
            [4,"d. No me interesa que va a ocurrir"],
        ],
        widget = widgets.RadioSelect
    )

    P2P7_amigos = models.StringField(
        label="7. Si le mostrarás estos 3 primeros capítulos a alguno de tus amigos creerías que:",
        choices=[
            [1,"a. Le parecería interesante y seguiría escuchando los otros capítulos"],
            [2,"b. No le interesaría y no seguiría escuchando"],
            [3,"c. Le sería indiferente"],
        ],
        widget = widgets.RadioSelect
    )


####PREGUNTAS POSTAUDIO3
    P3P1_emocion_3 = models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5])
    P3P2_responsable = models.StringField(
        label="2. ¿Quién era el responsable de cuidar el dinero recolectado para la obra de teatro?",
        choices=[
            [1,"a. Frankie"],
            [2,"b. Pelusa"],
            [3,"c. Alex"],
            [4,"d. Doralba"],
        ],
        widget = widgets.RadioSelect
    )

    P3P3_hallacas = models.StringField(
        label="3. ¿Qué son las hallacas?",
        choices=[
            [1,"a. Son un plato típico venezolano con pasas."],
            [2,"b. Son unas manualidades típicas venezolanas."],
            [3,"c. Son unas pulseras de amistad."],
        ],
        widget = widgets.RadioSelect
    )

    P3P4_hospital = models.StringField(
        label="4. ¿A quién se encuentra Frankie en el hospital? ",
        choices=[
            [1,"a. A Erika, quien estaba visitando a su mamá que es enfermera."],
            [2,"b. A Juan, un compañero de Frankie que está enfermo de la barriga."],
            [3,"c. A Pelusa, que estaba visitando a su mamá porque está enferma."],
        ],
        widget = widgets.RadioSelect
    )

    P3P5_aceptado = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])

    P3P6_amigos = models.StringField(
        label="6. Si le mostrarás estos 3 primeros capítulos a alguno de tus amigos creerías que:",
        choices=[
            [1,"a. Le parecería interesante y seguiría escuchando los otros capítulos"],
            [2,"b. No le interesaría y no seguiría escuchando"],
            [3,"c. Le sería indiferente"],
        ],
        widget = widgets.RadioSelect
    )

####PREGUNTAS POSTAUDIO4
    P4P1_emocion_4 = models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5])
    P4P2_musica = models.StringField(
        label="2. ¿Qué género musical escogieron los alumnos para la obra de teatro? ",
        choices=[
            [1,"a. Rock"],
            [2,"b. Pop"],
            [3,"c. Reggaeton"],
            [4,"d. Hip Hop"],
        ],
        widget = widgets.RadioSelect
    )

    P4P3_papa = models.StringField(
        label="3. ¿Por qué el papá de Frankie no está con ellos? ",
        choices=[
            [1,"a. Porque no soporta a la mamá de Frankie."],
            [2,"b. Porque murió de una enfermedad cardiaca."],
            [3,"c. Porque le tocó quedarse en Venezuela."],
        ],
        widget = widgets.RadioSelect
    )

    P4P4_busca = models.StringField(
        label="4. ¿Quién busca a Doralba para que les ayude a ganar el partido contra el otro colegio?",
        choices=[
            [1,"a. Pelusa."],
            [2,"b. El profesor Milton"],
            [3,"c. Erika"],
            [4,"d. El señor Humberto"],
        ],
        widget = widgets.RadioSelect
    )

    P4P5_identifica = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])

    P4P6_amigos = models.StringField(
        label="6. Si le mostrarás estos 3 primeros capítulos a alguno de tus amigos creerías que:",
        choices=[
            [1,"a. Le parecería interesante y seguiría escuchando los otros capítulos"],
            [2,"b. No le interesaría y no seguiría escuchando"],
            [3,"c. Le sería indiferente"],
        ],
        widget = widgets.RadioSelect
    )

####PREGUNTAS POSTAUDIO5
    P5P1_emocion_5 = models.IntegerField(widget=widgets.RadioSelect, choices=[1,2,3,4,5])
    P5P2_radionovela = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])

    P5P3_celebracion = models.StringField(
        label="3. ¿Que estaban celebrando en el barrio?",
        choices=[
            [1,"a. La inauguración del Centro Cultural Colombo - Venezolano."],
            [2,"b. El cumpleaños de Doralba"],
            [3,"c. La construcción de una piscina en el colegio."],
        ],
        widget = widgets.RadioSelect
    )

    P5P4_pelusa = models.StringField(
        label="4. ¿Con quién vive Pelusa?",
        choices=[
            [1,"a. Con su tía y tío"],
            [2,"b. Con su abuelo y su papa"],
            [3,"c. Con su hermano"],
        ],
        widget = widgets.RadioSelect
    )

    P5P5_erika = models.StringField(
        label="5. ¿Qué le cambió la vida a Erika?",
        choices=[
            [1,"a. Haber aprendido manualidades"],
            [2,"b. Haber conocido a Frankie."],
            [3,"c. Haber aprendido a jugar fútbol."],
        ],
        widget = widgets.RadioSelect
    )

    P5P6_amigo = models.StringField(
        label="6. Si le mostrarás esta radionovela, a un amigo o vecino de tu misma edad, crees que:",
        choices=[
            [1,"a. Le parecería interesante y divertida, por lo que escucharía la Radionovela completa."],
            [2,"b. No le prestaría atención, porque le parecería aburrida y poco interesante."],
            [3,"c. No le gustaría y preferiría no escuchar ningún capítulo."],
        ],
        widget = widgets.RadioSelect
    )

    P5P7_familiar = models.StringField(
        label="7. Si le mostrarás esta radionovela, a un familiar tuyo de más edad, como tu mamá o tu abuelo, crees que:",
        choices=[
            [1,"a. Les encantaría, les parecería innovador y entretenido."],
            [2,"b. No llamaría su atención porque pensarían que es una historia para adolescentes."],
            [3,"c. No les gustaría."],
        ],
        widget = widgets.RadioSelect
    )

    def generar_numero_aleatorio(self):
        numero_aleatorio = randint(1, Constants.max_number_random)

        # Reiniciar la lista de números usados después del capítulo 10
        if self.round_number > 10:
            if numero_aleatorio not in self.session.vars.get('numeros_usados_2', []):
                self.session.vars.setdefault('numeros_usados_2', []).append(numero_aleatorio)
                return numero_aleatorio
            else:
                # Si el número ya fue usado, intentar de nuevo
                return self.generar_numero_aleatorio()
        else:
            if numero_aleatorio not in self.session.vars.get('numeros_usados', []):
                self.session.vars['numeros_usados'].append(numero_aleatorio)
                return numero_aleatorio
            else:
                # Si el número ya fue usado, intentar de nuevo
                return self.generar_numero_aleatorio()



