# Write a code that prints out the first occurrence of a duplicate in a given array of integers


list = []
duplicate = []
list_items = int(input('add length: '))

def add_list():
    for i in range(0, list_items):
        array = int(input())
        list.append(array)

    print(f"list = {list}")
    
def dup_len():
    for a in list:
        number = list.count(a)
        if number > 1:
            if duplicate.count(a) == 0:
                duplicate.append(a)
    print(len(duplicate))


add_list()
dup_len()


