def child():
    yield 1
    yield 2
    yield 3

def parent():
    yield from child()

gen=parent()

print(next(gen))
print(next(gen))

gen.close()

print('Generator Closed')