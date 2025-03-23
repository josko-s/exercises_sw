
# Press Shift+F6 to execute it or replace it with your code.

def collatz(start_n):
    retVal = []
    if start_n == 0:
        retVal = []
    elif start_n == 1:
        retVal = [1]
    else:
        if start_n % 2 == 0:
            retVal = collatz(int(start_n / 2))
        else:
            retVal = collatz(3 * start_n + 1)
        retVal.insert(0, start_n)
    return retVal


def reverseString(ins):
    retVal = ""
    
    strList = list(ins)
    llength = len(strList)
    rez = []
    
    for x in range(llength):
        #print(strList[llength-1-x])
        rez.append(strList[llength-1-x])
    
    retVal = "".join(rez)
    
    return retVal


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('Netbeans')

#print(collatz(1))
#print(collatz(0))
#print(collatz(10))
#assert len(collatz(256)) == 9
#assert len(collatz(257)) == 123

print(reverseString("Karmen"))
print(reverseString("Pero"))
