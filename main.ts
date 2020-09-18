input.onButtonPressed(Button.A, function () {
    if (Number2 == 1) {
        basic.showNumber(Number1)
        Number1 += 1
    }
    if (Number2 == 2) {
        basic.showNumber(Number22)
        Number22 += 1
    }
})
input.onButtonPressed(Button.AB, function () {
    Number2 = 2
})
input.onButtonPressed(Button.B, function () {
    if (Number2 == 1) {
        basic.showNumber(Number1)
        Number1 += -1
    }
    if (Number2 == 2) {
        basic.showNumber(Number22)
        Number22 += -1
    }
})
let Number2 = 0
let Number1 = 0
let Number22 = 0
Number22 = 0
Number1 = 0
Number2 = 1
basic.forever(function () {
	
})
