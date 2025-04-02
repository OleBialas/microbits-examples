from microbit import *
import radio
import audio

radio.config(group=1)
radio.on()

emotion_counter = 0
message_out = ""

while True:
    message_in = radio.receive()
    if message_in == 'happy':
        display.show(Image.HAPPY)
        audio.play(Sound.HAPPY)
    elif message_in == 'sad':
        display.show(Image.SAD)
        audio.play(Sound.SAD)
    elif message_in == 'sleepy':
        display.show(Image.ASLEEP)
        audio.play(Sound.YAWN)
    
    if button_b.was_pressed():
        if emotion_counter == 4:
            emotion_counter = 0 # reset
        if emotion_counter == 0:
            display.show(Image.HAPPY)
            message_out="happy"
        elif emotion_counter == 1:
            display.show(Image.SAD)
            message_out="sad"
        elif emotion_counter == 2:
            display.show(Image.ASLEEP)
            message_out="sleepy"
        emotion_counter+=1
        
    if button_a.was_pressed():
        display.clear()
        radio.send(message_out)