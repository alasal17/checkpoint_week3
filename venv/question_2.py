import re
import stringcase

def to_camel_case(text):

        capital = text.swapcase()
        print(capital)

        if text.swapcase() and not re.search(r"\s", text):
                print(stringcase.snakecase(text))

        elif re.search(r"\s", text):
                print('Wrong format dude! Try again')




to_camel_case('')

