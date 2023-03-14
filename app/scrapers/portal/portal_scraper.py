import json
import requests


class PortalScraper:
    

    def scrape_h1_portals(): # Get Gotchi Stats
        
        h1_supply = {'h1':{'closed': 0, 'opened': 0, 'claimed': 0}}
        
        for x in range(1, 10000): # Do 1, 10K, last portal is 9999
            
            print(x)
            
            query = f'''{{
            portal(id: {x}) {{
                status
            }}
            }}'''
            
            url = 'https://subgraph.satsuma-prod.com/tWYl5n5y04oz/aavegotchi/aavegotchi-core-matic/api'
            r = requests.post(url, json={'query': query})
            h1_portals_raw_data = json.loads(r.text)
            
            portal_status = h1_portals_raw_data['data']['portal']['status']
                        
            if portal_status == 'Opened':
                h1_supply['h1']['opened'] += 1
                
            elif portal_status =='Claimed':
                h1_supply['h1']['claimed'] += 1
                
            elif portal_status == 'Bought':
                h1_supply['h1']['closed'] += 1
        
        # Dump H2 Supply to json File
        with open('gotchitraits/app/data_libraries/portal_supply/h1_supply.json', 'w') as f:
            json.dump(h1_supply, f)
    
    

    def scrape_h2_portals(): # Get Gotchi Stats
        
        h2_supply = {'h2':{'closed': 0, 'opened': 0, 'claimed': 0}}
        
        for x in range(10000, 25001): # Do 10K, 25.001K, last portal is 25000
            
            print(x)
            
            query = f'''{{
            portal(id: {x}) {{
                status
            }}
            }}'''
            
            url = 'https://subgraph.satsuma-prod.com/tWYl5n5y04oz/aavegotchi/aavegotchi-core-matic/api'
            r = requests.post(url, json={'query': query})
            h2_portals_raw_data = json.loads(r.text)
            
            portal_status = h2_portals_raw_data['data']['portal']['status']
            
            if portal_status == 'Opened':
                h2_supply['h2']['opened'] += 1
                
            elif portal_status =='Claimed':
                h2_supply['h2']['claimed'] += 1
                
            elif portal_status == 'Bought':
                h2_supply['h2']['closed'] += 1
        
        
        # Dump H2 Supply to json File
        with open('gotchitraits/app/data_libraries/portal_supply/h2_supply.json', 'w') as f:
            json.dump(h2_supply, f)
        
    


PortalScraper.scrape_h1_portals()
PortalScraper.scrape_h2_portals()