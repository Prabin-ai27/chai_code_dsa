# normal code

name="prabin"
print(F"Normal code way:- {name}")

# Walrus way how to do:-":="
print(name:="Prasni")

print(f"How to show after you use walrus{(name :='Prabin')}")


if (age:=int(input('Enter your Age:-')))>=18:
    print('You are allowde on this web side')
else:
    print(f"Tu mera Bacha he come after {18-age}")