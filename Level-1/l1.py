import pygame
pygame.init()
#screen=pygame.display.set_mode()
position=(5,5)
color=(255,255,255)
width,height=1200,600
canvas=pygame.display.set_mode((width,height))
font = pygame.font.Font(None, 36)

plate2=pygame.image.load(r'C:\Users\OMOMON073\Desktop\Sindhu DP\L1\plate2.png')
bread2=pygame.image.load(r'C:\Users\OMOMON073\Desktop\Sindhu DP\L1\breadsl.png')
lettuce2=pygame.image.load(r'C:\Users\OMOMON073\Desktop\Sindhu DP\L1\lettuce2.png')
cheese2=pygame.image.load(r'C:\Users\OMOMON073\Desktop\Sindhu DP\L1\Cheesesl.png')
tomatosl=pygame.image.load(r'C:\Users\OMOMON073\Desktop\Sindhu DP\L1\TS.png')
onionsl=pygame.image.load(r'C:\Users\OMOMON073\Desktop\Sindhu DP\L1\OS.png')
image1 = pygame.image.load(r'C:\Users\OMOMON073\Desktop\Sindhu DP\L1\bread.png')
b_rect=image1.get_rect()
image2 = pygame.image.load(r'C:\Users\OMOMON073\Desktop\Sindhu DP\L1\plate.png')
pl_rect=image2.get_rect()
image3=pygame.image.load(r'C:\Users\OMOMON073\Desktop\Sindhu DP\L1\Cheeseslice.jpg')
ch_rect=image3.get_rect()
image4=pygame.image.load(r'C:\Users\OMOMON073\Desktop\Sindhu DP\L1\lettuce.png')
lt_rect=image4.get_rect()
image5=pygame.image.load(r'C:\Users\OMOMON073\Desktop\Sindhu DP\L1\Onion slice.png')
sl_rect=image5.get_rect()
image6=pygame.image.load(r'C:\Users\OMOMON073\Desktop\Sindhu DP\L1\TomatoSlice.jpg')
ts_rect=image6.get_rect()

rows, cols = 3, 2
cell_width, cell_height = 120, 120
pygame.display.set_caption("Breakfast")

img=pygame.image.load(r'C:\Users\OMOMON073\Desktop\Sindhu DP\L1\kitchentable.png')

rect1=img.get_rect()
table_width,table_height=((rect1.width)/2,(rect1.height)/2)
print(table_width,table_height)
tabwidth=820
tabheight=10
exit=False
foreground_position = False
canvas.fill(color)
canvas.blit(img,dest=position)
   
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
            #if event.button==1:
                #foreground_position= not foreground_position
            if rect1.collidepoint(event.pos):
                print("Clicked!")
            elif b_rect.collidepoint(event.pos):
               
                canvas.blit(bread2, (355,173))
            elif pl_rect.collidepoint(event.pos):
                #if foreground_position:
                canvas.blit(plate2, (305,90))
            elif  ch_rect.collidepoint(event.pos):
                canvas.blit(cheese2, (380,160))
               
            elif  lt_rect.collidepoint(event.pos):
                #flag=0
                #if flag==0:
               # print("lettuce has been clicked")
                    canvas.blit(lettuce2, (380,190))
                   # flag=1
                #else:
                    #canvas.blit(lettuce2, (395,210))
                    
            elif  sl_rect.collidepoint(event.pos):
                #print("Onion  has been clicked")
                canvas.blit(onionsl, (395,170))
            elif  ts_rect.collidepoint(event.pos):
                #print("Tomato has been clicked")
                canvas.blit(tomatosl,(380,160))

    pygame.display.update()
pygame.display.flip()
pygame.quit()