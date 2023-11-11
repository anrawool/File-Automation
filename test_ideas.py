import requests
from bs4 import BeautifulSoup

# Replace 'url' with the URL of the webpage you want to scrape
url = 'https://fiitjee-eschool.com/timetable.html'
response = requests.get(url)



if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    dropdown = soup.find('select', {'class': 'form-control'})
    selected_option_value = 'FeSCF327A1R'
    if dropdown:
        option_to_select = dropdown.find('option', {'value': selected_option_value})

        if option_to_select:
            option_to_select['selected'] = True

    table = soup.find('table', class_='table')
    if table:
        # Process the table data
        rows = table.find_all('tr')
        print(rows)
        for row in rows:
            columns = row.find_all('td')
            print(columns)
            for column in columns:
                print(column.text)
else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")
