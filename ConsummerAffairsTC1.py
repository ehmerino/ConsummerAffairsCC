'''
Created on 7 feb. 2019

@author: EHERRERA
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from random import *
import time

stateOptions__Select = ["Alaska",
                  "Alabama",
                  "Arkansas",
                  "Arizona",
                  "California",
                  "Colorado",
                  "Connecticut",
                  "District of Columbia",
                  "Delaware",
                  "Florida",
                  "Georgia",
                  "Hawaii",
                  "Iowa",
                  "Idaho",
                  "Illinois",
                  "Indiana",
                  "Kansas",
                  "Kentucky",
                  "Louisiana",
                  "Massachusetts",
                  "Maryland",
                  "Maine",
                  "Michigan",
                  "Minnesota",
                  "Missouri",
                  "Mississippi",
                  "Montana",
                  "North Carolina",
                  "North Dakota",
                  "Nebraska",
                  "New Hampshire",
                  "New Jersey",
                  "New Mexico",
                  "Nevada",
                  "New York",
                  "Ohio",
                  "Oklahoma",
                  "Oregon",
                  "Pennsylvania",
                  "Rhode Island",
                  "South Carolina",
                  "South Dakota",
                  "Tennessee",
                  "Texas",
                  "Utah",
                  "Virginia",
                  "Vermont",
                  "Washington",
                  "Wisconsin",
                  "West Virginia",
                  "Wyoming"]

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options, executable_path='driver\geckodriver.exe')
driver.maximize_window()
driver.get("https://www.consumeraffairs.com")
assert "ConsumerAffairs" in driver.title
driver.save_screenshot("screenshots/01_customer_affairs_screenshot.png")
allCategories__Link = driver.find_element_by_xpath("//a[@href='https://www.consumeraffairs.com/resources/#all-categories']")
allCategories__Link.click()
time.sleep(5)
driver.save_screenshot("screenshots/02_all_categories_screenshot.png")
financeCard__Expand = driver.find_element_by_partial_link_text("Take control of your finances")
financeCard__Expand.click()
time.sleep(5)
driver.save_screenshot("screenshots/03_finances_control_screenshot.png")
mortgages__Link = driver.find_element_by_xpath("//a[@href='https://www.consumeraffairs.com/finance/finance__companies.htm']")
mortgages__Link.click()
time.sleep(5)
driver.save_screenshot("screenshots/04_mortgages_screenshot.png")
loan__Link = driver.find_element_by_xpath("//a[@href='#choose-lender']")
loan__Link.click()
time.sleep(5)
driver.save_screenshot("screenshots/05_loan_screenshot.png")
calculator__Link = driver.find_element_by_xpath("//a[@href='https://www.consumeraffairs.com/finance/how-much-house-can-i-afford.html']")
calculator__Link.click()
time.sleep(5)
driver.save_screenshot("screenshots/06_calculator_screenshot.png")
annualIncome__Input = driver.find_element_by_xpath("//input[@name='household_income']")
interestRate__Input = driver.find_element_by_xpath("//input[@name='interest_rate']")
downPayment__Input = driver.find_element_by_xpath("//input[@name='down_payment']")
mortgageTerm__Input = driver.find_element_by_xpath("//input[@name='mortgage_term']")
stateValue__Select = driver.find_element_by_xpath("//select[@name='state_value']/option[text()='"+stateOptions__Select[randint(0, len(stateOptions__Select))]+"']")
annualIncome__Value = randint(0, 500000)
interestRate__Value = str(round(uniform(0, 10), 1))
downPayment__Value = randint(0, 270000)
mortgageTerm__Value = randint(15, 40)
annualIncome__Input.send_keys(annualIncome__Value)
interestRate__Input.send_keys(interestRate__Value)
downPayment__Input.send_keys(downPayment__Value)
mortgageTerm__Input.send_keys(mortgageTerm__Value)
stateValue__Select.click()
driver.save_screenshot("screenshots/07_calculator_result_screenshot.png")
time.sleep(5)
driver.close()
