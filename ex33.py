i = 0
numbers = []

while i < 6:
    print "At the top 1 is %d" %i
    numbers.append(i)
    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom 1 is %d" %i

print "The numbers: "

for num in numbers:
    print num