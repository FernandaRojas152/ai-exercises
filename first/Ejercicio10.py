f = open("people.txt","w")

class Person:
    def __init__(self, name, height, weight):
        self.name= name
        self.height= height
        self.weight= weight

    def IMCPerson(self):
        imc= self.weight/(self.height**2)
        return imc

people= []

people.append(Person("Amanda", 1.58, 60))
people.append(Person("Diego", 1.78, 70))
people.append(Person("Evan", 1.80, 60))
people.append(Person("Valery", 1.65, 54))
people.append(Person("Diana", 1.68, 49))


for i, p in enumerate(people):
    lines=[p.name, p.height, p.weight, round(p.IMCPerson(),2)]
    print(lines)
    f.write(str(lines))
f.close()
        
