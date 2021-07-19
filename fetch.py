# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 13:15:58 2021

@author: AVINASH
"""

from datetime import datetime as dt
from time import sleep
import datetime

# selenium imports
import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys as keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC



def get_xpaths():
    val = {"live": "//div[@class = 'event']//div[@class = 'status red']//span",
           "teamnames" : "//div[@class = 'event']//p[@class = 'name']", # more than one
           "scoreinfo": "//div[@class = 'event']//span[@class = 'score-info']", # one is empty
           "scores": "//div[@class = 'event']//span[@class = 'score']",# more than one
           "status": "//div[@class = 'event']//div[@class = 'status-text']//span",
           "over": "//span[@class = 'match-comment-over']",  # [0].text
           "run": "//div[@class = 'match-comment-run']//span",
           "ballinfo": "//div[@class = 'match-comment-short-text']", #[0].text
           "commentary": "//div[@class = 'match-comment-long-text']//p",  # [0].text
           "allteams": "//div[@class = 'match-score-block']//p[@class = 'name']", # more than one
           
           
     }
    return val


class Commenter:
    """Main commentary class object"""
    def __init__(self,mstr):
        self.id = dt.now().strftime('%M%S%f')
        
        # initialization
        self.status = False
        self.xpaths = get_xpaths()
        self.match = mstr
        self.logfile = "./logs/"+ self.id+".txt"
        self.log("ID: "+ mstr + self.id + " status: " + str(self.status))
        
        
        # browser intialization
        options = uc.ChromeOptions()
        options.add_experimental_option('w3c', False)
        options.add_argument("--headless")
        
        self.browser = uc.Chrome(options = options)
        self.browser.set_window_size(1669,827)
        
        self.browser.get('https://google.com')
        
        # decode team names from given string
        self.A, self.B = self.decode_team(mstr)
        #print(self.A, self.B,"a")
        pass
    
    def decode_team(self, mstr):
        return mstr[:mstr.find("vs")-1], mstr[mstr.find('vs')+3:]
        
    
    def ea(self, element_path):
        """element availability check"""
        #check if element is available
        try:
            self.browser.find_element(By.XPATH, element_path)
        except NoSuchElementException:
            return False
        return True  
    
    def fe(self,element_path,more_than_one = False):
        """fetch element(s)"""
        
        element = None
        # wait for 10 seconds max before timing out
        try:
            if more_than_one:
                element = self.browser.find_elements(By.XPATH,element_path)
            else:
                element = WebDriverWait(self.browser, 15).until(
                EC.presence_of_element_located((By.XPATH, element_path)))
        except:
            msg = f"Element Not found at location {element_path}"
            self.log(msg)
        return element
    
    def check_availability(self):
        """checks if match is live"""
        # Find the match and click on it
        self.browser.get("https://www.espncricinfo.com/live-cricket-score")   
        e = self.fe(self.xpaths['allteams'], more_than_one=True)
        for i in range(0,len(e),2):
            if self.issame(self.A, self.B, e[i].text.lower(), e[i+1].text.lower()):
                self.browser.execute_script("arguments[0].click();", e[i])
                self.status = True
                break   
        sleep(2)
            
        # Goto commentary and Check if it is live
        url  = self.browser.current_url.split('/').pop(-1)
        url = self.browser.current_url.replace(url,"ball-by-ball-commentary")
        if self.ea(self.xpaths['live']) and self.fe(self.xpaths['live']).text == "LIVE":
            self.status  = True
        else:
            self.status = False
        self.log(f"Checking status: {self.status}")
        self.browser.get(url)
        
        return self.status
    
    
    def issame(self, a , b, c , d):
        if a == c and b == d:
            return True
        elif a == d and b == c:
            return True            
        else:
            return False
        
        
    def scrap(self, old = ""):
        """Fetches comment text and updated match info"""
        # if asked for notifications
        if self.ea("//button[text()='Not Now']"):
            self.fe("//button[text()='Not Now']").click()
        
        self.browser.execute_script("window.scrollTo(0, 300);");
        # extract info
        val = {}
        e = self.fe(self.xpaths['scores'], more_than_one = True)
        if self.ea(self.xpaths['teamnames']):
            e = self.fe(self.xpaths['teamnames'], more_than_one = True)
            self.A = e[0].text
            self.B = e[1].text
            val['A'] = self.A
            val['B'] = self.B
            
        if self.ea(self.xpaths['scores']):
            e = self.fe(self.xpaths['scores'], more_than_one = True)
            try:
                val['Ascore'] = e[0].text
            except:
                val['Ascore'] = ""
            try:
                val['Bscore'] = e[1].text
            except:
                val['Bscore']= ""
            
        if self.ea(self.xpaths['scoreinfo']):
            e = self.fe(self.xpaths['scoreinfo'], more_than_one = True)
            if e[0].text == "":
                val['scoreinfo'] = e[1].text
            else:
                val['scoreinfo'] = e[0].text
        
        if self.ea(self.xpaths['over']):
            val['over'] = self.fe(self.xpaths['over']).text
        
        if self.ea(self.xpaths['ballinfo']):
            val['ballinfo'] = self.fe(self.xpaths['ballinfo']).text 
                
        if self.ea(self.xpaths['commentary']):
            val['commentary'] = self.fe(self.xpaths['commentary']).text
        
        if self.ea(self.xpaths['run']):
            val['run'] = self.fe(self.xpaths['run']).text
            
        if self.ea(self.xpaths['status']):
            val['status'] = self.fe(self.xpaths['status'], more_than_one = True)[0].text
        
        
        self.log(str(val))
        return val
    
    def log(self, msg):
        """Writes log files"""
        msg = str(datetime.datetime.now()) +"  "+ msg + "\n"
        # print(msg)
        f = open(self.logfile,"a")
        f.write(msg)
        f.close()
        
    def end(self):
        self.browser.close()
        self.browser.quit()
        
        

if __name__ == "__main__":
    c = Commenter("pakistan women vs zimbabwe women")
    a = c.check_availability()
    a = c.scrap()
    sleep(4)
    c.scrap()
    sleep(4)
    c.scrap()
    c.end()
    pass