from application import app
from flask import request
from random import choice

prison = ['bastille', 'stockade', 'chain', 'lock', 'bars', 'hook', 'machine']
gate = ['conduit', 'weir', 'passage', 'egress', 'slit', 'tear', 'split', 'barricade', 'barrier', 'dam']
blade = ['foil', 'scimitar', 'brand', 'edge', 'blade', 'crux', 'end', 'death', 'cessation']
mace = ['baton', 'cudgel', 'ferule', 'shillelagh', 'weight', 'mass', 'heft', 'comet', 'moon']
dagger = ['lacerator', 'sickle', 'shank', 'point', 'knife', 'unease', 'disquiet', 'dread']
scope = ['lens', 'eyeglass', 'instrument', 'eye', 'apprehender', 'optic', 'bioptic', 'trioptic', 'quadoptic']
armour = ['barricade', 'wall', 'facade', 'tenacity', 'stalwart', 'bulwark', 'ward', 'aegis', 'contender', 'preserver']
crown = ['chaplet', 'circlet', 'diadem', 'wreath', 'crown', 'moon', 'star', 'sun', 'veil', 'hood', 'guise', 'visage', 'visor']
scepter = ['cane', 'stave', 'rod', 'baton', 'shaft', 'sceptre', 'switch', 'wand', 'conviction', 'assent', 'mast' ]
throne = ['chair', 'seat', 'throne', 'place', 'attitude', 'outlook', 'rank', 'duty']
tower = ['ziggurat', 'rise', 'point', 'apex', 'awn', 'barb', 'claw', 'jag', 'spur', 'basilica', 'sanctuary','altar', 'shrine', 'sanctum']
lake = ['splay', 'azure', 'wash', 'rush', 'flow', 'tear', 'bath', 'soak', 'steep']
ocean = ['sea', 'wrath', 'fury', 'fervor', 'rage', 'remorse', 'expanse', 'surf', 'abyss', 'regret', 'blue', 'flat']
mount = ['mesa', 'rise', 'point', 'ire', 'claw', 'needle']
fort = ['citadel', 'garrison', 'rampart', 'keep', 'holme']

flame = ['red', 'burning', 'scorched', 'scalding']
earth = ['verdant', 'gladed', 'crystal']
water = ['fathomless', 'diver\'s', 'sunless', 'quenched']
air = ['sunkissed', 'frigid', 'rimed', 'gale-wrought']
celestial = ['holy', 'sacrosanct', 'promised', 'radient', 'sacred']
hellish = ['gnarled', 'forsworn', 'abandoned', 'imp\'s', 'ever-burning']
occult = ['omen\'d', 'six-fingered', 'woe-known', 'forgotten', 'blighted', 'cursed', 'true']
infernal = ['ravening', 'blistering', 'puckering', 'long-buried', 'ever-weeping']
void = ['black', 'terrible', 'unknowable', 'dark', 'forgotten', 'star-wrought']
fey = ['tricky', 'backwards', 'fleeting', 'whispering']
shadow = ['shaded', 'omen\'d', 'eclpised', 'darkest']
enchanted = ['shining', 'glowing', 'sparkling', 'keening']
illusion = ['eye-covered', 'ever-twirling', 'endless']
abberative = ['otherworldly', 'incomprehensible', 'beholder\'s', 'quivering']

@app.route('/final')
def final():
    data_sent = request.get_json()
    the_obj = data_sent[obj]
    the_source = data_sent[source]
    if the_source == 'flame':
        fin_souce = choice(flame)
    elif the_source == 'earth':
        fin_source = choice(earth)
    elif the_source == 'water':
        fin_source = choice(water)
    elif the_source == 'air':
        fin_source = choice(air)
    elif the_source == 'celestial':
        fin_source = choice(celestial)
    elif the_source == 'hellish':
        fin_source = choice(hellish)
    elif the_source == 'occult':
        fin_source = choice(occult)
    elif the_source == 'infernal':
        fin_source = choice(infernal)
    elif the_source == 'void':
        fin_source = choice(void)
    elif the_source == 'fey':
        fin_source = choice(fey)
    elif the_source == 'shadow':
        fin_source = choice(shadow)
    elif the_source == 'enchanted':
        fin_source = choice(enchanted)
    elif the_source == 'illusion':
        fin_source = choice(illusion)
    elif the_source == 'abberative':
        fin_source = choice(abberative)
      
    if the_obj == 'prison':
        fin_obj = choice(prison)
    elif the_obj == 'gate':
        fin_obj = choice(gate)
    elif the_obj == "weapon (bladed)":
        fin_obj = choice(blade)
    elif the_obj == "weapon (blunt)":
        fin_obj = choice(mace)
    elif the_obj == "dagger":
        fin_obj = choice(dagger)
    elif the_obj == "telescope":
        fin_obj = choice(scope)
    elif the_obj == "armour":
        fin_obj = choice(armour)
    elif the_obj == 'crown':
        fin_obj = choice(crown)
    elif the_obj == 'scepter':
        fin_obj = choice(scepter)
    elif the_obj == 'throne':
        fin_obj = choice(throne)
    elif the_obj == 'tower':
        fin_obj = choice(tower)
    elif the_obj == 'lake':
        fin_obj = choice(lake)
    elif the_obj == 'ocean':
        fin_obj = choice(ocean)
    elif the_obj == 'mountain':
        fin_obj = choice(mount)
    elif the_obj == 'fortress':
        fin_obj = choice(fort)

    return f"The ${fin_souce} ${fin_obj}"
