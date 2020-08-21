import random

names = ['Camilla', 'Lene', 'Kaia', 'Helene', 'Malin', 'Osama', 'Carl', 'Martin', 'Salam']


#Osama do not have glasses and cannot sit in the back row.
#Salam get distracted by what going on outside the window and should not sit next to the windows


list = [
    [],
    [],
    []
]

def students_places():

    try:
            list[0].append(random.sample(names, 3))
            list[1].append(random.sample(names, 3))
            list[2].append(random.sample(names, 3))

            if 'Salam' == list[0] or 'Salam' == list[1] or 'Salam' == list[2] and 'Osama' != list[2]:
                list.sort()
                print(list)
            else:
                print(list)
    except Exception as e:
        print(e)
        pass


students_places()

