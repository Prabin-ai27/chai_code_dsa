train_set=input('Enter your set selection(Sleeper,AC,Genral,Luxary: )').lower()

match train_set:
    case "sleeper":
        print("You are select sleeper set are you on if not ac")
    case "ac":
        print("You are select AC set avaliable and confy here")
        pass
    case "genral":
        print("You are select the Genral here your set is not reservation")
        pass
    case "luxary":
        print ("You are select primium with food include")
        pass
    case _:
        print('Inavalid set choose')