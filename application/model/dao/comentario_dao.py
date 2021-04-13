from application.model.entity.comentario import Comentario
import json
import os
from typing import List

class ComentarioDAO():
    def inserir(self, comentario: Comentario):
        comentario.set_autor('Pedro')
        comentario.set_cont('Muito Bom')