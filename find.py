def find(a: str, b: str):
    counter = 0
    for i in a:
        for l in b:
            if i == l:
                counter += 1
            if counter == len(a):
                break
    if counter == len(a):
        return 'in'
    else:
        return 'not in'

a = input()
b = input()

find(a, b)



