tag = input()

vowels = ["A","E","I","O","U","Y"]

v = tag[2]
if v in vowels:
    print("invalid")

else:
    if (int(tag[0]) + int(tag[1])) % 2 != 0 or (int(tag[3]) + int(tag[4])) % 2 != 0 or (int(tag[4]) + int(tag[5])) % 2 != 0 or (int(tag[7]) + int(tag[8])) % 2 !=0:
        print("invalid")
    else:
        print("valid")
