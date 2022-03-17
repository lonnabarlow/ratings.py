"""Restaurant rating lister."""



"""read in the scores file and get RestaurantName:Rating"""

scores_txt = open('scores.txt')

scores = {}

for line in scores_txt:
    line = line.rstrip()
    restaurant, score = line.split(":")
    scores[restaurant] = int(score)


print(scores)
print("Add a new rating for a restaurant")

restaurant = input("Restaurant Name: ")

rating = int(input("rating: "))
scores[restaurant] = rating
print(scores)
# sort by key alphabetically
scores = sorted(scores.items())

#print the ratings
print(rating)
