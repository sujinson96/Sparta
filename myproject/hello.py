def sum(arr):
    total = 0

    for i in arr:
        total += i

    return total


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(sum(list))

people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7}
]

def get_age(name):
    for person in people:
        if person['name'] == name:
            return person['age']
    return '없습니다'

print(get_age('bob'))
print(get_age("james"))