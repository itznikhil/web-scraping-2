from bs4 import BeautifulSoup as bs
import pandas as pd
import request
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars/"
browser = webdriver.Chrome("/Users/apoorvelous/Downloads/chromedriver")
browser.get(START_URL)
time.sleep(10)

def scrape():
    headers = ["Star", "Constellation", "Right_ascension", "Declination", "App_mag", "Distance", "Spectral_type", "Brown_dwarf", "Mass", "Radius", "Orbital_period", "Semimajor_axis", "eccentricity", "Discovery_date", "hyperlink"]
    moon_data = []
    for i in range (0, 420):
        soup - BeautifulSoup(browser.page_source, "html.parser")
        for ul_tag in soup.find_all("ul", attrs={"class", "brown_dwarfs"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            hyperlink_li_tag = li_tags[0]
            temp_list.append("https://en.wikipedia.org/wiki/List_of_brown_dwarfs"+hyperlink_li_tag.find_all("a", href=True)["href"])    
            moon_data.append("temp_list")        

def scrape_more_data(hyperlink):
    page = requests.get(hyperlink)      
    soup = BeautifulSoup(page.content, "html_parser") 
    for tr_tag in soup.find_all("tr", attrs={"class": "fact_row"}): 
        td_tags = tr_tag.find_all("td")
        temp_list = []
        for td_tag in td_tags:
             try:
                    temp_list.append(td_tag.find_all("div", attrs={"class": "value"})[0].contents[0])
                except:
                    temp_list.append("")
                    new_moon_data.append(temp_list)

scrape()
for data in moon_data:
    scrape_more_data(data[5])

final_moon_data = []
for index, data in enumerate(moon_data):
    new_moon_data_element = new_moon_data[index]
    new_moon_data_element = [elem.replace("\n", "") for elem in new_moon_data_element]
    new_moon_data_element = new_moon_data_element[:7]
    final_moon_data.append(data + new_moon_data_element)
