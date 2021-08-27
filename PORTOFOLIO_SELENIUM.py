#PORTOFOLI RIZKA KHOIRO TUNNISA

from selenium import webdriver
import pytest
import time

class TestRizka():
    @pytest.fixture()
    def test_setup(rizka): 
        global driver   
        driver = webdriver.Chrome(executable_path="C:/Windows/System32/chromedriver.exe")
        driver.get("https://www.demoblaze.com/")
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("Test Completed") 
            
    def test_home(rizka, test_setup):
        driver.find_element_by_css_selector("#navbarExample > ul > li.nav-item.active > a").click()
        category = driver.find_element_by_id("cat")
        assert category.text == "CATEGORIES"
        time.sleep(3)

    def test_Contact(rizka, test_setup):
        driver.find_element_by_css_selector("#navbarExample > ul > li:nth-child(2) > a").click()
        driver.find_elements_by_css_selector("#exampleModal > div > div")
        driver.find_element_by_id("recipient-email").send_keys("rizkaknisa@gmail.com")
        driver.find_element_by_id("recipient-name").send_keys("Rizka Khoirotunnisa")
        driver.find_element_by_id("message-text").send_keys("Haloo")
        driver.find_element_by_css_selector("#exampleModal > div > div > div.modal-footer > button.btn.btn-primary").click()
        driver.switch_to.alert.accept()
        time.sleep(2)
       

    def test_aboutUs(rizka, test_setup):
        driver.find_element_by_css_selector("#navbarExample > ul > li:nth-child(3) > a").click()
        time.sleep(2)
        driver.execute_script('document.getElementsByTagName("video")[0].play()')
        time.sleep(2)
        driver.find_element_by_css_selector("#videoModal > div > div > div.modal-footer > button").click()
        time.sleep(2)

    def test_Cart(rizka, test_setup):
        driver.find_element_by_id("cartur").click()
        driver.find_element_by_css_selector("#page-wrapper > div > div.col-lg-1 > button").click()
        driver.find_element_by_id("name").send_keys("Rizka Khoirotunnisa")
        driver.find_element_by_id("country").send_keys("Indonesia")
        driver.find_element_by_id("city").send_keys("Palembang")
        driver.find_element_by_id("card").send_keys("abc")
        driver.find_element_by_id("month").send_keys("August")
        driver.find_element_by_id("year").send_keys("2021")
        driver.find_element_by_css_selector("#orderModal > div > div > div.modal-footer > button.btn.btn-primary").click()
        time.sleep(3)
        driver.find_element_by_css_selector("body > div.sweet-alert.showSweetAlert.visible > div.sa-button-container > div > button").click()
        
    #Haven't registered yet
    def testnegative_login(rizka, test_setup):
        driver.find_element_by_id("login2").click()
        driver.find_element_by_id("loginusername").send_keys("rizkakhns")
        driver.find_element_by_id("loginpassword").send_keys("Rizka123")
        driver.find_element_by_css_selector("#logInModal > div > div > div.modal-footer > button.btn.btn-primary").click()
        time.sleep(4)
        obj = driver.switch_to.alert
        setobj = obj.text
        time.sleep(2)
        obj.accept()
        assert  setobj == "User does not exist."

    #Succes
    def testpositive_signup(rizka, test_setup):
        driver.find_element_by_id("signin2").click()
        driver.find_element_by_id("sign-username").send_keys("rizkakhns")
        driver.find_element_by_id("sign-password").send_keys("Rizka123")
        driver.find_element_by_css_selector("#signInModal > div > div > div.modal-footer > button.btn.btn-primary").click()
        time.sleep(2)
        obj = driver.switch_to.alert
        setobj = obj.text
        time.sleep(2)
        obj.accept()
        assert  setobj == "Sign up successful."
    
    #use same data
    def testnegative_signup(rizka, test_setup):
        driver.find_element_by_id("signin2").click()
        driver.find_element_by_id("sign-username").send_keys("rizkakhns")
        driver.find_element_by_id("sign-password").send_keys("Rizka123")
        driver.find_element_by_css_selector("#signInModal > div > div > div.modal-footer > button.btn.btn-primary").click()
        time.sleep(2)
        obj = driver.switch_to.alert
        setobj = obj.text
        time.sleep(2)
        obj.accept()
        assert  setobj == "This user already exist."
     
    #Login when registered yet
    def testpositive_login(rizka, test_setup):
        driver.find_element_by_id("login2").click()
        driver.find_element_by_id("loginusername").send_keys("rizkakhns")
        driver.find_element_by_id("loginpassword").send_keys("Rizka123")
        driver.find_element_by_css_selector("#logInModal > div > div > div.modal-footer > button.btn.btn-primary").click()
        time.sleep(4)
        name = driver.find_element_by_id("nameofuser")
        assert name.text == "Welcome rizkakhns"

    #sidebar
    def test_phone(rizka, test_setup):
        driver.find_element_by_id("itemc").click()
        time.sleep(3)
        category = driver.find_element_by_id("article")
        assert category.text == "The Samsung Galaxy S6 is powered by 1.5GHz octa-core Samsung Exynos 7420 processor and it comes with 3GB of RAM. The phone packs 32GB of internal storage cannot be expanded."
        time.sleep(3)

  

        

        


        
 