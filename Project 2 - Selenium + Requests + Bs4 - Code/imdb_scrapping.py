import time
import grequests
import pandas as pd
import re
import logging
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

# Set up logging
logging.basicConfig(filename='imdb_scraper.log', level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Set up Selenium webdriver (make sure to provide the appropriate path to the web driver)
chrome_options = Options()
# chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

try:
    # Navigate to the IMDb Top TV Shows page
    logging.info("Navigating to IMDb Top TV Shows page...")
    driver.get('https://www.imdb.com/chart/toptv/')
    time.sleep(5)  # Wait for page to load

    # Extract the URLs of the top 50 TV shows
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    show_titles = []
    shows_urls = []
    airing = []
    episodes = []
    show_type = []
    show_ratings = []
    tv_shows = soup.find_all('div', class_='sc-14dd939d-0 fBusXE cli-children')

    count = 0
    for tv_show in tv_shows:
        show_urls = tv_show.find_all('a')  # Use find_all to get all the anchor tags
        for show_url in show_urls:
            url = 'https://www.imdb.com' + show_url['href']
            shows_urls.append(url)
            count += 1
            if count >= 50:
                break  # Break the loop when 50 URLs are added
        show_meta = tv_show.find('div', class_='sc-14dd939d-5 cPiUKY cli-title-metadata')
        # Find all the span tags within the div
        spans = show_meta.find_all('span', class_='sc-14dd939d-6 kHVqMR cli-title-metadata-item')
        if len(spans) >= 3:
            airing.append(spans[0].text.strip())
            episodes.append(spans[1].text.strip())
            show_type.append(spans[2].text.strip())
        else:
            airing.append('N/A')
            episodes.append('N/A')
            show_type.append('N/A')

        title_h3 = tv_show.find_all('h3', {'class': 'ipc-title__text'})
        for title in title_h3:
            text_content = title.get_text(strip=True)
            show_titles.append(re.sub(r'^\d+\.\s*', '', text_content))

        rating_tag = tv_show.find('span', class_='ipc-rating-star--imdb')
        show_ratings.append(rating_tag.text)

    df = pd.DataFrame({
        'Show Title': show_titles,
        'Airing': airing,
        'Show Type': show_type,
        'Episodes': episodes,
        'Rating': show_ratings,
        'Show Url': shows_urls,
    })

    logging.info('Saving Data into excel file....')
    # Save the dataframe to an Excel file
    df.to_excel('IMDb.xlsx', index=False)

    logging.info("Data saved to IMDb.xlsx")
    print("Data saved to IMDb.xlsx")

except Exception as e:
    logging.error(f"Error occurred: {str(e)}")
    print(f"An error occurred: {str(e)}")

finally:
    # Close the browser
    driver.quit()
