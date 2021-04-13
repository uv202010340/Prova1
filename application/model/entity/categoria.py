class Categoria():
    __title:str
    __desc:str
    __urlIm:str

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title - title

    def get_desc(self):
        return self.__desc

    def set_desc(self, desc):
        self.__desc = desc

    def get_urlIm(self):
        return self.__urlIm

    def set_urlIm(self, urlIm):
        self.__urlIm = urlIm

    def to_dict(self):
        return {
            'title': self.get_title(),
            'desc': self.get_desc(),
            'urlIm': self.get_urlIm()
        }