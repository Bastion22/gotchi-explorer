import json
import requests

class GotchiScraper:
    
    def __init__(self, gotchi_id):
        self.gotchi_id = gotchi_id
        

    def get_stats(self): # Get Gotchi Stats

        query = f'''{{
        aavegotchi(id: {self.gotchi_id}) {{
            modifiedNumericTraits
        }}
        }}'''

        url = 'https://subgraph.satsuma-prod.com/tWYl5n5y04oz/aavegotchi/aavegotchi-core-matic/api'
        r = requests.post(url, json={'query': query})
        gotchi_raw_data = json.loads(r.text)

        list_of_stats = gotchi_raw_data['data']['aavegotchi']['modifiedNumericTraits']

        return list_of_stats
    

    def get_svg(self): # Get Gotchi SVG
        
        query = f'''{{
        aavegotchi(id: {self.gotchi_id}) {{
            svg
        }}
        }}'''

        url = 'https://api.thegraph.com/subgraphs/name/aavegotchi/aavegotchi-svg'
        r = requests.post(url, json={'query': query})
        gotchi_svg_raw_data = json.loads(r.text)


        parsed_svg_data = gotchi_svg_raw_data['data']['aavegotchi']['svg']
        return [parsed_svg_data]
    

    

# gotchi_earth = StatScraper(5129)
# print(gotchi_earth.get_stats())


# query = f'''{{
# aavegotchi(id: 9400) {{
#     svg
# }}
# }}'''



# url = 'https://api.thegraph.com/subgraphs/name/aavegotchi/aavegotchi-svg'
# r = requests.post(url, json={'query': query})

# gotchi_svg_raw_data = json.loads(r.text)

# print(gotchi_svg_raw_data)

# parsed_svg_data = gotchi_svg_raw_data['data']['aavegotchi']['svg']
# print(parsed_svg_data)
    
# gotchi_svg_raw_data = json.loads(r.text)


# parsed_svg_data = gotchi_svg_raw_data['data']['aavegotchi']['svg']
# print(parsed_svg_data)




