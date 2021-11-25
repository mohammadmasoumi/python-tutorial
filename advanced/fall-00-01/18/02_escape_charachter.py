import time

for idx in range(10):
    time.sleep(0.2)
    print(f"\r{idx}", end="")
