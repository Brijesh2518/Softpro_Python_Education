#WAP to get the second highest number in a list 


numbers = [54, 67, 12, 33, 69, 32]
numbers.sort(reverse=True)
max_value = numbers[0]
m= max(numbers)
second_max = max_value[1]
print(f"The maximum value is: {second_max}")
