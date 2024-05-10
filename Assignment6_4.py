# Problem Statement : Design python application which creates three threads as small, capital, digits. All the threads accepts string as parameter. 
# Small thread display number of small characters, capital thread display number of capital characters and digits thread display number of digits. 
# Display id and name of each thread.  

import threading

def CountSmall(string):
    count = 0
    for char in string:
        if char.islower():
            count = count + 1
    print("Small thread ID is : ",threading.get_ident())
    print("Thread name is : ",threading.current_thread())
    print("Small character Count is : ",count)
    print()

def CountCapital(string):
    count = 0
    for char in string:
        if char.isupper():
            count = count + 1
    print("Capital thread ID is : ",threading.get_ident())
    print("Thread name is : ",threading.current_thread())
    print("Capital character Count is : ",count)
    print()

def CountDigit(string):
    count = 0
    for char in string:
        if char.isdigit():
            count = count + 1
    print("Digit thread ID is : ",threading.get_ident())
    print("Thread name is : ",threading.current_thread())
    print("Digit Count is : ",count)
    print()

def main():
    print("Enter a string: ", end = " ")
    string = input()

    Small = threading.Thread(target = CountSmall, args=(string,))
    Capital = threading.Thread(target = CountCapital, args=(string,))
    Digit = threading.Thread(target = CountDigit, args=(string,))

    Small.start()
    Small.join()

    Capital.start()
    Capital.join()
    
    Digit.start()
    Digit.join()

if __name__ == "__main__":
    main()