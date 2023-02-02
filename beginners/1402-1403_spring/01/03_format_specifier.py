# return carriage
import time

print("Hell\rworld")
print("Hello\rworld")
print("Helloooo\rworld")

# Helloooo
# world
# worldooo

for i in range(50):
    time.sleep(0.1)
    print("\r" + "█" * (i * 10), end="")

# \r█
# \r██
# \r███
# \r████