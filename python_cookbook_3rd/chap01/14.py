# 1.14 Sorting Object Without Native Comparasion Support 

class User:
    def __init__(self, user_id):
        self.user_id = user_id
    
    def __repr__(self):
        return 'User({})'.format(self.user_id)

users = [User(23), User(3), User(10)]
lambda_sorted_users = sorted(users, key=lambda u: u.user_id)
# print(lambda_sorted_users)  # [User(3), User(10), User(23)]

# Instead or using lambda, an alternative approach is to use operator.attrgetter()
from operator import attrgetter
sorted_users = sorted(users, key=attrgetter('user_id'))
# print(sorted_users)  # [User(3), User(10), User(23)]


# Discussion:
# attrgetter() is a bit faster than lambda.
# attrgetter() allow multiple fields to be extracted simulaneously.

# by_name = sorted(users, key=attrgetter('last_name', 'first_name'))
# We can use max() and min() 
min_user = min(users, key=attrgetter('user_id'))
max_user = max(users, key=attrgetter('user_id'))

# print(min_user, max_user)  # User(3) User(23)
