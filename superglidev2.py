from pynput import keyboard, mouse
import time as t
import threading

# Global variables
space_pressed = False

# Callback for key press event
def on_press(key):
    global space_pressed



# Callback for key release event
def on_release(key):
    global space_pressed
    if key == keyboard.Key.space:
        space_pressed = True

# Callback for scroll event
def on_scroll(x, y, dx, dy):
    global space_pressed
    if space_pressed and dy < 0:
        keyboard.Controller().press(' ')
        keyboard.Controller().release(' ')
        t.sleep(0.004)
        keyboard.Controller().press('c')
        keyboard.Controller().release('c')

        threading.Timer(1, reset_space_pressed).start()


def reset_space_pressed():
    global space_pressed
    space_pressed = False

# Set up listeners
key_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
key_listener.start()

mouse_listener = mouse.Listener(on_scroll=on_scroll)
mouse_listener.start()

print("Superglide script started")

# Keep the script running
key_listener.join()
mouse_listener.join()
