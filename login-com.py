from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime

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
career_year=dvr.find_element(By.XPATH, '//*[@id="career_min_0"]/option[21]')
career_year.click()

# 근무형태
jtype= dvr.find_element(By.CSS_SELECTOR, '#job_type_list > li:nth-child(1) > span > label')
jtype.click()

# 급여 - 면접 후 결정
pay = dvr.find_element(By.XPATH, '//*[@id="salary_category"]/option[7]')
pay.click()

# 직무 추가
ad=dvr.find_element(By.CSS_SELECTOR, '#jobCategory > div.area_data > div.selected_item > button.btn_add')
ad.click()

# 직무 검색
jsearch = dvr.find_element(By.CSS_SELECTOR, '#recommend_search_input')
jsearch.send_keys('qa')

# qa 선택
time.sleep(0.5)
jsearch_qa = dvr.find_element(By.XPATH, '//*[@id="job_cate_search_99"]')
# click()이 안되면 send.keys 해보자. 쟤가 아마... input 타입이라 클릭이 안되고 send.keys가 된거같기도 해
jsearch_qa.send_keys(Keys.SPACE)
jsearch_submit = dvr.find_element(By.CSS_SELECTOR, '#jobCategory > div.area_data > div.wrap_layer > div > div.area_btn > button.btnSizeL.colorBlue.btn_complete')
jsearch_submit.click()

# 공고 제목 입력
rec_nm=dvr.find_element(By.CSS_SELECTOR, '#title')
# 월+일 4자로 보여주기 (ex. 0628)
a=(str(datetime.today().month)+str(datetime.today().day)).zfill(4)
rec_nm.clear()
rec_nm.send_keys(str(a)+'사람인 테스트 공고입니다. 지원 불가합니다.')

# 템플릿 반영
tem_apply=dvr.find_element(By.CSS_SELECTOR, '#template_insert')
tem_apply.click()

# 등록
submit = dvr.find_element(By.CSS_SELECTOR, '#content > div.wrap_recruit_frm > div.wrap_bottom_btn > button')
submit.click()

