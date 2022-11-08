#Joel Avery 11/7/22 Module 4 Assignment

''' program creates a tuple with 15-25 related values, initializes with values
    displays contents in a single statement
    iterates through the collection displaying the output as a single complete
    sentence for each value using f string to control the output. 
    Repeats the output in reverse order using a different context string.'''

#tuple intiliazed with states. 
states = ('Alabama', 'Alaska', 'Georgia', 'Kentucky', 'Texas', 'Missouri', 
    'Nebraska', 'Kansas', 'Washington', 'Flordia', 'Colorado', 'Oklahoma', 
    'Arizona', 'New Mexico', 'New York', 'Pennsylvania', 'Arkansas', 
    'Louisiana', 'California')

#prints the tuple contents in a single statement unpacking the tuple
print("Some states in the United States are", *(states))

#prints new line for space
print()

#iterates through the tuple, and and outputs the statement cleanly using fstring. 
for state in states: 
    print(f"I have been to {state} before!")

#prints a new line for space and readability
print()

#prints the tuple in reverse order using a loop and the reversed method. 
for state in reversed(states): 
    print(f"One of my favorite states is {state}!")


