from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# id = input("id를 입력하세요: ")
# pw = input("pw를 입력하세요: ")

id = 'tkfkadlsxptmxm'
pw = 'tkfkadls12!@'

# 로그인창 열기
dvr=webdriver.Chrome('./chromedriver')
dvr.get('https://www.saramin.co.kr/zf_user/auth?url=%2Fzf_user%2F')

#로그인
com_btn=dvr.find_element(By.XPATH,'//*[@id="login_frm"]/div[2]/div[1]/ul[1]/li[2]/a')
id_box=dvr.find_element(By.CSS_SELECTOR,'#id')
pw_box=dvr.find_element(By.CSS_SELECTOR,'#password')
lgn_btn=dvr.find_element(By.CSS_SELECTOR,'#login_frm > div.login_page_wrap > div.login_input_wrap > div.login-form > button')

com_btn.click()
id_box.send_keys(id)
pw_box.send_keys(pw)
lgn_btn.click()