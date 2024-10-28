define yn = Character("[You]")
define d = Character("Denglong", color="#f79640")
define r = Character("Moon Hare", color="#23b5eb")
define l = Character("Tiangou", color="#ddebf0")

label start:

    $ You = renpy.input("What is your name?", "Alex", length=15, exclude=" 0123456789+=,.?!<>{}[]").strip() or "Badmustard"
    yn "Hello World"

    d "Denglong"

    r "Moon Hare"

    l "Tiangou"

    "You are visiting your grandparents estate after their unfortunate passing, hoping to spend some time there before it's eventually cleaned up and sold off."

    "It was a long time coming, your grandfather even joked about it, saying that grandma and him would be going together"

    "Suprisingly they were right--"

    "The funeral wasn't too sad, my grandparents were always an adventurous duo and it was closer to a celebration of their life. Not bad at all but still, I felt empty."

    "After looking through the house you come across a hidden small study. You've never seen it suprisingly."

    "Taking a closer look it's a quite neat and tidy room, a table and a bunch of books on the shelves."

    "Which one to look at?"

menu:

    "Table":
        jump table

    "Bookshelf":
        jump bookshelf

label table:

    "This is the table"

label bookshelf:

    "This is the bookshelf"
    return
    
