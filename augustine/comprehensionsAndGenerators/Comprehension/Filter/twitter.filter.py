# A dictionary Users(twitter database) is given in which we have username and tweets.

users = [
    {"username": 'samuel', "tweets": ["i love cake", "i am good"]},
    {"username": 'andy', "tweets": []},
    {"username": 'kumal', "tweets": ["India", "Python"]},
    {"username": 'sam', "tweets": []},
    {"username": 'lokesh', "tweets": ["i am good"]},
]

# Filter out Users which dont have any tweets/Inactive Users

inactive_users = list(filter(lambda x : not x['tweets'], users))

print(inactive_users)

# Filter inactive users with just username in uppercase.

inactive_users = list(map(lambda x : x["username"].upper(), filter(lambda a : not a['tweets'], users )))
print(inactive_users)