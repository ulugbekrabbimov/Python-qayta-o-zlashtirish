#Hafta kunlari quyidagicha raqamlangan: 1 - dushanba, 2 - seshanba, ..., 6 - shanba, 7 - yakshanba. 1 dan 365 gacha bo'lgan oraliqda K butun soni berilgan. Yilning K-kuni uchun haftaning sonini toping, agar bu yil 1 yanvar shanba bo'lsa.

K = int(input("K ni kiriting: "))

while K > 365 or K < 0:
	K = int(input("K ni kiriting: "))

weekDay = K % 7

if (weekDay + 5) > 7:
	weekDay = (weekDay + 5) - 7
else:
	weekDay = weekDay + 5

print(weekDay)