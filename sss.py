a=input("")
a=a.casefold()
bc=reversed(a)
if list(a) == list(bc):
    print("yes")
else:
    print("no")
