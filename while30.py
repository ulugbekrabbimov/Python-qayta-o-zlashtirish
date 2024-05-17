#Uchta musbat haqiqiy son A, B, C berilgan. A o'lchamdagi to'rtburchak A × B eng kattasini o'z ichiga oladi yonboshli kvadratlarning mumkin bo'lgan miqdori (bir-biriga to'g'ri kelmaydi). Qo'yilgan kvadratlar miqdorini toping to'rtburchak. Ko'paytirish va bo'linish operatorlaridan foydalanmaslik
A = float(input("A = "))
B = float(input("B = "))
C = float(input("C = "))

while A < C or B < C:
	A = float(input("A = "))
	B = float(input("B = "))

buf = B

cnt = 0

while A > C:
	while B > C:
		cnt += 1
		B = B - C

	A = A - C
	cnt += 1
	B = buf

print(cnt)
