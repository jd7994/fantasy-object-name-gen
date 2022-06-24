from application import app
from random import choice

@app.route('/rand_2', methods=['GET'])
def rand_2(): #changethis
    sources = ["flame", "earth", "water", "air", "celestial", "hellish", "occult", "infernal", "void", "fey", "shadow", "enchanted", "illusion", "abberative"]
    selection = choice(sources)
    return selection
    