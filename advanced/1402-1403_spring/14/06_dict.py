
class Dict(dict):

    def print(self):
        print(self)

    def pop(self, key):
        print("Hacked!")

# del dict.clear
# delattr(Dict, 'clear')


d = Dict({'a': 1})
d.pop('a')
d.print()
d.clear()
