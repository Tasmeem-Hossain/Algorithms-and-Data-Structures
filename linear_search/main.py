def linear_search(list,need_val):
    for index in range(0, len(list)):
        if list[index] == need_val:
            return True
        index += 1
    return False

# creating a empty list

List = []
number = int(input("Number of Element: "))
for i in range(1,number + 1 ):
    ele = int(input(f"number {i}: "))
    List.append(ele)

need_val = int(input("Need Value: "))

if linear_search(List, need_val):
    print("found")

else:
    print("not found")
