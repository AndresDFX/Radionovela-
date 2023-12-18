from otree.api import models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer, widgets

class Constants(BaseConstants):
    name_in_url = 'CapitulosPrueba'
    players_per_group = None
    max_number_random = 6
    extension_sounds = "mp3"
    names_chapters = [
        "Frankie llega al colegio",
        "Cuando un carajito también es un chino",
        "Es cuestión de respeto"
    ]
    num_rounds = len(names_chapters)  # Número de capítulos/audios


class Subsession(BaseSubsession):
    def creating_session(self):
        # Inicializa la lista de números usados si no existe
        if 'numeros_usados' not in self.session.vars:
            self.session.vars['numeros_usados'] = []

        if 'ronda_intermedia' not in self.session.vars:
            self.session.vars['ronda_intermedia'] = Constants.num_rounds // 2

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    tiempos_reproduccion_json = models.LongStringField(blank=True)
    numero_aleatorio = models.IntegerField(initial=0)
####PREGUNTAS POSTAUDIO1
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



