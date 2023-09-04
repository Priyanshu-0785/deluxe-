def on_player2_button_a_pressed():
    pass
controller.player2.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player2_button_a_pressed)

def on_update_interval():
    pass
game.on_update_interval(500, on_update_interval)
