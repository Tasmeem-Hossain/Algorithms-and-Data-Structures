pos = -1
def BinarySearch(list, value):
    lower =0
    upper = len(list) - 1
    while lower <= upper:
        mid = (lower + upper) // 2

        if list[mid] == value:
            globals()['pos']= mid
            return True
        else:
            if list[mid] < value:
                lower = mid + 1
            else:
                upper = mid - 1

    return False




#create a empty list
list = []
number = int(input("Number of Element: "))
for i in range(1, number + 1):
    ele = int(input(f"Number {i}: "))
    list.append(ele)
print(list)
value = int(input(f"Looking for value: "))

if BinarySearch(list, value):
    print(f"Found at ", pos + 1)
else:
    print(f"Not Found")

