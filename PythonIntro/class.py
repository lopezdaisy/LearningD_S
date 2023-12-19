class Human:
    #defining properties
    def __init__(self,name, occupation) -> None:
        self.name = name
        self.occupation = occupation

    #defining methods
    def do_work(self):
        if self.occupation =="tennis player":
            print(self.name,"plays tennis")
        elif self.occupation == "actor":
            print(self.name,"shoots a film")

    def speak(self):
        print(self.name,"says how are you?")

daisy =  Human("Daisy Lopez","tennis player")
daisy.do_work()
daisy.speak()

maria = Human("Maria Sharl","actor")
maria.do_work()
maria.speak()
