import scrapy
import pandas as pd

class pokemonspider(scrapy.Spider):
    name = 'pokemons'
    start_urls = [
        'https://pokemondb.net/pokedex/all'
    ]

    def parse(self, response):
        # Initialize lists to store data
        types_list = []
        ids = response.css('span.infocard-cell-data::text').extract()
        names = response.css('.ent-name::text').extract()
        icon_links = response.css(".icon-pkmn::attr(src)").extract()

        # Loop through each td.cell-icon to extract types
        for type_list in response.css('td.cell-icon'):
            # Extract the text of each <a> tag within td.cell-icon and append to types_list
            a_tag_text = type_list.css('a::text').extract()
            types_list.append(a_tag_text)

        # Extract other data from respective CSS selectors
        total = response.css('.cell-total::text').extract()
        hp = response.css('.cell-total+ .cell-num::text').extract()
        attack = response.css('.cell-num:nth-child(6)::text').extract()
        defense = response.css('.cell-num:nth-child(7)::text').extract()
        sp_attack = response.css('.cell-num:nth-child(8)::text').extract()
        sp_defense = response.css('.cell-num:nth-child(9)::text').extract()
        speed = response.css('.cell-num:nth-child(10)::text').extract()

        # Store all data in a dictionary
        context = {
            'ids': ids,
            'icon links': icon_links,
            'names': names,
            'types': types_list,
            'total': total,
            'hp': hp,
            'attack': attack,
            'defense': defense,
            'sp_attack': sp_attack,
            'sp_defense': sp_defense,
            'speed': speed,
        }

        # Convert dictionary to DataFrame and save as Excel file
        df = pd.DataFrame(context)
        df.to_excel('pokemon_data.xlsx', index=False)
