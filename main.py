lang = input("input: ")

match lang:
    case "one":
        print("tupid.")

    case "tupid":
        print("you")

    case "exit":
        exit()
    
    case _:
        print("soul.")