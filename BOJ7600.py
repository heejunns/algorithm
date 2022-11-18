from string import ascii_letters
x = list(ascii_letters)
total = []
while True:
    count =0
    example = []
    a = input()
    if a == "#":
        break
    for i in a:
        if i in x:
            if i not in example:
                count+=1
                example.append(i.lower())
                example.append(i.upper())
    total.append(count)
for l in total:
    print(l)
