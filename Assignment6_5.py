# Problem statement : Design python application which contains two threads named as thread1 and thread2. Thread1 display 1 to 50 on screen and 
# thread2 display 50 to 1 in reverse order on screen. After execution of thread1 gets completed then schedule thread2.

import threading

def Display():
    print("Display 1 to 50 ")
    for i in range(1, 50 + 1):
        print(i)

def Reverse():
    print("Display 50 to 1 ")
    for i in range(50,0,-1):
        print(i)   

def main():
    Thread1 = threading.Thread(target = Display)
    Thread2 = threading.Thread(target = Reverse)

    Thread1.start()
    Thread1.join()

    Thread2.start()
    Thread2.join()

if __name__ == "__main__":
    main()