from otree.api import models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer, widgets

class Constants(BaseConstants):
    name_in_url = 'radionovela'
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
    

