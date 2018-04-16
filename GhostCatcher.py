from gamelib import *

game = Game(900,600, "Ghost Catcher")

#Graphics Variables
bk = Image("cartoongraveyard.jpg", game)
bk.resizeTo(900,600)
game.setBackground(bk)
bkt = Image("Capture 77.png",game)
bkt.resizeTo(900,600)
bke = Image("larry dies end game.png",game)
bke.resizeTo(900,600)
play = Image("play button.jpg",game)
play.resizeBy(-40)
play.y -= 10
#bk.draw()
larry =  Image("larry(2).gif", game)
larry.resizeBy(-65)
larry.x -= 385
larry.y -= 15
larry.draw()
ghost1 = Image("ghost1.png",game)
ghost1.resizeBy(-40)
ghost1.x += 385
ghost1.y += 15
ghost2 = Image("ghostheh.png",game)
ghost2.x += 385
ghost2.y += 15
ghost2.resizeBy(-85)
soul = Image("soul.png", game)
soul.visible = False
#soul.x = larry.x
#soul.y = larry.y+50

spook = Sound("GHOST8B.wav",1)
collect = Sound("collect.wav",2)
hit = Sound("hit.wav",3)



souls = []
for index in range(8):
    souls.append( Image( "soul.png", game ) )
#Title Screen
game.over = False
while not game.over:
    game.processInput()
    bkt.draw()
    play.draw()

    if play.collidedWith(mouse) and mouse.LeftClick:
        game.over = True
    game.update(30)
    
    
    
#Level 1
game.over = False
ghost1spassed = 0
while not game.over:
    game.processInput()
    #game.clearBackground()
    bk.draw()
    larry.draw()
    soul.move()
    ghost1.draw()
    #ghost2.draw()

    for index in range(8):
        x = randint(60,870)
        y = randint(400,580)
        souls[1].moveTo(70,580)
        souls[2].moveTo(160,450)
        souls[3].moveTo(260,550)
        souls[4].moveTo(300,450)
        souls[5].moveTo(380,400)
        souls[6].moveTo(470,500)
        souls[7].moveTo(870,500)
        if larry.collidedWith(souls[index]):
            souls[index].visible = False
            larry.health += 5
            collect.play()

    ghost1.forward(6)
    ghost1.move()

    if ghost1.x>20 and ghost1.y>25:
        #a = ghost1.angleTo(larry)
        ghost1.setSpeed(6,90)
        ghost1.draw()
        #ghost1.rotateTo(a)

    #ghost2.forward(6)
    ghost2.visible = False
    #ghost2.moveTo(870,400)
    

    #a = ghost2.angleTo(larry)
    #ghost2.rotateTo(a-90)
    #ghost2.moveTowards(larry,6)

    
        
        
        
    if ghost1.isOffScreen ("left") or soul.collidedWith(ghost1):
        ghost1.visible = False
        ghost1.setSpeed(0,0)
        ghost2.visible = True
        
        
        ghost2.setSpeed(6,90)
        ghost2.speed += 1
        #ghost2.draw()
        ghost2.move()

        
   
    if keys.Pressed[K_UP]:
        larry.y -= 6
    if keys.Pressed[K_DOWN]:
        larry.y += 6
    if keys.Pressed[K_RIGHT]:
        larry.x += 6
    if keys.Pressed[K_LEFT]:
        larry.x -= 6

    if keys.Pressed[K_SPACE]:
        soul.moveTo(larry.x,larry.y+50)
        soul.setSpeed(24,-90)
        soul.visible = True

    if soul.collidedWith(ghost1):
        ghost1.health -= 100
        #ghost1.visible = False
        soul.visible = False
        game.score += 1
        hit.play()

    if larry.collidedWith(ghost1):
        larry.health -= 1
        spook.play()

    if ghost2.isOffScreen("left") or ghost2.collidedWith(soul):
        y = randint(100,500)
        ghost2.moveTo(game.width, y)
        ghost2.setSpeed(6,90)
        ghost2.speed += 1

        
        
        ghost2.visible = True
        game.score += 1

    if ghost2.collidedWith(larry):
        larry.health -= 1


    

    if ghost1.health <1:
        ghost1.visible = False
        game.over = True

    if larry.health <1:
        game.over = True



    game.drawText("Health: " + str(larry.health),800,10)
    game.drawText("Ghosts Killed/Passed: " + str(game.score), 20, 40)
    game.update(60)

#End Screen
#game.over = False
#while not game.over:
game.processInput()
bke.draw()
game.drawText("Press [ESC] to Quit",305,400)
game.update(30)
game.wait(K_ESCAPE)
game.quit()
    
