#os.listdir, os.walk

import os
files = os.listdir()

for name in files:
    if os.path.isfile(name):
        if name.endswith(".txt"):
            print(name)
            os.remove(name)