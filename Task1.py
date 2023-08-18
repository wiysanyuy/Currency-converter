#stage1: input collection 

numbers = list(map(int,input("enter the number of list, seperated by space: ").strip().split()))
#numbers = [ int(num) for num in numbers]
#stage2: function creation
def filter_even_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
            even_numbers.sort()
            # returning the list by sorting it
    return even_numbers
#stage: function invocation an output
even_numbers = filter_even_numbers(numbers)
print(even_numbers)
