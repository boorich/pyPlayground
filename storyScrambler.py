import random

roles = ("business owner ", "user ", "service provider ", "early adopter ", "developer ")
objects = ("box", "car", "wardrobe", "type", "functional parameter")
verbs = ("run", "hit", "jump", "derive", "copy", "expand", "duplicate")
components = ("service", "tool", "object", "function", "class")
goals = ("helpdesk.", "return.", "pipeline.")
adv = ("crazily ", "dutifully ", "foolishly ", "merrily ", "occasionally ")
adj = ("adorable ", "clueless ", "dirty ", "odd ", "stupid ")

for i in range(100):
    print('As a ' + roles[random.randrange(5)] + 'I want to ' + verbs[random.randrange(7)] + ' a ' + objects[random.randrange(5)] + ', so I can ' + adv[random.randrange(5)] + verbs[random.randrange(7)] + ' a ' + adj[random.randrange(5)] + goals[random.randrange(3)])