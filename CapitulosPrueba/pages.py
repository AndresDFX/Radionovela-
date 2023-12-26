import json
from random import randint, random
from otree.api import Page
from .models import Constants


class TiemposReproduccion(Page):
    form_model = 'player'
    form_fields = ['tiempos_reproduccion_json']

    def vars_for_template(self):
        max_capitulos_disponibles = self.session.vars.get('max_capitulos_disponibles', 0)
        nombres_capitulos_anteriores = Constants.names_chapters[:self.round_number - 1]
        lista_numeros = list(range(1, min(self.round_number + 1, max_capitulos_disponibles + 1)))
        rutas_audios = [f'sounds/capitulo{i}.{Constants.extension_sounds}' for i in lista_numeros]

        capitulos_y_rutas = list(zip(nombres_capitulos_anteriores, rutas_audios[:-1]))

        return {
            'num_pagina': self.round_number,
            'ruta_ultimo_audio': rutas_audios[-1] if self.round_number <= max_capitulos_disponibles else None,
            'capitulos_y_rutas': capitulos_y_rutas,
            'nombre_actual': Constants.names_chapters[self.round_number - 1],
            'mostrar_capitulos': self.round_number <= max_capitulos_disponibles
        }

    def live_method(self, data):
        if not self.numero_aleatorio:
            self.numero_aleatorio = self.generar_numero_aleatorio()
            # Enviar el número aleatorio al frontend
            return {self.id_in_group: self.numero_aleatorio}

class ResultadosParciales1(Page):
    def is_displayed(self):
        return self.round_number == 3

    def vars_for_template(self):
        boletas_adicionales = self.player.contador_correctas_p1
        numeros_aleatorios = [p.numero_aleatorio for p in self.player.in_all_rounds()]
        numeros_aleatorios_p1 = json.loads(self.player.numeros_aleatorios_p1 or '[]')
        tiempos_reproduccion = [p.tiempos_reproduccion_json for p in self.player.in_all_rounds()]

        todos_los_numeros = numeros_aleatorios + numeros_aleatorios_p1

        return {
            'boletas_adicionales': boletas_adicionales,
            'todos_los_numeros': todos_los_numeros,
            'tiempos_reproduccion': tiempos_reproduccion,
        }
    
class ResultadosFinales(Page):
    def is_displayed(self):
        # Solo mostrar esta página en la última ronda
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        numeros_aleatorios = [p.numero_aleatorio for p in self.player.in_all_rounds()]
        tiempos_reproduccion = [p.tiempos_reproduccion_json for p in self.player.in_all_rounds()]
        return {
            'numeros_aleatorios': numeros_aleatorios,
            'tiempos_reproduccion': tiempos_reproduccion,
        }

class PaginaIntermedia(Page):
    def is_displayed(self):
        return self.round_number == (Constants.num_rounds)

    def vars_for_template(self):
        numeros_aleatorios = [p.numero_aleatorio for p in self.player.in_all_rounds() if p.numero_aleatorio is not None]
        return {
            'numeros_aleatorios': numeros_aleatorios,
            'num_pagina': self.round_number
        }

class Inicio(Page):
    def is_displayed(self):
        return self.round_number == 1
    form_model = 'player'


class Preguntas1(Page):

    form_model = 'player'
    form_fields = ['P1P1_emocion_1', 'P1P2_palabras', 'P1P3_ciudad', 'P1P4_carajito', 'P1P5_mama', 'P1P6_gusto', 'P1P7_personajes', 'P1P8_amigos']

    def is_displayed(self):
        return self.round_number == 3

    def before_next_page(self):
        numeros_aleatorios_p1 = []
        for campo in self.form_fields:
            if getattr(self.player, campo) == Constants.respuestas_correctas_p1.get(campo, ''):
                self.player.contador_correctas_p1 += 1
                nuevo_numero = self.player.generar_numero_aleatorio()
                numeros_aleatorios_p1.append(nuevo_numero)

        self.player.numeros_aleatorios_p1 = json.dumps(numeros_aleatorios_p1)
class Preguntas2(Page):

    form_model = 'player'
    form_fields = ['P2P1_emocion_2', 'P2P2_jugar', 'P2P3_capitan', 'P2P4_preocupados', 'P2P5_futbol', 'P2P6_proximos', 'P2P7_amigos']
    def is_displayed(self):
        return self.round_number == 6
class Preguntas3(Page):
    def is_displayed(self):
        return self.round_number == 9
    form_model = 'player'
    form_fields = ['P3P1_emocion_3', 'P3P2_responsable', 'P3P3_hallacas', 'P3P4_hospital', 'P3P5_aceptado', 'P3P6_amigos']

class Preguntas4(Page):
    def is_displayed(self):
        return self.round_number == 12
    form_model = 'player'
    form_fields = ['P4P1_emocion_4', 'P4P2_musica', 'P4P3_papa', 'P4P4_busca', 'P4P5_identifica', 'P4P6_amigos']

class Preguntas5(Page):
    def is_displayed(self):
        return self.round_number == 15
    form_model = 'player'
    form_fields = ['P5P1_emocion_5', 'P5P2_radionovela', 'P5P3_celebracion', 'P5P4_pelusa', 'P5P5_erika', 'P5P6_amigo', 'P5P7_familiar']


page_sequence = [Inicio, TiemposReproduccion, PaginaIntermedia, Preguntas1,  ResultadosParciales1,
                Preguntas2, Preguntas3,
                Preguntas4, Preguntas5 ]


