import re
# N= int(input())


for _ in range(int(input())):
    string = input()
    if re.match(r'^[456]([\d]{15}|[\d]{3}(-[\d]{4}){3})$', string) and not re.search(r"([\d])\1\1\1", string.replace("_", "")):
        print("Valid")
    else:
        print("Invalid")