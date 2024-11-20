define yn = Character("[You]")
define d = Character("Denglong", color="#f79640")
define m = Character("Moon Hare", color="#23b5eb")
define t = Character("Tiangou", color="#ddebf0")
define u = Character("???", color="#fff")

transform hare_position:
    zoom 0.8
    xpos 1000

transform t_position:
    zoom 0.8
    xpos 1000

transform d_position:
    zoom 0.8
    ypos 1500
    xpos 2200

label start:

    $ You = renpy.input("What is your name?", "Yu", length=15, exclude=" 0123456789+=,.?!<>{}[]").strip() or "Badmustard"
    # yn "Hello World"

    # d "Denglong"

    # r "Moon Hare"

    # l "Tiangou"

    # "Narration"

    # show moon hare happy
    
    scene day with fade

    "You are visiting your grandparents estate after their unfortunate passing, hoping to spend some time there before it's eventually cleaned up and sold off."

    "It was a long time coming, your grandfather even joked about it, saying that grandma and him would be going together"

    "Suprisingly they were right--"

    "The funeral wasn't too sad, my grandparents were always an adventurous duo and it was closer to a celebration of their life. Not bad at all but still, I felt empty."

    scene study with fade

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
    
    "A blue book with a bubbly textured cove":
        jump story_two

    "A red book with leaf printed on the cover":
        jump story_three

# Story One
label story_one:

    "You open the book and a light flashes from the book."
    
    show denglong silouhette at right with fade:
        zoom 0.8
        ypos 1500
        xpos 2200
    
    "A strange beast pops out of the book. Landing on the ground on all fours. At a glance you can tell it has several features of different animals. Kinda like a chimera from fantasy novels."

    "\"Aren't though the one who summoned me?\""

    "It speaks in a majestic manner. "

menu: 

    "Yes, it was me.":
        jump was_me

    "No, it was not.":
        jump not_me

label was_me: 
    
    show denglong happy at right:
        zoom 0.8
        ypos 1500
        xpos 2200

    u "\"I see... it's quite nice to get out once in a while-- I finally have some time to stretch my legs out of that decreipt book\""

    "The creature does a wide stretch, similar to a cat's stretch after a bit he recomposes himself."

    d "I am Denglong, how may I help you today?"

menu question_denglong: 

    "What are you?!":
        
        show denglong default at right:
            zoom 0.8
            ypos 1500
            xpos 2200
            
        d "I am \"Hou\", the great son of the Dragon King, but I am more known as \"Denglong\" amongst the common population"

        d "My job is to deliver the will of heaven onto the humans"

        d "...and help guide them on the right path."

        d "Does that suffice?"

        menu:

            "I think so":
                jump question_denglong
            
            "Why were you in a book?":
                jump book_explanation
        
    "Why were you in a book?":
        jump book_explanation

label not_me:

    show denglong disappointed at right:
        zoom 0.8
        ypos 1500
        xpos 2200

    u "I see..."

    u "..."

    u "...Deceit, however small..."

    show denglong default at right:
        zoom 0.8
        ypos 1500
        xpos 2200

    u "...does not help you find the answers you desire."
    
    u "If you wish to find me again, try in another life."
    
    hide denglong default with dissolve

    "The mysterious being returns into the book"

    jump n_ending

label book_explanation:

    d "I'm not too sure myself {i}haha{/i}"

    d "But it wouldn't be wise to delve into the details otherwise it'd take all day"

    d "So I'd urge you to let it be, you don't get to talk to a messenger from heaven every day."

    menu:

        "Ask about my grandparents":
            jump denglong_grandparents
        
        "Ask about heaven":
            d "Heaven itself is more of a concept."

            d "To some it might be like paradise, while to others it's like a rest point."

            d "They are able to be comforted in the fact their lives don't ultimately end after dying."

label denglong_grandparents:

    show denglong pleading at right:
        zoom 0.8
        ypos 1500
        xpos 2200

    d "Your grandparents?"

    "You nod asking them about if you've seen them there"

    d "Unfortunately, I have not"

    show denglong default at right:
        zoom 0.8
        ypos 1500
        xpos 2200

    d "If I had to describe what heaven felt like..."

    d "It'd be like a vast ocean of souls, waiting for the tides to take them to their next journey."

    d "There's very little distinction between each soul"

    d "and trying to find specific souls would very like trying to find a needle in a haystack"

    menu:

        "Do you know if they'll be okay?":
            jump denglong_okay

        "I see...":
            d "It seems like my time here is done for now"

            d "I can't spend too long outside of the book or else I'm overcome with extreme fatigue"

            d "A quirk of being a myth in a modern era"

            d "I believe I'll be asleep for a little while"

            show denglong sleeping at right:
                zoom 0.8
                ypos 1500
                xpos 2200

            d "... maybe 80 years... {i}yawn{/i} remember to live well."

            "The beast recedes back into the book, the book seems to have lost a lot of it's spark, you probably won't be able to call for him again."

            jump n_ending

label denglong_okay: 

    show denglong happy at right:
        zoom 0.8
        ypos 1500
        xpos 2200

    d "Oh don't worry!"

    show denglong default at right:
        zoom 0.8
        ypos 1500
        xpos 2200

    d "They'll be fine."

    d "Souls must be reincarnated otherwise they become fragmented and corrupted"

    d "Turning into mindless beasts, preying for other souls to fufill their own fragmented soul in an endless loop."

    d "That's why I exist, to make sure that doesn't happen."

    d "But that's quite a rarity nowadays, heaven is already quite meticulous, I don't need to intervene unless necessary"

    d "You must care a lot about your grandparents, dont you?"

    menu:

        "I guess I do...":
            
            "For some reason you begin to tear up."

            d "It's okay to let it out, I can hear you out"

            scene denglongsit with fade

            "Denglong lays down and you sit next to him"

            "You talk a lot about your grandparents, you talk about how you regret not being able to be there at their deathbeds."

            "You talk about being at their house a lot since your parents were working fulltime jobs"

            "You talk about the memories you made with them."

            "At some point your tears had became full on sobbing then found yourself running out of tears after letting it all out."

            "But you felt a lot better now."

            "Denglong had been attentively listening to your story, something that no one else could have really done."

            d "You loved them a lot but couldn't really speak about it due to how it all happened right?"

            d "..."

            d "Souls are often afraid of being forgotten."  

            d "I think they would be proud of having a grandchild like you."

            menu:

                "Thank you":
                    jump denglong_ending

label story_two: 

    "You open the book and a light flashes from the book."

    "A strange beast pops out of the book."

    "Landing with a light hop, a small rabbit bounces and makes it's personality quite apparent."

    show h-silouhette at hare_position
    with fade

    u "Yo! You the one who called?"

    menu:

        "Yeah...!!!":
            jump yeah_exclamation

        "Yeah...?": 
            jump yeah_question

label yeah_exclamation:

    m "I like your energy, I'm known as a Moon Hare, a {i}*very*{/i} kind and *very* helpful servant of the Moon Goddess."

    show h-Default at hare_position

    "A little perplexed at the situation of a speaking rabbit, you try to maintain your composure."

    show h-excited at hare_position

    m "I'm responsible for making rice cakes for the goddess, and I make mean one, care to try one?"

    "The Hare pulls out one of their rice cakes from seemingly out of nowhere!"

    "The rice cake it about the size of it's paw and it gives you puppy dog eyes as if begging you to try one."

    menu: 

        "Try a rice cake":
            jump trying_cake

        "Refuse rice cake":
            
            "The rabbit is saddened by your refusal, drooping it's ears down visibly."

            show h-sad at hare_position

            m "I guess this was a waste of time... not even a mortal wants my rice cake {i}sob{/i}"

            "The creature recedes back into the book."

            jump n_ending

label trying_cake:

    show h-Default at hare_position

    "You take a bite..."

    "and it's suprisingly good! There's a lot of depth to it despite seemingly presenting itself as a normal rice cake."

    "There's a bit of a fruity taste in it, but it isn't overwhelming, you could eat it in a savoury meal."

    "There's also a lot of texture in it, you can chew it quite well and it's quite compelling for another bite!"

    m "So how is it?"

    "The Hare looks at you expecting praise for it's masterpiece."

    menu: 

        "It was great!":
            jump rice_cake_great


        "Could've been better":
            
            "The rabbit is instantly dejected and it's ears droop down in a sad twist of fate."

            show h-sad at hare_position

            m "Is that so..."

            "You feel a little bad, but it was your honest opinion..."

            show h-default at hare_position

            m "I guess I'll have to work harder! I'll catch you later and come back with an even better cake! In maybe 50 or so years!"

            yn "Fifty-?!"

            "Before you can get another word in the rabbit recedes back into the book"

            jump n_ending

label rice_cake_great:

    "I know right!!! It even gives you immortality!! Isn't that wonderful!" 

    show h-snicker at hare_position

    "The rabbit gives a sly sneer"

    menu:

        "It gives me what?!":

            show h-excited at hare_position

            m "I'm just kidding!"

            yn "(Urgh...)"

            yn "(This rabbit is tiresome)"

            show h-default at hare_position

            m "Immortality isn't something I can give out just like that."

            show h-happy at hare_position

            m "So I just gave you my personal ones I made to eat"

            "You give a sigh of relief"

            m "Humans are made to live to the fullest within their limited lifespans."

            m "If you aren't happy now then what's the point?"

            m "There is a reason why all living beings struggle to achieve content in their lives."

            m "It gives meaning to existence!"

            m "If I were to hand over immortality at the drop of a hat, life would have no meaning anymore."

            menu: 

                "Then what about you?": 

                    show h-default at hare_position
                    
                    m "Like I said, I serve the Moon Goddess, I'll probably be doing that for a long time to come {i}hehe{/i}"

                    m "My immortality gives the ability to do that so I'm content with where my life is now!"

                    show h-sleepy at hare_position

                    m "{i}yawn{/i}"

                    m "It seems like I was out for too long... I'll have to go back soon"

                    m "Remember find yourself a reason and even immortality isn't a concern!"

                    m "Take care!"

                    "And just like that the rabbit hops right back into the book"

                    "The book loses it's shimmer and luster"

                    jump moonhare_ending_good

# Story Three
label story_three: 

    "You open the book and a light flashes from the book."

    "A strange beast pops out of the book."

    "You hear a skip sound and 4 legs touch the ground and a white fox seemingly appears out of nowhere."

    show t-shaded at t-position
    with fade

    u "Are you the loathesome human who called me?"

    menu: 

        "Loathesome?!":

            u "I mean what I said"

            menu: 

                "Who are you?":
                    jump tiangou_who

        "Yeah...?":

            u "Rightfully so I guess"

            menu:

                "Who are you?":
                    jump tiangou_who

label tiangou_who:

    show t-default at t-position
    with fade

    t "I am Tiangou, a spirit known for many things" 

    show t-snicker at t-position
    with fade

    t "It jeers with a sly smile"

    t "what about you?"

    menu: 

        "I am [yn]":
            jump tiangou_me

        "...":
            t "Not even a word?"

            show t-frown at t-position
            with fade

            t "What a waste of time"

            "The beast recedes back into the book without much of another word"

            jump n_ending

label tiangou_me: 

    show t-closed at t-position
    with fade

    t "Is that all?"

    t "Is there anything else? A title? nickname?"

    t "Not too sure yourself, right? You just go along with what others do."

    "You're not sure what brought this on but the beast is right"

    "Even at your grandparents funeral it was like this."

    t "Don't worry! You're still young and have a lot of time to find out."

    t "How about this uncle fox help you out a bit"

    show t-snicker at t-position
    with fade

    "The beast gives off a little jeering smile"

    t "I am known for many things."

    t "To some, I'm an arbiter for protection"

    t "... to others I eat away at their light, their sun."

    "The wolf pauses, you felt as if impending doom was fast approaching."

    show t-closed at t-position
    with fade

    t "But that's a rarity these days! I'm pretty much retired these days {i}haha{/i}"

    "... You give a slight sigh of relief"

    t "If you need any advice, I'm all pointy ears!"

    menu:

        "What do you mean by protection?":
            
            show t-default at t-position
            with fade

            t "Simple, I just give my blessings!" 

            show t-sneer at t-position
            with fade

            "The wolf proudly declares"

            t "... although it's placebo at best since it only prevents bad things from happening, you'd never really notice it."

            show t-closed at t-position
            with fade

            t "Your grandparents actually had my blessings" 

            "!!!"
            
            show t-default at t-position
            with fade

            t "Did you think that they when they passed together it was simply coincidental?"

            t "My blessings simply equalized their remaining life and they were content with that."

            t "It's very objective. I have no hand in the results or consequences of what bad actually means."

            t "Say... what do you think about receiving my blessing? Your grandparents had it."

            menu: 

                "Give me the blessing":
                    jump tiangou_ending_good_two

                
                "You're too suspicious":
                    
                    t "Alright but if you ever change your mind let me know!"

                    show t-sleepy at t-position
                    with fade   

                    t "I'll... just... {i}yawn{/i} take a nap for a while"

                    "The fox recedes back into the book seemingly exhausted."

                    "You take a moment to comprehend what just happened but you are glad to know a little more about what happened with your grandparents."

                    hide t-sleepy with fade

                    jump n_ending

        "What does eating the sun look like?":

            show t-default at t-position
            with fade   

            t "It's as you think, metaphorically and literally, although the latter I was made to spit it back out"

            t "...it's not like it was tasty or anything!"

            show t-sneer at t-position
            with fade   

            "You can see a small amount of saliva drooling from it's mouth"

            "You wish you hadn't seen that"

            t "But what I basically do is eat away the lights of peoples lives, this also works in vice versa"

            t "Is that something that interests you?"

            menu:

                "Eat away my sun": 
                    jump tiangou_ending_bad

                "Eat away my moon":
                    jump tiangou_ending_good_one

# ENDINGS

label n_ending:
    
    scene sunset with fade

    "Exiting my grandparents house, I wonder if there's a part of me I left in it."

    "Was what I saw real? Or maybe I've just been overworking too hard."

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

    scene sunset with fade

    "Leaving the house, you resolve yourself to pursue your dreams"

    "Ending 2/6: Dug up Feelings"

    $ MainMenu(confirm=False)()

label moonhare_ending_good: 

    scene sunset with fade

    "You leave The house, a bit confused on what just happened-- but you take what the Moon Hare had to say about living life to the fullest."

    "You pull out your phone from your pocket and ring up your parents."

    yn "Hey mom..."

    yn "I'm thinking about maybe traveling for a little while."

    "Ending 3/6: The meaning of life"

    $ MainMenu(confirm=False)()

label tiangou_ending_good_one:

    scene sunset with fade

    "You find yourself in front of your grandparents house and think about all the wonderful things you did with them growing up."

    "Giving a bow to the house as a whole, you bid farewell and pay your respects one last time."

    "Ending 4/6: Eat Away my Moon"

    $ MainMenu(confirm=False)()

label tiangou_ending_good_two: 

    scene tmoon with fade

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

    scene sunset with fade

    "You walk out of the house and you make a call."

    yn "Hey mom..."

    yn "I'd like to inherit the house"

    "Ending 5/6: Inheritance"

    $ MainMenu(confirm=False)()

label tiangou_ending_bad: 

    scene tsun with fade

    scene night with fade

    "You find yourself in front of a house that you don't recognize, but it is familiar."

    "You try to recall what happened in the past couple minutes..."

    "...but can't seem to put your finger on what you were doing in particular."

    "Checking the time on your watch you find that it's getting quite late and decide to go home."

    "Ending 6/6: Eat Away my Sun"

    $ MainMenu(confirm=False)()

    return
    
