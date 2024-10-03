#Crea un software che stampi il nome del tasto cliccato su tastiera (solo lettere)
from pynput import keyboard

def key_on_press(key):
    try:
        if key.char.isalpha():
            print(f"tasto premuto: {key.char}")
    except:
        # Ignora i tasti speciali (come Shift, Ctrl, etc.)
        pass

def key_stop(key):
    if key == keyboard.Key.esc:
        return False
with keyboard.Listener(on_press = key_on_press, on_release=key_stop) as listener:
    listener.join()



