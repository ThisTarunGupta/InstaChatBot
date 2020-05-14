#!/usr/bin/python3

from selenium import webdriver
#from selenium.webdriver.chrome.options import Options #if you want to run Chrome Headless
from login_details import login
from response import chat
from time import sleep
import datetime
from random import choice

class InstaChatBot:
    def __init__(self, username, password):
        try:
            self.username = username
            self.password = password
            
            #config Chrome if using headless
#            chrome_options = Options()
#            chrome_options.add_argument("--disable-extensions")
#            chrome_options.add_argument("--disable-gpu")
#            chrome_options.add_argument("--no-sandbox") #only for linix
#            chrome_options.add_argument("--headless")

            #opens browser
            #self.driver = webdriver.Chrome(options=chrome_options) if using headless
            
            #self.driver = webdriver.Chrome(DRIVER_EXEC_PATH_DOWNLOADED)
            
            self.driver = webdriver.Chrome() #only for linux
            self.driver.get('https://www.instagram.com/')
            self.driver.implicitly_wait(10)

            #login
            self.driver.find_element_by_xpath('//input[@name=\"username\"]').send_keys(self.username)
            self.driver.find_element_by_xpath('//input[@name=\"password\"]').send_keys(self.password)
            self.driver.find_element_by_xpath('//button[@type="submit"]').click()
            sleep(4)

            self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()

            try:
                self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
            except:
                print("working...")
                
            print("Working...")

        except:
            return

    def ChatBot(self):
        #direct message
        self.driver.find_element_by_xpath("//a[contains(@href, '/direct/inbox')]").click()
        self.driver.implicitly_wait(5)
        
        while True: #or datetime.datetime.now().hour < 'time'
            try:
                #check new message
                link = self.driver.find_elements_by_xpath('//div[@style="height: 8px; width: 8px;"]')[0]
                if link:
                    link.click()
                    self.driver.implicitly_wait(5)
                    sleep(3)
                    
                    #get message
                    messages = self.driver.find_elements_by_tag_name("span")
                    message = messages[-1].get_attribute("innerHTML").lower()
                    
                    if message[0] == '/':
                        #respond to message
                        response = chat(message, user)

                        if response == None:
                            response = "Sorry. I can't get it."

                    else:
                        response = "Command not found or Invalid syntax. Use '/' before command.'"


                    self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(response)
                    self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()                

                    self.driver.back()
                    print("message sent...")
            except:
                print("no message...")

            self.driver.implicitly_wait(2)


    def quit(self):
        self.driver.quit()



if __name__ == '__main__':
    try:
        bot = InstaChatBot(login['username'], login['password'])
        bot.ChatBot()
    except:
        print("not connected to internet...")
        exit()

    finally:
        bot.quit()
        exit()
