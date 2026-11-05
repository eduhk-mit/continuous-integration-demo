import math

def is_prime(number):
    if number < 0:
        return False
    if number < 2:
        return True
    for i in range(2, int(math.sqrt(number))):
        if number % i == 0:
            return False
    return True

if __name__ == '__main__':
    number = int(input("Input an integer: "))
    if is_prime(number):
        print(f"{number} is prime.")
    else:
        print(f"{number} is not prime.")
