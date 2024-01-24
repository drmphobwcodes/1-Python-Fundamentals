state_capitals = {"Washington": "Olympia",
                    "Oregon": "Salem", "California": "Sacramento"}
#print(state_capitals["Washington"])
state_capitals["Washington"] = "Aberdeen"
print(state_capitals["Washington"])
print(state_capitals)
del state_capitals["California"]
#print(state_capitals)

state_capitals.pop("Oregon")
print(state_capitals)