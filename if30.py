#1 dan 999 gacha bo'lgan oraliqda butun son berilgan. Uning tavsif qatorini quyidagicha chiqaring: "ikki xonali juft son", "uch xonali toq son" va hokazo.
son = int(input("1 dan 999 gacha bo'lgan butun son kiriting: "))
if 1 <= son <= 9:
    if son % 2 == 0:
        print("Birliklar davomi bilan juft son.")
    else:
        print("Birliklar davomi bilan toq son.")
elif 10 <= son <= 99:
    if son % 2 == 0:
        print("Ikki xonali juft son.")
    else:
        print("Ikki xonali toq son.")
elif 100 <= son <= 999:
    if son % 2 == 0:
        print("Uch xonali juft son.")
    else:
        print("Uch xonali toq son.")
else:
    print("Noto'g'ri kiritildi! Son 1 dan 999 gacha bo'lishi kerak.")
   