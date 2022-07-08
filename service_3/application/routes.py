from application import app
from random import choice

@app.route('/rand_2', methods=['GET'])
def rand_2(): 
    sources = ["flame", "earth", "water", "air", 'the celestial', "hellfire", "the occult", "the infernal", "the void", "fey", "shadow", "enchantment", "illusion", "abberation"]
    selection = choice(sources)
    return selection
    
def new_func():
    pass