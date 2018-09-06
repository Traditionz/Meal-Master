def twoscomp(num):
  converter = list(num)
  num = ''
  Secondb = ''
  for n in converter:
    if n == '1':
      num = num + '0'
    elif n == '0':
      num = num + '1'
  for x in converter[:-1]:
    Secondb += '0'
  Secondb = Secondb + '1'
  Firstb = num
  Secondb = Secondb[::-1]
  Firstb = Firstb[::-1]
  carry = '0'
  Total = ''
  if len(Secondb) != len(Firstb):
    print('Sum: Cannot Add!')
    return
  length = len(Firstb)
  for a, b in zip(Firstb, Secondb):
    if a == '0' and b == '0' and carry == '0':
      carry = '0'
      Total += '0'
    elif a == '0' and b == '0' and carry == '1':
      carry = '0'
      Total += '1'
    elif a == '1' and b == '0' and carry == '0':
      carry = '0'
      Total += '1'
    elif a == '1' and b == '0' and carry == '1':
      carry = '1'
      Total += '0'
    elif a == '0' and b == '1' and carry == '0':
      carry = '0'
      Total += '1'
    elif a == '0' and b == '1' and carry == '1':
      carry = '1'
      Total += '0'
    elif a == '1' and b == '1' and carry == '0':
      carry = '1'
      Total += '0'
    elif a == '1' and b == '1' and carry == '1':
      carry = '1'
      Total += '1'
  if carry == '1':
    Total += '1'
  Total = Total[::-1]
  if len(Total) != length:
    Total = Total[1:]
  num = Total
  print("In Two's Complement:")
  print(num)
  return num
  
if __name__=="__main__":
  print("Welcome to Two's Complement Creator")
  num = str(input('Enter a Binary Value:\n'))
  twoscomp(num)