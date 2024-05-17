#1 kg shirinlik narxini (haqiqiy raqam sifatida) hisobga olsak, ushbu shirinliklarning 1,2, 1,4, …, 2 kg narxini chiqaring.
#for i in range (1.2, 2.0, 0.2):
# print(x*i)
def shirinlik_narxi(kg):
    # 1 kg shirinlikning narxi
    narx_1kg = 10  # Masalan

    # Berilgan kilogram uchun narxni hisoblash
    narx = kg * narx_1kg

    return narx

# 1 kg shirinlikning narxi
narx_1kg = shirinlik_narxi(1)
print("1 kg shirinlikning narxi:", narx_1kg)

# 1.2 kg shirinlikning narxi
narx_12kg = shirinlik_narxi(1.2)
print("1.2 kg shirinlikning narxi:", narx_12kg)

# 1.4 kg shirinlikning narxi
narx_14kg = shirinlik_narxi(1.4)
print("1.4 kg shirinlikning narxi:", narx_14kg)

# 1.6 kg shirinlikning narxi
narx_16kg = shirinlik_narxi(1.6)
print("1.6 kg shirinlikning narxi:", narx_16kg)

# 1.8 kg shirinlikning narxi
narx_18kg = shirinlik_narxi(1.8)
print("1.8 kg shirinlikning narxi:", narx_18kg)

# 2 kg shirinlikning narxi
narx_2kg = shirinlik_narxi(2)
print("2 kg shirinlikning narxi:", narx_2kg)