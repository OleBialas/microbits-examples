from microbit import *
import audio
import speech

love_timer = 0
hunger_timer = 0

display.show(Image(
    "00000:"
    "09090:"
    "00000:"
    "09990:"
    "00000"))

audio.play(Sound.HELLO)

while True:
    if pin_logo.is_touched():
        love_timer = 0
        display.show(Image.HAPPY)
        audio.play(Sound.HAPPY)
    elif accelerometer.was_gesture('shake'):
        love_timer = 0
        display.show(Image.SURPRISED)
        audio.play(Sound.GIGGLE)
    elif button_b.was_pressed():
        hunger_timer = 0
        display.show(Image.HAPPY)
        speech.say("OM - NOM - NOM")

    else:
        sleep(500)
        love_timer += 0.5
        hunger_timer += 0.5

    if hunger_timer == 10:
        display.show(Image.ANGRY)
        speech.say('I. Am. Hungry.')
    elif hunger_timer == 30:
        display.show(Image.SKULL)
        audio.play(Sound.MYSTERIOUS)
        break

    if love_timer == 20:
        display.show(Image.SAD)
        audio.play(Sound.SAD)
    elif love_timer == 30:
        display.show(Image.ASLEEP)
        audio.play(Sound.YAWN)
    elif love_timer == 40:
        display.show(Image.SKULL)
        audio.play(Sound.MYSTERIOUS)
        break