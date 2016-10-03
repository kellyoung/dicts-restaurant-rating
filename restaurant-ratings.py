def get_restaurant_ratings(rating_file):
    restaurants_and_ratings = {}
    
    with open(rating_file) as restaurant_ratings:
        for restaurant_line in restaurant_ratings:
            restaurant, rating = restaurant_line.rstrip().split(':')
            restaurants_and_ratings[restaurant] = rating

    sorted_restaurants = sorted(restaurants_and_ratings.items())

    for restaurant, rating in sorted_restaurants:
        print "{} is rated at {}.".format(restaurant, rating)

get_restaurant_ratings('scores.txt')
