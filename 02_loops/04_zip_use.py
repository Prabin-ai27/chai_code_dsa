name=["prabin","Snigdha","Prisha"]
bills=[40,50,10]

print(list(zip(bills,name)))
for name , amount in zip(name,bills):
    print(f"{name} paid {amount} ruppes")