from random import randint, random
from otree.api import Page
from .models import Constants


class TiemposReproduccion(Page):
    form_model = 'player'
    form_fields = ['tiempos_reproduccion_json']

    def vars_for_template(self):
        nombres_capitulos_anteriores = Constants.names_chapters[:self.round_number - 1]
        lista_numeros = list(range(1, self.round_number + 1))
        rutas_audios = [f'sounds/capitulo{i}.{Constants.extension_sounds}' for i in lista_numeros]

        capitulos_y_rutas = list(zip(nombres_capitulos_anteriores, rutas_audios[:-1]))

        return {
            'num_pagina': self.round_number,
            'ruta_ultimo_audio': rutas_audios[-1],
            'capitulos_y_rutas': capitulos_y_rutas,
            'nombre_actual': Constants.names_chapters[self.round_number - 1],
        }

    def live_method(self, data):
        if not self.numero_aleatorio:
            numero_aleatorio = randint(1, Constants.max_number_random)
            while numero_aleatorio in self.session.vars['numeros_usados']:
                numero_aleatorio = randint(1, Constants.max_number_random)

            self.session.vars['numeros_usados'].append(numero_aleatorio)
            self.numero_aleatorio = numero_aleatorio

            # Enviar el número aleatorio al frontend
            return {self.id_in_group: numero_aleatorio}

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

# En views.py
class PaginaIntermedia(Page):
    def is_displayed(self):
        return self.round_number == (Constants.num_rounds // 2)

    def vars_for_template(self):
        numeros_aleatorios = [p.numero_aleatorio for p in self.player.in_all_rounds() if p.numero_aleatorio is not None]
        return {
            'numeros_aleatorios': numeros_aleatorios,
            'num_pagina': self.round_number
        }


page_sequence = [TiemposReproduccion, PaginaIntermedia,  ResultadosFinales]


