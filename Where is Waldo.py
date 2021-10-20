people = ["Waldo","Jackson","Ray","Eric","Vaughn","Jesse","Herbert","Robert", "Rodrigo","Elija","Sasha","Nathaniel","Ellie","Allison","Jeremiah", "Paula", "Alisha","Tory","Troy", "Faye"]
random.shuffle(people)
zin = "Waldo zit op stoelnummer:"

print(people)
index = 0
for x in people:
    if x == "Waldo":
        print(zin, index)
    index += 1