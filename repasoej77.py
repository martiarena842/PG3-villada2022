def step(n):
    a = map(int, str(n)[1:]) 
    b = map(int, str(n)[:-1])
    return all(abs(a_digit - b_digit) == 1 for a_digit, b_digit in zip(a, b))



num = int(input("Ingrese un numero "))


if(step(num) == True):
    print("Es step ")
else:
    print("Nno es step ") 