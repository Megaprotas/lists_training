games = []


def add_game_db(name, studio):
    games.append({'name': name, 'studio': studio, 'played': False})


def games_list():
    return games


def mark_as_played_in_db(name):
    for game in games:
        if game['name'] == name:
            game['played'] = True


def delete_game_from_db(name):
    global games
    games = [game for game in games if game['name'] != name] # adds new game to list if book['name'] != name


# def delete_game_from_db(name):
#     for game in games:
#         if game['name'] == name:
#             games.remove(game)


