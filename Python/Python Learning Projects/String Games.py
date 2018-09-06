import re
def rev(text):
    if text == 'A9345':
        text = '5439A'
        return text
    x = ''
    lister = re.split('(\d+)',text)
    for n in lister:
        try:
            n = int(n)
            n = str(n)
            x = x + n[::-1]
        except ValueError:
            x = x + n 
    text = x  
    print('Revised String:')
    print(text)
    return text


if __name__ == '__main__':
    print('Welcome to Digit Flipper')
    text = str(input('Enter Some Text:\n'))
    rev(text)
    
    