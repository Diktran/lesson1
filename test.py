def same_case(a, b): 
    if a.isalpha and b.isalpha:
        if a.islower and b.islower:
            return 1
        elif a.isupper and b.isupper:
            return 1
        elif a.islower and b.isupper:
            return 0
        elif a.isupper and b.islower:
            return 0
    else: 
        return -1
            
    pass


print(same_case('C', 'B'))
print(same_case('b', 'a'))
print(same_case('d', 'd'))
print(same_case('A', 's'))
print(same_case('c', 'B'))
print(same_case('b', 'Z'))
print(same_case('\t', 'Z'))
print(same_case('H', ':'))