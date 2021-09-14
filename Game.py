from Wizard import Wizard


# this class will be responsible for the game loop and reading from files

class Game:
    harry = Wizard("Harry")          # instance of harry
    voldemort = Wizard("Voldemort")  # instance of Voldemort
    line_count = 0

    @classmethod
    def read_power(cls, spell):  # this function searches with the given spell in the spells file to determine spell power
        search_file = open("spells.txt", "r")
        for line in search_file:
            if spell in line:
                number = line[-4:]  # getting the power of each spell
                return int(number)
        search_file.close()

    @classmethod
    def read_input(cls, i):  # this function reads the input form input file
        print("Enter the two spells (harry then Voldemort): ")
        file1 = open('input.txt', 'r')
        lines = file1.readlines()
        harry_spell, voldemort_spell = lines[i].split()
        cls.harry.set_spell(harry_spell)
        cls.voldemort.set_spell(voldemort_spell)
        print(cls.harry.get_spell() + "   " + cls.voldemort.get_spell())

        file1.close()

    @classmethod
    def num_line(cls):
        file1 = open('input.txt', 'r')
        lines = file1.readlines()
        cls.line_count = len(lines)

    @classmethod
    def print_result(cls):
        print("        Harry            Voldemort")
        print("Health: " + str(cls.harry.get_health()) + "\t\t\t\t\t" + str(cls.voldemort.get_health()))
        print("Energy: " + str(cls.harry.get_energy()) + "\t\t\t\t\t" + str(cls.voldemort.get_energy()))
        print()

    @classmethod
    def declare_winner(cls):
        if cls.harry.get_health() == 0 or cls.harry.get_energy() == 0:
            print("Voldemort is the winner..")
        elif cls.voldemort.get_health() == 0 or cls.voldemort.get_energy() == 0:
            print("Harry is the winner..")
        else:
            print("No Winner !!")
