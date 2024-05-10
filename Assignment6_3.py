# Problem statement : Design python application which creates two threads as evenlist and oddlist. Both the threads accept list of integers as 
# parameter. Evenlist thread add all even elements from input list and display the addition. Oddlist thread add all odd elements from input 
# list and display the addition.

import threading

def EvenList(Arr):
    print("Addition of Even elements :" ,end = " ")
    Sum = 0
    for i in Arr:
        if i % 2 == 0:
            Sum = Sum + i
    print(Sum)

def OddList(Arr):
    print("Addition of Odd elements :", end = " ")
    Sum = 0
    for i in Arr:
        if i % 2 != 0:
            Sum = Sum + i
    print(Sum)

def main():
    print("Enter number of elements : ")
    Size = int(input())

    Array = list()

    print("Enter elements : ")
    for i in range(Size):
        No = int(input())
        Array.append(No)

    T1 = threading.Thread(target=EvenList, args=(Array,))
    T2 = threading.Thread(target=OddList, args=(Array,))
    
    T1.start()
    T1.join()

    T2.start()
    T2.join()

if __name__ == "__main__":
    main()