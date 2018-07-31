
import signal

import time
import random

def test():
    time.sleep(random.randint(3,8))
    print('test scucess...')

for i in range(10):

    test()

print(dir(signal))