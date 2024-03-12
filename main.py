import time
import pyautogui
import pyperclip

from pathlib import Path
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException

from config import *


class Browser:
    browser, service = None, None

    def __init__(self, driver:str):
        self.service = Service(driver)
        self.browser = webdriver.Chrome(service = self.service)

    def open_page(self, url:str):
        self.browser.get(url)

    def add_input(self, by:By, id:str, value:str):
        field = self.browser.find_element(by = by, value = id)
        field.send_keys(value)
        time.sleep(1) 

    def click_button(self, by:By, id:str):
        button = self.browser.find_element(by = by, value = id)
        button.click()
        time.sleep(1)

    def login_NC(self, email:str, password:str):
        self.add_input(by = By.ID, id = 'email', value = email)
        self.add_input(by = By.ID, id = 'password', value = password)
        self.click_button(by = By.CLASS_NAME, id = 'relative')

    def get_header(self):
        header = self.browser.find_element(by=By.TAG_NAME, value='h1')
        header = header.text.replace(' ' ,'_')
        # normalise header so that it can be used as a file name
        replaced_chars = [replacements.get(char, char) for char in header]
        header = ''.join(replaced_chars)
        # truncate long ad names to max file name length
        header = header[:135] if len(header) > 135 else header
        return header

    def make_folder(self):
        header = self.get_header()
        Path(header).mkdir(parents=False, exist_ok=True)

    def save_page(self, filename:str):
        print("going to save:")
        print(filename)
        pyautogui.hotkey('ctrl','s')
        time.sleep(timers['hotkey'])
        pyperclip.copy(filename)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(timers['hotkey'])
        pyautogui.press('enter')
        print("saving page...")

    def unlock_page(self, filename:str):
        print("trying to unlock...")
        with open(filename, 'r', encoding='utf8') as html_file:
            soup = BeautifulSoup(html_file, 'html.parser')
        target_script = soup.find('script', id='__NEXT_DATA__')
        target_script.decompose()
        with open(filename, 'w', encoding='utf8') as html_file:
            html_file.write(soup.prettify())
        print("page unlocked")

    def save_and_unlock(self, folder:str, filename:str, counter:int):
        filepath = str(root) + '\\' + folder + '\\' + str(counter).zfill(2) + '_' + filename + '.html'
        self.save_page(filepath)
        time.sleep(timers['pagesave'])
        self.unlock_page(filepath)
        counter +=1
        return counter

    def click_and_save(self, button:WebElement,  folder:str, counter:int):
        button.click()
        time.sleep(timers['pageload'])
        header = self.get_header()
        counter = self.save_and_unlock(folder=folder, filename=header, counter=counter)
        return counter

    def save_ticked(self, folder:str, counter:int):
        buttons = self.browser.find_elements(by = By.CSS_SELECTOR, value = 'button.bg-lightBackground')
        for button in buttons:
            counter = self.click_and_save(button = button, folder=folder, counter=counter)
        return counter

    def save_unticked(self, folder:str, counter:int):
        try:
            next_button = self.browser.find_element(by=By.XPATH, value='//button[text()="Next"]')
            while next_button:
                counter = self.click_and_save(button=next_button, folder=folder, counter=counter)
                next_button = self.browser.find_element(by=By.XPATH, value='//button[text()="I\'m done!"]')
        except NoSuchElementException:
            print("end of chapter")
            return

    def save_chapter(self, first_page:str):
        self.open_page(first_page)
        time.sleep(timers['pageload'])
        self.make_folder()
        folder = self.get_header()
        counter = 0
        self.save_and_unlock(folder = folder, filename = folder, counter = counter)
        counter = self.save_ticked(folder = folder, counter = counter)
        self.save_unticked(folder=folder, counter=counter)

def main():
    browser = Browser('./drivers/chromedriver.exe')
    browser.open_page('https://account.northcoders.com/login')
    time.sleep(timers['pageload'])
    browser.login_NC(credentials['email'],credentials['password'] )
    time.sleep(timers['pageload'])
    for page in first_page_list:
        browser.save_chapter(page)
    time.sleep(timers['hotkey'])
    print("All done. Bye!")

if __name__ == "__main__":
    main()
