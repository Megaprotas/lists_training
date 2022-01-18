from lists_db.utils import db

USER_CHOICE = '''
Enter Your choice:
    Add new game - a,
    List book - l,
    Mark as read - r,
    Delete - d,
    quit - q
    
Your choice:
'''


def choices():
    choice = input(USER_CHOICE)
    while choice != 'q':
        if choice == 'a':
            add_game()
        elif choice == 'l':
            list_games()
        elif choice == 'r':
            mark_as_played()
        elif choice == 'd':
            delete_game()
        else:
            print('Unknown command')

        choice = input(USER_CHOICE)


def add_game():
    game = input('Enteer game name: ')
    studio = input('Enter studio: ')

    db.add_game_db(game, studio)


def list_games():
    games = db.games_list()
    for game in games:
        played = 'YES' if game['played'] else 'NO'
        print(f"{game['name'].title()} made by {game['studio'].title()}. played already: {played.upper()}")


def mark_as_played():
    game = input('Enter the name of a game: ')
    db.mark_as_played_in_db(game)


def delete_game():
    game = input('Enter the name of a game: ')
    db.delete_game_from_db(game)


choices()