class Player:
    def __init__(self, player):
        self.name = player["name"]
        self.age = player["age"]
        self.position = player["position"]
        self.team = player["team"]

    def display_player(self):
        print(self.name)
        print(self.age)
        print(self.position)
        print(self.team)

player = {
    "name": "Matthew",
    "age": 31,
    "position": "Midfielder",
    "team": "Atlanta United"
}

matthew = Player(player)
matthew.display_player()

