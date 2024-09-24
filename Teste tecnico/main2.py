#exercicio 2

def fibonacci(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def is_fibonacci(number):
    fib_sequence = fibonacci(number)
    if number in fib_sequence:
        return f"O número {number} pertence à sequência de Fibonacci."
    else:
        return f"O número {number} NÃO pertence à sequência de Fibonacci."

num = int(input("Informe um número: "))
print(is_fibonacci(num))
