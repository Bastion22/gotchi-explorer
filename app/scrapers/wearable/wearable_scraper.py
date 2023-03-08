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


    
    

# scrapertje = WearableScraper(1)

# scrapertje.get_svg()
    





