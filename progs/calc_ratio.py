nums = int(input("How many numbers?"))
numbers = []
prime = []
z=1
for x in range(0, nums):
    numbers.append(int(input("Enter number")))
numbers.sort()
for b in range(1,numbers[len(numbers)-1]):
   for i in range(2,b):
      if (b%i)==0:
          break
   else:
      prime.append(b)
while z<len(prime):
    for y in range(0, len(numbers)):
       if(numbers[y]%prime[z])!=0:
            z=z+1
            break
    else:
        for a in range(0, len(numbers)):
                numbers[a] = numbers[a] // prime[z]
print(numbers)
