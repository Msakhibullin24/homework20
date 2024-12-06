from functools import partial

def sort_users_by_age_ascending(users):
    return _sort_users_by_age(users)

def sort_users_by_age_descending(users):
    return _sort_users_by_age(users, reverse=True)

'''
from functools import partial

def _sort_users_by_age(users, reverse=False):
    return sorted(users, key=lambda user: user['age'], reverse=reverse)


'''
