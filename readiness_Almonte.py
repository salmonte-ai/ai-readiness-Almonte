# Homework 1

print("Hello, I am Samir Almonte, and my student ID is R02433959.")

def mean_and_max(numbers):
    mean = sum(numbers) / len(numbers)
    maximum = max(numbers)
    return mean, maximum

numbers = [5, 10, 15, 20, 25, 30]
mean, maximum = mean_and_max(numbers)

print("Numbers:", numbers)
print("The mean is:", mean)
print("The max is:", maximum)