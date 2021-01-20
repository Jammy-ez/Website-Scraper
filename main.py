import requests 
import pyfiglet
import time
from bs4 import BeautifulSoup
from os import system, name
from tqdm import tqdm
from colorama import Fore, Back, Style
def clear():
    _ = system('cls')
print(Fore.RED + "Loading...")
for i in tqdm(range(1000),
    ncols=75):
    time.sleep(0.00000002)
    ...
clear()
TEXT1 = pyfiglet.figlet_format("WEBSITE SCRAPER", font="rectangles")
TEXT2 = pyfiglet.figlet_format("SCRAPING", font="rectangles")
time.sleep(1)
print(Fore.BLUE + TEXT1)
time.sleep(1)
print("Made by jam")
URL = input("Enter page to scrape from: ")
print("If this does not work (Likely) change the user agent to yours")
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 OPR/72.0.3815.465'}
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
print("Scraping, output will be written to scraped.txt")
time.sleep(1)
print(TEXT2)
time.sleep(1)
print("==================================================")
print(" ")
time.sleep(1)
clear()
print(soup.prettify())
print(" ")
print("==================================================")
time.sleep(1)
print("Copy the output")
time.sleep(10000)
