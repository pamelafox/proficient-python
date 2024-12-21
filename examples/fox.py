class Fox:
  species_name = 'Vulpes vulpes'

  def __init__(self, name):
      self.name = name
      self.happiness = 0

  def say(self):
      return f'{self.name} says Wa-pa-pa-pa-pa-pow'

  def play(self, num_hours):
      self.happiness += num_hours
      
