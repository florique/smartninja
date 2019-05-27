from smartninja_nosql.odm import Model

class User(Model):

    def __init__(self, name, mail, **kwargs):
        self.name = name
        self.mail = mail

        super().__init__(**kwargs)