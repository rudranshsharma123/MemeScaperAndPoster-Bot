from redditScraper import RedditHandler
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
# PATH = 'C:/Users/gaura/Desktop/geckodriver'

# ##### Handling of Allow Pop Up In Facebook
option = Options()
option.add_argument("--disable-infobars")
# option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# # Pass the argument 1 to allow and 2 to block
# option.add_experimental_option("prefs", { 
#     "profile.default_content_setting_values.notifications": 2 
# })

driver = webdriver.Firefox(executable_path="geckodriver", options=option)
# driver.maximize_window()
driver.get("https://www.facebook.com/")

class fbPoster():
  def __init__(self, driver):
    self.driver = driver
###Login To The Account
  def login(self, id,password):
    email = self.driver.find_element_by_id("email")
    email.send_keys(id)
    Password = self.driver.find_element_by_id("pass")
    Password.send_keys(password)
    sleep(10)
    button = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button").click()
    pass
#### Post Content On FaceBook
  def post_content(self, post):
    button = self.driver.find_element_by_class_name("sx_0b6f88").click()
    sleep(3) ## A 3 second break in the program so that everythin loads perfectly
    actions= ActionChains(self.driver) ##Action Chains
    actions.send_keys(Keys.TAB)  ##Press TAB
    actions.send_keys(Keys.ENTER) ##Press ENTER
    actions.send_keys(post)
    actions.send_keys(Keys.TAB * 10)  ### Press TAB 10 Times to reach POST button
    actions.send_keys(Keys.ENTER) ### Press ENTER to post the content on facebook
    actions.perform()  ## To perfrom all the operations in the action chains
    pass

  def go_to_page(self):
    page_button = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div/div/div[1]/div[2]/ul/li/div/a/div[1]/div[2]/div/div/div/div/span/span")
    page_button.click()
    sleep(5)
  
  def post_on_page(self, image):
      
      post_button = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div/div[4]/div[2]/div/div[2]/div[1]/div/div/div[1]/div[2]/div/div")
      sleep(5)
      post_button.click()
      sleep(5)
      post_button = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div[1]")
      sleep(5)
      action = ActionChains(self.driver)
      action.send_keys(image)
      # action.send_keys(Keys.TAB * 5)
      # action.send_keys(Keys.ENTER)
      # action.send_keys(Keys.TAB * 5)
      # action.send_keys(Keys.ENTER)
      # action.send_keys("C:/Users/gaura/Desktop/cursedcomments/Cursed_ashes.jpg")
      action.perform()
      # sleep(5)
      # self.driver.send_keys("C:/Users/gaura/Desktop/cursedcomments/Cursed_ashes.jpg")
      # element = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div[2]/div/div[3]/div[1]/div[2]/div[1]/div/span/div/div/div[1]/div/div/div[1]")

      # post_button.send_keys("hello")

      # element.send_keys("C:/Users/gaura/Desktop/cursedcomments/Cursed_ashes.jpg")
      sleep(6)
      post_button = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div[2]/div/div[3]/div[4]/div/div")
      sleep(7)
      post_button.click()
      sleep(5)
      action= ActionChains(self.driver)
      action.send_keys(Keys.TAB)
      # # action.send_keys(Keys.ENTER)
      # action.send_keys_to_element("C:/Users/gaura/Desktop/cursedcomments/Cursed_ashes.jpg")
      # action.send_keys("C:/Users/gaura/Desktop/cursedcomments/Cursed_ashes.jpg")
      action.perform()




usernameFaceBook = "your email"
passwordFaceBook = "your password"

fb = fbPoster(driver)
fb.login(id = usernameFaceBook, password=passwordFaceBook)
fb.go_to_page()
fb.post_on_page("https://i.redd.it/lt5sj6peb3y61.jpg") #Sample Image
# login(username,password) 
sleep(5)	
# post_on_page()
# content = "I am a Bot Posting On Facebook"  ## Demo Content
# post_content(content)
