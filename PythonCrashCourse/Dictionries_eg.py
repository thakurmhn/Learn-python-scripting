# Nested Dictionaries

users={
    'mohant': {
    'first': 'mohan',
    'last': 'thakur',
    'location': 'pune'
    },
    'akshayc': {
    'first': 'akshay',
    'last': 'chavan',
    'location': 'thane'
    }
}

for key, value in users.items():
    # print(key, value)
    print(f"\nUsername: {key}")
    full_name = value['first'] + " " + value['last']
    print(f"Full_name: {full_name.title()}")
    print(f"Location: {value['location'].title()}")

#eg
people=[
    {'tabala': 'zakir', 'flute': 'shrini'},
    {'classical': 'kaushiki', 'folk': 'geeta'},
    {'philosopher': 'aristotle', 'poet': 'williams'}
]

print(f"Tabala Player: {people[0]['tabala'].title()}")
print(f"Flute Player: {people[0]['flute'].title()}")
print(f"Classical Singer: {people[1]['classical'].title()}")
print(f"Folk Singer: {people[1]['folk'].title()}")
print(f"Philosopher: {people[2]['philosopher'].title()}")
print(f"Poet: {people[2]['poet'].title()}")

#eg

pets=[
    {'dog': 'sheru', 'dog_owner': 'vedak'},
    {'cat': 'dona', 'cat_owner': 'raja'},
    {'tiger': 'sherkhan', 'tiger_owner': 'mogali'}
]

for item in pets:
    for key, value in item.items():
        print(type(value))

        #print(f"Dog Name: {key.title()}")
        # print(f"Dog Owner: {value['dog_owner'].title()}")
        # print(f"Cat Name: {value['cat'].title()}")
        # print(f"Cat Owner: {value['cat_owner']}")
