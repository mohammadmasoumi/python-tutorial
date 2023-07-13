# Load bar or Progress bar
import time
# "█"

"████████"

print(ord("█"))
print(chr(9608))

# "Hello\rBye"
# # Byelo

for i in range(100):  # i: 0 ... 99
    # █ i=0
    # ██ i=1
    # ███ t=3

    # \r█\r██\r███\r████
    # ████
    # print("\r"+"█"*(i+1), end="")
    print("\r"+"🚚"*(i+1), end="")
    time.sleep(0.5)
