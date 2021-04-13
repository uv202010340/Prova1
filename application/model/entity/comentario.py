class Comentario():
    __autor:str
    __cont:str

    def get_autor(self):
        return self.__autor

    def set_autor(self, autor):
        self.__autor = autor

    def get_cont(self):
        return self.__cont

    def set_cont(self, cont):
        self.__cont = cont

    def to_dict(self):
        return {
            'autor': self.get_autor(),
            'cont': self.get_cont()
        }