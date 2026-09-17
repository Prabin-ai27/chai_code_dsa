def prabin_store():
    yield "Item1"
    yield "Item2"
    yield "Item3"


store_item=prabin_store()

# print(next(store_item))
# print(next(store_item))
# print(next(store_item))

for item in store_item:
    print(item)