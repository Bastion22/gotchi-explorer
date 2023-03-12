import json
import requests

class WearableScraper:
    
    def __init__(self, wearable_id):
        self.wearable_id = wearable_id
    

    def get_svg(self): # Get Gotchi SVG
        

        url = f'https://app.aavegotchi.com/images/items/{self.wearable_id}.svg'
        r = requests.get(url)
        wearable_svg_data = r.text
        
        return [wearable_svg_data]
    
    def get_name(self):
        
        query = f'''{{
            itemType(id: {self.wearable_id}) {{
                name
            }}
            }}'''
        
        url = f"https://subgraph.satsuma-prod.com/tWYl5n5y04oz/aavegotchi/aavegotchi-core-matic/api"
        r = requests.post(url, json={'query': query})
        wearable_name_raw_data = json.loads(r.text)
        
        wearable_name = wearable_name_raw_data['data']['itemType']['name']
        
        return wearable_name
    

        
    def get_trait_modifiers(self): # Get Gotchi Stats

        query = f'''{{
            itemType(id: {self.wearable_id}) {{
                traitModifiers
            }}
            }}'''

        url = 'https://subgraph.satsuma-prod.com/tWYl5n5y04oz/aavegotchi/aavegotchi-core-matic/api'
        r = requests.post(url, json={'query': query})
        trait_modifiers_raw_data = json.loads(r.text)

        list_of_modifiers = trait_modifiers_raw_data['data']['itemType']['traitModifiers']

        return list_of_modifiers


    
    


# scrapertje = WearableScraper(100)

# scrapertje.get_trait_modifiers()
    





