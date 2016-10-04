import random

def display_restaurants(display_ratings, restaurants):
    """ Displays all restaurants with optional ratings """
    sorted_restaurants = sorted(restaurants.items())

    if display_ratings:
        for restaurant, rating in sorted_restaurants:
            print "{} is rated at {}.".format(restaurant, rating)
    
    else:
        for restaurant, rating in sorted_restaurants:
            print "{}".format(restaurant)


def rate_restaurants(rating_file):
    """ Interactive tool allowing user to view, add, and update restaurant
         ratings"""
    restaurants_and_ratings = {}
    
    with open(rating_file) as restaurant_ratings:
        for restaurant_line in restaurant_ratings:
            restaurant, rating = restaurant_line.rstrip().split(':')
            restaurants_and_ratings[restaurant] = rating

    while True:
        print "\n"
        print ("Would you like to see restaurant ratings (1), or rate"
               " a new restaurant(2), or update a restaurant's rating(3),"
               " or quit(4)?")
        user_choice = raw_input("Make your choice: ")

        if user_choice == '1':
            # Display restaurants with ratings
            display_restaurants(True, restaurants_and_ratings)

        elif user_choice == '2':
            user_restaurant = raw_input("Please provide a restaurant name: ")
            user_rating = raw_input("Please provide the restaurant's rating (1-5): ")

            restaurants_and_ratings[user_restaurant] = int(user_rating)

        elif user_choice == '3':
            # Display restaurants without ratings
            display_restaurants(False, restaurants_and_ratings)
            chosen_rest = raw_input("Enter the restaurant to rate: ")

            if chosen_rest in restaurants_and_ratings:
                user_new_rating = raw_input("Enter rating between 1 and 5: ")
                restaurants_and_ratings[chosen_rest] = int(user_new_rating)
            else:
                print "You have chosen an invalid restaurant."
        
        elif user_choice == '4':
            break
        
        else:
            print "Try again"

rate_restaurants('scores.txt')
