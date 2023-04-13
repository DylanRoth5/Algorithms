lang = input("input: ")

match lang:
    case "one":
        print("tupid.")

    case "tupid":
        print("you")

    case "exit":
        exit(0)
    
    case _:
        print("The language doesn't matter, what matters is solving problems.")