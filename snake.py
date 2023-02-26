import pygame,sys
import random
from pygame.math import Vector2
from pygame import mixer


# #  Initialise pygame
pygame.init()

mixer.init()
# #  charger la musique
pygame.display.set_caption("Yellow Magic Orchestra – Rydeen Official Music Video.mp3")

# # Charger la  musique
pygame.mixer.music.load('Music/test.mp3')
pygame.mixer.music.play()

# Création de l'écran
cell_size = 20
cell_number = 20
screen = pygame.display.set_mode((cell_number*cell_size,cell_number*cell_number))
clock = pygame.time.Clock()

# Créaction du snake
class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.new_block = False 

    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos =int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
            pygame.draw.rect(screen,('purple'),block_rect)

    # Mouvemnt du serpent
    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0]+ self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0]+ self.direction)
            self.body = body_copy[:]
    
    # Créer la nouvelle block pour le serpent
    def add_block(self):
        self.new_block = True


# Création d'un classe pomme
class POMME:
    def __init__(self):

        # Faire en sorte les dimension du x et du y soit aléatoire
        self.x = random.randint(0,cell_number - 1) 
        self.y = random.randint(0,cell_number - 1) 
        self.pos = pygame.math.Vector2(self.x,self.y)

    # Definition fruit
    def draw_fruit(self):
        fruit_rect =pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size), cell_size, cell_size)
        pygame.draw.rect(screen,('blue'),fruit_rect)

    #  Créer le variable de randomize
    def randomize(self):
        # Faire en sorte les dimension du x et du y soit aléatoire
        self.x = random.randint(0,cell_number - 1) 
        self.y = random.randint(0,cell_number - 1) 
        self.pos = pygame.math.Vector2(self.x,self.y)
        #  Ces trois lignes de cod vont créer des positions aléatoire



#  Connexion de la pommeau serpent
class MAIN():
    def __init__(self):
        # Appelle des classes fruit
        self.snake = SNAKE()
        self.fruit = POMME()
    
    def update(self):
       self.snake.move_snake()
       self.check_collision()
       self.check_fail()
        # Déssin des éléments qui seront dans le jeu
    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    
    #  Quand le fruit sera manger
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            #  Repositionner le fruit
            self.fruit.randomize()
            # Ajouter un autre block quand le fruit est est manger
            self.snake.add_block()
        
    # verifier si le serpent  sort de la map
    def check_fail(self):
        if not 0<= self.snake.body[0].x <cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        # si le serpent se mange la queu
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
    #  Si les condition sont reunies la partie doit s'arreter
    def game_over():
         pygame.quit()
         sys.exit()


     
   

#  Une variable a déclencher en créant une muniterie par seconde
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

main_game = MAIN()

# Création de toutes les éléments
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
             main_game.update()    
        
        # Créaction du clavier
        if event.type == pygame.KEYDOWN:
            main_game.update()

            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                 main_game.snake.direction = Vector2(0,-1)
            
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                 main_game.snake.direction = Vector2(1,0)
            
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0,1)

            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction =Vector2(-1,0)

    screen.fill(('gold'))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)


