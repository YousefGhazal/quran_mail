class Living:
    def eat(self, food):
        return "5ra"

class Human(Living):
    def walk(self):
        print("walking")

    def eat(self, food):
        print('cook')
        # s = super().eat(food)
        print('clean')
        return "done"


yoss = Human()

print(yoss.eat("food"))