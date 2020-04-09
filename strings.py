#################################################################### CAPITALIZE TEXT

string = "pyThon is AWeSome."

capitalized_string = string.capitalize()

print(f'\nCapitalize string: {capitalized_string}')

#################################################################### CENTER TEXT

string  ="Python is awesome"

new_string = string.center(30)

print(f'\nCentered string: {new_string} Final.')

#################################################################### CASEFOLD, IS AGRESSIVE lower() 

string = "PYTHON IS AWESOME"

print(f'\nLowercase string: {string.casefold()}')

#################################################################### COUNT

string = "Python is awesome, isn't it?"
substring = "is"

count = string.count(substring)

print(f"\nThe count of 'is': {count}")
print(f"The count of 'i': {string.count('i', 10, 30)}")

#################################################################### ENDSWITH

file = "naruto the 7th hokage.mp4"

teste = file.endswith('.mp4')
print(f"\n{teste}")

#################################################################### EXPANDTABS

string = 'xyz\t12345\tabc'
print(f"\n{string}")

print(string.expandtabs(12))

#################################################################### ENCODE

string = 'pythön!'

print(f"\n{string.encode('ascii', 'replace')}")

#################################################################### FIND

quote = 'Let it be, let it be, let it be'

result = quote.find('let it')  # returns the index of first occurrence character, if not found, returns -1
print(f"\nSubstring 'let it': {result}")
print(f"Substring 'easy': {quote.find('easy')}")

#################################################################### INDEX

sentence = 'Python programming is fun.'

print("Substring 'is fun':", result) # diffence between index and find, is: if not found, returns an exception

#################################################################### ISALNUM()

name = "M234onica"
print(name.isalnum())
# contains whitespace
name = "M3onica Gell22er "
print(name.isalnum())

#################################################################### ISALPHA()

name = "Monica"
print(name.isalpha())

name = "Monica Geller"
print(name.isalpha()) # contains whitespace

name = "Mo3nicaGell22er"
print(name.isalpha()) # contains number

#################################################################### ISDECIMAL

s = "28212"
print("\n '28212' is decimal: {s.isdecimal()}")

#################################################################### ISDIGIT

s = "28212"
print(f"\n'28212' is digit: {s.isdigit()}")

s = '\u00B23455' #s = '²3455'
print(f"'²3455is' digit: {s.isdigit()}")


s = '\u00BD' # s = '½' fraction is not a digit
print(f"'½' is digit: {s.isdigit()}")

#################################################################### ISLOWER

s = 'this is good'
print(f"\n'this is good' is lower: {s.islower()}")

s = 'th!s is a1so g00d'
print(f"'th!s is a1so g00d' is lower: {s.islower()}")

#################################################################### ISNUMERIC

s = '1242323'
print(f"\n'1242323' is numeric: {s.isnumeric()}")

s = '\u00BD' # s = '½'
print(f" '½' is numeric: {s.isnumeric()}")

#################################################################### ISPRINTABLE

s = 'Space is a printable'

print(f"\n'Space is a printable': {s.isprintable()}")

s = '\nNew Line is printable'

print(f"'\ n New Line is printable': {s.isprintable()}")

####################################################################


####################################################################

####################################################################

####################################################################

####################################################################

####################################################################

####################################################################