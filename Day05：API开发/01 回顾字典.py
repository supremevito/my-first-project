info = {
    "name":"Vi",
    "age":18,
    "is_married":False
}

#扩展

info = {
    "name":"Vi",
    "age":18,
    "is_married":False,
    # "gfs":["Eva","Fan","X"]
    "gfs":[
        # ["Eva",18,165],
        # ["Eva2",18,165],
        # ["Eva3",18,165],
#最好还是键值对套键值对
        {"name":"Eva",
        "age":18,
        "height":165
         },
        {"name":"Fan",
        "age":18,
        "height":165
         },
        {"name":"X",
        "age":18,
        "height":165
         },
    ]
}

for i in info.get("gfs"):
    print(i.get("name"))

# print(info.get("gfs"))