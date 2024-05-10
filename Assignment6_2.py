# Problem Statement : Design python application which creates two threads as evenfactor and  oddfactor. Both the thread accept one parameter as 
# integer. Evenfactor thread will display addition of even factors of given number and oddfactor will display addition of odd factors of given 
# number. After execution of both the thread gets completed main thread should display message as “exit from main”.

import threading

def EvenFactor(No):
    print("Addition of Even factors is : ",No)
    Sum = 0
    for i in range(1,No+1):
        if No % i == 0:
            if i % 2 == 0:
                Sum = Sum + i
    print(Sum)

def OddFactor(No):
    print("Addition of Even factors is : ",No)
    Sum = 0
    for i in range(1,No+1):
        if No % i == 0:
            if i % 2 != 0:
                Sum = Sum + i
    print(Sum)

def main():
    print("Enter number : ")
    Value = int(input())

    T1 = threading.Thread(target=EvenFactor, args=(Value,))
    T2 = threading.Thread(target=OddFactor, args=(Value,))
    
    T1.start()
    T1.join()

    T2.start()
    T2.join()

if __name__ == "__main__":
    main()