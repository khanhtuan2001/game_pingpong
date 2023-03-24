import pygame 
import sys,random


game_over = False
class animation():
 def ball_animation():
    global ball_speed_x,ball_speed_y,player_score,opponent_score,game_over
    ball.x += ball_speed_x
    ball.y += ball_speed_y 

    if ball.top <= 0 or ball.bottom >= screen_height:
         pygame.mixer.Sound.play(plob_sound)
         ball_speed_y *= -1
    #player score     
    if ball.left <=0 : 
         ball_restart.restart()
         player_score += 1
    #opponent score     
    if  ball.right >= screen_width:
        ball_restart.restart()
        opponent_score += 1    
 
    if ball.colliderect(player) or ball.colliderect(opponent):
         pygame.mixer.Sound.play(plob_sound)
         ball_speed_x *= -1 
    

        

 def player_animation():
     player.y += player_speed
     if player.top <= 0: 
         player.top =0
     if player.bottom >= screen_height:
          player.bottom =screen_height 
 def opponent_ai():
    if opponent.top <= ball.y:
         opponent.top += opponent_speed
    if opponent.top >= ball.y:
         opponent.bottom -= opponent_speed    
    if opponent.top <= 0: 
         opponent.top = 0
    if opponent.bottom >= screen_height:
          opponent.bottom =screen_height  
class ball_restart():           
 def restart():
    global ball_speed_x,ball_speed_y
    ball.center = (screen_width/2,screen_height/2)
    ball_speed_y *= random.choice((1,-1))
    ball_speed_x *= random.choice((1,-1))

# Running test window

class start():
 def __init__(self):
     self.state = 'intro'   
 def intro(self):
     global player_speed
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             pygame.quit()
             
             sys.exit()
         if event.type == pygame.MOUSEBUTTONDOWN:
             self.state = 'main_game'
         
     
     screen.fill(bg_color)
     screen.blit(start_text,(screen_width/2 -140,screen_height/2-100))
     pygame.display.flip()

 def  main_game(self):
     global player_speed
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
                  pygame.quit()
                  sys.exit()
                 
         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_DOWN:
                 player_speed += 7
             if event.key == pygame.K_UP:
                 player_speed -=7  
             if event.key == pygame.K_SPACE:
                 sys.exit()            
         if event.type == pygame.KEYUP:
             if event.key == pygame.K_DOWN:
                 player_speed -= 7
             if event.key == pygame.K_UP:
                 player_speed +=7   
         #if game_over == True:
          #   self.state ='end'      
     animation.ball_animation()  
     animation.player_animation()
     animation.opponent_ai()
     
     
     screen.fill(light_grey)
     pygame.draw.rect(screen,playercolor,player)
     pygame.draw.rect(screen,opponentcolor,opponent)
     pygame.draw.ellipse(screen,ballcolor,ball)
     pygame.draw.aaline(screen,ballcolor,(screen_width/2,0),(screen_width/2,screen_height))
     
     
     #hien thi diem
     player_text = basic_font.render(f'player: {player_score}',False,linecolor)
     screen.blit(player_text,(screen_width/2 + 20,screen_height - 680))
     
     opponent_text = basic_font.render(f'computer : {opponent_score}',False,linecolor)
     screen.blit(opponent_text,(screen_width/2 - 220,screen_height -680))
     
     exit_text = basic_font.render(f'Press space to exit ',False,linecolor)
     screen.blit(exit_text ,(10,screen_height -680))
     pygame.display.flip()

 
              
 def start_manager(self):
     if self.state == 'intro':
         self.intro()
     if self.state == 'main_game':
         self.main_game()
    

pygame.mixer.pre_init(44100,-16,1, 1024)    
pygame.init()
clock = pygame.time.Clock()
gamestart = start()

#khai bao
screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('ping pong')


ball = pygame.Rect(screen_width/2 - 15,screen_height/2 -15 ,20,20)
player = pygame.Rect(screen_width -10,screen_height/2 -70,10,140)
opponent = pygame.Rect(0,screen_height/2-70,10,140)

#color
bg_color = (198,226,255)
light_grey = (46, 139, 87)
linecolor =(255 ,204, 153)
playercolor = (30, 144, 255)
opponentcolor =(223,53,	57)
ballcolor=(255 ,255 ,255)



#speed
ball_speed_x = 6 *1.3* random.choice((1,-1))
ball_speed_y = 6 *1.3* random.choice((1,-1))
player_speed = 0
opponent_speed = 8
# Score Text
player_score = 0
opponent_score = 0
basic_font = pygame.font.Font('freesansbold.ttf', 32)
#sound
plob_sound = pygame.mixer.Sound("pong.ogg")

start_text = pygame.image.load("start_btn.png")

while True:
     gamestart.start_manager()
     clock.tick(60)
     
