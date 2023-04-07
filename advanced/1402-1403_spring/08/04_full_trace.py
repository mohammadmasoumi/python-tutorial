import traceback
import sys

try:
    raise OSError()
except Exception:
    with open("file.txt", "w") as f:
        f.write(traceback.format_exc())
        # or
        # print(sys.exc_info()[2])