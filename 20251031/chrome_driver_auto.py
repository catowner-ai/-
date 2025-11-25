#%%

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

url='http://tw.yahoo.com'

driver = webdriver.Chrome(service=webdriver.ChromeService(ChromeDriverManager().install()))

driver.get(url)