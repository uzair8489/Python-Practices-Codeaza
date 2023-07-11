import grequests
import re
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import pandas as pd

# Initialize the webdriver
driver = webdriver.Chrome()
driver.get("https://www.laufen.co.at/produkte/waschtische")

def click_next_button():
    # Check if the next button is displayed and click it
    try:
        next_button = driver.find_element(By.ID, 'nextButtonDiv')
        if next_button.is_displayed():
            next_button.click()
            return True
        else:
            return False
    except NoSuchElementException:
        return False

def get_urls():
    # Get the URLs of the products
    product_url = []
    while True:
        time.sleep(2)
        products = driver.find_elements(By.XPATH, "//div[@class='product-card']")
        
        # Check if the next button is not visible and retrieve the product URLs
        if not click_next_button():
            print(f"Total Products found: {len(products)}\n")
            for product in products:
                try:
                    if len(product.find_elements("xpath", ".//h3[@class='title-producto']/a")) > 0:
                        urls = product.find_elements("xpath", ".//h3[@class='title-producto']/a")
                        for url in urls:
                            product_url.append(url.get_attribute("href"))
                    else:
                        product_url.append("NULL")
                except Exception as e:
                    print(f"Error occurred while scraping price: {str(e)}")

            break

    return product_url


def get_data(urls):
    # Send asynchronous requests to fetch the data for each product URL
    reqs = [grequests.get(link) for link in urls]
    responses = grequests.map(reqs)
    return responses

def extract_details(responses):
    # Extract the desired details from the responses
    series = []
    name = []
    article = []
    length = []
    width = []
    height = []
    category1 = [] 
    category2 = [] 
    colors = []
    types = []
    main_image = []
    galary_images = []
    material = []
    datasheet_hrefs = []
    long_description = []
    short_description = []
    tags_3d_hrefs = []
    url = []

    try:
        for r in responses:
            sp = BeautifulSoup(r.content, 'lxml')
            data = sp.find_all('div', {'id': 'layout-column_column-1'})
            for item in data:
                # Extract the series
                series_tag = item.find('h2', class_='coleccion-name', id='collname')
                series_text = series_tag.get_text(strip=True) if series_tag else "None"
                series.append(series_text)

                # Extract the name
                name_tag = item.find('h1', {'id': 'prod-name'})
                name_text = name_tag.get_text(strip=True) if name_tag else "None"
                name.append(name_text)

                # Extract the article number
                p_tag = item.find('p', {'class' : 'coleccion-article'})
                if p_tag:
                    article_text = p_tag.get_text(strip = True).replace('Artikelnummer: ', '')
                    article.append(article_text)
                else:
                    article.append("None")

                # Extract the dimensions
                dimensions_tag = item.find('span', {'id': 'dim-txt'})
                if dimensions_tag:
                    dimension_text = dimensions_tag.get_text(strip=True)
                    numbers = re.findall(r'\d+', dimension_text)
                    if len(numbers) >= 3:
                        length.append(int(numbers[0]))
                        width.append(int(numbers[1]))
                        height.append(int(numbers[2]))
                else:
                    length.append("None")
                    width.append("None")
                    height.append("None")

                # Extract the categories
                ul_tag = item.find('div', {'class': 'col'})
                if ul_tag:
                    a_tags = ul_tag.find_all('a')
                    if len(a_tags) >= 4:
                        category1_text = a_tags[2].get_text(strip=True)
                        category2_text = a_tags[3].get_text(strip=True)
                        category1.append(category1_text)
                        category2.append(category2_text)
                    else:
                        category1.append("None")
                        category2.append("None")
                else:
                    category1.append("None")
                    category2.append("None")
                
                # Extract the colors
                colors_div = item.find('div', {'class': 'colors'})
                if colors_div:
                    label_tags = colors_div.select('label.fondo img[alt]')
                    colors_text = [label['alt'] for label in label_tags]
                    colors.append(colors_text)
                else:
                    colors.append("None")

                # Extract the types
                select_tag = item.find('select', class_='form-control cfg-option')
                span_tag = item.find('span', {'class': 'cfg-options'})
                if select_tag:
                    option_tags = select_tag.find_all('option')
                    option_values = [option['data-value'] for option in option_tags]
                    types.append(option_values)
                elif span_tag:
                    types.append([span_tag.get_text(strip=True)])
                else:
                    types.append(["None"])

                # Extract the main image
                image_div = item.find('div', {'class': 'image-overflow'})
                if image_div:
                    image_tag = image_div.find('img', {'data-finish': True})
                    if image_tag:
                        main_image.append("https://www.laufen.co.at" + image_tag['src'])
                    else:
                        main_image.append("None")
                else:
                    main_image.append("None")

                # Extract the gallery images
                image_div = item.find('div', {'id': 'productDetailThumbnailSlider'})
                if image_div:
                    image_tag = image_div.find_all('img')
                    image_urls = [img['src'] for img in image_tag]
                    if image_urls:
                        full_image_urls = ["https://www.laufen.co.at" + url for url in image_urls]
                        galary_images.append(full_image_urls)
                    else:
                        galary_images.append("None")
                else:
                    galary_images.append("None")

                # Extract the material
                material_tag = item.find('p', {'data-code': 'Material'})
                if material_tag:
                    material_text = material_tag.get_text(strip=True)
                    material.append(material_text.replace("Material:", "").strip())
                else:
                    material.append("Null")

                # Extract the 3D files
                divs = item.find_all('div', {'class': 'tabla-ficha'})
                for div in divs:
                    tabla_title = div.find('p', class_='tabla-title')
                    tabla_title_text = tabla_title.get_text(strip = True)
                    if tabla_title_text == '3D':
                        download_links = div.find_all('a', class_='icon-stp')
                        tags_3d_hrefs.append("https://www.laufen.co.at" + link['href'] for link in download_links)

                # Extract Long Description
                tag_long_desc = item.find('p', {'class': 'clamp'})
                if tag_long_desc:
                  long_desc_text = tag_long_desc.get_text(strip=True)
                  long_description.append(long_desc_text)
                else:
                    long_description.append("Null")

                # Extract the short description
                for item in data:
                    main_div = item.find('div', class_='row r-body zero-margin-bottom')
                    if main_div:
                        child_divs = main_div.find_all('div')
                        short_description.append([])  # Create a new list for the current page
                        
                        for div in child_divs:
                            p_tags = div.select('p[data-code]')
                            for p in p_tags:
                                p_text = p.get_text(strip=True)
                                short_description[-1].append(p_text)
                
                # Extract the datasheet
                files_tag = item.find_all('a', {'class': 'descarga'})
                item_urls = []  # Store the hrefs for the current item
                found_technisches_datenblatt = False
                
                for tag in files_tag:
                    text = tag.get_text(strip=True)
                    if "Technisches Datenblatt" in text:
                        href = tag['href']
                        if href:
                            full_url = "https://www.laufen.co.at" + href
                            item_urls.append(full_url)
                            found_technisches_datenblatt = True
                    if not found_technisches_datenblatt:
                            pass    
            datasheet_hrefs.append(item_urls)
                # Extract the URL
            url.append(r.url)

        # Create a dataframe to store the extracted data
        df = pd.DataFrame({
            'Category1': category1,  # Category 1
            'Category2': category2,  # Category 2
            'Series': series,
            'Name': name,
            'Article Number': article,
            'Length': length,
            'Width': width,
            'Height': height,
            'Colors': colors,
            'Types': types,
            "Short Description" : short_description,
            'Material' : material,  
            "Datasheet Urls" : datasheet_hrefs,
            # "3D Files Urls" : tags_3d_hrefs,
            "Long Description" : long_description,
            'Main Image': main_image,
            'Gallery Images': galary_images,
            'URL': url
        })


        

        # Save the dataframe to an Excel file
        df.to_excel('Products_Data.xlsx', index=False)

        print("Data saved to Product_Data.xlsx")

    except Exception as e:
        print("Error occurred:", str(e))

# Get the product URLs
urls = get_urls()

# Fetch the data for each URL
responses = get_data(urls)

# Extract the details from the responses
extract_details(responses)

# Close the webdriver
driver.quit()
