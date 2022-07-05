from application import app
from random import choice

@app.route('/rand_1', methods=['GET'])
def rand_1(): 
    choices = ["prison", "gate", "weapon (bladed)", "weapon (blunt)", "dagger", "telescope", "armour", "crown", "scepter", "throne", "tower", "lake", "ocean", "mountain", "fortress"]
    selection = choice(choices)
    return selection