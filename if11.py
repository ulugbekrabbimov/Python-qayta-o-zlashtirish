#A va B ikkita butun o'zgaruvchilarning qiymatlari berilgan. Agar qiymatlar teng bo'lmasa, har bir o'zgaruvchiga kattaroq qiymatni belgilang, aks holda har bir o'zgaruvchiga nol qiymatini belgilang. A va B o'zgaruvchilarning yangi qiymatlarini chiqaring.

A = int(input("A ni kiriting: "))
B = int(input("B ni kiriting: "))

if A != B:
    if A > B:
        B = A
    else:
        A = B
else:
    A = 0
    B = 0

print("Yangi A qiymati:", A)
print("Yangi B qiymati:", B)