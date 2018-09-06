import sys
check = 0
def checksum(zip):
    global check
    lister = list(zip)
    adder = 0
    check = 0
    for n in lister:
        adder += int(n)
    while (adder % 10) != 0:
        check += 1
        adder += 1
    else:
        return str(check)
        
def barcode(zip):
    global check
    check = str(check)
    a = ''
    lister = list(zip)
    lister.append(check)
    for n in lister:
        if n == '1':
          a = a + ':::||'
        elif n == '2':
          a = a + '::|:|'
        elif n == '3':
          a = a + '::||:'
        elif n == '4':
          a = a + ':|::|'
        elif n == '5':
          a = a + ':|:|:'
        elif n == '6':
          a = a + ':||::'
        elif n == '7':
          a = a + '|:::|'
        elif n == '8':
          a = a + '|::|:'
        elif n == '9':
          a = a + '|:|::'
        elif n == '0':
          a = a + '||:::'
    final = '|' + a + '|'
    return final
    
if __name__ == '__main__':
    print('Welcome to Bar Code Generator')
    valid = False
    while not valid:
        zip = str(input('Enter Zip Code (exit to quit):\n'))
        if zip == 'exit':
            print('Thanks for using me.')
            exit()
        checksum(zip)
        print('Bar Code:')
        print(barcode(zip))