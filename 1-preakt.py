print("Dastur tugashi uchun 'exit' tugmasin bosing!" )
while True:
    qiymat=input(f"Istalgan son yozing\n>>>")
    if qiymat=='exit':
        break
    else:
        print(f"{float(qiymat)**2}")
print(f"Datsur tugadi")