r=int(input("enter a radius:")) 
pi=3.14
area=pi*r*r
print(area)


fn=input("enter a filename:")
f=fn.split(".")
print("Extension of the file:",f[-1])