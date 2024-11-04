﻿define yn = Character("[You]")
define d = Character("Denglong", color="#f79640")
define m = Character("Moon Hare", color="#23b5eb")
define t = Character("Tiangou", color="#ddebf0")
define u = Character("???", color="#fff")


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
# Story One
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

    u "\"I see... it's quite nice to get out once in a while-- I finally have some time to stretch my legs out of that decreipt book\""

    "The creature does a wide stretch, similar to a cat's stretch after a bit he recomposes himself."

    d "I am Denglong, how may I help you today?"

menu question_denglong: 

    "What are you?!":
        d "I am \"Hou\", the great son of the Dragon King, but I am more known as \"Denglong\" amongst the common population"

        d "My job is to deliver the will of heaven onto the humans"

        d "...and help guide them on the right path."

        d "Does that suffice?"
        
    "Why were you in a book?":
        jump book_explanation

label not_me:

    u "I see..."

    u "..."

    u "...Deceit, however small..."

    u "...does not help you find the answers you desire."

    u "If you wish to find me again, try in another life."

    "The mysterious being returns into the book"

    jump n_ending

label book_explanation:

    "Test"

# ENDINGS

label n_ending:

    "Exiting my grandparents house, I wonder if there's a part of me I left in it."

    "I spend some time thinking about what ocurred but couldn't make any sense of it."

    "This discontent won't kill me but it'll surely be buried."

    "Ending 1/6: Buried Feelings"

    $ MainMenu(confirm=False)()

label denglong_ending:

    d "Denglong begins to start fading out"

    d "It seems like my energy is running out and I'll have to return into the book..."

    d "It might take a while... maybe 100 years before I can come out here again."

    d "It was nice to talk have a small chatter before going back."

    d "If I end up running into your folks I'll let them know that you are living your best, take care!"

    "As he ends his sentence he dissipates, as if the entire conversation has never happened."

    "Leaving the house, you resolve yourself to pursue your dreams"

    "Ending 2/6: Dug up Feelings"

    $ MainMenu(confirm=False)()

label moonhare_ending_good: 

    "You leave The house, a bit confused on what just happened-- but you take what the Moon Hare had to say about living life to the fullest."

    "You pull out your phone from your pocket and ring up your parents."

    yn "Hey mom..."

    yn "I'm thinking about maybe traveling for a little while."

    "Ending 3/6: The meaning of life"

    $ MainMenu(confirm=False)()

label tiangou_ending_good_one:

    "You find yourself in front of your grandparents house and think about all the wonderful things you did with them growing up."

    "Giving a bow to the house as a whole, you bid farewell and pay your respects one last time."

    "Ending 4/6: Eat Away my Moon"

    $ MainMenu(confirm=False)()

label tiangou_ending_good_two: 

    t "Alright! You have my blessing!"

    t ""

    "..."

    "..."

    "..."

    "Nothing really feels different, almost underwhelming really. It really is almost placebo."

    t "It won't be clear when it works but you'll probably be a little happier for the most part"

    t "I'm just passing on what your grandparents left behind ♫"

    t "I'm getting a bit sleepy {i}yawn{/i} I'll catch you later"

    "The fox recedes back into the book."

    "You spend some time thinking about what the Tiangou creature talked about."

    yn "Passing on what my grandparents left behind..."

    "You walk out of the house and you make a call."

    yn "Hey mom..."

    yn "I'd like to inherit the house"

    "Ending 5/6: Inheritance"

    $ MainMenu(confirm=False)()

label tiangou_ending_bad: 

    "You find yourself in front of a house that you don't recognize, but it is familiar."

    "You try to recall what happened in the past couple minutes..."

    "...but can't seem to put your finger on what you were doing in particular."

    "Checking the time on your watch you find that it's getting quite late and decide to go home."

    "Ending 6/6: Eat Away my Sun"

    $ MainMenu(confirm=False)()

    return
    
