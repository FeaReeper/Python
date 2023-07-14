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

kevin = {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
}
jason = {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
}
kyrie = {
    	"name": "Kyrie Irving", 
    	"age":32, "position": "Point Guard", 
    	"team": "Brooklyn Nets"
}
    
# Create your Player instances here!
# player_jason = ???
player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

player_kevin.display_player()
player_jason.display_player()
player_kyrie.display_player()
