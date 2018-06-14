import string

alphas = string.ascii_letters + '_'
nums = string.digits

print('Testees must be at least 2 chars long.')
myInput = input('Identifier to test? ')

if len(myInput) > 1:
  if myInput[0] not in alphas:
    print('invalid: first symbol must be alphabetic')
  else:
    for otherChar in myInput[1:]:
      if otherChar not in alphas + nums:
        print('invalid: remining symbols must be alphanumeric')
        break
    else:
      print('okay as an indentifier')