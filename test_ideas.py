from selenium import webdriver
from selenium.webdriver.support.ui import Select

# Assuming you have a WebDriver instance (e.g., ChromeDriver)
driver = webdriver.Firefox()

# Navigate to the webpage with the dropdown
driver.get('https://fiitjee-eschool.com/timetable.html')

# Locate the dropdown element by its HTML attribute (e.g., 'id' or 'name')
dropdown_element = driver.find_element_by_class_name('form_control')

# Create a Select object
dropdown = Select(dropdown_element)


# or Select by value attribute
dropdown.select_by_value('FeSCF327A1R')

# or Select by index (0-based)
# dropdown.select_by_index(index)

# Perform other actions or submit the form if needed
# ...

# Close the browser window
driver.quit()
