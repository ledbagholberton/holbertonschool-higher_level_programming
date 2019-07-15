class Person:
    def say_hi(self):
        print('Hello, how are you?')
    def say_hola(self):
        print('Ahora.... que hacemos?')

p = Person()
p.say_hi()
Person().say_hola()
# The previous 2 lines can also be written as
# Person().say_hi()
