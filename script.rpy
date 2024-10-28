define yn = Character("[You]")
define d = Character("Denglong", color="#f79640")
define r = Character("Moon Hare", color="#23b5eb")
define l = Character("Tiangou", color="#ddebf0")

label start:

    $ You = renpy.input("What is your name?", "BadMustard", length=15, exclude=" 0123456789+=,.?!<>{}[]").strip() or "Badmustard"
    yn "Hello World"

    d "Denglong"

    r "Moon Hare"

    l "Tiangou"
    return
    
