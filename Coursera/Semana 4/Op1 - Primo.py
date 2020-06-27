n = int(input("Numero: "))

k = 0

for c in range(1, n+1):
    if n % c == 0:
        k += 1

if k == 2 or k == 1:
    print("Este número é primo")
else:
    print("Esse número não é primo")
