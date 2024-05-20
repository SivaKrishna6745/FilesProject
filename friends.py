# Ask the user for a list of 3 friends
# For each friend, we'll tell the user whether they are nearby
# For each nearby friend, we'll save their name to "nearby_friends.txt"

friends = input("Enter 3 friends names separated with a ', ': \n").split(', ')

people = open('people.txt', 'r')
people_content = [ line.strip() for line in people.readlines()]
people.close()

nearby_friends_txt = open('nearby_friends.txt', 'w')
for friend in people_content:
    if friend in friends:
        print(f'{friend} is a nearby friend')
        nearby_friends_txt.write(f'{friend}\n')
nearby_friends_txt.close()

