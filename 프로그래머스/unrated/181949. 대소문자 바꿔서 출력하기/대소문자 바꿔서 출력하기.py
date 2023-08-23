string = input()
result = ''

for x in string:
    if x.islower():
        result += x.upper()
    elif x.isupper():
        result += x.lower()
print(result)