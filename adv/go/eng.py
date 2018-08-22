class Action(object):

	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.paths = []
	
	def go(self, act):
		return self.paths.get(act, None)
	
	def add_paths(self, paths):
		self.paths = paths
		
	def change(self, description):
		self.description = description
	

start = Action("start", """Welcome to "Beta" Zork
You are Buzz Lightyear. Part toy and part cyborg. \
You were on a peace-keeping initiative when you were attacked by a band of notorious space pirates. \
You're currently tied to a chair and you are gagged.""")

breakFree = Action("breakFree", "You move around ineffectively against your bonds.")
laser = Action("laser", "Your laser battery is dead.")
detach = Action("detach", "You fired one of your arms and reattached them. You're free now. There's a door in front of you.")
open_door = Action("open", "Door opened. There's a corridor ahead.")

inventory0 = Action("sack0", "You got nothing but still everything.")
inventory1 = Action("sack1", "You have a rope.")
inventory2 = Action("sack2", "You have a rope and freeze ray.")
inventory3 = Action("sack3", "You have a freeze ray.")

corridor = Action("corridor", """You have entered an empty hallway. \
There's a dark passage on the left and you hear footsteps approaching from the right.""")
hide = Action("hide", "You went back inside, closed the door and waited for the guard to enter. The guard enters-")
wanderLeft = Action("wanderLeft", "You start towards the dark passage but the guard spots you and shoots you on sight. You lost.")
wanderRight = Action("wanderRight", "You walked right towards the guard and he freezed you using his freeze-ray. See ya in spring!")

attack = Action("attack", """Attack with what?""")
punch = Action("punch", "You punched the ravager on the head. You have a few seconds before he shoots you with his freeze ray.")
kick = Action("kick", "You kicked the ravager but it didn't have any effect.")
detach2 = Action("detach2", "You fired your right arm at the ravager and knocked him out for a few seconds.")
tie = Action("tie", """You tied the guard's legs, incapacitating him as you ran away into the dark. To be continued...""")
freeze = Action("freeze", """You froze that guy. Welcome to the dark side! You now posses the unbridled power of the force... Kidding. Or am I?""")
force = Action("force", "You fell for it haha... To be continued.")
run = Action("run", "You ran away but the ravager alerted his buddies and you so dead brah.")

take = Action("take", "Freeze ray taken.")
drop = Action("drop", "This ain't Zork but whatever... Freeze ray dropped.")

start.add_paths({'break': breakFree,'laser': laser,'detach': detach, 'inventory': inventory0})
inventory0.add_paths(start.paths)
laser.add_paths(start.paths)
breakFree.add_paths(start.paths)
detach.add_paths({'open': open_door, 'inventory': inventory1, 'items': inventory1})
inventory1.add_paths({'inventory': inventory1, 'open': open_door})
open_door.add_paths({'corridor': corridor, 'inventory': inventory1, 'items': inventory1})

corridor.add_paths({'hide': hide, 'back': hide, 'inside': hide, 'left': wanderLeft, 'right': wanderRight})
hide.add_paths({'attack': attack, 'punch': punch, 'detach': detach2, 'kick': kick})
attack.add_paths({'rope': tie, 'fist': punch, 'leg': kick, 'laser': laser, 'arm': detach2})
detach2.add_paths({'tie': tie, 'take': take, 'snatch': take, 'run': run})

take.add_paths({'freeze': freeze, 'shoot': freeze, 'tie': tie, 'drop': drop, 'run': run})
drop.add_paths({'take': take, 'pick': take, 'freeze': freeze, 'shoot': freeze, 'tie': tie, 'run': run})
freeze.add_paths({'force': force})