from models.user import User
users = {
        "player1": User(username="player1", credit=1000),
        "player2": User(username="player2", credit=1000),
        "player3": User(username="player3", credit=1000),
        "player4": User(username="player4", credit=1000),
        "player5": User(username="player5", credit=1000)
        }

def get_user(username: str):
    print(users[username])
    return users[username]

def update_user_credit(username: str, credit: int):
    users[username].credit = credit
