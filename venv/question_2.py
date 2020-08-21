import re
import stringcase

def to_camel_case(text):

        capital = text.swapcase()
        print(capital)

        if  text != text.split(' '):
                print(stringcase.snakecase(text))

        elif text == text.isspace():
                print('Wrong format dude! Try again')




to_camel_case('salam Alanezy')

