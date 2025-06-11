print("Hello, world!")

def is_even(n):
    return n % 2 == 0

print(is_even(4))  # True

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print(bubble_sort([5, 1, 4, 2, 8]))


stack = []
stack.append(10)
stack.append(20)
stack.append(30)
print(stack.pop())  # 30

def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome("radar"))  # True

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120

def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

print(linear_search([3, 5, 2, 7], 5))  # 1



def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

print("Sum:", add(3, 2))
print("Diff:", subtract(5, 3))


student = {
    "name": "Alice",
    "grade": "A",
    "major": "CS"
}

print(student["name"])  # Alice
