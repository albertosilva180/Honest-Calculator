def select_dates(potential_dates):
    desired_age = 30
    my_list = [item_list['name'] for item_list in potential_dates if item_list['age'] > desired_age 
               and item_list['city'] == 'Berlin' and 'art' in item_list['hobbies']]
    return ', '.join(my_list)
