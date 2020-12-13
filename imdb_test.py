import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

class ViewMovieDetails(unittest.TestCase):
    # declare variable to store the URL to be visited
    base_url="https://www.imdb.com/"

    # declare variable to store search term
    search_term="Silicon Valley"

    # --- Pre - Condition ---
    def setUp(self):
        # declare and initialize driver variable
        self.driver=webdriver.Chrome(executable_path="C:\\chromedriver.exe")       
        # browser should be loaded in maximized window
        self.driver.maximize_window()
        # driver should wait implicitly for a given duration, for the element under consideration to load.
        # to enforce this setting we will use builtin implicitly_wait() function of our 'driver' object.
        self.driver.implicitly_wait(10)  #10 is in seconds
    
    # --- Steps for IMDB_Search_TC_001 ---
    def test_IMDB_Search_TC_001_load_home_page(self):
        """User should be able to load IMDB's Home Page"""
        # to initialize a variable to hold reference of webdriver instance being passed to the function as a reference.
        driver=self.driver
        # to load a given URL in browser window
        driver.get(self.base_url)
        
        # test whether correct URL/ Web Site has been loaded or not
        self.assertIn("IMDb: Ratings, Reviews, and Where to Watch the Best Movies & TV Shows",self.driver.title)
        # to verify if the search results page contains any results or no results were found.
        self.assertNotIn("No results found.",self.driver.page_source) 
    
    # --- Steps for IMDB_Search_TC_002 ---
    def test_IMDB_Search_TC_002_search_for_a_movie(self):
        """User should be able to search movies."""
        # to load a given URL in browser window
        self.driver.get(self.base_url)         
        # to enter search term, we need to locate the search textbox
        searchTextBox=self.driver.find_element_by_id("suggestion-search")
        # to clear any text in the search textbox
        searchTextBox.clear()
        # to enter the search term in the search textbox via send_keys() function
        searchTextBox.send_keys(self.search_term)
        # to search for the entered search term
        searchTextBox.send_keys(Keys.RETURN)
        # to see movie title element
        searchMovieBox = self.driver.find_element_by_link_text("Silicon Valley")
        # to verify if the search results page loaded
        self.assertIn("Find - IMDb",self.driver.title)
        # to verify if the search results page contains any results or no results were found.
        self.assertNotIn("No results found.",self.driver.page_source)   

    # --- Steps for IMDB_Search_TC_003 ---
    def test_IMDB_Search_TC_003_see_movie_details(self):
        """User should be able to see movie details."""
        # to load a given URL in browser window
        self.driver.get(self.base_url)         
        # to enter search term, we need to locate the search textbox
        searchTextBox=self.driver.find_element_by_id("suggestion-search")
        # to clear any text in the search textbox
        searchTextBox.clear()
        # to enter the search term in the search textbox via send_keys() function
        searchTextBox.send_keys(self.search_term)
        # to search for the entered search term
        searchTextBox.send_keys(Keys.RETURN)
        # to click on movie title 
        searchMovieBox = self.driver.find_element_by_link_text("Silicon Valley").click()
        #self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath('//head/title[1]')
        # to verify if the search results page loaded
        self.assertIn("Silicon Valley (TV Series 2014–2019) - IMDb",self.driver.title)
        # to verify if the search results page contains any results or no results were found.
        self.assertNotIn("No results found.",self.driver.page_source)  

    # --- post - condition ---
    def tearDown(self):
        # to close the browser
        self.driver.quit()
        
if __name__ == '__main__':
    current_directory = os.getcwd()
    output_file = str(current_directory + "\\Reports")
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=output_file))