radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 5) {
        music.playMelody("C5 A B G A F G E ", 110)
    } else if (receivedNumber == 7) {
        basic.showIcon(IconNames.Silly)
    } else {
        music.playMelody("G F G A - F E D ", 120)
    }
})
input.onLogoEvent(TouchButtonEvent.Released, function () {
    radio.sendNumber(6)
})
basic.forever(function () {
    radio.setGroup(1)
})
