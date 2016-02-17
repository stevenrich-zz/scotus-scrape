from selenium import webdriver
from pyvirtualdisplay import Display
from BeautifulSoup import BeautifulSoup
import time

outfile = open("supreme.html", "w")

print "Scraping Supreme Court site..."

display = Display(visible=0, size=(800,600))
display.start()

url = "http://www.supremecourt.gov/opinions/slipopinions.aspx"

driver = webdriver.Firefox()
driver.get(url)
time.sleep(30)
page = driver.page_source
soup = BeautifulSoup(page)
print >> outfile, soup.prettify()

driver.quit()
display.stop()

#parse data

#delete tempfiles

os.remove("supreme.html")
