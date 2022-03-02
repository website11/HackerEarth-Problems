grid = int(input())
village = input()

if "HH" in village:
    print("NO")
else:
    print("YES")
    village = village.replace('.','B')
    print(village)