from otree.api import *


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'EncuestaSeguimiento'
    players_per_group = None
    max_number_random = 6500

    num_rounds = 1


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
    numero_aleatorio = models.IntegerField(initial=0)
    # ******************************************************************************************************************** #
    # *** Variables Cuestionario
    # ******************************************************************************************************************** #    
    ES_c1_familia= models.IntegerField(widget=widgets.RadioSelect, choices=[-5,-4,-3,-2,-1,0,1,2,3,4,5])
    ES_c2_barrio= models.IntegerField(widget=widgets.RadioSelect, choices=[-5,-4,-3,-2,-1,0,1,2,3,4,5])
    ES_c3_policia= models.IntegerField(widget=widgets.RadioSelect, choices=[-5,-4,-3,-2,-1,0,1,2,3,4,5])
    ES_c4_jueces= models.IntegerField(widget=widgets.RadioSelect, choices=[-5,-4,-3,-2,-1,0,1,2,3,4,5])
    ES_c5_caleños= models.IntegerField(widget=widgets.RadioSelect, choices=[-5,-4,-3,-2,-1,0,1,2,3,4,5])
    ES_c6_españoles= models.IntegerField(widget=widgets.RadioSelect, choices=[-5,-4,-3,-2,-1,0,1,2,3,4,5])
    ES_c7_venezolanos= models.IntegerField(widget=widgets.RadioSelect, choices=[-5,-4,-3,-2,-1,0,1,2,3,4,5])
    ES_c8_chilenos= models.IntegerField(widget=widgets.RadioSelect, choices=[-5,-4,-3,-2,-1,0,1,2,3,4,5])
    ES_c9_bancos= models.IntegerField(widget=widgets.RadioSelect, choices=[-5,-4,-3,-2,-1,0,1,2,3,4,5])
    ES_c10_presidente= models.IntegerField(widget=widgets.RadioSelect, choices=[-5,-4,-3,-2,-1,0,1,2,3,4,5])
    ES_c11_iglesia= models.IntegerField(widget=widgets.RadioSelect, choices=[-5,-4,-3,-2,-1,0,1,2,3,4,5])
    
    ES_F1_habla_mujeres= models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3])
    ES_F2_habla_jovenes= models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3])
    ES_F3_habla_pobres= models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3])
    ES_F4_habla_indigenas= models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3])
    ES_F5_habla_venezolanos= models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3])
    ES_F6_habla_mayores= models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3])

    ES_F7_actividad_recreativa = models.StringField(
        label="7. En 2023, ¿Con qué frecuencia te reuniste con amigos para una actividad recreativa  (ir a un concierto, fiesta, cine, ver fútbol, hacer deporte)?",
        choices=[ 
            [0,"a. Nunca"],
            [1,"b. Una vez al mes"],
            [2,"c. Todas las semanas una vez"],
            [3,"d. Todas las semanas varias veces"],
            [4,"e. A diario"],
        ],
        widget = widgets.RadioSelect
    )

    ES_F8_act_recreativa_migrantes = models.StringField(
        label="8. ¿En cuántos de estos eventos había personas nacidas fuera de Colombia?",
        choices=[ 
            [0,"a. Ninguno"],
            [1,"b. Algunos, muy pocos"],
            [2,"c. Bastantes"],
            [3,"d. Muchos"],
        ],
        widget = widgets.RadioSelect
        )
    ES_F9_amigos_venezolanos = models.StringField(
        label="9. ¿Tienes amigos o amigas cercanos que hayan nacido en Venezuela?",
        choices=[ 
            [0,"a. No"],
            [1,"b. Si"],
        ],
        widget = widgets.RadioSelect
    )

    ES_cuantos2 = models.IntegerField(label="¿Cuantos amigos cercanos tienes que hayan nacido en Venezuela?", initial="0")

    ES_F10_vecinos_españoles = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    ES_F11_vecinos_venezolanos = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    ES_F12_vecinos_norteamericanos = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    ES_F13_vecinos_chilenos = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    ES_F14_pareja_venezolana = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    ES_F15_amigos_venezuela = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    ES_F16_exp_col_controles_migrantes = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    ES_F17_exp_col_prioridad_colombianos = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    ES_F20_ven_edu_colombianos = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    ES_F21_ven_respeto = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    ES_F22_ven_contratados = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    ES_F23_ven_acceso_servicios = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    ES_F24_ven_juiciosos = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])
    ES_F25_ven_ladrones = models.IntegerField(widget=widgets.RadioSelect, choices=[0,1,2,3,4,5,6,7,8,9,10])

    ES_F26_campaña = models.StringField(
        label="24. ¿Participarías en una campaña para conseguir 1,000 empleos para jóvenes venezolanos en Colombia",
        choices=[ 
            [0,"a. No, no me interesa."],
            [1,"b. No, no quiero."],
            [1,"b. No, no tengo tiempo."],
            [1,"b. Si"],
            
        ],
        widget = widgets.RadioSelect
    )

# PAGES
class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass

class Consentimiento(Page):
    form_model = 'player'

class Inicio(Page):
    form_model = 'player'

class Page3_ParteC(Page):
    form_model = 'player'
    form_fields = ['ES_c1_familia', 'ES_c2_barrio', 'ES_c3_policia', 'ES_c4_jueces', 'ES_c5_caleños', 'ES_c6_españoles', 'ES_c7_venezolanos', 
    'ES_c8_chilenos', 'ES_c9_bancos', 'ES_c10_presidente', 'ES_c11_iglesia',
]

class Page6_ParteF(Page):
    form_model = 'player'
    form_fields = ['ES_F1_habla_mujeres', 'ES_F2_habla_jovenes', 'ES_F3_habla_pobres', 'ES_F4_habla_indigenas', 'ES_F5_habla_venezolanos',
    'ES_F6_habla_mayores', 'ES_F7_actividad_recreativa', 'ES_F8_act_recreativa_migrantes', 'ES_F9_amigos_venezolanos', 'ES_cuantos2',  
    'ES_F10_vecinos_españoles', 'ES_F11_vecinos_venezolanos', 'ES_F12_vecinos_norteamericanos', 'ES_F13_vecinos_chilenos',
    'ES_F14_pareja_venezolana', 'ES_F15_amigos_venezuela', 'ES_F16_exp_col_controles_migrantes', 'ES_F17_exp_col_prioridad_colombianos',
    'ES_F20_ven_edu_colombianos', 'ES_F21_ven_respeto', 
    'ES_F22_ven_contratados', 'ES_F23_ven_acceso_servicios', 'ES_F24_ven_juiciosos', 'ES_F25_ven_ladrones', 'ES_F26_campaña',
]

class Page7_Final(Page):
    form_model = 'player'


class Final(Page):
    form_model = 'player'
    def live_method(self, data):
        if not self.numero_aleatorio:
            numero_aleatorio = randint(1, Constants.max_number_random)
            while numero_aleatorio in self.session.vars['numeros_usados']:
                numero_aleatorio = randint(1, Constants.max_number_random)

            self.session.vars['numeros_usados'].append(numero_aleatorio)
            self.numero_aleatorio = numero_aleatorio

            # Enviar el número aleatorio al frontend
            return {self.id_in_group: numero_aleatorio}
        
    def vars_for_template(self):
        numeros_aleatorios = [p.numero_aleatorio for p in self.player.in_all_rounds()]
        return {
            'numeros_aleatorios': numeros_aleatorios,
        }



page_sequence = [Inicio, Page3_ParteC, Page6_ParteF, Page7_Final ]
