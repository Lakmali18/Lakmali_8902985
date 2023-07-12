# Importing required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the cineplex.com homepage
driver.get("https://www.cineplex.com/")
time.sleep(3)

# Clicking on search icon button
search_icon = driver.find_element("xpath","/html/body/div/div[3]/div/header/nav/div[2]/ul/li[3]/button")
search_icon.click()
time.sleep(5)

# Finding the search bar and entering text
search_bar = driver.find_element("xpath","/html/body/div/div[3]/div/div[5]/div[2]/div/div/div/form/div/div/div/input")
search_bar.send_keys("transformers")
# Submitting the search query
search_bar.send_keys(Keys.RETURN)
# Waiting for the search results page to load
time.sleep(5)

# Verifying that the search results page has loaded
assert "Cineplex.com | Search 2015" in driver.title

# Scrolling down
driver.execute_script("window.scrollTo(0, 300)")
# Selecting a transformers English movie from the search results
movie_link = driver.find_element("xpath","/html/body/div[1]/div[1]/div/div[2]/div/div[4]/div/div/div/div/div[1]/div[2]/div[1]/div/div[1]/div/div[2]/a")
# Clicking on find show time button
driver.execute_script("arguments[0].click();", movie_link)
time.sleep(5)

# Scrolling down
driver.execute_script("window.scrollTo(0, 500)")
# Clicking on show time button
showtime = driver.find_element("xpath","/html/body/div/div[3]/div/div[5]/div[2]/div/div/div/div/div[1]/div[3]/div[1]/div[2]/div[2]/div[3]/div[1]/button")
showtime.click()
time.sleep(5)

# Closing the webdriver
driver.close()
