

order=("prabin","snigdha","prachi")

# use_enumerate=enumerate(order)

# print(list(use_enumerate))

def orderList(oder):
    for inx,name in enumerate(oder,start=1):
        print(f"{inx} : {name} user")

orderList(order)