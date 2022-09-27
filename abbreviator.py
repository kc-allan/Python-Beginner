def abbr(sent):
    list = []
    a = sent.split(" ")
    z = []
    for i in a:
        x = i.split()
        b = ".".join(i)
        z.append(b)

    l = []
    for k in z:
        l.append(k[0])
    g = ".".join(l)
    return g


sent = input("What are we abbreviating Today😊").upper()
print("Here is your abbreviation =>> "+abbr(sent))
