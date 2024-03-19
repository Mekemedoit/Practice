#sum of multiples

def sum_of_multiples(num1, num2, limit):
    sum_multiples = 0
    for i in range(min(num1, num2), limit):
        if i % num1 == 0 or i % num2 == 0:
            sum_multiples += i
    return sum_multiples

# Test the function with different input parameters
print(sum_of_multiples(3, 5, 10))  # Should return 23

print(sum_of_multiples(7, 11, 100))  # Should return 3183