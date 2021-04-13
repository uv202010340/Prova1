class Video():
    __urlV:str
    __urlIm:str
    __title:str
    __desc:str
    __Qvi:int
    __Qlike:int
    __data:int
    __categoria:object

    def get_urlV(self):
        return self.__urlV

    def set_urlV(self, urlV):
        self.__urlV = urlV

    def get_urlIm(self):
        return self.__urlIm

    def set_urlIm(self, urlIm):
        self.__urlIm = urlIm

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_desc(self):
        return self.__desc

    def set_desc(self, desc):
        self.__desc = desc

    def get_Qvi(self):
        return self.__Qvi

    def set_Qvi(self, Qvi):
        self.__Qvi = Qvi

    def get_Qlike(self):
        return self.__Qlike

    def set_Qlike(self, Qlike):
        self.__Qlike = Qlike

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def to_dict(self):
        return {
            'urlV': self.get_urlV(),
            'urlIm': self.get_urlIm(),
            'title': self.get_title(),
            'desc': self.get_desc(),
            'Qvi': self.get_Qvi(),
            'Qlike': self.get_Qlike(),
            'data': self.get_data()
        }