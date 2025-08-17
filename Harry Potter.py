class Wizard:
    def __init__(self, n, h, p, w):
        self.name = n
        self.age = 11
        self.school = "Hogwarts"
        self.house = h
        self.patronus = p
        self.wand_core = "dragon heartstring"
        self.wand_length = w

    def get_patronus(self):
        return self.patronus

    def personal_info(self):
        print(self.name,"is", self.age,"years old and has a wand with a core of", self.wand_core,".")
    def school_info(self):
        print(self.name, "belongs to the House of", self.house, "at Hogwarts.")
    def expelliarmus(self, person):
        print(self.name, "has disarmed", person,".")
    def birthday(self):
        print(self.age + 1)
        self.age +=1
        
    
harry_potter = Wizard("Harry Potter", "Gryffindor", "Stag", 11)

ron_Weasley = Wizard("Ron Weasley", "Gryffindor", "Jack Russell Terrier", 14)

hermione_Grangier = Wizard("Hermione Grangier", "Gryffindor", "Otter", 15)

draco_Malfoy = Wizard("Draco Malfoy", "Slytherin", None, 15)

cedric_Diggory = Wizard("Cedric Diggory", "Hufflepuff", "Badger", 12.24)

newt_Scamander = Wizard("Newt Scamander", "Hufflepuff", "Kelpie", 14)

fleur_Delacour = Wizard("Fleur Delacour", "Bellefeuille", "Non-corporeal", 9.5)





print("Harry Potter has a patronus of an", harry_potter.get_patronus(),".")

print("Ron Weasley has a patronus of an", ron_Weasley.get_patronus(),".")

print("Hermione Grangier has a patronus of an", hermione_Grangier.get_patronus(),".")

print("Draco Malfoy has a patronus of an", draco_Malfoy.get_patronus(),".")


ron_Weasley.personal_info()
hermione_Grangier.personal_info()
draco_Malfoy.personal_info()
cedric_Diggory.personal_info()
newt_Scamander.personal_info()
fleur_Delacour.personal_info()

print(ron_Weasley.school_info())
print(hermione_Grangier.school_info())
print(draco_Malfoy.school_info())
print(cedric_Diggory.school_info())
print(newt_Scamander.school_info())
print(fleur_Delacour.school_info())




harry_potter.personal_info()
harry_potter.school_info()
harry_potter.expelliarmus(draco_Malfoy.name)
harry_potter.birthday()

cedric_Diggory.birthday()
cedric_Diggory.birthday()
cedric_Diggory.birthday()

fleur_Delacour.birthday()
fleur_Delacour.birthday()
fleur_Delacour.birthday()

newt_Scamander.age = 97
newt_Scamander.personal_info()
draco_Malfoy.expelliarmus(fleur_Delacour.name)

harry_potter.personal_info()
ron_Weasley.personal_info()
hermione_Grangier.personal_info()
draco_Malfoy.personal_info()
cedric_Diggory.personal_info()
newt_Scamander.personal_info()
fleur_Delacour.personal_info()







