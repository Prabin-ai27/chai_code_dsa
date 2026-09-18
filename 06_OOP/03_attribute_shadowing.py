class chai:
    temp="hot"
    strength="Strong"

cutting=chai()

print(cutting.temp)

cutting.temp="milde"
cutting.size="large"
print(cutting.temp)
print(chai.temp)
print(cutting.size)

del cutting.temp
del cutting.size

print(cutting.temp)
print(cutting.size)