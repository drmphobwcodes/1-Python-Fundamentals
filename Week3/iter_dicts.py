state_capitals = {"Washington": "Olympia",
                    "Oregon": "Salem", "California": "Sacramento"}

'''for state in state_capitals:
    print( state)'''

for state, city in state_capitals.items():
    print(city, "is the capital of", state )

