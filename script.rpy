# The script of the game goes in this file
#For some reason all resources load in images folder instead of individual ones

label splashscreen:
    scene black
    with Pause(1)

    hide text with dissolve
    with Pause(1)

    return

label start:
    scene info
    play music "pallet_town.mp3" fadeout 1.0
    scene houses
    "I just moved into my new home town and helped my family unpack."
    pause
    define a = Character("Alice")
    show alice
    pause
    a "Hello, you must be the new kid around here. I'm Alice. What's your name?"
    $ b=renpy.input("What is my name?")
    while b.isalpha() == False:
        'Enter valid name.'
        $ b=renpy.input("What is my name?")
    b 'Hi my name is [b]'
    a "Nice to meet you! After you're done unpacking, want me to show you around?"
    menu:
        "Decline":
            $ choice1 = 1
            jump option1
        "Accept":
            $ choice1 = 2
            jump option2
label option1:
    b "Sorry, but I think it would be best to take a rest after all this manual labor"
    jump scene2
label option2:
    b "Sure!"
    jump scene2
label scene2:
    if choice1 == 1:
        a "Okay, no problem! We can hang out tomorrow since it's the weekend."
        jump scene3
    if choice1 == 2:
        a "Great! I'll bring you to the school so you know where to go on Monday. Then we can chill at the mall since there isn't much to do around here."
        jump scene4
label scene3:
    play music "sunlight.mp3" fadeout 1.0 fadein 1.0
    with dissolve
    scene breakfast
    'I am eating breakfast when my phone interrupts me from eating my cereal.'
    a 'Hey [b], ready to meet up?'
    menu:
        'Accept':
            jump option4
        'Decline':
            jump option5
label option4:
    b "Ok sure, I'll head over soon."
    'I unfortunately had to prematurely end my cereal session :('
    jump scene4
label option5:
    stop music
    b "I don't want to"
    jump end

label scene4:
    play music "royal.mp3" fadein 0.5
    scene nice_building
    'Alice and I are walking towards the school when I see a nice building. Maybe it won\'t be too bad going here.'
    b 'Is that our school Alice?!'
    a 'No, that building is owned by the rival school. This is the school we go to.'
    with dissolve
    scene scary_school
    'This is the school we go to? Aw man :(('
    play music "whos_there.mp3" fadeout 1.0
    b 'Wait who is that.'
    show dingo
    pause
    hide dingo
    show dingo_oliver
    b 'Who are you?'
    define oliver = Character('Oliver')
    stop music
    oliver 'I am Oliver and this is my dingo.'
    show Alice
    a "He's one of our teachers here."
    "But he's scary."
    a "Don't mind him, he's a lil weird. C'mon, let's go to the mall."
with dissolve
scene town
play music "<from 10>royal.mp3" fadeout 1.0 fadein 1.0
with dissolve
scene mall
show alice
a 'Here we are at the mall!'
b 'At least this place seems fine.'
show chad
a 'Hey Chad.'
define chad = Character('Chad')
default chad_interact = 0
chad "What's up?!"
'What should I do?'
menu:
    'Can you leave?.':
        $ choice2 = 1
    'Nothin much, nice to meet you, see you around I guess.':
        $ choice2 = 2
    'Back off.':
        $ choice2 = 1
if choice2 == 1:
    stop music
    chad 'Well, fine.'
    $ chad_interact = 1
if choice2 == 2:
    chad 'U2'
    $ chad_interact = 2
hide chad
play music "heart.mp3" fadeout 1.0 fadein 1.0
a 'How about we go look around and maybe find a movie to rent or something.'
b 'Aight'
hide alice
'Alice and I enter the Blockbuster and look around for movies. After looking for a bit, we narrowed our options down to these few choices.'
show scoob
show cheetah
show joker
'Which one should we get?'
menu:
    'Scoob!':
        $ movie = 1
    'The Cheetah Girls 2':
        $ movie = 2
    'Joker':
        $ movie = 3
if movie == 1:
    'We go with Scoob unfortunately.'
if movie == 2:
    'Thank God we went with the Cheetah Girls 2.'
if movie == 3:
    'We go with Joker, solid choice.'
hide scoob
hide cheetah
hide joker
'While walking around the mall, I see the GameStahp. I wanna get a video game.'
b 'Lets go there.'
'I look around for game to play and narrow the options to these few.'
show knack
show oneechan
show persona
'Which should I pick?'
menu:
    'Knack II':
        $ vidya = 1
    'Onechanbara Z2 Chaos: Banana Split Limited Edition':
        $ vidya = 2
    'Persona 5 Dancing in Starlight':
        $ vidya = 3
if vidya == 1:
    'I choose Knack II the best video game of all time, but also Onechanbara because it is also the best game ever.'
if vidya == 2:
    'I choose Onechanbara Z2 Chaos: Banana Split Edition, I have been dying to play this game.'
if vidya == 3:
    'I choose Persona 5 Dancing in Starlight. But I also get Onechanbara because it is the best game ever.'
with dissolve
scene houses
'We go home to watch the movie'
play music "memory.mp3" fadeout 1.0 fadein 1.0
with dissolve
scene family_room
if movie == 1:
    'I put Scoob into the DVD player. It started off kinda interesting, but became so weird.'
    'Halfway through the movie, it feels like it\'s not even the same movie, it\'s a rollercoaster lmaoo I love it.'
    'Finally we made it to the end, and oh my gosh it was awful, I think Alice started crying because we sat through it all and paid for the rental.'
if movie == 2:
    'I happily insert the Cheetah Girls 2 disk into the DVD player.'
    'This is my jam, but I had to contain myself as to not scare away Alice. Whenever she started singing along, I followed quietly.'
    'We made it to the end of the movie and I am holding back the tears. What a timeless masterpiece, gets me everytime.'
if movie == 3:
    'I put the Joker disk into the DVD player.'
    'Joaquin is doing great in this movie, though he looks like he needs to go to the hospital.'
    'We got to the end of the movie and I liked it, but Alice seems to be disturbed. I knew I should\'ve just gotten the Cheetah Girls 2 DVD instead.'
'After the movie is over, Alice gets ready to leave.'
play music "tender.mp3" fadeout 1.0
'Alice goes back home and I go to bed.'
play music "peaceful.mp3" fadeout 1.0 fadein 1.0
with dissolve
scene night
'I take a nice, peaceful sleep.'
'I lie down in bed and think how much time I\'ve been wasting and hopefully school tomorrow won\'t be too bad.'

play music "sunlight.mp3" fadeout 1.0 fadein 1.0
with dissolve
scene breakfast
'Today is the first day of school.'
play music "<from 10>royal.mp3" fadeout 1.0 fadein 1.0
with dissolve
scene scary_school
'I arrive at school and see alice in the distance.'
show alice
a 'Hi [b]!'
b "'Sup."
with dissolve
scene hall
'alice and I mostly have the same classes so we walk together down the hall. Further down, we see Chad.'
show chad
chad "What's up guys?!"
if chad_interact == 2:
    "Chad wraps his arm around me and starts tussling my hair."
    jump scene5
elif chad_interact == 1:
    'Chad smacks me in the face and starts beating me up. What should I do?'
    jump detention
label scene5:
    b 'Hi. Glad to see you, but Alice and I gotta head to class, see ya.'
    with dissolve
    hide chad
    'I hurried away to get to class. If I have to spend more time with Chad, I\'m gonna explode.'
    jump scene6
label detention:
    default bully = False
    menu:
        'Stand up for myself':
            $ brave = 1
        'Cry':
            $ brave = 2
        'Weird him out':
            $ brave = 3
    if brave == 1:
        'I pretend to be down, then I kick him in the knee. He falls down.'
        'I have detention with Chad.'
        play music "<from 30>wolf.mp3" fadeout 1.0 fadein 1.0
        'I ran away to go live the wolves.'
        jump end
    if brave == 2:
        'I started crying hopefully to guilt him into stopping, but in reality, I just looked stupid.'
        jump scene6
    if brave == 3:
        "I pretended to be into the beating and talked like Kyle's cousin to weird him out and get him to leave."
        'This tactic worked, and security came and chased after Chad down the hallway.'
        $ bully = True
        jump scene6

label scene6:
    play music "daylight.mp3" fadeout 1.0 fadein 0.5
    with dissolve
    scene classroom
    show dingo_oliver
    oliver 'Welcome back to another day of school. Today we have a new student. Hey [b] can you introduce yourself?'
    oliver 'Okay, so today we are gonna learn about Australia.'
    scene hall
    b 'I walk around the hallways looking for alice but I realize that this school is full of freaks.'
    b 'I really need to find alice.'
    'I run around the school until I run into alice.'
    show alice
    a '[b], ready to leave?'
    b 'Yes please.'

with dissolve
scene family_room
'We go home and she watches me play games for some reason. Probably has nothing better to do.'
'I remember that I bought some games that other day, but all I cared about was Onechanbara.'
'First, I played some Devil May Cry before playing Onechanbara to hype me up even more.'
play music "<from 80>dmc.mp3" fadeout 1.0
scene dmc
pause
'After, I play Onechanbara, it was exhilarating. However, the soundtrack was kind of a letdown so I put on some epic combat music in the background.'
play music "grandma.mp3" fadeout 1.0
scene onechanbara
a 'Why are you so weird?!'
'Alice leaves my house'

play music "peaceful.mp3" fadeout 1.0 fadein 1.0
with dissolve
scene night
'Now that no one here talks to me but my family, I don\'t have to deal with all the weirdos at school.'
if bully:
    play music "mask.mp3" fadeout 1.0 fadein 1.0
    with dissolve
    scene family_room
    'The school year went by slowly. Some people from the insane asylum got loose.'
    'The people at school and my family were telling me to not go out too late. Idk, I was too busy to listen. Hope it wasn\'t important.'
    play music "shrek.mp3" fadeout 1.0 fadein 1.0
    show shrek2
    'I was watching Shrek 2 on Blu-Ray in my family room on a typical, rainy night. My parents and sister were out.'
    'I heard the door open.'
    b 'Mom, can you cook some chicken tendies?'
    play music "whos_there.mp3" fadeout 1.0 fadein 1.0
    'I heard no response except for a muffled "What?"'
    b 'C\'mon dad you know you want some too.'
    hide shrek2
    'Now, no response. I hear some squeaky footsteps. I assume it\'s one of the clowns from the asylum. I turn around to see if he wanted to hang out and watch Shrek 2 on Blu-Ray with me.'
    show jason
    'I turn around and see some dude dressed as Jason Vorhees.'
    b '... So you wanna watch Shrek 2 on Blu-Ray?'
    'He starts walking towards me, menacingly.'
    'I get so scared, I tried to hop out of the window.'
    jump end
else:
    play music "<from 30>wakeup.mp3" fadeout 1.0 fadein 1.0
    with dissolve
    scene houses
    'The school year went by slowly.'

label end:
    play music "<from 60>plasticlove.mp3" fadeout 1.0 fadein 1.0
    scene end
    "The end"
return
