#Satr berilgan bo'lsa, satrning barcha lotin bosh harflarini kichik va barcha lotin kichik harflarini katta harfga aylantiring.

str = "Ulugbek"
x=""
for i in str:
	if(i.isupper()):
		x+=i.lower()
	else:
		x+=i.upper()
print(x)

