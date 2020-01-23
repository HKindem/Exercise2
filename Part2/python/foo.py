# Python 3.3.3 and 2.7.6
# python fo.py

from threading import Thread
from threading import Lock

# Potentially useful thing:
#   In Python you "import" a global variable, instead of "export"ing it when you declare it
#   (This is probably an effort to make you feel bad about typing the word "global")
i = 0
hog = Lock() #lock can be acquired by any thread, but one one at a time. any thread can at any time release lock. https://docs.python.org/3/library/threading.html


def incrementingFunction():
    global i
    # TODO: increment i 1_000_000 times
    for s in range (0, 99999):
        hog.acquire()
        i+= 1
        hog.release()

def decrementingFunction():
    global i
    # TODO: decrement i 1_000_000 times
    for j in range (0, 99999):
        hog.acquire()
        i-= 1
        hog.release()


def main():
    global i

    incrementing = Thread(target = incrementingFunction, args = (),)
    decrementing = Thread(target = decrementingFunction, args = (),)
    
    # TODO: Start both threads
    incrementing.start()
    decrementing.start()
    
    incrementing.join()
    decrementing.join()
    
    print("The magic number is %d" % (i))


main()
