from pygame import *
from soundButtons import *
from characters import *
init()
mixer.init()

width = 900
height = 720
screen = display.set_mode((width,height))
#Characters
FloChar = Characters('Flo', 75, 600, 'chars/floChar.png','chars/Flo.png')
TimChar = Characters('Tim', 200, 600, 'chars/Tim.png','chars/TimChar.png')
HaineChar = Characters('Haine', 325, 600, 'chars/Haine.png','chars/HaineChar.png')
JennyChar = Characters('Jenny', 450, 600, 'chars/Jenny.png','chars/JennyChar.png')
HannahChar = Characters('Hannah', 575, 600, 'chars/Hannah.png','chars/HannahChar.png')


#Buttons
Button1 = SoundButton('Rain','sounds/soft-rain-ambient.mp3',(255,0,0), 20,20,True)
Button2 = SoundButton('BG_Cello','sounds/emotional-cello.mp3',(255,0,0), 140,20,True)
Button3 = SoundButton('BG_Moody','sounds/fatigue-moody-ambient.mp3',(255,0,0), 260,20,True)
Button4 = SoundButton('Horror_1','sounds/horror_atmosphere_1.mp3',(255,0,0), 380,20,True)
Button5 = SoundButton('Horror_2','sounds/horror_atmosphere_2.mp3',(255,0,0), 20,140,True)
Button6 = SoundButton('Horror_3','sounds/horror_atmosphere_3.mp3',(255,0,0), 140,140,True)
Button7 = SoundButton('BG_Piano','sounds/horror-spooky-piano.mp3',(255,0,0), 260,140,True)
Button8 = SoundButton('Horror_Tension','sounds/tense-horror-background.mp3',(255,0,0), 380,140,True)
#Game
program_running = True
while program_running:
    # event loop
    for e in event.get():
        if e.type == QUIT:
            program_running = False
        if e.type == MOUSEBUTTONDOWN:
            pos = mouse.get_pos()
            Button1.CheckClick(pos)
            Button2.CheckClick(pos)
            Button3.CheckClick(pos)
            Button4.CheckClick(pos)
            Button5.CheckClick(pos)
            Button6.CheckClick(pos)
            Button7.CheckClick(pos)
            Button8.CheckClick(pos)

    posit = mouse.get_pos()
    FloChar.CheckMouse(posit)
    HaineChar.CheckMouse(posit)
    TimChar.CheckMouse(posit)
    JennyChar.CheckMouse(posit)
    HannahChar.CheckMouse(posit)



    screen.fill((0,0,0))
    FloChar.ShowIcon(screen)
    HaineChar.ShowIcon(screen)
    TimChar.ShowIcon(screen)
    JennyChar.ShowIcon(screen)
    HannahChar.ShowIcon(screen)

    Button1.ButtonDrawn(screen)
    Button2.ButtonDrawn(screen)
    Button3.ButtonDrawn(screen)
    Button4.ButtonDrawn(screen)
    Button5.ButtonDrawn(screen)
    Button6.ButtonDrawn(screen)
    Button7.ButtonDrawn(screen)
    Button8.ButtonDrawn(screen)
    FloChar.TableDrawn(screen)
    HaineChar.TableDrawn(screen)
    TimChar.TableDrawn(screen)
    JennyChar.TableDrawn(screen)
    HannahChar.TableDrawn(screen)


    display.flip()