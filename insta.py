from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
#import winsound
import os
#import autoit
import time


def post(username,passw,link,comment):

        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        mobile_emulation = { "deviceName": "Nexus 5" }
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)


        driver.get("https://www.instagram.com/")
        print("it,s done")
        break;

        time.sleep(10)
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]").click()
        time.sleep(4)
        driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/div[2]/button").click()
        time.sleep(4)
        driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[3]/div/label/input").send_keys(username)
        time.sleep(4)
        driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[4]/div/label/input").send_keys(passw)
        driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[4]/div/label/input").send_keys(Keys.RETURN)
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/button").click()
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/div[1]/section/nav[2]/div/div/div[2]/div/div/div[3]").click()
        time.sleep(5)
        autoit.win_active("Megnyitás") 
        time.sleep(2)
        autoit.control_send("Megnyitás","Edit1",link) 
        time.sleep(1.5)
        autoit.control_send("Megnyitás","Edit1","{ENTER}")
        time.sleep(4)
        driver.find_element_by_xpath("/html/body/div[1]/section/div[1]/header/div/div[2]/button").click()
        time.sleep(4)
        driver.find_element_by_xpath("/html/body/div[1]/section/div[2]/section[1]/div[1]/textarea").send_keys('Check the link in My Bio!'+Keys.RETURN+'Share the picture with your friend!'+Keys.RETURN+ 'Follow @'+username+Keys.RETURN+'#loveanimals #animals #animalsofinstagram #animalsco #cuteanimals #babyanimals #wildanimals #buzzfeedanimals #veganfortheanimals #splendid_animals #igcutest_animals #animalsmood #animals_captures #animalsaddict #animalshots #animals_in_world #animalsinfluence #animalslover #animalsanctuary #animalskull')
        time.sleep(4)
        driver.find_element_by_xpath("/html/body/div[1]/section/div[1]/header/div/div[2]/button").click()
        time.sleep(10)
        driver.close()
        driver.quit()
        


###---Like comment By hastag---
def like_comment_by_hastag(username,passw,hastag,comment):
        chrome_options = Options()  
        #chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920x1080")
        mobile_emulation = { "deviceName": "Nexus 5" }
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        chrome_driver2 = (r"C:\Users\Sandor Matyas\Downloads\chromedriver_win32\chromedriver.exe")
        driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver2)
        driver.get("https://www.instagram.com/")
        time.sleep(10)
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]").click()
        time.sleep(4)
        driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/div[2]/button").click()
        time.sleep(4)
        driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[3]/div/label/input").send_keys(username)
        time.sleep(4)
        driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[4]/div/label/input").send_keys(passw)
        driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[4]/div/label/input").send_keys(Keys.RETURN)
        time.sleep(4)
        driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/button").click()
        time.sleep(4)
        driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
        time.sleep(4)
        x=0
        while (x<6) :
                driver.get('https://www.instagram.com/explore/tags/{}/'.format(hastag))
                time.sleep(4)
                a=driver.find_elements_by_xpath("//*[@class='v1Nh3 kIKUG  _bz0w']")
                a[x].click()
                time.sleep(4)    
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)  
                b=driver.find_elements_by_xpath("//*[@class='QBdPU ']")
                b[1].click()
                time.sleep(1)
                b[2].click()
                time.sleep(4)
                c=driver.find_elements_by_xpath("//*[@class='Ypffh']")
                c[0].send_keys(comment+Keys.RETURN)
                time.sleep(3)
                x=x+1
        driver.close()
        driver.quit()

        
#---unfollow 10 pers---
def unfollow(username,passw):
        chrome_options = Options()  
        #chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920x1080")
        mobile_emulation = { "deviceName": "Nexus 5" }
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        chrome_driver2 = (r"C:\Users\Sandor Matyas\Downloads\chromedriver_win32\chromedriver.exe")
        driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver2)
        driver.get("https://www.instagram.com/")
        time.sleep(10)
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]").click()
        time.sleep(4)
        driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/div[2]/button").click()
        time.sleep(4)
        driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[3]/div/label/input").send_keys(username)
        time.sleep(4)
        driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[4]/div/label/input").send_keys(passw)
        driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[4]/div/label/input").send_keys(Keys.RETURN)
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/button").click()
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
        time.sleep(5)
        driver.get("https://www.instagram.com/"+username+"/")
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/div[1]/section/main/div/ul/li[3]/a").click()
        time.sleep(10)
        a=driver.find_elements_by_class_name('sqdOP')
        for i in range(10):
                a[i].click()
                time.sleep(1)
                driver.find_element_by_class_name('aOOlW').click()
                time.sleep(1)
        driver.close()
        driver.quit()

def follow(username,passw,account):
        chrome_options = Options()  
        #chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920x1080")
        mobile_emulation = { "deviceName": "Nexus 5" }
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        chrome_driver2 = (r"C:\Users\Sandor Matyas\Downloads\chromedriver_win32\chromedriver.exe")
        driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver2)
        driver.get("https://www.instagram.com/")
        time.sleep(10)
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]").click()
        time.sleep(4)
        driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/div[2]/button").click()
        time.sleep(4)
        driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[3]/div/label/input").send_keys(username)
        time.sleep(4)
        driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[4]/div/label/input").send_keys(passw)
        driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[4]/div/label/input").send_keys(Keys.RETURN)
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/button").click()
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
        time.sleep(5)
        driver.get("https://www.instagram.com/"+account+"/")
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/div[1]/section/main/div/ul/li[2]/a").click()
        time.sleep(15)
        a=driver.find_elements_by_class_name('sqdOP')
        for i in range(1,11):
                a[i].click()
                time.sleep(1)
                #driver.find_element_by_class_name('aOOlW').click()
                time.sleep(1)
        driver.close()
        driver.quit()


post('dobedooanimals','Appleid99.',r"C:\Users\Sandor Matyas\Downloads\animals.co\1 ("+str(i)+").jpg","comment")

