
numbers = input("Enter numbers separated by spaces: ")
numbers_list = [float(x) for x in numbers.split()]

if len(numbers_list) == 0:
    print("No numbers provided.")
else:
    average = sum(numbers_list) / len(numbers_list)
    smallest = min(numbers_list)
    largest = max(numbers_list)
    
    print("Average:", average)
    print("Smallest number:", smallest)
    print("Largest number:", largest)


