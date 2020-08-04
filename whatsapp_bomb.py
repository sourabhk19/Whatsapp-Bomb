from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from webdriver_manager.chrome import ChromeDriverManager #1st changer
import time
from selenium.common import exceptions
from selenium.webdriver.support import expected_conditions as EC
import random

def banner():
	print('''
		  Whatsapp Text  Bomb is intitiating....


		''')
def main():
	driver = webdriver.Chrome(ChromeDriverManager().install()) #2nd change
	driver.get('https://web.whatsapp.com/')

	name =input("Enter name of the contact -  ")
	msg=input("Enter the message -  ")
	count = input("Enter number of messages -  ")
  
	input('Enter any key after scanning QR code')

	user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
	user.click()
	
	# The classname of message box may vary.
	#msg_box = driver.find_element_by_class_name('_13mgZ') 
	inp_xpath = '//div[@dir="ltr"][@data-tab="1"][@spellcheck="true"]'
	#inp_xpath = '//div[@class="_2S1VP copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]'
	msg_box = driver.find_element_by_xpath(inp_xpath) 
	for i in range(count):
		try:  
			time.sleep(0.5)
			r=random.randint(0,5)
			msg_box.send_keys(messages[r]+Keys.ENTER)
			
			# The classname of send button may vary.
			time.sleep(0.5)
			
		except:
			print("exception")

	print('Bombing Complete!!')

banner()
main()