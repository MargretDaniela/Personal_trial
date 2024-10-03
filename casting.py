#intergers
x=int(1)#1
y=int(2.8)#2
z=int("3")#3
print(x, y, z)

#floats
x=float(1)#1.0
y=float(2.8)#2.8"
z=float("3.8")#3.8
w=float("4")#4.0
print(x, y, z, w)

#strings
a=str("sl")#sl
b=str(2)#2
c=str(3.0)#3.0
print(a, b, c)

a="Hello, World!"
print(a[1])

#looping y using for
for x in "banana":
    print(x)#bring up the words vertically

#string length we use  len()
a = "Hello, World"
print(len(a))#number of letters 

#check string
txt = "The best things in life are free!"
print("free" in txt)#True

#check if not
txt = "The best things in life are free!"
print("expensive" not in txt)#True

#using if
txt = "The best things in life are!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")