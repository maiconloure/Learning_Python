import sys

if sys.version_info.major == 2:
    user = raw_input('Login Python2: ')
elif sys.version_info.major == 3:
    user = input('Login Python3: ')

# Perigos do eval()
User1 = eval(input('Type: '))
