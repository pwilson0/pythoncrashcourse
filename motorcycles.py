# activity 3.4 - invite famous dead people to dinner
deadpoets = ['keats', 'tennyson', 'williams']
print("The poet " + deadpoets[0].title() + " is hereby invited to dinner.")
print("The poet " + deadpoets[1].title() + " is hereby invited to dinner.")
print("The poet " + deadpoets[2].title() + " is hereby invited to dinner.")

# activity 3.5 - add to that guest list
print("Just kidding, the poet " + deadpoets[2].title() + " will not be able to attend.")
del deadpoets[2]
deadpoets.append("rilke")
print("The poet " + deadpoets[0].title() + " is hereby invited to dinner.")
print("The poet " + deadpoets[1].title() + " is hereby invited to dinner.")
print("The poet " + deadpoets[2].title() + " is hereby invited to dinner.")

# activity 3.6 - more guests
print("The table just got 10 feet longer!")
deadpoets.insert(0, "shelley")
deadpoets.insert(2, "shakespeare")
deadpoets.append("milton")
print("The poet " + deadpoets[0].title() + " is hereby invited to dinner.")
print("The poet " + deadpoets[1].title() + " is hereby invited to dinner.")
print("The poet " + deadpoets[2].title() + " is hereby invited to dinner.")
print("The poet " + deadpoets[3].title() + " is hereby invited to dinner.")
print("The poet " + deadpoets[4].title() + " is hereby invited to dinner.")
print("The poet " + deadpoets[5].title() + " is hereby invited to dinner.")

# activity 3.7 - the list shrinks
print("Actually, I can only invite two people to dinner. How embarrassing!\nThe table just got 10 feet shorter.")
deadpoets_popped = deadpoets.pop()
print("Sorry, " + deadpoets_popped.title() + " there's just no room for you at the table.")
deadpoets_popped = deadpoets.pop()
print("Sorry, " + deadpoets_popped.title() + " there's just no room for you at the table.")
deadpoets_popped = deadpoets.pop()
print("Sorry, " + deadpoets_popped.title() + " there's just no room for you at the table.")
deadpoets_popped = deadpoets.pop()
print("Sorry, " + deadpoets_popped.title() + " there's just no room for you at the table.")
print("Whew, " + deadpoets[0].title() + ", so glad we were able to ditch those bores.")
print("Whew, " + deadpoets[1].title() + ", so glad we were able to ditch those bores.")
del deadpoets[0]
del deadpoets[0]
print(deadpoets)