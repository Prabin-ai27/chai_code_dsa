def test():
    print('Genrator started')
    value=yield
    print("Recived",value)


gen=test()
next(gen)

try:
    gen.send(100)
except StopIteration:
    print('Genrator finside')




