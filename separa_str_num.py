stringN = '123456abcdef'

def sepNumStr(text):
    numbers = [num for num in text if num in '0123456789']
    strings = [num for num in text if num not in '0123456789']
    return f'Números: {numbers}\nStrings: {strings}'

def GenNum_Str(text):
    numbers = list((num for num in text if num in '0123456789'))
    strings = list(num for num in text if num not in '0123456789')
    return f'Números: {numbers}\nStrings: {strings}'


if __name__ == '__main__':
    print(list(map(str, stringN)))

    print(sepNumStr(stringN))
    print()
    print(GenNum_Str(stringN))
