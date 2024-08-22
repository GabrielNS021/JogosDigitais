class NaveEspacial:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.position = (0, 0)  # Posição inicial
        self.direction = 0  # Direção inicial (0 graus)
        self.speed = 0  # Velocidade inicial
        self.shield = 100  # Nível de escudo inicial
        self.energy = 100  # Energia inicial

    def move(self):
        # Implementação para mover a nave
        print(f"{self.name} está se movendo para a frente.")

    def turn(self, direction):
        # Implementação para girar a nave
        if direction.lower() == 'esquerda':
            self.direction -= 90  # Exemplo de rotação
        elif direction.lower() == 'direita':
            self.direction += 90
        print(f"{self.name} virou para a {direction}.")

    def shoot(self):
        # Implementação para lançar um projétil
        if self.energy >= 10:
            self.energy -= 10  # Custo de energia para atirar
            print(f"{self.name} lançou um projétil.")
        else:
            print(f"{self.name} não tem energia suficiente para atirar.")

    def hit(self, damage):
        # Implementação para quando a nave é atingida
        self.shield -= damage
        if self.shield <= 0:
            self.alive = False
            print(f"{self.name} foi destruída.")
        else:
            print(f"{self.name} foi atingida! Escudo restante: {self.shield}")

    def recharge(self):
        # Implementação para recarregar energia
        self.energy = 100
        print(f"{self.name} recarregou sua energia.")

    def info(self):
        print(f"{self.name} tem {self.energy} de energia e {self.shield} de escudo")

def jogar(nave):
    print("Jogador escolha sua açao:")
    print("1 - Informaçoes")
    print("2 - Mover")
    print("3 - Virar")
    print("4 - Atirar")
    print("5 - Dano")
    print("6 - Recarregar")
    menu = int(input("Digite o valor desejado: "))
    if menu == 1:
        nave.info()

    elif menu == 2:
        nave.move()

    elif menu == 3:
        dire = input("Esquerda ou Direita: ")
        if dire.lower() == "esquerda":
            nave.turn("esquerda")
        elif dire.lower() == "direita":
            nave.turn("direita")
        else:
            print("Houve algum erro escolha novamente a opçao e digite a direçao novamente")

    elif menu == 4:
        nave.shoot()

    elif menu == 5:
        if nave.alive == True:
            nave.hit(20)

        if nave.alive == False:
            ver = False

    elif menu == 6:
        nave.recharge()


#Jogo
p1 = input("Digite o nome da nave do jogador 1: ")
p2 = input("Digite o nome da nave do jogador 2: ")

nave1 = NaveEspacial(p1)
nave2 = NaveEspacial(p2)

while nave1.alive and nave2.alive:
    jogar(nave1)
    jogar(nave2)