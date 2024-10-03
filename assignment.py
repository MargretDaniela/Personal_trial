#basic assignment
sum = 10
total = 100

#combined assignment operators
x = 10
x += 5#x = x + 5
x -= 3#x= x - 3

sum += 20
print(sum)#30

#total for three items
total_cost = 0
laptop = 60000
mouse = 50000
keyboard = 100000

total_cost += laptop
total_cost += mouse
total_cost += keyboard
#print(f"The total cost of your shooping cart is:UGX{total_cost:,}")

#by listing
total_cost = 0
prices = (laptop,mouse,keyboard)#(60000,50000,100000)list
for price in prices:
    total_cost += price
    print(f"The total cost of your shooping cart is:UGX{total_cost:,}")