def findlen(str):
    counter = 0
    for i in str:
        counter += 1
    return counter
str = input()
print(findlen(str))