def on_received_number(receivedNumber):
    if receivedNumber == 5:
        music.play_melody("C5 A B G A F G E ", 110)
    elif receivedNumber == 7:
        basic.show_icon(IconNames.SILLY)
    else:
        music.play_melody("G F G A - F E D ", 120)
radio.on_received_number(on_received_number)

def on_logo_released():
    radio.send_number(6)
input.on_logo_event(TouchButtonEvent.RELEASED, on_logo_released)

def on_forever():
    radio.set_group(1)
basic.forever(on_forever)
