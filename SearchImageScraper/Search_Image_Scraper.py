
# coding: utf-8

# In[ ]:

"""
The objective of this programme is to pull images from google image search
In order for this module to run correctly selenium must be installed.
You will also need the relevant webdriver for selenium
This module was built with Chrome in mind, so ensure that you amend
the browser driver if needed
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib
from os import path

class Image_Scraper:
    """This class will find images based on criteria
    inputs for this class are:
    image_subject : string
        The subject that you're looking for
    image_number : int
        The number of images you're looking for
    file_save_name : str
        The name that you want the files saved under
    folder_destination : str
        The folder that you wish to save images to
    Example:
    
    test_image_scraper=Image_Scraper('Oranges',5,file_save_name='Oranges ',folder_destination="C://Users//Me//Documents//Testing//Turtles//")
    
    """
    images=[]
    def __init__(self,image_subject,image_number,browser_driver="chrome",file_save_name="Image",folder_destination=""):
        self.image_subject=image_subject
        self.image_number=image_number
        self.browser_driver=browser_driver.lower()
        self.file_save_name=file_save_name
        self.folder_destination=folder_destination
        self.test_folder_destination()
        self.run_search()
        self.save_images()
    def run_search(self):
        
        #website used for searching
        regular_search="https://images.google.com/"
        
        #select webdriver to use - launch webdriver
        if self.browser_driver=='chrome':
            driver=webdriver.Chrome()
        elif self.browser_driver=='firefox':
            driver=webdriver.FirefoxProfile
        elif self.browser_driver=='ie' or self.browser_driver=='internet explorer':
            driver=webdriver.Ie
        elif self.browser_driver=='opera':
            driver=webdriver.Opera
        elif self.browser_driver=='phantomjs':
            driver=webdriver.PhantomJS
        elif self.browser_driver=='remote':
            driver=webdriver.Remote
        elif self.browser_driver=='desiredcapabilities':
            driver=webdriver.DesiredCapabilities
        elif self.browser_driver=='actionchains':
            driver=webdriver.ActionChains
        elif self.browser_driver=='touchactions':
            driver=webdriver.TouchActions
        elif self.browser_driver=='proxy':
            driver=webdriver.Proxy
        else:
            print('invalid webdriver selected. Please ensure a valid webdriver is selected.\n Default option is set to Chrome')
            return None
        #go to website to search and find all images
        driver.get(regular_search)
        element=driver.find_element_by_xpath("//input[@title='Search']")
        element.send_keys(self.image_subject,Keys.ENTER)
        img_elements=driver.find_elements_by_xpath("//img[@class='rg_ic rg_i']")
        self.images = driver.find_elements_by_tag_name('img')
    def save_images(self):
        """Iterate through images and save to requested destination"""
        file_destination=self.folder_destination + self.file_save_name
        image_counter=0
        for image in self.images:
            if image_counter==0:
                image_counter+=1
                continue
            if image_counter > self.image_number:
                print('Run complete')
                break
            image_counter+=1
            image_name=file_destination + ' {0}.jpg'.format(image_counter-1)
            src=image.get_attribute('src')
            urllib.request.urlretrieve(src,image_name)
    def test_folder_destination(self):
        if self.folder_destination != "":
            if not path.exists(self.folder_destination):
                print('Warning: No such folder destination exists')

