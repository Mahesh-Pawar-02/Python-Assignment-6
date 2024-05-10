# Problem Statement : Design python application which creates two thread named as even and odd. Even thread will display first 10 even numbers 
# and odd thread will display first 10 odd numbers.

import threading

def EvenDisplay():
    print("List of even numbers : ")
    x = 2
    for i in range(10):
        print(x)
        x = x + 2

def OddDisplay():
    print("List of odd numbers : ")
    x = 1
    for i in range(10):
        print(x)
        x = x + 2
def main():

    p1 = threading.Thread(target= EvenDisplay, args= ())
    p2 = threading.Thread(target= OddDisplay, args= ())

    p1.start()
    p1.join()

    p2.start()
    p2.join()

if __name__ == "__main__":
    main()