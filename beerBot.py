from selenium import webdriver
driver = webdriver.Chrome()

# request
driver.get('')

# selecting a product
cup_wanted = driver.find_element_by_xpath('')
cup_wanted.click()


# checkout
checkoutButton = driver.find_element_by_xpath('')
checkoutButton.click()

# cart view
cartView = driver.find_element_by_xpath('')
cartView.click()

# qty button
qty = driver.find_element_by_xpath('')
qty.send_keys()

# going to payment center
go_toPayment = driver.find_element_by_xpath('')
go_toPayment.click()

# billing info
firstName = driver.find_element_by_xpath('')
firstName.send_keys('James')
lastName = driver.find_element_by_xpath('')
lastName.send_keys('Bot')

streetAddress = driver.find_element_by_xpath('')
streetAddress.send_keys('')

# apt, suite, unit, ect... optional
unitAddress = driver.find_element_by_xpath('')
unitAddress.send_keys('')

townOrcity = driver.find_element_by_xpath('')
townOrcity.send_keys('')


state = driver.find_element_by_xpath('')
state.send_keys('')
state.click()










