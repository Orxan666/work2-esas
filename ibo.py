class Soldier():
    health=110
    def __init__(self,name,uniform_color,power):
        self.name = name
        self.uniform_color = uniform_color
        self.power=power
    def fire(self,enemy):
        enemy.health=enemy.health-self.power 

soldier1=Soldier(name="Ibo",uniform_color="green",power=40)
soldier2=Soldier(name="Ferid",uniform_color="red",power=60)
soldier1.fire(soldier1)
soldier1.fire(soldier1)
soldier1.fire(soldier1)
print(soldier1.health)