from selenium import webdriver
from time import sleep
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
# Login file with username and password
from login_instagram import username, password
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pickle


class InstaBot:
    """Instagram Bot that filters all people from your account that don't follow you back and unfollows them
    """

    def __init__(self, name, pw):
        """Login and some necessary clicks on the beginning

        :param name: your username
        :param pw: your password
        """
		# TODO: insert your chromedriver path here
        executable_path = ""
        self.driver = webdriver.Chrome(executable_path)
        self.username = name
        self.driver.get("https://instagram.com")
        # Cookie Window
        WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR,
             'body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.bIiDR'))).click()
        # Paste Username
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#loginForm > div > div:nth-child(1) > div > label > input"))).send_keys(username)
        # Paste Password
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#loginForm > div > div:nth-child(2) > div > label > input"))).send_keys(pw)
        # Press Login Button
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR,
             '#loginForm > div > div:nth-child(3) > button'))).click()
        # Press Some other Buttons
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR,
             '#react-root > section > main > div > div > div > div > button'))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR,
             'body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm'))).click()

    def get_unfollowers(self):
        """Get all people which don't follow back

        :return: not_following_back: list, of people who don't follow you back
        """
        # Get on profile
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@href,'/{}')]".format(self.username)))).click()
        # Click on Following
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@href,'/following')]"))).click()
        # Get list of all people you follow
        following = self._get_names()
        # save it to a file
        with open("following.txt", "wb") as fp:  # Pickling
            pickle.dump(following, fp)
        # Click on Followers
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@href,'/followers')]"))).click()
        # Get list of followers
        followers = self._get_names()
        # save it to a file
        with open("follower.txt", "wb") as f:  # Pickling
            pickle.dump(followers, f)
        # get list of users you follow, but who don't follow you
        not_following_back = [user for user in following if user not in followers]
        # save it to a file
        with open("notfollowing.txt", "wb") as y:  # Pickling
            pickle.dump(not_following_back, y)
        return not_following_back

    def _get_names(self):
        """Gets list of all names from follower or following list

        :return: names_list: list of followers or following
        """
        # scroll until the end, so all users are in the list, sleep(5) between each scrolling
        self.scroll(10)
        # Initialize Scraper for the page
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        # get all elements from the list
        name_list = soup.find_all("span", "Jv7Aj mArmR MqpiF")
        # get the usernames from all elements
        names_list = [name.get_text() for name in name_list]
        # Press close button on the end and return names_list
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR,
             "body > div.RnEpo.Yx5HN > div > div > div:nth-child(1) > div > div:nth-child(3) > button > div > svg"))).click()
        return names_list

    def scroll(self, scroll_pause_time):
        """Scrolls down as long as possible

        :param scroll_pause_time: pause between each scrolling to load next elements
        :return:
        """
        # sleep to find scroll_box
        sleep(scroll_pause_time)
        # scroll_box for scrolling
        scroll_box = self.driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div.isgrP")
        # Get scroll height
        last_height = self.driver.execute_script("return arguments[0].scrollHeight", scroll_box)

        while True:
            # Scroll down to bottom
            self.driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", scroll_box)
            # Wait to load page
            sleep(scroll_pause_time)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return arguments[0].scrollHeight", scroll_box)
            if new_height == last_height:
                # If heights are the same it will exit the function
                break
            last_height = new_height

    def unfollow_all(self):
        """Unfollow all people from not_following_back list

        :return:
        """
        # read usernames from file
        with open("notfollowing.txt", "rb") as y:  # Pickling
            unfollow_list = pickle.load(y)
        count = 0
        # unfollow_list.pop()
        unfollow_list_help = unfollow_list
        for i in reversed(unfollow_list):
            self.unfollow(i)
            count = count + 1
            # remove unfollowed user from list
            unfollow_list_help.remove(i)
            # save updated list to file
            with open("notfollowing.txt", "wb") as y:
                pickle.dump(unfollow_list_help, y)
            # do not unfollow too many because instagram can block you
            if count == 200:
                break

    def unfollow(self, obj):
        """Unfollow for each profile

        :param obj: one username of not_following_back list
        :return:
        """
        # get profile
        self.driver.get("https://instagram.com/" + obj)
        ignored_exceptions = (StaleElementReferenceException)
        # press unfollow button
        WebDriverWait(self.driver, 30, ignored_exceptions=ignored_exceptions).until(EC.element_to_be_clickable(
            (By.CLASS_NAME,
             'glyphsSpriteFriend_Follow.u-__7'))).click()
        # confirm unfollow
        WebDriverWait(self.driver, 20, ignored_exceptions=ignored_exceptions).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR,
             "body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.-Cab_"))).click()
        sleep(2)


if __name__ == '__main__':
    my_bot = InstaBot(username, password)
    my_bot.get_unfollowers()
    my_bot.unfollow_all()
