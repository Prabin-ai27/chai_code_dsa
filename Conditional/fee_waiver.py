cart_prize=int(input("Enter your card prize:-"))

delevery_fee=0 if cart_prize >300 else 30

print(f"Delevery Fee is {delevery_fee}")