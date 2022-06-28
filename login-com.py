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

#공고등록 페이지 이동
url='https://www.saramin.co.kr/zf_user/memcom/recruit/select-recruit-type'
dvr.get(url)

#일반공고
ori = dvr.find_element(By.CSS_SELECTOR,'#content > div > div > ul > li:nth-child(2) > a')
ori.click()

# 새로 쓰기
new = dvr.find_element(By.CSS_SELECTOR, '#btnAddRecruit')
new.click()

time.sleep(1)

# 모집부문명 작성
apply_nm=dvr.find_element(By.CSS_SELECTOR, '#recruitment_title_0')
apply_nm.send_keys('test')

# 경력 - 경력
career = dvr.find_element(By.CSS_SELECTOR, '#line_detail_0 > div.fulldata > div:nth-child(2) > div.area_data.type_txt > span:nth-child(2) > label')
career.click()

# 근무형태
jtype= dvr.find_element(By.CSS_SELECTOR, '#job_type_list > li:nth-child(1) > span > label')
jtype.click()

# 직무 추가
ad=dvr.find_element(By.CSS_SELECTOR, '#jobCategory > div.area_data > div.selected_item > button.btn_add')
ad.click()

# 직무 검색
jsearch = dvr.find_element(By.CSS_SELECTOR, '#recommend_search_input')
jsearch.send_keys('qa')

# qa 선택
time.sleep(0.5)
jsearch_qa = dvr.find_element(By.XPATH, '//*[@id="job_cate_search_99"]')
jsearch_qa.click()
jsearch_submit = dvr.find_element(By.CSS_SELECTOR, '#jobCategory > div.area_data > div.wrap_layer > div > div.area_btn > button.btnSizeL.colorBlue.btn_complete')
jsearch_submit.click()




