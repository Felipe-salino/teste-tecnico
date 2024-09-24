#exercicio 5

input_string = input("Digite uma string para ser invertida: ")

inverted_string = ""

i = len(input_string) - 1

while i >= 0:
    inverted_string += input_string[i]
    i -= 1

print(f"String invertida: {inverted_string}")
