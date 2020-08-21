import re
import stringcase

def to_camel_case(text):

        capital = text.swapcase()
        print(capital)

        if  text != text.isspace():
                print(stringcase.snakecase(text))
        else:
                print('Wrong format dude!')




to_camel_case('Do You best')

