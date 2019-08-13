class Fish:
    def __init__(self, color, fish_name):
        self.breathes = "Water"
        self.skin = "scales"
        self.color = color
        self.name = fish_name
    def move(self, speed):
        print ("Swimming " + speed + "!")
        
