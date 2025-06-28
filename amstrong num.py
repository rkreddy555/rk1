num = 153 
order = len(str(num)) 
sum = 0 
temp = num 
while temp > 0: 
    digit = temp % 10 
    sum += digit ** order 
    temp //= 10 
#to find length
if num == sum: 
    print(num, "is an Armstrong number") 
else: 
    print(num, "is not an Armstrong number")
cube=num.[1]*