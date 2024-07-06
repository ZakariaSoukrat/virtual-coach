import json
import os

class Coach :
        
    def __init__(self, name, sport, experience,clients):
               self.name = name
               self.sport = sport
               self.experience = experience
               self.clients = clients

JSON_FILE = 'src\static_assets\coaches.json'

def load_coaches():
    with open(JSON_FILE, 'r') as file:
        return json.load(file)
    
def save_coach(coach : Coach):
    coach_objet = {
        'name' : coach.name,
        'sport': coach.spo,
        'experience':coach.experience,
        'clients':[]
    }
    with open(JSON_FILE, 'w') as file:
        json.dump(coach_objet, file, indent=4)
