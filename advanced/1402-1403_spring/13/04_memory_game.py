import time
import threading
import queue
from tkinter import *
from random import shuffle
from functools import partial
from PIL import Image, ImageTk

root = Tk()

# options = {
#    'command': lambda :print("hello"),
#    'borderwidth': 2
# }
# Button(root, cnf=options)
# Button(root, command=lambda: print("Bye"), borderwidth=2)

IMAGE_WIDTH = 100
IMAGE_HEIGHT = 100
DEFAULT_CARD_IMG = ".\\images\\card.png"

fruits = [
    "cherry", "cherry", "apple", "apple",
    "grape","grape", "watermelon", "watermelon", 
    "pomegranate", "pomegranate", "orange", "orange",
    "banana", "banana", "lemon", "lemon"
]
shuffle(fruits)
selected_card_queue = queue.Queue()  

img = Image.open(DEFAULT_CARD_IMG)
resized_img = img.resize((IMAGE_WIDTH, IMAGE_HEIGHT))
default_image = ImageTk.PhotoImage(resized_img)

class Card(Button):

   MATCHED_CARDS = 0

   def __init__(self, name=None, master=None, cnf={}, **kw):
      self.name = name

      backimg = Image.open(f".\\images\\{name}.png")
      resized_backimg = backimg.resize((IMAGE_WIDTH, IMAGE_HEIGHT))
      back_image = ImageTk.PhotoImage(resized_backimg)

      self.back_image = back_image

      cnf.update(image=default_image)
      cnf.update(command=partial(on_command, self))

      super().__init__(master, cnf, **kw)

   def back(self):
      self.configure(image=self.back_image) 

   def front(self):
      self.configure(image=default_image) 

   # def __eq__(self, card):
   #    if isinstance(card, Card):
   #       return self.name == card.name
      
   #    return ValueError(f"can't compare card instance with {type(card)}")
   def __eq__(self, card):
      return not self.__ne__(card)

   def __ne__(self, card): # instance1 != instance2 
      # instance1.__ne__(instance2)
      if isinstance(card, Card):
         return self.name != card.name
      
      return ValueError(f"can't compare card instance with {type(card)}")

def compare():
      
   while True:
      if selected_card_queue.qsize() > 1:
         time.sleep(0.5)
         card1 = selected_card_queue.get(block=False)
         card2 = selected_card_queue.get(block=False)

         if card1 != card2:
            card1.front()
            card2.front()
         else:
            Card.MATCHED_CARDS += 2
            if Card.MATCHED_CARDS == 16:
               global thread
               thread.join()
               time.sleep(1)
               root.destroy()


thread = threading.Thread(target=compare)
thread.start()


def on_command(card: Card):
   if selected_card_queue.qsize() < 2: 
      card.back()
      selected_card_queue.put(card)


for y in range(4):
    for x in range(4):
         card = Card(name=fruits[y*4+x], master=root,relief=SUNKEN, width=IMAGE_HEIGHT, height=IMAGE_HEIGHT)
         card.grid(row=y, column=x)


root.mainloop()

