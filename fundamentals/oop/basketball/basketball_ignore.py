
class Player:
    num_players = 0

    def __init__(self, player, i):
        self.name = player[i]["name"]
        self.age = player[i]["age"]
        self.position = player[i]["position"]
        self.team = player[i]["team"]
        Player.num_players += 1
        # new_team.append(player)

    def display_player_info(self):
        print(f'Name: {self.name} ' + '\n' + f'Age: {self.age}' + '\n' + f'Position: {self.position}' + '\n' + f'Team: {self.team}')
        return self





players = [
    {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age":32, "position": "Point Guard", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", 
        "age":33, "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age":32, "position": "Power Foward", 
        "team": "Philidelphia 76ers"
    },
    {
        "name": "", 
        "age":16, 
        "position": "P", 
        "team": "en"
    }
]
new_team = []






kevin = Player(players, 0)
jason = Player(players, 1)
kyrie = Player(players, 2)
Damian = Player(players, 3)
Joel = Player(players, 4)



kevin.display_player_info()
print(Player.num_players)
print(new_team)










class User:
    def __init__(self, fname, lname, email, password):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.password = password

    @staticmethod
    def validate():

        












