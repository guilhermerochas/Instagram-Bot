#!/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import random
from urllib import request
import os


class instagramBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Edge(executable_path=driver_path)
        self.ig_path = 'https://www.instagram.com/'

    def login(self, username, password):
        self.driver.get(self.ig_path + "accounts/login")
        time.sleep(4)
        self.driver.find_elements_by_class_name('_2hvTZ')[0].send_keys(
            username)
        self.driver.find_elements_by_class_name('_2hvTZ')[1].send_keys(
            password)
        time.sleep(1)
        button = self.driver.find_element_by_class_name(name='Igw0E')
        button.click()
        time.sleep(4)

    def get_all_posts(self, url):
        self.url = url
        self.driver.get(self.ig_path + url)
        time.sleep(3)
        posts = self.driver.find_elements_by_class_name('_9AhH0')[0]
        posts.click()
        time.sleep(2)
        if not os.path.exists('./imgs/' + self.url):
            os.mkdir('./imgs/' + self.url)
        self.__get_posts()

    def __get_posts(self):
        while (True):
            self.__open_new_tab(self.driver.current_url)
            try:
                next = self.driver.find_element_by_class_name('_65Bje')
                time.sleep(2)
                next.click()
            except:
                break
            time.sleep(2)

    def __open_new_tab(self, url):
        self.driver.execute_script('''window.open("''' + url +
                                   '''","_blank");''')
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2)
        self.__get_files()
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def __get_files(self):
        self.__check_file_type(post_pos=0)
        while (True):
            print("Procurando se existem mais imagens nesse post...")
            self.__check_file_type(post_pos=0)
            time.sleep(1)
            try:
                self.driver.find_element_by_class_name('_6CZji').click()
            except:
                break

    def __check_file_type(self, post_pos):
        try:
            video = self.driver.find_element_by_class_name(
                'tWeCl').get_attribute('src')
            self.__download_file(file_addr=video, extension='mp4')
        except:
            picture = self.driverfind_element_by_class_name(
                'FFVAD').get_attribute('src')
            self.__download_file(file_addr=picture, extension='jpg')

    def __download_file(self, file_addr, extension):
        time.sleep(1)
        request.urlretrieve(file_addr,
                            filename='./imgs/' + self.url + '/file_' +
                            str(random.randint(0, 10000)) + '.' + extension)


def main():
    instabot = instagramBot(driver_path='./path/to/your/webdriver')


if __name__ == "__main__":
    main()
