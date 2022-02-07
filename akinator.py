database = [{"name": "Spider man", "human": True, "movie": True, "original": False},
            {"name": "Nemo", "human": False, "movie": True, "original": False}]


def take_chance(answer, property):
    if answer == "y":
        ans = True
    else:
        ans = False

    to_remove = []
    for d in database:
        if d[property] != ans:
            to_remove.append(d)

    for i in to_remove:
        database.remove(i)

    if len(database) == 1:
        print("your character is " + database[0]["name"])
        quit()


ans = input("is your character human(y,n)")
take_chance(ans, "human")

ans = input("Is your character in a movie(y,n)")
take_chance(ans, "movie")

ans = input("Is your character original(y,n)")
take_chance(ans, "original")
i = 0
