import keyboard

text = keyboard.record(until='esc')

for item in text:
    print(item)