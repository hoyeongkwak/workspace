from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')
driver.implicitly_wait(3)
driver.get('http://nid.naver.com/nidlogin.login')

driver.find_element_by_name('id').send_keys('hamolf')
driver.find_element_by_name('pw').send_keys('Happy001$')

driver.find_element_by_xpath('//*[@id="log.login"]').click()