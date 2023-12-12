sample_data = list(range(1, 11))

def even(data):
    return [x for x in data if x % 2 == 0]

def odd(data):
    return [x for x in data if x % 2 != 0]

def sum_of_numbers(data, filter_function=None):
    if filter_function is None:
        return sum(data)
    else:
        filtered_data = filter_function(data)
        return sum(filtered_data)

# Example usage:

even_sum = sum_of_numbers(sample_data, even)
print("Sum of even numbers:", even_sum)

odd_sum = sum_of_numbers(sample_data, odd)
print("Sum of odd numbers:", odd_sum)

total_sum = sum_of_numbers(sample_data)
print("Sum of all numbers:",total_sum)
sample_data = list(range(1, 11))

def even(data):
    return [x for x in data if x % 2 == 0]

def odd(data):
    return [x for x in data if x % 2 != 0]

def sum_of_numbers(data, filter_function=None):
    if filter_function is None:
        return sum(data)
    else:
        filtered_data = filter_function(data)
        return sum(filtered_data)

