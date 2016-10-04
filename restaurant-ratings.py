import random

def get_restaurant_ratings(rating_file):
    restaurants_and_ratings = {}
    
    with open(rating_file) as restaurant_ratings:
        for restaurant_line in restaurant_ratings:
            restaurant, rating = restaurant_line.rstrip().split(':')
            restaurants_and_ratings[restaurant] = rating

    while True:
        print "\n"
        print ("Would you like to see restaurant ratings (1), or rate"
               " a new restaurant(2), or update a random restaurant's rating(3),"
               " or quit(4)?")
        user_choice = raw_input("Make your choice: ")

        if user_choice == '1':
            sorted_restaurants = sorted(restaurants_and_ratings.items())

            for restaurant, rating in sorted_restaurants:
                print "{} is rated at {}.".format(restaurant, rating)

        elif user_choice == '2':
            user_restaurant = raw_input("Please provide a restaurant name: ")
            user_rating = raw_input("Please provide the restaurant's rating (1-5): ")

            restaurants_and_ratings[user_restaurant] = int(user_rating)

        elif user_choice == '3':
            random_rest = random.choice(restaurants_and_ratings.keys())
            print ("What is your new rating for {}. Current rating."
                  " is {}".format(random_rest, restaurants_and_ratings[random_rest]))
            user_new_rating = raw_input("Enter rating between 1 and 5: ")

            restaurants_and_ratings[random_rest] = int(user_new_rating)
        
        elif user_choice == '4':
            break
        
        else:
            print "Try again"

get_restaurant_ratings('scores.txt')
