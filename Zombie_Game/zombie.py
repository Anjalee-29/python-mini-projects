import random

score = 0

print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣤⣤⣤⣤⣤⣤⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠾⠛⠉⠉⠀⠀⠀⠀⠀⠀⢀⡤⠊⠉⠉⠛⠳⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢮⡀⠀⠀⠀⠀⠀⠀⠙⢷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⡡⢤⠀⠀⠀⢰⣛⣉⣉⣓⠢⣄⠀⠀⠀⠈⢉⡁⠐⠒⠒⠂⠉⠉⠉⠛⢶⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡞⠁⣘⡒⠁⢀⠀⠀⠀⣀⣀⣀⣈⣹⣾⣕⠀⢠⡎⠁⡹⠀⣠⠄⠀⠀⠀⠀⠀⠀⠙⢷⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⢀⣎⡩⠃⢠⣏⡴⠞⠛⠉⠉⠀⠀⠀⠀⠹⡏⠀⠉⠉⣠⣾⠖⠋⠉⠻⣅⠀⣠⠖⢲⠌⢻⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⡠⠔⢿⠀⢀⡟⠉⠀⠀⠀⣀⣤⣤⡀⠀⠀⠀⣿⠀⠀⠀⡼⠉⠉⠒⢦⣀⠘⠷⡛⠒⡿⣄⠈⣷⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⡏⠀⣠⠏⠀⢸⠀⠀⠀⠀⢰⣿⣿⣿⡇⠀⠀⢀⡿⠀⠀⣸⠃⠀⠀⣀⣄⡙⢷⣄⡇⠘⠀⢸⡆⢹⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⣧⠞⠁⠀⠀⢸⡆⠀⠀⠀⠸⣿⣿⡿⠃⠀⢀⣼⠃⠀⠀⣿⣆⠀⠀⣿⣿⡟⠀⠙⣧⠳⡤⠞⠀⢸⡇⠀⠀⠀⠀
⠀⢀⣠⠤⠤⢄⡀⠈⣧⢈⣧⠀⠀⢸⣿⣄⣀⣀⣠⣬⣥⠴⠶⢚⣿⠋⠀⠀⠀⢻⣿⣦⣄⠈⠁⠀⠀⣰⠟⠆⠀⠀⠀⢸⣡⠴⠖⠶⣦
⢠⠏⠀⠀⠀⢀⠈⠓⢿⡄⢳⠀⠀⠀⢳⣌⠻⠯⣤⣀⣀⣀⣴⣿⠏⢀⣶⢰⣦⠈⢿⣿⣿⣷⣀⣠⡼⠋⠀⢀⡀⠀⢀⣿⠥⢄⠀⠀⣿
⣏⠀⠀⠀⡟⢉⡽⣦⡈⢻⣼⠄⠀⠀⠀⠉⠓⠦⠤⠬⣏⣡⠾⠃⢀⣾⣿⢸⣿⣇⠈⠻⡯⠽⢯⡽⠁⠠⣴⠝⠃⢀⣾⢋⣁⠈⢀⡾⠃
⠘⠶⠲⢦⣷⠸⣤⣸⡇⠀⢻⣦⡀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠘⠛⠋⠘⠋⠋⠀⠀⠑⠚⠉⠀⠀⠀⠈⣠⣠⡾⠳⠤⣿⡀⣾⠁⠀
⠀⠀⠀⠀⠸⢧⠉⠉⠀⢀⡾⠀⠉⠻⣦⠀⠀⠀⠈⢟⡽⠄⠀⠀⢀⣀⣤⣤⣤⣄⣀⠀⠀⠀⢀⡀⠀⠀⣴⡿⠛⠻⢶⣤⣿⡿⠋⠀⠀
⠀⠀⠀⠀⠀⠙⠒⠒⠚⠋⠀⠀⠀⠀⠸⣧⠀⠀⠀⠀⠁⠀⣠⣾⡿⢿⠀⠀⢀⣮⣙⡻⣦⡈⠙⠿⠀⣸⠏⠀⠀⠀⠀⢀⣿⣇⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡆⠀⠀⠀⠀⣼⣿⣿⣇⣸⣷⣶⣾⡀⣯⣻⣿⣿⡄⠀⠀⡿⠀⠀⠀⠀⠀⢻⣾⡛⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⡇⠀⠀⠀⠀⠀⠀⠛⠟⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⡀⠀⢸⣿⣿⡟⢻⡿⠿⣇⣿⢸⠿⣿⣿⣿⡏⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠐⡇⠀⠸⣯⠉⠙⠒⣃⣀⣈⣭⣭⣤⣀⣩⡟⠁⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡄⠃⠀⣀⣽⠷⠞⠛⠉⠉⠁⠀⣠⠤⠤⢤⣉⠙⠢⠤⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⠀⠘⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣶⠀⠹⠂⠀⣰⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠛⠶⢦⣤⣀⣀⠀⠀⠀⠀⢀⣈⣛⣥⣤⠴⠾⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
print("Take this quiz and find out how long you would survive amongst the walking dead.")
print("There are easy, intermediate and hard questions all mixed together.")
print("There may be more than one correct answer.\nGood luck!\n")

# ---- question 1 ----
print("Q1. Your house is burning down. What do you save?")
print("""(1) your dog
(2) some food cans
(3) your clothes
(4) your cell phone""")
answer = input("> ")

if answer == "1":
    score += random.randint(10, 20)
elif answer == "2":
    score += random.randint(5, 10)
else:
    score += 3

print("")

# ---- question 2 ----
print("Q2. It is night, and you will freeze to death soon. Making too much noise/light will attract zombies. What do you do?")
print("""(1) keep moving around
(2) build a tiny fire
(3) build a normal fire
(4) try to wait out the night""")
answer = input("> ")

if answer == "2":
    score += random.randint(10, 20)
elif answer == "4":
    score += random.randint(5, 10)
else:
    score += 3

print("")

# ---- question 3 ----
print("Q3. You are cornered in a grocery store with only a knife. A horde is moving in from all sides. What do you do?")
print("""(1) kill zombies to make a path
(2) try to climb up on the wobbly shelves
(3) shout for help
(4) accept your fate""")
answer = input("> ")

if answer == "2":
    score += random.randint(10, 20)
elif answer == "1":
    score += random.randint(5, 10)
else:
    score += 3

print("")

# ---- question 4 ----
print("Q4. You see a group of survivors ahead on the road. What do you do?")
print("""(1) watch them for a while
(2) ignore them
(3) kill them and steal their stuff
(4) try to greet them""")
answer = input("> ")

if answer == "1":
    score += random.randint(10, 20)
elif answer == "3":
    score += random.randint(5, 10)
else:
    score += 3

print("")

# ---- question 5 ----
print("Q5. A group of about 6 people take your stuff at gunpoint, then tell you to get in a storage container. What do you do?")
print("""(1) get in the container
(2) try to reason with them
(3) refuse
(4) try to fight them""")
answer = input("> ")

if answer == "1":
    score += random.randint(10, 20)
elif answer == "4":
    score += random.randint(5, 10)
else:
    score += 3

print("")

# ---- question 6 ----
print("Q6. You and 3 other people are down to 1 last can of food. What do you do?")
print("""(1) share it
(2) eat it yourself
(3) give it to them
(4) burn it so there is no argument""")
answer = input("> ")

if answer == "2":
    score += random.randint(10, 20)
elif answer == "1":
    score += random.randint(5, 10)
else:
    score += 3

print("")

# ---- question 7 ----
print("Q7. You are given the choice between 4 weapons. What do you take?")
print("""(1) katana
(2) crossbow
(3) pistol
(4) RPG""")
answer = input("> ")

if answer == "2":
    score += random.randint(10, 20)
elif answer == "3":
    score += random.randint(5, 10)
else:
    score += 3

print("")

# ---- question 8 ----
print("Q8. You only have room in your pack for 1 more package of food. What do you take?")
print("""(1) trail mix
(2) crackers
(3) oreos
(4) raw chicken""")
answer = input("> ")

if answer == "3":
    score += random.randint(10, 20)
elif answer == "4":
    score += random.randint(5, 10)
else:
    score += 3

print("")

# ---- question 9 ----
print("Q9. You have some choices on where to set up camp.")
print("""(1) next to the river
(2) in the mountains
(3) near the ocean
(4) next to the city""")
answer = input("> ")

if answer == "1":
    score += random.randint(10, 20)
elif answer == "2":
    score += random.randint(5, 10)
else:
    score += 3

print("")

# ---- question 10 ----
print("Q10. Your camp, with your group of ~20 people, has been overrun by a horde. What do you do?")
print("""(1) follow your friends
(2) run
(3) try and save the camp
(4) get your stuff from your tent""")
answer = input("> ")

if answer == "3":
    score += random.randint(10, 20)
elif answer == "4":
    score += random.randint(5, 10)
else:
    score += 3

print("")

# ---- end ----
print("The results are in!")
print("You scored {} points.\n".format(score))

if score in range(0, 6):
    print("You would be one of the first people to die in the apocalypse.\nYou panic at the sight of a zombie and have no survival skills, getting eaten within an hour.\nPathetic.")
elif score in range(6, 21):
    print("You would live a few hours in the apocalypse.\nAs the chaos begins, you make a desperate attempt to save your stuff.\nGetting into the car, you get surrounded.\nThey break open the windows and eat you.\nThat must suck.")
elif score in range(21, 51):
    print("You would live a few days in the apocalypse.\nAs the chaos begins, you attempt to go to the emergency shelters.\nYou die when they get overcrowded and overrun.\nToo bad.")
elif score in range(51, 81):
    print("You would live a month in the apocalypse.\nYou find a camp and manage to survive for a month, but when the camp gets overrun, you get bit.\nSo close, yet so far.")
elif score in range(81, 111):
    print("You would live a few months in the apocalypse.\nYour camp moves from place to place before settling at an old school building.\nAfter living there for a month, you accidentally shoot yourself with a crossbow while attempting to load it.\nAt least you tried.")
elif score in range(111, 131):
    print("You would live a few years in the apocalypse.\nYour group settles at a town in Tennessee, fortifying it so that it can withstand a horde.\nWhile on a run, you fall through a floor and break your leg, attracting zombies and getting eaten.\nYou will be remembered.")
else:
    print("You would live for a really long time in the apocalypse.\nBeing the leader of your group, you settle at a town near the beach, where hardly any hordes pass through.\nYou help build a utopia named Z-Land.\nAt the age of 79, you pass away in your sleep.\nThere was a statue of you built.")
