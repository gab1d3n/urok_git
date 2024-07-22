from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_currency_rates():
    url = 'https://example.com/currency'
    
    driver = webdriver.Chrome(executable_path='путь_до_chromedriver.exe')  

    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="currency-rates"]'))
        )
        currency_elements = driver.find_elements(By.XPATH, '//div[@class="currency-rates"]//span[@class="currency-rate"]')
        
        print("Курсы валют:")
        for currency in currency_elements:
            print(currency.text)
    
    finally:
        driver.quit()

def get_marketplace_prices():
    url = 'https://example.com/marketplace'
    
    driver = webdriver.Chrome(executable_path='путь_до_chromedriver.exe')  
    
    try:
        driver.get(url)
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//div[@class="product-price"]'))
        )
        
        price_elements = driver.find_elements(By.XPATH, '//div[@class="product-price"]')
        
        print("\nЦены на товары:")
        for price in price_elements:
            print(price.text)
    
    finally:
        driver.quit()

if __name__ == "__main__":
    get_currency_rates()
    get_marketplace_prices()
