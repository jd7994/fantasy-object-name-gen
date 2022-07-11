from application import app
from flask import request
from random import choice

obj_dict = {
    "prison":['bastille', 'stockade', 'chain', 'lock', 'bars', 'hook', 'machine'],
    "gate":['conduit', 'weir', 'passage', 'egress', 'slit', 'tear', 'split', 'barricade', 'barrier', 'dam'],
    "weapon (bladed)":['foil', 'scimitar', 'brand', 'edge', 'blade', 'crux', 'end', 'death', 'cessation'],
    "weapon (blunt)":['baton', 'cudgel', 'ferule', 'shillelagh', 'weight', 'mass', 'heft', 'comet', 'moon'],
    "dagger":['lacerator', 'sickle', 'shank', 'point', 'knife', 'unease', 'disquiet', 'dread'],
    "telescope":['lens', 'eyeglass', 'instrument', 'eye', 'apprehender', 'optic', 'bioptic', 'trioptic', 'quadoptic'],
    "armour":['barricade', 'wall', 'facade', 'tenacity', 'stalwart', 'bulwark', 'ward', 'aegis', 'contender', 'preserver'],
    "crown":['chaplet', 'circlet', 'diadem', 'wreath', 'crown', 'moon', 'star', 'sun', 'veil', 'hood', 'guise', 'visage', 'visor'],
    "scepter":['cane', 'stave', 'rod', 'baton', 'shaft', 'sceptre', 'switch', 'wand', 'conviction', 'assent', 'mast' ],
    "throne":['chair', 'seat', 'throne', 'place', 'attitude', 'outlook', 'rank', 'duty'],
    "tower":['ziggurat', 'rise', 'point', 'apex', 'awn', 'barb', 'claw', 'jag', 'spur', 'basilica', 'sanctuary','altar', 'shrine', 'sanctum'],
    "lake":['splay', 'azure', 'wash', 'rush', 'flow', 'tear', 'bath', 'soak', 'steep'],
    "ocean":['sea', 'wrath', 'fury', 'fervor', 'rage', 'remorse', 'expanse', 'surf', 'abyss', 'regret', 'blue', 'flat'],
    "mountain":['mesa', 'rise', 'point', 'ire', 'claw', 'needle'],
    "fortress":['citadel', 'garrison', 'rampart', 'keep', 'holme']}
    
source_dict = {
    "flame":['red', 'burning', 'scorched', 'scalding'],
    "earth":['verdant', 'gladed', 'crystal'],
    "water":['fathomless', 'diver\'s', 'sunless', 'quenched'],
    "air":['sunkissed', 'frigid', 'rimed', 'gale-wrought'],
    "the celestial":['holy', 'sacrosanct', 'promised', 'radient', 'sacred'],
    "hellfire":['gnarled', 'forsworn', 'abandoned', 'imp\'s', 'ever-burning', 'beast\'s'],
    "the occult":['omen\'d', 'six-fingered', 'woe-known', 'forgotten', 'blighted', 'cursed', 'true'],
    "the infernal":['ravening', 'blistering', 'puckering', 'long-buried', 'ever-weeping'],
    "the void":['black', 'terrible', 'unknowable', 'dark', 'forgotten', 'star-wrought'],
    "fey":['tricky', 'backwards', 'fleeting', 'whispering'],
    "shadow":['shaded', 'omen\'d', 'eclpised', 'darkest'],
    "enchantment":['shining', 'glowing', 'sparkling', 'keening'],
    "illusion":['eye-covered', 'ever-twirling', 'endless'],
    "abberation":['otherworldly', 'incomprehensible', 'beholder\'s', 'quivering']
}

@app.route('/final', methods=['POST'])
def final():
    
    data_sent = request.get_json()
    the_obj = data_sent["obj"]
    the_source = data_sent["source"]
    
    fin_source = choice(source_dict[the_source])
    fin_obj = choice(obj_dict[the_obj])

    cap_source = fin_source.capitalize()
    cap_obj = fin_obj.capitalize()
    #first version
    #return f"The {cap_source} {cap_obj}"

    #second version
    if cap_source[-1] == "s" and cap_source[-2] == "'":
        return f"{cap_obj}, The {cap_source[0:-2]}"
    else: 
        return f"{cap_obj}, The {cap_source}"

    