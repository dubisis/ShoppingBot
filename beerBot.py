from selenium import webdriver
driver = webdriver.Chrome()

# request
driver.get('https://shop.rarbrewing.com/')

# selecting a product
cup_wanted = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/main/ul/li[10]/a[1]/img')
cup_wanted.click()


# checkout
checkoutButton = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/main/div[2]/div[2]/form/button')
checkoutButton.click()

# cart view
cartView = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[1]/div/a')
cartView.click()

# qty button
qty = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[2]/main/article/div/div/form/table/tbody/tr[1]/td[5]/div/input')
qty.send_keys()

# going to payment center
go_toPayment = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[2]/main/article/div/div/div[2]/div/div/a')
go_toPayment.click()

# billing info
firstName = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/main/article/div/div/form[3]/div[1]/div[1]/div[1]/div/p[1]/span/input')
firstName.send_keys('James')
lastName = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/main/article/div/div/form[3]/div[1]/div[1]/div[1]/div/p[2]/span/input')
lastName.send_keys('Bot')

streetAddress = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/main/article/div/div/form[3]/div[1]/div[1]/div[1]/div/p[4]/span/input')
streetAddress.send_keys('123 fuck off lane')

# apt, suite, unit, ect... optional
unitAddress = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/main/article/div/div/form[3]/div[1]/div[1]/div[1]/div/p[5]/span/input')
unitAddress.send_keys('999')

townOrcity = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/main/article/div/div/form[3]/div[1]/div[1]/div[1]/div/p[6]/span/input')
townOrcity.send_keys('East hartford')


state = driver.find_element_by_xpath('/html/body/span/span/span[1]/input')
state.send_keys('Connecticut')
state.click()










