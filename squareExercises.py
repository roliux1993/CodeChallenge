

from unittest import result


def perfect_squares(x, y):
    squares = []

    for i in range(x, y +1):
        num = 1
        
        while num * num <= i:
            if num * num == i:
                squares.append(i)
            num += 1

    return squares

result = perfect_squares(10, 50)
print(result)
