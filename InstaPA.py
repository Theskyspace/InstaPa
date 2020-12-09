import eel
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("chromedriver.exe") 
actions = ActionChains(driver)
eel.init('web')

#https://www.instagram.com/explore/tags/<tagname>/
@eel.expose
def login(uname,pwd):

	
	driver.get("https://www.instagram.com/")

	actions = ActionChains(driver)
	driver.implicitly_wait(300) 

	username = driver.find_element_by_name('username')
	password = driver.find_element_by_name('password')



	if pwd != None or username != None:
		username.send_keys(uname)
		password.send_keys(pwd)
		password.send_keys(Keys.RETURN)

#If the person logs in then the fuction carries out that does like comment wala purpose

@eel.expose
def MainProcess(hashtags,comments,no_of_likes):
	no_of_likes = int(no_of_likes)
	for tag in hashtags:
		url = 'https://www.instagram.com/explore/tags/'+ tag	
		driver.get(url)
		time.sleep(5)

		#Clicks on The first Photo
		pic = driver.find_element_by_class_name("_9AhH0")    
		pic.click() 


		for i in range(no_of_likes + 1): 

			time.sleep(10)

			#Likes the photo
			like = driver.find_element_by_class_name("_9AhH0")
			like.click()
			like.click()

			time.sleep(random.randint(2,5))

			# Writes a comment
			if comments != None:
				driver.find_element_by_class_name('Ypffh').click()
				comment = random.choice(comments)
				driver.find_element_by_class_name('Ypffh').send_keys(comment)
				driver.find_element_by_class_name('Ypffh').send_keys(Keys.RETURN)
				
			#next photo
			for i in range(random.randint(1,8)):		
				time.sleep(random.randint(1,4))
				actions.send_keys(Keys.RIGHT)
				actions.perform()

eel.expose
def terminate():
	driver.close()	


eel.start('main.html', port=8080, size=(1000,600),host= '127.0.0.1',)

