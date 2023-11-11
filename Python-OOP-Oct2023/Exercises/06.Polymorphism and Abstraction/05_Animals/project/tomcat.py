from project.cat import Cat


class Tomcat(Cat):
    def __init__(self, name, age):
        self.gender = 'Male'
        super().__init__(name, age, self.gender)

    def make_sound(self):
        return "Hiss"


#
# t = Tomcat('ime',3)
# print(t)
# print(t.make_sound())