from application.model.entity.categoria import Categoria
import json
import os
from typing import List

class CategoriaDAO():
    def __init__(self, categoria: Categoria):
        categoria.set_title('Filmes')
        categoria.set_desc('Videos sobre Filmes')
        categoria.set_urlIm('')