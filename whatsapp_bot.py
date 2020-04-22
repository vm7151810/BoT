from selenium import webdriver
driver = webdriver.Chrome()#install the chrome divers for this code to work(accordance to your chrome version)
driver.get('https://web.whatsapp.com/')
name = input('Enter the name of user or group : ')#whom you wanna sent
msg = input('Enter your message : ')#what you wanna sent
input('Enter anything after scanning QR code')#just to make sure u scanned the code (you can remove it if u want)
user = driver.find_element_by_xpath(f'//span[@title = "{name}"]')#finds the path(where to go) to the name of the person or group 
user.click()#click on that group/user
msg_box = driver.find_element_by_class_name('_1Plpp')# you should change this according to you(more info at the bottom of the code)
msg_box.send_keys(msg)
button = driver.find_element_by_class_name('_35EW6')
button.click()

# open web whatsapp>log in > press F12 > Go to elements(by default you are already on it)
# Then in body scroll through divs' to and hover on the div's to see which div selects what part of your web whatsapp
# deep in the divs > you will find footer > where you will find a class name 
# paste that class name there and the code should work just fine

