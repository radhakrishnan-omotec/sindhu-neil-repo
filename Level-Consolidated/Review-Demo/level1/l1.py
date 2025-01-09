import pygame
pygame.init()
#screen=pygame.display.set_mode()
position=(5,5)
color=(255,255,255)
width,height=1200,600
canvas=pygame.display.set_mode((width,height))
font = pygame.font.Font(None, 36)
for_msg= (150,150, 150)
plate2=pygame.image.load('level1/Images/plate2.png')
bread2=pygame.image.load('level1/Images/breadsl.png')
lettuce2=pygame.image.load('level1/Images/lettuce2.png')
cheese2=pygame.image.load('level1/Images/Cheesesl.png')
tomatosl=pygame.image.load('level1/Images/TS.png')
onionsl=pygame.image.load('level1/Images/OS.png')
image1 = pygame.image.load('level1/Images/bread.png')
b_rect=image1.get_rect()
image2 = pygame.image.load('level1/Images/plate.png')
pl_rect=image2.get_rect()
image3=pygame.image.load('level1/Images/Cheeseslice.jpg')
ch_rect=image3.get_rect()
image4=pygame.image.load('level1/Images/lettuce.png')
lt_rect=image4.get_rect()
image5=pygame.image.load('level1/Images/Onion slice.png')
sl_rect=image5.get_rect()
image6=pygame.image.load('level1/Images/TomatoSlice.jpg')
ts_rect=image6.get_rect()

rows, cols = 3, 2
cell_width, cell_height = 120, 120

pygame.display.set_caption("Breakfast")

img=pygame.image.load('level1/Images/kitchentable.png')

rect1=img.get_rect()
table_width,table_height=((rect1.width)/2,(rect1.height)/2)
print(table_width,table_height)
tabwidth=820
tabheight=10
exit=False
foreground_position = False
canvas.fill(color)
canvas.blit(img,dest=position)
message = ""  
font = pygame.font.SysFont("Arial", 24)
def draw_message(message_text):
    canvas.fill((255,255 , 255), (0, height - 50, width, 50))
    text = font.render(message_text, True, for_msg)
    message_area=canvas.blit(text, (width // 2 - text.get_width() // 2, height - 50))
    canvas.blit(text,message_area)
    

   
br_fl=0
ch_fl=0
ts_fl=0
os_fl=0
lt_fl=0
br_cntr=0
pl_fl=0
    #def draw_table(tablearea,)
for row in range(rows):
    for col in range(cols):
        x = col * cell_width+tabwidth
        y = row * cell_height+tabheight
        if row == 0 and col == 0:
            canvas.blit(image1,(x,y) )   
            b_rect.topleft=(x,y)
        elif row == 0 and col == 1:
            canvas.blit(image2, (x, y))
            pl_rect.topleft=(x,y)
        elif row==1 and col==0:
            canvas.blit(image3,(x,y))
            ch_rect.topleft=(x,y)
        elif row==1 and col==1:
            canvas.blit(image4,(x,y))
            lt_rect.topleft=(x,y)
        elif row==2 and col==0:
            canvas.blit(image5,(x,y))
            sl_rect.topleft=(x,y)
        elif row==2 and col==1:
            canvas.blit(image6,(x,y))
            ts_rect.topleft=(x,y)
           
while not exit:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
                exit=True
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if rect1.collidepoint(event.pos):
                print("Clicked!")
            elif pl_rect.collidepoint(event.pos):
                canvas.blit(plate2, (305,90))
                pl_fl=1
            elif b_rect.collidepoint(event.pos):
                if pl_fl==1 and br_cntr!=2:
                    canvas.blit(bread2, (355,173))
                    br_fl=1
                    br_cntr+=1
                else:
                   message=f"Plate has to be taken first"
            elif  ch_rect.collidepoint(event.pos):
                if br_fl==1:
                    canvas.blit(cheese2, (380,160))
                    ch_fl=1
                else:
                    message=f"Bread has to selected"
            elif  lt_rect.collidepoint(event.pos):
                if br_fl==1:
                    canvas.blit(lettuce2, (380,190))
                    lt_fl=1
                else:
                    message=f"Bread has to selected"
            elif  sl_rect.collidepoint(event.pos):
                if br_fl==1:
                    canvas.blit(onionsl, (395,170))
                    os_fl=1
                else:
                    message=f"Bread has to selected"
            elif  ts_rect.collidepoint(event.pos):
                if br_fl==1:
                    canvas.blit(tomatosl,(380,160))
                    ts_fl_fl=1
                else:
                    message=f"Bread has to selected"
            #if br_cntr!=2:
             #   print("it would be nice if bread is placed on top and at last too!")
            if br_cntr==2 and (ch_fl==1 or ts_fl==1 or os_fl==1 or lt_fl==1):
                message=f"Sandwich is ready!!"
    draw_message(message)
    pygame.display.update()
pygame.display.flip()
pygame.quit()