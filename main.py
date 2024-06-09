import pygame
import random

# Definování barev:
black=(0, 0, 0)
green=(0, 255, 0)
red=(255, 0, 0)

pygame.init()  #Inicializace modulů pygame

# Nastavení okna:
screen = pygame.display.set_mode((800, 800))      #Vytvoření herního okna
pygame.display.set_caption("Snake")   #Nastavení popisku
screen.fill(black)   #Nastavení barvy pozadí okna 

# Vytvoření třídy hlavy hada:
class snake_head:
    def __init__(self):
        self.segment = ((400, 400)) # Nastavení segmentu hada
        self.segment_size = 20      # Nastavení velikosti segmentu
        self.direction = "RIGHT"    # Nastavení počáteččního směru
        
    def move(self):
        head_x, head_y = self.segment        # Získání souřadnic hlavy
        self.segment = (head_x, head_y)
        
        if self.direction == "RIGHT":        # Jestliže směr je doprava  
            head_x += self.segment_size      # Hlavní segment se posune o jeho velikost na x souřadnici do +, tedy doprava
            
        elif self.direction == "LEFT":
            head_x -= self.segment_size  
            
        elif self.direction == "UP":
            head_y += self.segment_size   
            
        elif self.direction == "DOWN":
            head_y -= self.segment_size            

head= snake_head()  # Volání třídy snake_head

# Vytvoření třídy segmentu hada:
class snake_body:
    def __init__(self):
        self.segments = []
        
    def add_segment(self, x, y):
        self.segments.append((x, y))
        
    # Posun všech segmentů hada:        
    def move(self, head_x, head_y):
        
        if self.segments:                                     # Pokud existují segmenty těla hada
            for i in range(len(self.segments) - 1, 0, 1):     # Postupné procházení seznamu 
                if i > 0:                                     
                    self.segments[i] = self.segments[i - 1]   # Nastavení segmentu na pozici předešlého segmentu

            self.segments[0] = (head_x, head_y)               # Posun 1. segmentu na pozici, kde byla dříve hlava

body = snake_body()     # Volání třídy snake_body

# Vytvoření třídy ovoce:
class snake_fruit:
    def __init__(self):
        fruit_positions = list(range(20, 781, 20))                                       # Vytvoření pozic pro ovoce        
        self.segment = (random.choice(fruit_positions), random.choice(fruit_positions))  # Nastavení souřadnic na náhodné pozice
        self.segment_size = 20                                                           # Nastavení velikosti ovoce

fruit = snake_fruit()     # Volání třídy snake_fruit



# Cyklus pro zobrazování okna:
running=True    
while running:
    for event in pygame.event.get():   # Pro každý zjištěný event
        if event.type == pygame.QUIT:  # Jestliže uživatel klikl na křížek
            running = False            # Ukončení cyklu
    
    head_x, head_y = head.segment
    head.move()                        # Volání funkce pro pohyb hlavy hada
    body.move(head_x, head_y)          # Volání funkce pro pohyb těla hada
    
    pygame.draw.rect(screen, (green), (head_x, head_y, head.segment_size, head.segment_size))                  # Vykreslení hlavy hada
    pygame.draw.rect(screen, (255, 0, 0), (fruit.segment[0], fruit.segment[1], fruit.segment_size, fruit.segment_size)) # Vykreslení ovoce
    
    pygame.display.update()   # Obnova okna
    
pygame.quit()                 # Konec knihovny pygame
          