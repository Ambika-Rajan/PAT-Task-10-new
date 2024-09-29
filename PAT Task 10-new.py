from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the path to your WebDriver
driver = webdriver.Chrome()

try:
    # Step 1: Navigate to the Instagram profile
    driver.get("https://www.instagram.com/guviofficial/")

    # Step 2: Wait for the page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//header//section"))
    )

    # Step 3: Extract the total number of followers
    followers = driver.find_element(By.XPATH, "//a[contains(@href, '/followers')]//span").get_attribute("title")

    # Step 4: Extract the total number of following
    following = driver.find_element(By.XPATH, "//a[contains(@href, '/following')]//span").text

    # Step 5: Print the results
    print("Total Followers:", followers)
    print("Total Following:", following)

finally:
    # Close the browser
    driver.quit()
