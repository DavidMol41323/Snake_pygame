import pygame
import random

pygame.init()  # Inicializace modulů pygame

# Definování barev:
black=(0, 0, 0)
green=(0, 255, 0)
red=(255, 0, 0)

# Funkce pro vytváření umístění a text pro skóre:
def text_create_score(score):
    font_score = pygame.font.SysFont(None, 50, bold=True, italic=False)         # Nastavení fontu pro text SCORE
    score_text = font_score.render(f"Score: {score}" , True, green)             # Nastavení textu SCORE
    score_text_rect = score_text.get_rect(center=(400, 400))                    # Nastavení umístění textu SCORE
    return score_text, score_text_rect                                          # Vrací umístění a text

score = 0      # Nastavení Skóre
# Funkce pro obnovu skóre:
def update_score(function):
    global score
    if function == "plus_score":        # Funkce přičtě 1 ke skóre
        score += 1                      
    elif function == "show_score":      # Funkce zobrazí skóre
        return score
    elif function == "zero_score":      # Funkce vrátí skóre na 0
        score -= score
        
# Zobrazení textu GAME OVER
font_big = pygame.font.SysFont(None, 100, bold=True, italic=False)          # Nastavení fontu pro velké nápisy
font_small = pygame.font.SysFont(None, 25, bold=False, italic=False)        # Nastavení fontu pro malé nápisy
space_text = font_small.render("Press SPACE to continue...", True, green)   # Nastavení textu SPACE
game_over = font_big.render("GAME OVER!", True, red)                        # Nastavení textu GAME OVER!
paused_text = font_big.render("PAUSED", True, green)                        # Nastavení textu PAUSED
space_text_rect = space_text.get_rect(center=(400, 450))                    # Nastavení umístění textu SPACE
game_over_rect = game_over.get_rect(center=(400, 350))                      # Nastavení umístění textu GAME OVER!
paused_text_rect = paused_text.get_rect(center=(400, 400))                  # Nastavení umístění textu PAUSED


# Nastavení okna:
screen = pygame.display.set_mode((800, 800))      #Vytvoření herního okna
pygame.display.set_caption("Snake")               #Nastavení popisku
screen.fill(black)                                #Nastavení barvy pozadí okna 


# Vytvoření třídy hlavy hada:
class snake_head:
    def __init__(self):
        self.segment = ((400, 400)) # Nastavení segmentu hada
        self.segment_size = 20      # Nastavení velikosti segmentu
        self.direction = "RIGHT"    # Nastavení počáteččního směru
        
    def change_direction(self, keys):
        if keys[pygame.K_UP]:              # Jestliže je stisknutá šipka nahoru
            self.direction = "UP"          # Odkaz na snake_head move pro pohyb nahoru
        elif keys[pygame.K_DOWN]:
            self.direction = "DOWN"
        elif keys[pygame.K_LEFT]:
            self.direction = "LEFT"
        elif keys[pygame.K_RIGHT]:
            self.direction = "RIGHT"
    
    def move(self):
        head_x, head_y = self.segment        # Získání souřadnic hlavy
        self.old_segment = (head_x, head_y)  # Uložení staré pozice hlavy pro pohyb prvního segmentu
        
        if self.direction == "RIGHT":        # Jestliže směr je doprava  
            head_x += self.segment_size      # Pozice hlavy se posune o jeho velikost na x souřadnici do +, tedy doprava
            
        elif self.direction == "LEFT":
            head_x -= self.segment_size  
            
        elif self.direction == "UP":
            head_y -= self.segment_size   
            
        elif self.direction == "DOWN":
            head_y += self.segment_size  
            
        self.segment = (head_x, head_y)      # Aktualizace souřadnic hlavy hada          


# Vytvoření třídy segmentu hada:
class snake_body:
    def __init__(self):
        self.segments = []                   # Seznam segmentů
        self.segment_size = 20
        
    # Přidání dalšího segmentu:   
    def add_segment(self, x, y):
        self.segments.append((x, y))         # Vložení souřadnic segmentu do seznamu
        
    # Posun všech segmentů hada:        
    def move(self, head_x, head_y):
        
        if self.segments:                                     # Pokud existují segmenty těla hada
            for i in range(len(self.segments) - 1, 0, -1):     # Postupné procházení seznamu pozpátku
                if i > 0:                                     
                    self.segments[i] = self.segments[i - 1]   # Nastavení segmentu na pozici předešlého segmentu
            #print(self.segments)                             # Pro testování 
            self.segments[0] = (head_x, head_y)               # Posun 1. segmentu na pozici, kde byla dříve hlava


# Vytvoření třídy ovoce:
class snake_fruit:
    def __init__(self):
        fruit_positions = list(range(20, 781, 20))                                       # Vytvoření pozic pro ovoce        
        self.segment = (random.choice(fruit_positions), random.choice(fruit_positions))  # Nastavení souřadnic na náhodné pozice
        self.segment_size = 20                                                           # Nastavení velikosti ovoce

head= snake_head()             # Volání třídy snake_head
body = snake_body()            # Volání třídy snake_body
fruit = snake_fruit()          # Volání třídy snake_fruit

clock = pygame.time.Clock()    # Hodiny

paused = False                 # Definice proměnné paused
running = True
off = True 

# Hlavní herní cyklus:  
while True:
    body.segments = []         # Nastavení na 0 segmentů 
    head.segment = (400, 400)  # Nastavení hlavy na počáteční pozici 
    fruit = snake_fruit()      # Změnění pozice ovoce
    
        
    # Okno GAME OVER!: 
    if running == False:       # Pokud byl cyklus vypnut
        off = True          
        
        score = update_score("show_score")
        score_text, score_text_rect = text_create_score(score)     # Volání funkce pro skóre
        
        while off:
            for event in pygame.event.get():              # Pro každý zjištěný event
                if event.type == pygame.QUIT:             # Jestliže uživatel klikl na křížek
                    pygame.quit()                         # Ukončení programu
                elif event.type == pygame.KEYDOWN:        # Jestliže je stisknutá klávesa
                    if event.key == pygame.K_SPACE:       # Jestliže je stisknutá klávesa SPACE
                        off = False                     
            screen.fill(black)                            # Vyčištění okna
            screen.blit(game_over, game_over_rect)        # Zobrazení textu GAME OVER!
            screen.blit(space_text, space_text_rect)      # Zobrazení textu SPACE
            screen.blit(score_text, score_text_rect)      # Zobrazení textu SCORE
            pygame.display.update()                       # Obnova okna
            
        update_score("zero_score")                        # Nastavení skóre na nulu
    
    running=True               # Nastavení running na True - Obnovení cyklu
    while running:
        for event in pygame.event.get():                  # Pro každý zjištěný event
            if event.type == pygame.QUIT:                 # Jestliže uživatel klikl na křížek
                pygame.quit()                             # Ukončení programu   
            elif event.type == pygame.KEYDOWN:            # Jestliže je stisknutá klávesa
                keys = pygame.key.get_pressed()           # Vrátí seznam se všemi stisknutými klávesy
                if keys[pygame.K_p]:                      # Jestliže je stisklé p
                    paused = not paused                   # Obrátí hodnotu proměnné paused 
         
                                
        if paused == True:
            screen.fill(black)                            # Vyčištění okna
            screen.blit(paused_text, paused_text_rect)    # Zobrazení textu PAUSED      
                
        if  paused == False:
                                
            #Pohyb hada:  
            keys = pygame.key.get_pressed()               # Vrátí seznam se všemi stisknutými klávesy      
            head.change_direction(keys)                   # Volání funkce pro změnu směru
            head.move()                                   # Volání funkce pro pohyb hlavy hada
            old_head_x, old_head_y = head.old_segment     # Nastavení předešlých souřadnic hlavy
            body.move(old_head_x, old_head_y)             # Volání funkce pro pohyb těla hada

            screen.fill(black)                            # Smazání starých pozic segmentů
                
            # Přidávání nových segment:    
            if head.segment == fruit.segment:
                if head.direction == "RIGHT":                                               # Jestliže směr hlavy je do prava
                    body.add_segment(head.segment[0] - body.segment_size, head.segment[1])  # Přidá se segment na souřadnice vlevo od hlavy
                elif head.direction == "LEFT":
                    body.add_segment(head.segment[0] + body.segment_size, head.segment[1])
                elif head.direction == "UP":
                    body.add_segment(head.segment[0], head.segment[1] - body.segment_size)
                elif head.direction == "DOWN":
                    body.add_segment(head.segment[0], head.segment[1] + body.segment_size)
                    
                screen.fill(black)
                update_score("plus_score")
                #print(update_score("show_score"))                    # Testování
                
                # Spawn nového ovoce, tak aby se nespawnul na místě segmentech hada:
                fruit_generation = True                 
                while fruit_generation:
                    new_fruit = snake_fruit()                                     # Vytvoří novou pozici pro ovoce
                    if new_fruit != head.segment and new_fruit != body.segments:  # Jestliže vygenerované souřadnice pro ovoce nejsou na segmentech hada   
                        fruit = new_fruit                                         # Vygenerované ovoce bude mít souřadnice new_fruit
                        fruit_generation = False                                  # Přesrušení cyklu

                    else:                                                         # Jinak cyklus pokračuje
                        fruit_generation = True
                
            pygame.draw.rect(screen, (green), (head.segment[0], head.segment[1], head.segment_size, head.segment_size))   # Vykreslení hlavy hada
            pygame.draw.rect(screen, (red), (fruit.segment[0], fruit.segment[1], fruit.segment_size, fruit.segment_size)) # Vykreslení ovoce
                    
            # Zobrazení segmentů těla:  
            for segment in body.segments:          
                pygame.draw.rect(screen, (green), (segment[0], segment[1], body.segment_size, body.segment_size))

            # Detekce kolize se stěnami:
            if head.segment[0] > 780 or head.segment[1] > 780 or head.segment[0] < 20 or head.segment[1] < 20: # Jestliže se hlava dotkne stěny
                #print("kolize_stena")              # Pro testování
                running = False                     # Vypnutí cyklu
                    
            # Detekce kolize s tělem hada
            for segment in body.segments:           # Pro každdý segment těla
                if head.segment == segment:         # Jestliže se hlava dotkne segmentu těla
                    #print("kolize_telo")           # Pro testování
                    running = False                 # Vypnutí cyklu
                    
        clock.tick(7.5)           # Omezení na 7.5 snímku za sekundu
        pygame.display.update()   # Obnova okna
        
pygame.quit()                     # Konec knihovny pygame
          