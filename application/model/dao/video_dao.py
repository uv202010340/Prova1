from application.model.entity.video import Video
import json
import os
from typing import List

class VideoDAO():
    def inserir(self, video: Video):
        video.set_title('titulo')