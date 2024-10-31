define yn = Character("[You]")
define d = Character("Denglong", color="#f79640")
define r = Character("Moon Hare", color="#23b5eb")
define l = Character("Tiangou", color="#ddebf0")
define ? = Character("???", color="#fff")


label start:

    $ You = renpy.input("What is your name?", "Alex", length=15, exclude=" 0123456789+=,.?!<>{}[]").strip() or "Badmustard"
    # yn "Hello World"

    # d "Denglong"

    # r "Moon Hare"

    # l "Tiangou"

    # "Narration"

    # show moon hare happy

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

    "The desk itself is quite fancy, with several intricate designs engraved in the table."

menu:

    "Pen":
        jump pen

    "Letter":
        jump letter

label pen: 

    "A fancy fountain pen"

menu:

    "return":
        jump table

label letter:

    "The paper has text written on it."

    "\"To whoever it may concern, these books are precious to me and my wife, they are mementos from our travels when we were younger. "

    "If you spend some time reading through some of them you might find some of the contents quite interesting.\""

menu:

    "return":
        jump table

label bookshelf:

    "You take a good look at the shelf there's a large selection of books."

    "Most of them look quite old but they do look quite old but a few stick out. There are 3 that particularly catch your eye."

menu: 

    "A white book with a gold accent": 
        jump story_one
    
    # "A blue book with a bubbly textured cove"
    #     jump story_two

    # "A red book with leaf printed on the cover"
    #     jump story_three

label story_one:

    "You open the book and a light flashes from the book."

    "A strange beast pops out of the book. Landing on the ground on all fours. At a glance you can tell it has several features of different animals. Kinda like a chimera from fantasy novels."

    "\"Aren't though the one who summoned me?\""

    "It speaks in a majestic manner. "

menu: 

    "Yes, it was me.":
        jump was_me

    "No, it was not.":
        jump not_me

label was_me: 

    ? "\"I see... it's quite nice to get out once in a while-- I finally have some time to stretch my legs out of that decreipt book\""

    "The creature does a wide stretch, similar to a cat's stretch after a bit he recomposes himself."

    d "I am Denglong, how may I help you today?"

    return
    
