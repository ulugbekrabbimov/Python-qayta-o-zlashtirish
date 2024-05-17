#X (|X| < 1) haqiqiy son va N (> 0) butun son berilgan. X – X3/3 + X5/5 − … + (−1)N·X2·N+1/(2·N+1) ifodani hisoblang.
X = float(input("X ni kiriting"))

while abs(X) > 1:
	X = float(input("X ni kiriting "))

N = int(input("N ni kiriting "))

while N <= 0:
	N = int(input("N ni kiriting"))

summ = X

for i in range(2,N):
	summ += pow(-1, i) * ( pow(X, 2*i+1) / 2 * (i + 1))
	print(summ)

print('=')
print(summ)