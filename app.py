from time import sleep
from selenium import webdriver

from pynput.keyboard import Key, Controller


def open_teams_in_browser(url, username="Test"):

    keyboard = Controller()
    driver = webdriver.Chrome("/Users/hoelzlm/chromedriver")
    driver.get(meeting_url)

    sleep(2)
    # cancle open in teams app
    keyboard.press(' ')

    driver.find_element_by_xpath('//*[@id="buttonsbox"]/button[2]').click()

    sleep(10)
    # accept camera and micro access
    keyboard.press(Key.tab)
    keyboard.press(Key.tab)
    keyboard.press(Key.tab)
    keyboard.press(' ')

    sleep(2)
    # input username
    name_input = driver.find_element_by_xpath('//*[@id="username"]')
    name_input.send_keys(username)

    sleep(2)
    # disable camera and mic
    driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[2]/toggle-button[1]/div/button').click()
    driver.find_element_by_xpath('//*[@id="preJoinAudioButton"]/div/button').click()

    sleep(2)
    # join meeting
    driver.find_element_by_xpath(
        '//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div[2]/button').click()

    # returning driver to be able to close the window
    return driver


def hang_up(driver):
    # click hang up button
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div/calling-screen/div/div[2]/calling-unified-bar/section/div/div/div[5]/items-group/div/item-widget/push-button/div/button').click()

    sleep(2)

    # close browser window
    driver.close()


if __name__ == '__main__':

    num_of_sessions = 5
    meeting_url = ""

    sessions = []

    for i in range(num_of_sessions):
        print(f"open session {i}")
        browser = open_teams_in_browser(meeting_url, username=f"Test {i}")
        sleep(2)


    input()

    for browser in sessions:
        hang_up(browser)


