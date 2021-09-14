class Wizard:

    def __init__(self, name):
        self._name = name
        self._health = 100
        self._energy = 500
        self._shield = 3  # each wizard has only 3 sheilds
        self._spell = ""

    def set_health(self, health):
        self._health = health

    def set_energy(self, energy):
        self._energy = energy

    def set_shield(self, shield):
        self._shield = shield

    def get_health(self):
        return self._health

    def get_energy(self):
        return self._energy

    def get_shield(self):
        return self._shield

    def set_spell(self, spell):
        self._spell = spell

    def get_spell(self):
        return self._spell

    def cast_spell(self, power):
        if self.get_energy()-power < 0:  # to avoid getting negative energy
            self.set_energy(0)
        else:
            self.set_energy(self.get_energy()-power)

    def receive_spell(self, power1, power2, spell_name):
        if spell_name == "sheild":  # if the wizard uses a sheild
            if self.get_shield() != 0:  # checking if there is available sheild
                self._shield -= 1
            else:
                if self.get_health() - abs(power1 - power2) < 0:  # to avoid getting negative health
                    self.set_health(0)
                else:
                    if power1 == power2:
                        pass
                    elif power1 < power2:
                        self.set_health(self.get_health() - abs(power1 - power2))
                    else:
                        pass
        else:
            if self.get_health()-abs(power1-power2) < 0:  # to avoid getting negative health
                self.set_health(0)
            else:
                if power1 == power2:
                    pass
                elif power1 < power2:
                    self.set_health(self.get_health()-abs(power1-power2))
                else:
                    pass
