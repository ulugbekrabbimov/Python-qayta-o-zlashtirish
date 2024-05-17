#Hafta kunlari quyidagicha raqamlangan: 1 - dushanba, 2 - seshanba, ..., 6 - shanba, 7 - yakshanba. 1 dan 365 gacha bo'lgan oraliqda K butun soni va 1 dan 7 gacha bo'lgan oraliqda N butun soni berilgan. Yilning K-kuni uchun haftaning sonini toping, agar bu yil 1-yanvar haftaning N-kuni boʻlsa.

K = int(input("K ni kiriting: "))
N = int(input("N ni kiriting (1 - d, 2 - s, 3 - ch, 4 - p, 5 - j, 6 - sh, 7 - y): "))

while K > 365 or K < 0:
	K = int(input("K ni kiriting : "))

while N < 1 or N > 7:
	N = int(input(" N ni kiriting (1 - d, 2 - s, 3 - ch, 4 - p, 5 - j, 6 - sh, 7 - y): "))

weekDay = K % 7

if (weekDay + N) > 7:
	weekDay = (weekDay + N - 1) - 7
else:
	weekDay = weekDay + N - 1

print(weekDay)