import time
import threading
from tkinter import *

"""
------------------------
|  X  |     |     |     |
-------------------------      
|     |     |     |     |
-------------------------
|     |     |     |     |
-------------------------
|     |     |     |  X  |
-------------------------
"""
root = Tk()

total_score = 0
BACK_CONTENT = "A"
selected_card = []
show_card_stage = False

class Card(Button):
    CARDS = []

    def __init__(self, content, master=None, cnf={}, **kwargs):
        self.__content = content
        super().__init__(master, cnf, **kwargs)

        Card.CARDS.append(self)

    @property
    def content(self):
        return self.__content

    def front(self):
        self.configure(text=self.__content, state=DISABLED)

    def back(self):
        self.configure(text=BACK_CONTENT, state=NORMAL)

    @classmethod
    def get_cards(cls):
        return cls.CARDS


def to_back_all_cards():
    global selected_card, score_label, total_score, show_card_stage, back_card_thread
    while True:
        if show_card_stage:
            time.sleep(3)
            card: Card # type
            for card in Card.get_cards():
                card.back()

            show_card_stage = False

        if len(selected_card) == 2:
            first_card = selected_card[0]
            second_card = selected_card[1]

            if first_card.content != second_card.content:
                time.sleep(2)
                first_card.back()
                second_card.back()
            else:
                total_score += 1
                score_label.configure(text=str(total_score))
                if total_score == 8:
                    score_label.configure(text="You have won!")
                    time.sleep(5)
                    root.destroy()
                    break

            selected_card.clear()

    back_card_thread.join()

back_card_thread = threading.Thread(target=to_back_all_cards, name='back_card_thread')
back_card_thread.start()

def partial_command(card):
    def command():
        if len(selected_card) < 2:
            card.front()
            selected_card.append(card)

    return command


contents = [
    ["🍗", "🥩", "🥗", "🧀"],
    ["🌮", "🍨", "🍭", "🍹"],
    ["🍗", "🥩", "🥗", "🧀"],
    ["🌮", "🍨", "🍭", "🍹"]
]

score_label = Label(root, text=str(total_score), font=("B Nazanin", 20, "bold"))
score_label.grid(column=0, row=0, columnspan=4) 

for y, content in enumerate(contents):
    # content: []
    for x, c in enumerate(content):
        card = Card(
            content=c, 
            master=root, 
            text=BACK_CONTENT, 
            width=10, 
            height=5, 
            font=("B Nazanin", 10, "bold")
        )
        # card.configure(command=lambda : card.front())
        card.configure(command=partial_command(card))
        card.grid(column=x, row=y+1)


def show_cards():
    global start_button, show_card_stage
    card: Card # type
    for card in Card.get_cards():
        card.front()

    show_card_stage = True
    start_button.configure(state=DISABLED)

start_button = Button(
    root, 
    text="Start", 
    font=("B Nazanin", 20, "bold"),
    command=show_cards
)
start_button.grid(column=0, row=6, columnspan=4) 


# A Tkinter Button has three states : active, normal, disabled

# activebackground, activeforeground, anchor,
# background, bitmap, borderwidth, cursor,
# disabledforeground, font, foreground
# highlightbackground, highlightcolor,
# highlightthickness, image, justify,
# padx, pady, relief, repeatdelay,
# repeatinterval, takefocus, text,
# textvariable, underline, wraplength

# command, compound, default, height,
# overrelief, state, width
root.mainloop()