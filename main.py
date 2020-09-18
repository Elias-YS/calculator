def on_button_pressed_a():
    global Number1
    if Number2 == 1:
        basic.show_number(Number1)
        Number1 += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global Number2
    Number2 = 2
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global Number1
    if Number2 == 1:
        basic.show_number(Number1)
        Number1 += -1
    if Number2 == 2:
        basic.show_number(Number1)
        Number1 += -1
input.on_button_pressed(Button.B, on_button_pressed_b)

Number2 = 0
Number1 = 0
Number22 = 0
Number1 = 0
Number2 = 1

def on_forever():
    pass
basic.forever(on_forever)


