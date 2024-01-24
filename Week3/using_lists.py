states = ["Washington", "Oregon", "California"]

'''for state in states:
    state = state.lower()
    print(state)


print("Washington" in states)
print("Tennessee" in states)
print("Washington" not in states)
'''
states2 = ["Arizona", "Ohio", "Louisiana"]
best_states = states + states2
print(best_states)
print(len(best_states))
#retrieves list items with index 1-3 not including 3(so index 1 and 2)
print(best_states[1:3])
#retrieves list item from index 3 to the end
print(best_states[3:])
#retrieves list item from index 0 to index 2 not including 2(so index 0 and 1)
print(best_states[:2])
#retrieves list item from index 0 to index 4 not including 4(so index 0,1,2,3)
print(best_states[4])