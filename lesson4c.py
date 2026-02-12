# A for loop can also be used to iterate through a list ,tuple,string or even a dictionary.

name = "Telvin"

for letter in name:
    if letter  == "l":
        print("This is letter L")
    else:
        print(letter)

print("===========================")
# Below is alist of counties
counties  = ["Nairobi" , "Mombasa","Kisumu","Nakuru", "Eldoret","Kajiado","Machakos","Meru","Embu"]
print(counties)

for county in counties:
    print(county)

print("===========================")
if "Nakuru" in counties:
    print("Nakuru found")

else:
    print("Nakuru not found")

print("===========================")
# the for loop can be used to iterate through a dictionary

player = {
    "name":"Mbappe",
    "age": 25,
    "teams":["PSG","Real","France"],
    "Nationality":"French"
}

for key in player:
    print(key)

for x in player:
    print(player[x])

print("===========================")
# loop through the teams he has played for
for teams in player["teams"]:
   print(teams)