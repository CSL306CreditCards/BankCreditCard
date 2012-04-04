"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.test import Client
from django.test import TestCase
#from django.utils import unittest
#from django.test.client import Client
#from selenium import selenium
import unittest
from selenium import webdriver
#from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
        
    def test_basic_mult(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(2 * 3, 6)
    def test_details(self):
        client = Client()
        response = client.get('/creditcard/home/')
        self.assertEqual(response.status_code, 200)

    def test_index(self):
        client = Client()
        response = client.get('/creditcard/home/')
        self.assertEqual(response.status_code, 200)		

    def test_statement_display(self):
        """
        Check the simple funds transfer
        """        
        c = Client()
        response = c.post('/creditcard/user/statement.html', {'card_number':'10001', 'from_date':'10002', 'to_date':5000})
        self.assertEqual(response.status_code, 301)
        #account = Bank_Account.objects.get(ba_acc_no="10001")
        #self.assertEqual(account.ba_acc_bal,Decimal(25000))
        #account2 = Bank_Account.objects.get(ba_acc_no="10002")
        #self.assertEqual(account2.ba_acc_bal,Decimal(68000))

    def test_forget_password(self):	
        c = Client()
        response = c.post('/creditcard/home/', {'':'10001', 'from_date':'10002', 'to_date':5000})
        self.assertEqual(response.status_code, 301)
        #account = Bank_Account.objects.get(ba_acc_no="10001")
        #self.assertEqual(account.ba_acc_bal,Decimal(25000))
        #account2 = Bank_Account.objects.get(ba_acc_no="10002")
        #self.assertEqual(account2.ba_acc_bal,Decimal(68000))



class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000/creditcard/home/"
        self.verificationErrors = []
    
    def test_login(self):
        driver = self.driver
        driver.get("http://localhost:8000/creditcard/home/")
        driver.find_element_by_name("username").clear()

        driver.find_element_by_name("username").send_keys("a")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("asdfghjk")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        
        
    def test_login_error(self):
        driver = self.driver
        driver.get("http://localhost:8000/creditcard/home/")
        driver.find_element_by_name("username").clear()

        driver.find_element_by_name("username").send_keys("x")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("asdfghjk")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()    
    
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException: return False
        return True
    
    def tearDown(self):
        #self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()



class PaymentTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000/creditcard/home/index.html"
        self.verificationErrors = []
    
    def test_payment(self):
        driver = self.driver
        driver.get("http://localhost:8000/creditcard/home/index.html")
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("a")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("asdfghjk")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_link_text("Payments").click()
        driver.find_element_by_name("card_number").clear()
        driver.find_element_by_name("card_number").send_keys("10704841418625110")
        driver.find_element_by_name("user_name").clear()
        driver.find_element_by_name("user_name").send_keys("Aayush")
        driver.find_element_by_name("password").send_keys("64597")
        driver.find_element_by_name("account_number").clear()
        driver.find_element_by_name("account_number").send_keys("111111111")
        driver.find_element_by_name("amount").clear()
        driver.find_element_by_name("amount").send_keys("11")
        driver.find_element_by_name("description").clear()
        driver.find_element_by_name("description").send_keys("payment test case")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        
    def test_payment2(self):
        driver = self.driver
        driver.get("http://localhost:8000/creditcard/home/index.html")
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("a")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("asdfghjk")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_link_text("Payments").click()
        driver.find_element_by_name("card_number").clear()
        driver.find_element_by_name("card_number").send_keys("10704841418625110")
        driver.find_element_by_name("user_name").clear()
        driver.find_element_by_name("user_name").send_keys("Aayush")
        driver.find_element_by_name("password").send_keys("64597")
        driver.find_element_by_name("account_number").clear()
        driver.find_element_by_name("account_number").send_keys("111111111")
        driver.find_element_by_name("amount").clear()
        driver.find_element_by_name("amount").send_keys("123")
        driver.find_element_by_name("description").clear()
        driver.find_element_by_name("description").send_keys("payment test case")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()    
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException: return False
        return True
    
    def tearDown(self):
        #self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()


class Auto(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000/creditcard/home/index.html"
        self.verificationErrors = []
    
    def test_auto(self):
        driver = self.driver
        driver.get("http://localhost:8000/creditcard/home/index.html")
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("a")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("asdfghjk")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_link_text("Services").click()
        driver.find_element_by_name("card_number").clear()
        driver.find_element_by_name("card_number").send_keys("10704841418625110")
        driver.find_element_by_name("account_no").clear()
        driver.find_element_by_name("account_no").send_keys("123")
        driver.find_element_by_name("description").clear()
        driver.find_element_by_name("description").send_keys("test")
        driver.find_element_by_name("amount").clear()
        driver.find_element_by_name("amount").send_keys("123")
        driver.find_element_by_name("date").clear()
        driver.find_element_by_name("date").send_keys("10")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        #driver.find_element_by_css_selector("a > i").click()
        
        
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException: return False
        return True
    
    def tearDown(self):
        #self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

class statement(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000/creditcard/home/index.html"
        self.verificationErrors = []
    
    def test_auto(self):
        driver = self.driver
        driver.get("http://localhost:8000/creditcard/home/index.html")
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("a")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("asdfghjk")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_link_text("Statements").click()
        driver.find_element_by_name("card_number").clear()
        driver.find_element_by_name("card_number").send_keys("10704841418625110")
        driver.find_element_by_name("from_date").clear()
        driver.find_element_by_name("from_date").send_keys("2011-11-23")
        driver.find_element_by_name("to_date").clear()
        driver.find_element_by_name("to_date").send_keys("2011-11-25")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        #driver.find_element_by_css_selector("a > i").click()
        
        
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException: return False
        return True
    
    def tearDown(self):
        #self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()


class RegisterTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000/creditcard/home/index.html"
        self.verificationErrors = []
    
    def test_register(self):
        driver = self.driver
        driver.get("http://localhost:8000/creditcard/home/index.html")
        driver.find_element_by_link_text("Register").click()
        driver.find_element_by_name("USER_NAME").clear()
        driver.find_element_by_name("USER_NAME").send_keys("karan")
        driver.find_element_by_id("PASSWORD").clear()
        driver.find_element_by_id("PASSWORD").send_keys("password")
        driver.find_element_by_id("CONFIRM_PASSWORD").clear()
        driver.find_element_by_id("CONFIRM_PASSWORD").send_keys("password")
        driver.find_element_by_name("FIRST_NAME").clear()
        driver.find_element_by_name("FIRST_NAME").send_keys("karan")
        driver.find_element_by_name("LAST_NAME").clear()
        driver.find_element_by_name("LAST_NAME").send_keys("verma")
        driver.find_element_by_name("FATHER_NAME").clear()
        driver.find_element_by_name("FATHER_NAME").send_keys("rajiv")
        driver.find_element_by_name("FATHER_NAME").clear()
        driver.find_element_by_name("FATHER_NAME").send_keys("rajiv verma")
        driver.find_element_by_name("MOTHER_NAME").clear()
        driver.find_element_by_name("MOTHER_NAME").send_keys("tulika verma")
        driver.find_element_by_name("GENDER").click()
        driver.find_element_by_name("EDUCATION").clear()
        driver.find_element_by_name("EDUCATION").send_keys("B.tech")
        driver.find_element_by_name("CURRENT_ADDRESS").clear()
        driver.find_element_by_name("CURRENT_ADDRESS").send_keys("street no. 14, rajnagar, chandigarh")
        driver.find_element_by_name("PD_CITY").clear()
        driver.find_element_by_name("PD_CITY").send_keys("chandigarh")
        driver.find_element_by_id("PD_PINCODE").clear()
        driver.find_element_by_id("PD_PINCODE").send_keys("143456")
        driver.find_element_by_name("PERMANENT_ADDRESS").clear()
        driver.find_element_by_name("PERMANENT_ADDRESS").send_keys("street no. 14, rajnagar, chandigarh")
        driver.find_element_by_name("TELEPHONE").clear()
        driver.find_element_by_name("TELEPHONE").send_keys("1520223456")
        driver.find_element_by_id("MOBILE").clear()
        driver.find_element_by_id("MOBILE").send_keys("9779614945")
        driver.find_element_by_name("COMPANY_TYPE").clear()
        driver.find_element_by_name("COMPANY_TYPE").send_keys("IT")
        driver.find_element_by_name("DESIGNATION").clear()
        driver.find_element_by_name("DESIGNATION").send_keys("Manager")
        driver.find_element_by_id("INCOME").clear()
        driver.find_element_by_id("INCOME").send_keys("1000000")
        driver.find_element_by_id("WORK_YEARS").clear()
        driver.find_element_by_id("WORK_YEARS").send_keys("10")		
        # ERROR: Caught exception [ERROR: Unsupported command [select]]
        driver.find_element_by_name("NAME").clear()
        driver.find_element_by_name("NAME").send_keys("Karan Verma")
        driver.find_element_by_name("OFFICE_ADDRESS").clear()
        driver.find_element_by_name("OFFICE_ADDRESS").send_keys("street no. 14, rajnagar, chandigarh")
        driver.find_element_by_name("ED_CITY").clear()
        driver.find_element_by_name("ED_CITY").send_keys("chandigarh")
        driver.find_element_by_id("ED_PINCODE").clear()
        driver.find_element_by_id("ED_PINCODE").send_keys("123434")
        driver.find_element_by_name("EMAIL_ID").clear()
        driver.find_element_by_name("EMAIL_ID").send_keys("karan@gmail.com")
        driver.find_element_by_name("ACCOUNT_NUMBER").clear()
        driver.find_element_by_name("ACCOUNT_NUMBER").send_keys("12345345")
        driver.find_element_by_name("BANK_NAME").clear()
        driver.find_element_by_name("BANK_NAME").send_keys("abc")
        driver.find_element_by_name("BRANCH_ADDRESS").clear()
        driver.find_element_by_name("BRANCH_ADDRESS").send_keys("chandigarh")
        driver.find_element_by_name("ACCOUNT_TYPE").clear()
        driver.find_element_by_name("ACCOUNT_TYPE").send_keys("saving")
        driver.find_element_by_name("CARD_TYPE").clear()
        driver.find_element_by_name("CARD_TYPE").send_keys("Platinum")
        # ERROR: Caught exception [ERROR: Unsupported command [select]]
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()


class Forgotpasswordtest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000/creditcard/home/index.html"
        self.verificationErrors = []
    
    def test_forgotpassword(self):
        driver = self.driver
        driver.get("/creditcard/home/")
        driver.find_element_by_link_text("exact:Forgot your password?").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("ppp")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
