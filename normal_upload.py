from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sympy import false, true

# id = input("id를 입력하세요: ")
# pw = input("pw를 입력하세요: ")

id = 'tkfkadlsxptmxm'
pw = 'tkfkadls12!@'

# 로그인창 열기
dvr=webdriver.Chrome('./chromedriver')
url='https://www.saramin.co.kr/zf_user/auth?url=%2Fzf_user%2F'
dvr.get(url)

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
dvr.get('https://www.saramin.co.kr/zf_user/memcom/recruit/select-recruit-type')

#일반 채용공고 선택
nor=dvr.find_element(By.CSS_SELECTOR,'#btnSelectRecruit > ul > li:nth-child(1) > div > button')
nor.click()

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
# a=문자형(오늘.월).2자리 될때까지 0으로 채우기+문자형(오늘, 일).2자리 될때까지 0으로 채우기
a=(str(datetime.today().month).zfill(2)+str(datetime.today().day).zfill(2))

i = 1

# 다 지우기
rec_nm.clear()
#제목: a+제목+i
rec_nm.send_keys(a+' 사람인 테스트 공고입니다. 지원 불가합니다. '+ str(i))

# 템플릿 반영
tem_apply=dvr.find_element(By.CSS_SELECTOR, '#template_insert')
tem_apply.click()

# 알럿이 나오면 누르고 아님 넘겨라
try:dvr.switch_to.alert.accept()
except: pass

while (true) :
    # 등록 버튼 클릭 > 알럿(저기서 알럿이 뜨면 동일한 제목~~ 일듯) 뜨면 닫고, 안뜨면 반복문 끝
    dvr.find_element(By.CSS_SELECTOR, '#content > div.wrap_recruit_frm > div.wrap_bottom_btn > button').send_keys(Keys.ENTER)
    try:dvr.switch_to.alert.accept()
    except: break

    i+=1
    rec_nm.clear()
    rec_nm.send_keys(a+' 사람인 테스트 공고입니다. 지원 불가합니다. '+ str(i))
    dvr.find_element(By.CSS_SELECTOR, '#content > div.wrap_recruit_frm > div.wrap_bottom_btn > button').send_keys(Keys.ENTER)

    try:dvr.switch_to.alert.accept()
    except: break

# 등록전 확인 레이어
# 주의: find_element하면 웹엘리먼트로 나오지만 find_elements하면 값이 리스트로 나온다

sel1 = dvr.find_elements(By.CLASS_NAME, 'salaryLawItem')

for i in sel1:
    i.send_keys(Keys.SPACE)

next=dvr.find_element(By.CSS_SELECTOR, '#submitAfterSalaryLawCheck')
next.click()

time.sleep(2)
# 효과높이기 - 등록
dvr.find_element(By.CSS_SELECTOR, '#btnRecruitComplete').click()

print("끝!")