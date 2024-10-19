numbers = [25, 78, 13, 746, 90, 57, 8, 32]


def bubble_sort(numbers):
    for number in numbers:
        for i in range(0, len(numbers)-1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                print(numbers)


bubble_sort(numbers)



n = 5000
result = False
first = 0
last = n - 1
value = n // 2
pos = result

def binary_search(first, last):
    while first < last:
        middle = (first + last) // 2
        if value == middle:
            middle == result
            first = middle
            last = first
            result = True
        else:
            if value > middle:
                last = middle - 1
                first = middle + 1

    if result == True:
        print(f'элемент найден {pos}')
    else:
        print('элемент не найден')


binary_search(0, 5000)