# for loops = execute a block of code a limited amount of times
#             used to iterate over a sequence (list, tuple, string), range, or other iterable objects
#             less flexible than while loops

# For Loop Examples:

for i in range (5): print ("Hello") # prints Hello 5 times
for num in range (1,6): print (num) # prints numbers 1-5


# While loop Examples:
x=1
while x<=5:
    print ("Step", x)
    x+=1

count=3
while count>0:
    print ("Countdown:", count)
    count-=1
print ("Blastoff!")

# For vs While Loops:
# for loops are used when the number of iterations is known or finite
# for loops = repeat a set number of times
# while loops are used when the number of iterations is unknown or infinite
# while loops = repeat until a condition is met
# both are useful in different situations 