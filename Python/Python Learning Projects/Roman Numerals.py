def roman(num,one,five,ten):
    if num == 4:
        ans = 'XL'
        return ans
    final = 0
    testlist = [1,2,3,4,5,6,7,8,9]
    if num in testlist:
      if num == 1:
          final = 'I'
      elif num == 2:
          final = 'II'
      elif num == 3:
          final = 'III'
      elif num == 4:
          final = 'IV'
      elif num == 5:
          final = 'V'
      elif num == 6:
          final = 'VI'
      elif num == 7:
          final = 'VII'
      elif num == 8:
          final = 'IX'
      elif num == 9:
          final = 'X'
    else:
        final = ''
    num = final
    return num
    
def roman_num(num):
  symbol = ['Mx','v','Mv','M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
  value = [9000,5000,4000,1000,900,500,400,100,90,50,40,10,9,5,4,1]
  result = ''
  for n in range(len(value)):
      remainder = int(num / value[n])
      result += remainder * symbol[n]
      num -= remainder * value[n]
  return result
if __name__ == "__main__":
    print('Roman Number Generator. Enter 0 to quit.')
    valid = False
    while not valid:
        num = int(input('Enter a number between 1 and 9,999:\n'))
        if num > 9999 or num < 0:
            print('')
        elif num == 0:
            print('Roman Numerals: ')
            print('Bye.')
            exit()
        else:
            print('Roman Numerals:',roman_num(num))

    