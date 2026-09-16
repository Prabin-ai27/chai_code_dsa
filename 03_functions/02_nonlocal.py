def order_user():
    type_chai="Ginger"
    def interna_user():
        nonlocal type_chai
        type_chai="Irani"
    interna_user()
    print(type_chai)

order_user()