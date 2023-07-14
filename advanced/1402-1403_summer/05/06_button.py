
class Button:

    def __init__(self, id, text, callback):
        self.id = id
        self.text = text
        self.callback = callback

    def clicked(self):
        self.callback()


# def btn_callback():
    print("Boooooom ... !")

# create button
# btn1 = Button(id=1, text="danger!", callback=btn_callback)
# btn1.clicked()

# function builder
def callback(id, text):
    def wrapper():
        print(f"button {id} with {text} has been clicked!")

    return wrapper

buttons = []
for i in range(10):
    index = i + 1
    text = f"btn-{index}"
    # btn = Button(id=index, text=text, callback=callback(index, text))
    # res = callback(index, text)
    # res: None
    # btn = Button(id=index, text=text, callback=None)
    # -------------------
    # callback: function
    # callback: no params
    btn = Button(id=index, text=text, callback=callback(index, text))
    buttons.append(btn)


for btn in buttons:
    btn.clicked()

