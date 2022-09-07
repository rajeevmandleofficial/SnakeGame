import turtle
import time
import random
import winsound

#Creating delay variable
delay=0.1

#Creating variable for score and highscore
score=0
total_score=0

#Creating life variable
life=5

#Creating level variable
level=1

#setup screen
wn=turtle.Screen()
wn.title('Snake & The Apple by ASR')
wn.bgpic('Bg1x.gif')
wn.setup(600,600)
wn.tracer(0)

#Creating snake head
head=turtle.Turtle()
head.speed(0)
head.penup()
head.color('black')
head.shape('square')
head.goto(0,0)
head.direction='stop'

segments=[]                                #Taking list to add segments to form snake body 

#Creating food of snake
food=turtle.Turtle()
food.speed(0)
food.penup()
food.color('red')
food.shape('circle')
food.goto(0,180)

#Creating turtle for score & life
pen=turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write('Score : {}    Totalscore : {}    Life : {} '.format(score,total_score,life),False,align='center',font=('Arial',20,'bold'))

#Creating turtle for level
lev=turtle.Turtle()
lev.speed(0)
lev.color('white')
lev.penup()
lev.goto(0,-290)
lev.hideturtle()
lev.write('Level : {}'.format(level),False,align='center',font=('Arial',22,'bold'))


#Function for playing sound
def play_sfx(x):
    winsound.PlaySound(x, winsound.SND_ASYNC)

#Moving snake
def go_up():
    if head.direction!='down':
        head.direction='up'

def go_down():
    if head.direction!='up':
        head.direction='down'

def go_left():
    if head.direction!='right':
        head.direction='left'    

def go_right():
    if head.direction!='left':
        head.direction='right'

def move():
    if head.direction=='up':
        y=head.ycor()
        head.sety(y+20)

    if head.direction=='down':
        y=head.ycor()
        head.sety(y-20)

    if head.direction=='left':
        x=head.xcor()
        head.setx(x-20)

    if head.direction=='right':
        x=head.xcor()
        head.setx(x+20)

#Making function to bring snake at x=0,y=0(origin)
def reset_snake():
    time.sleep(1)
    head.goto(0,0)
    head.direction='stop'

    #Hiding the segments at collision
    for i in segments:
        i.goto(1000,1000)
        i.hideturtle()

    #Removing the segments from the list
    segments.clear()

    #Reset score
    score=0
    pen.clear()
    pen.write('Score : {}    Totalscore : {}    Life : {} '.format(score,total_score,life),False,align='center',font=('Arial',20,'bold'))        

#Creating function to add bonus score after completing the level
def bonus_score():
    global total_score
    total_score+=5
    pen.clear()
    pen.write('Score : {}    Totalscore : {}    Life : {} '.format(score,total_score,life),False,align='center',font=('Arial',20,'bold'))

turtle.listen()
turtle.onkeypress(go_up,'Up')
turtle.onkeypress(go_down,'Down')
turtle.onkeypress(go_left,'Left')
turtle.onkeypress(go_right,'Right')

play_sfx('startbg1.wav')
        

#Main game loop
while True:
    wn.update()

    #Creating levels for game
    if total_score==30:
        level=2
        lev.clear()
        lev.write('Level : {}'.format(level),False,align='center',font=('Arial',22,'bold'))
        wn.bgpic('Bg2x.gif')
        reset_snake()

        #Adding bonus for completing the level in total_score
        bonus_score()

    if total_score==60:
        level=3
        lev.clear()
        lev.write('Level : {}'.format(level),False,align='center',font=('Arial',22,'bold'))
        wn.bgpic('Bg3x.gif')
        reset_snake()

        #Adding bonus for completing the level in total_score
        bonus_score()

    if total_score==90:
        level=4
        lev.clear()
        lev.write('Level : {}'.format(level),False,align='center',font=('Arial',22,'bold'))
        wn.bgpic('Bg4x.gif')
        reset_snake()

        #Adding bonus for completing the level in total_score
        bonus_score()

    if total_score==120:
        level=5
        lev.clear()
        lev.write('Level : {}'.format(level),False,align='center',font=('Arial',22,'bold'))
        wn.bgpic('Bg5x.gif')
        reset_snake()

        #Adding bonus for completing the level in total_score
        bonus_score()

    if total_score==150:
        level=6
        lev.clear()
        lev.write('Level : {}'.format(level),False,align='center',font=('Arial',22,'bold'))
        wn.bgpic('Bg6x.gif')
        reset_snake()

        #Adding bonus for completing the level in total_score
        bonus_score()
        

    if total_score==180:
        level=7
        lev.clear()
        lev.write('Level : {}'.format(level),False,align='center',font=('Arial',22,'bold'))
        wn.bgpic('Bg7x.gif')
        reset_snake()

        #Adding bonus for completing the level in total_score
        bonus_score()

    if total_score==210:
        level=8
        lev.clear()
        lev.write('Level : {}'.format(level),False,align='center',font=('Arial',22,'bold'))
        wn.bgpic('Bg8x.gif')
        reset_snake()

       #Adding bonus for completing the level in total_score
        bonus_score()


    if total_score==240:
        level=9
        lev.clear()
        lev.write('Level : {}'.format(level),False,align='center',font=('Arial',22,'bold'))
        wn.bgpic('Bg9x.gif')
        reset_snake()

       #Adding bonus for completing the level in total_score
        bonus_score()

    if total_score==270:
        level=10
        lev.clear()
        lev.write('Level : {}'.format(level),False,align='center',font=('Arial',22,'bold'))
        wn.bgpic('Bg10x.gif')
        reset_snake()

       #Adding bonus for completing the level in total_score
        bonus_score()

    #Closing game when life becomes zero
    if life==0:
        play_sfx('endbg.wav')
        print("+_+_+_+ GAME OVER +_+_+_+")
        print()
        print("****BETTER LUCK NEXT TIME****")
        break

    #Checking for collision between boundary and snake
    if head.xcor()>240 or head.xcor()<-240 or head.ycor()>240 or head.ycor()<-240:
        play_sfx('borderhit.wav')
        time.sleep(1)
        head.goto(0,0)
        head.direction='stop'

        #Hiding the segments at collision
        for i in segments:
            i.goto(1000,1000)
            i.hideturtle()

        #Removing the segments from the list
        segments.clear()

        #Reset score at collision
        score=0

        #Reset life
        life-=1

        pen.clear()
        pen.write('Score : {}    Totalscore : {}    Life : {} '.format(score,total_score,life),False,align='center',font=('Arial',20,'bold'))


        #Reset delay
        delay=0.1
        
    #Checking for collision between snake head and it's segments
    for i in segments:
        if head.distance(i)<20:
            play_sfx('bodyhit.wav')
            time.sleep(1)
            head.goto(0,0)
            head.direction='stop'

             #Hiding the segments at collision
            for i in segments:
                i.goto(1000,1000)
                i.hideturtle()

             #Removing the segments from the list
            segments.clear()

             #Reset score at collision
            score=0

             #Reset life
            life-=1

            pen.clear()
            pen.write('Score : {}    Totalscore : {}    Life : {} '.format(score,total_score,life),False,align='center',font=('Arial',20,'bold'))

            #Reset delay
            delay=0.1
             
    #Check for collision of snake and food
    if head.distance(food)<20:
        x=random.randint(-240,240)
        y=random.randint(-240,240)
        food.goto(x,y)

        play_sfx('appleeat.wav')

        #Appending new segment in the list at collision with food
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.color('grey')
        new_segment.shape('square')
        new_segment.penup()
        segments.append(new_segment)

        #Increasing score on collision
        score+=5

        if score>total_score:
            total_score=score
        pen.clear()
        pen.write('Score : {}    Totalscore : {}    Life : {} '.format(score,total_score,life),False,align='center',font=('Arial',20,'bold'))

        #Reducing delay to increase speed                                                       # To make the game more challenging we are increasing
                                                                                                                      # the speed when the snake's head collides with the 
                                                                                                                      # food by reducing the delay(variable)
        delay-=0.003                                                                                                   

    #Moving segments in reverse order
    for index in range(len(segments) -1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)

    #Adding first segment of the list to snake head
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)

    move()    
     
        

    #Controlling turtle movement
    time.sleep(delay)
    
turtle.bye()









    
    
