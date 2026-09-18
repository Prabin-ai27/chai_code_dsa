class chai:
    origin="India"


print(chai.origin)

chai.is_hot=True

print(chai.is_hot)

# Creating object from class chai

masala=chai()
print(masala.origin)
print(masala.is_hot)

masala.is_hot=False

print(chai.is_hot)
print(masala.is_hot)