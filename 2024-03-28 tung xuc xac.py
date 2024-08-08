import keyboard
import random

def tung_xuc_sac():
    return random.randint(1, 6)

def xu_ly_sukien(event):
    if event.name == 'space':
        so = tung_xuc_sac()
        print(f"Số trên xúc sắc: {so}")

keyboard.on_press(xu_ly_sukien)    
keyboard.wait('esc')