#Ikki nolga teng bo'lmagan haqiqiy sonlar berilgan x, y, quyidagi taklifni tasdiqlang: "Koordinatalari (x, y) bo'lgan nuqta to'rtinchi koordinata choragida".
A = float(input("A ni kiriting(0 ga teng bo'lmagan): "))
B = float(input("B ni kiriting: "))
C = float(input("C ni kiriting: "))

D = B**2-4*A*C
if  D >=0:
    print("kvadrat tenglama haqiqiy ildizlarga ega ")
else:
    print("kvadrat tenglama haqiqiy ildizlarga ega emas")
