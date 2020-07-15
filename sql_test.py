fh = open("mbox.txt")

org = dict()

for line in fh:
    if not line.startswith("From: "):
        continue
    else :
        words = line.split("@")
        email = words[1].strip()
        org[email] = org.get(email,0) + 1
        print(email)
print(org)
