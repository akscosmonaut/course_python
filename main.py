from course_python import ls2

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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # result = ls1.count_square()

    # value1 = 5
    # value2 = "five"
    # func_result = ls1.test_function(value1=value1, value2=value2)

    # print(type(new_json[0]))
#   обращение к i элементу списка
#    new_json[i]
#     new_dict = new_json[0]

    # print(new_dict["name"])
    # new_dict["gender"] = "male"
    # print(new_dict["gender"])
    # print(len(new_dict["friends"]))
    # print(new_dict["friends"][1]["name"])

    ls2.test_function2(5, 6, 7, 8, 9, 20)
    ls2.test_function3(value1=40, value2=50, value3=100)


