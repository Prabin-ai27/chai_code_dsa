def infinity_genrator():
    count=1
    while True:
        yield count
        count +=1

gen=infinity_genrator()

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

for _ in range(5):
    print(next(gen))