new_json = [
    {
        "_id": "6335b5157d03f8dc868808b1",
        "index": 0,
        "guid": "f0faa6a3-7408-470a-9b80-4a14e6ecac72",
        "balance": "$1,106.18",
        "picture": "http://placehold.it/32x32",
        "age": 33,
        "eyeColor": "brown",
        "name": "Lydia Vaughn",
        "gender": "female",
        "company": "UNCORP",
        "email": "lydiavaughn@uncorp.com",
        "phone": "+1 (874) 457-2891",
        "address": "774 Church Avenue, Heil, New York, 5198",
        "about": "Culpa sint consequat dolor amet dolor. Voluptate ullamco "
                 "cillum ullamco occaecat magna ex esse dolor irure laborum. "
                 "Aute ipsum proident dolore laboris in non cupidatat in "
                 "velit cupidatat ad laboris est. Labore do consequat dolor "
                 "veniam consectetur dolor fugiat commodo esse pariatur "
                 "nostrud duis. Minim aute laboris consectetur nisi esse "
                 "labore qui.\r\n",
        "registered": "2017-12-04T02:15:49 -03:00",
        "latitude": -11.505877,
        "longitude": -22.248036,
        "tags": [
            "eiusmod",
            "ea",
            "et",
            "magna",
            "deserunt",
            "labore",
            "nostrud"
        ],
        "friends": [
            {
                "id": 0,
                "name": "Dianna Forbes"
            },
            {
                "id": 1,
                "name": "Strickland Underwood"
            },
            {
                "id": 2,
                "name": "Aurelia Gibbs"
            }
        ],
        "greeting": "Hello, Lydia Vaughn! You have 4 unread messages.",
        "favoriteFruit": "strawberry"
    }
]


def get_json_name():
    # обращение к i элементу списка
    # new_json[i]

    print(roll_json(new_json[0])) #распечатается имя, которое вернёт функция


def roll_json(new_dict):
    # обращение к значению словаря через ключ ("key1")
    # new_dict["key1"]
    print(new_dict["name"])

    # присвоение значения по ключу
    new_dict["gender"] = "male"

    # получить длину списка "friends"
    print(len(new_dict["friends"]))

    return new_dict["friends"][1]["name"]
