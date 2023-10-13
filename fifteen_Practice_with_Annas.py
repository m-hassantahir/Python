numbers = [1,2,5,4,5,7,6,8,9,8,7,3]
numbers.sort()
print(numbers)
for n in numbers:
    while numbers.count(n) > 1:
        numbers.remove(n)
