import pandas as pd
import username_pw
import time
import random
import qrcode
from variables import *
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import autoit

def test_input_bobs_cafe():
    d = { 'first_name' : ['Eugene', 'Ng', 'Xavier', "Yi Kai", 'Tin', 'Gabriel', 'Bai', 'Chih', 'Tim', 'Zhen Ye'], 'last_name' : [ 'Tan', 'Zheng Wei', 'Chin', 'Kong', 'En Hao', 'Lee', 'Shun Yao', 'Ying Ho', 'Lorenz', 'Neo'], 'token' : ['FB_V-12_6438e8dd-2988-45e7-9f64-d80f666fdd6b', 'FB_V-13_41934190-3835-476c-8753-0307f206abff', 'FB_V-14_3338f930-0c27-477a-9c95-928e64b95a28',
        'FB_V-14_3338f930-0c27-477a-9c95-928e64b95a28','FB_V-14_3338f930-0c27-477a-9c95-928e64b95a28','FB_V-14_3338f930-0c27-477a-9c95-928e64b95a28','FB_V-14_3338f930-0c27-477a-9c95-928e64b95a28','FB_V-14_3338f930-0c27-477a-9c95-928e64b95a28','FB_V-14_3338f930-0c27-477a-9c95-928e64b95a28','FB_V-14_3338f930-0c27-477a-9c95-928e64b95a28']}
    global tracker
    tracker = pd.DataFrame(data=d)
    tracker['Name'] = tracker['first_name'] + ' ' + tracker['last_name']
    tracker['Message Status'] = 'Not Sent'
    tracker['expiry_date'] = '2021-08-26'
    print(tracker.head())

def client_info_input(customers_file_location):
    global tracker
    tracker = pd.read_csv(customers_file_location)
    if 'Name' in tracker.columns and 'Message Status' in tracker.columns:
        tracker = pd.read_csv(customers_file_location)
        print('Reading from tracker file.')
        print(tracker.head())
    else:
        tracker.fillna('', inplace= True)
        tracker['Name'] = tracker['first_name'] + ' ' + tracker['last_name']
        tracker['Message Status'] = 'Not Sent'
        print('Reading from initial csv file.')
        print(tracker.head())

def check_duplicate(username):
    name_list = []
    global duplicate_users
    duplicate_users = []
    global customer_position
    global no_of_users
    xpath = users_xpath
    for i in range(1, 50):
        xpath1 = xpath.replace('@', str(i))
        try:
            user = driver.find_element_by_xpath(xpath1)
        except NoSuchElementException:
            break

        if user.text == username:
            customer_position = i
            duplicate_users.append(i)

        no_of_users += 1
        name_list.append(user.text)

    count = name_list.count(username)
    if count == 1:
        return True
    else:
        return False

def update_tracker(status, i):
    global tracker
    # tracker.at[i, 'Message Status'] = status
    # message_status[i] = status --- This may return temporary object instead of actually editing the dataframe
    tracker.loc[i, 'Message Status' ] = status
    with open(save_to_file, 'w', newline='', encoding='utf-8') as t:
           tracker.to_csv(t)

def wait(xpath):
    try:
        myelem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
        return True
    except (TimeoutException, NoSuchElementException) as error:
        return False

def wait_css_selector(css_selector):
    try:
        search_field = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
        return True
    except:
        return False

def close_search():
    elem = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, exit_button_xpath)))
    exit_button = driver.find_element_by_xpath(exit_button_xpath)
    exit_button.click()

#Functions for sending of messages
def linebreak():
    chatbox.send_keys(Keys.SHIFT, Keys.ENTER)

def enter_text(text_to_send):
    for message in text_to_send:
            chatbox.send_keys(message)
            linebreak()

#Deprecated
# def send_image():
#     if len(imgs) >= 1:
#         print(token)
#         for img_path in imgs:
#             file_input = driver.find_element_by_xpath(file_input_xpath)
#             file_input.send_keys(img_path)
#         try:
#             send_button_clickable = WebDriverWait(driver, 20).until(
#                 EC.element_to_be_clickable((By.XPATH, send_button_xpath)))
#         except TimeoutException:
#             close_search()
#             return False
#         send_button = driver.find_element_by_xpath(send_button_xpath)
#         send_button.click()
#         return True

# def find_and_click_search_button():
#     search_button_clickable = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, search_button_xpath)))
#     search_button = driver.find_element_by_xpath(search_button_xpath)
#     search_button.click()

def find_and_enter_search_box():
    try:
        search_field = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Search"]')))
        search_box = driver.find_element_by_css_selector('input[placeholder="Search"]')
        try:
            for letter in customer_name[i]:
                time.sleep(0.3)
                search_box.send_keys(letter)
            time.sleep(2)
        except TypeError:
            return False
        return True
    except TimeoutException:
        return False

def check_for_history_else_enter_last_name():
    # check whether got chat history
    search_box = driver.find_element_by_css_selector('input[placeholder="Search"]')
    if wait(first_user):
        pass
    else:  # search using last name then first name because sometimes facebook doesnt give results using surname
        try:
            for letter in customer_name[i]:
                search_box.send_keys(Keys.BACKSPACE)
            last_name = tracker['last_name'][i]
            first_name = tracker['first_name'][i]
            for letter in last_name:
                search_box.send_keys(letter)
                time.sleep(0.2)
            search_box.send_keys(Keys.SPACE)
            for letter in first_name:
                search_box.send_keys(letter)
                time.sleep(0.2)
        except TypeError:
            close_search()
            return False
    if wait(first_user):
        return True
    else:
        close_search()
        return False

def click_on_messenger_convo_history():
    if wait(message_history_xpath):
        convo_description = driver.find_element_by_xpath(convo_description_xpath)
        if convo_description.text == 'MESSENGER CONVERSATIONS':
            messenger_convo = driver.find_element_by_xpath(message_history_xpath)
            messenger_convo.click()
            return True
        else:
            close_search()
            return False
    else:
        close_search()
        return False

def send_img_windows_gui():
    if len(imgs) > 0:
        for i in range(len(imgs)):
            try:
                file_upload_button = driver.find_element_by_xpath(file_upload_button_xpath)
            except:
                return False
            file_upload_button.click()
            autoit.win_wait_active("Open", 5)
            if autoit.win_exists("Open"):
                time.sleep(0.5)
                autoit.control_set_text("Open", "Edit1", imgs[i])
                autoit.control_send('Open', 'Edit1', "{ENTER}")
            image_sent = False
            while not image_sent: # testing using while loop to address auto it not sending text into file explorer
                try:
                    send_button_clickable = WebDriverWait(driver, 20).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[value="1"][type="submit"]')))
                    image_sent = True
                except TimeoutException:
                    print('Waiting to send image')
                    pass
                    # return False
            if not manual_mode:
                send_button = driver.find_element_by_css_selector('button[value="1"][type="submit"]')
                send_button.click()
    return True

def generate_dynamic_text(promotion_text, username):
    return_promo_text = []
    for sentence in promotion_text:
        return_promo_text.append(sentence.replace('<Customer name>', username))
    return return_promo_text

def generate_new_exp_date_text(promotion_text):
    return_text = []
    for sentence in promotion_text:
        return_text.append(sentence.replace('<new_exp>', tracker['expiry_date'][i]))
    print(return_text)
    return return_text

def get_delay():
    # random delay to prevent getting identified as bot on FB
    delay = random.randint(2, 7)
    return delay

# choose testing mode or actual run mode
if testing == True:
    test_input_bobs_cafe() #run this function for testing with Bob's cafe
else:
    client_info_input(customers_file_location) #run this function to generate tracker df for actual execution
start_time = time.time()


#prevent notifications from popping up
option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1})

#load open to messanger
driver = webdriver.Chrome(chrome_options=option,
                          executable_path=chromedriver_path)
driver.get('https://www.facebook.com/pages/?category=your_pages&ref=bookmarks')
actions = ActionChains(driver)

#sign in
username = driver.find_element_by_xpath('//*[@id="email"]')
username.send_keys(username_pw.username)
pw = driver.find_element_by_xpath('//*[@id="pass"]')
pw.send_keys(username_pw.pw)
pw.send_keys(Keys.ENTER)

successfully_sent = 0
customer_name = tracker['Name']
message_status = tracker['Message Status']

#iterate through csv to get each name
for i in range(len(tracker['Name'])):

    if successfully_sent != 0:
        time.sleep(get_delay())

    if successfully_sent >= customer_sending_limit: # Check if limit for the day is exceeded
        break
    if message_status[i] != 'Not Sent': # check if criteria for sending is met - entry not run before
        continue

    page_loaded = False
    while not page_loaded:
        try:
            myelem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Search"]')))
            page_loaded = True
        except (TimeoutException, NoSuchElementException) as error:
            print('Waiting for inbox')
            pass

    customer_position = None
    no_of_users = 0

    # Find search box and enter name into it
    if find_and_enter_search_box():
        pass
    else:
        update_tracker('Cannot type into search box/Empty name field', i)
        continue

    if check_for_history_else_enter_last_name():
        pass
    else:
        update_tracker('No chat history found', i)
        continue

    #check for duplicate
    if check_duplicate(customer_name[i]) and customer_position is not None:
        user = driver.find_element_by_xpath(f'/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/div[1]/div/div/div/li[{customer_position}]')
        print(user.text.split())
        user.click()
    elif no_of_users == 1:
        user = driver.find_element_by_xpath(first_user)
        print(user.text.split())
        user.click()
    else:
        # update_tracker('Duplicates Not Sent', i)
        # close_search()
        # continue
        no_of_duplicates_fb = len(duplicate_users)
        no_of_duplicates_file = sum(tracker['Name'] == customer_name[i]) #get number of duplicates in csv
        indexes_of_duplicates_in_file = tracker.index[tracker['Name'] == customer_name[i]].tolist() # get list of all duplicate index
        print(customer_name[i])
        print(indexes_of_duplicates_in_file)
        print(duplicate_users)

        if no_of_duplicates_fb == 0:
            update_tracker('No exact match duplicate not sent', i)
            close_search()
            continue

        close_search() # close so can re search and click all duplicates

        if QR_Code:
            if no_of_duplicates_file > no_of_duplicates_fb:
                 to_use = no_of_duplicates_fb
            else:
                to_use = no_of_duplicates_file
        else:
            to_use = no_of_duplicates_file



        for x in range(to_use):

            page_loaded = False
            while not page_loaded:
                try:
                    myelem = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Search"]')))
                    page_loaded = True
                except (TimeoutException, NoSuchElementException) as error:
                    print('Waiting for inbox')
                    pass

            # Find search box and enter name into it
            if find_and_enter_search_box():
                pass
            else:
                continue

            if check_for_history_else_enter_last_name():
                pass
            else:
                continue

            xpath = users_xpath
            xpath1 = xpath.replace('@', str(duplicate_users[x]))
            user = driver.find_element_by_xpath(xpath1)
            user.click()

            if click_on_messenger_convo_history():
                pass
            else:
                continue

            if QR_Code:
                token = tracker['token'][(indexes_of_duplicates_in_file[x])]
                qrCodeImg = qrcode.make(token)
                qrCodeImg.save('temp_qr_code.jpg')

            if not manual_mode:
                if wait_css_selector('textarea[placeholder="Write a reply…"]'):
                    # send text
                    chatbox = driver.find_element_by_css_selector('textarea[placeholder="Write a reply…"]')
                    enter_text(promotion_text)
                    # enter_text(generate_dynamic_text(promotion_text, tracker['Name'][i]))
                    chatbox.send_keys(Keys.RETURN)
                    # send image
                else:
                    continue
            if not send_img_windows_gui():
                continue

            successfully_sent += 1
            if successfully_sent % 1 == 0:
                print(
                    f'Duplicates of {i} sent, time running: {(time.time() - start_time):.2f}s -> {(time.time() - start_time) / 60:.2f}min"')

            if not manual_mode:
                close_search()

        for i in indexes_of_duplicates_in_file:
            if message_status[i] == 'Not Sent':
                update_tracker(f'Duplicates - Successfully Sent on {date.today()}', i)
        continue

#click on the messenger convo history
    if click_on_messenger_convo_history():
        pass
    else:
        update_tracker('Unable to click on messenger convo or Not Messenger User', i)
        continue

    if QR_Code == True:
        token = tracker['token'][i]
        qrCodeImg = qrcode.make(token)
        qrCodeImg.save('temp_qr_code.jpg')

    # send  image and text
    if not manual_mode:
        if wait_css_selector('textarea[placeholder="Write a reply…"]'):
            # send text
            chatbox = driver.find_element_by_css_selector('textarea[placeholder="Write a reply…"]')
            time.sleep(1)
            # enter_text(generate_dynamic_text(promotion_text, tracker['Name'][i]))
            enter_text(promotion_text)
            chatbox.send_keys(Keys.RETURN)
            # send image
        else:
            update_tracker('Cannot Enter Text into Text box', i)
            close_search()
            continue
    if not send_img_windows_gui():
        update_tracker('Image cannot be sent', i)
        continue

    #update tracker
    update_tracker(f'Successfully Sent on {date.today()}', i)
    successfully_sent += 1
    if successfully_sent % 1 == 0:
        print(f'{successfully_sent} sent this session, time running: {(time.time() - start_time):.2f}s -> {(time.time() - start_time) / 60:.2f}min"')

    #clear search field
    if not manual_mode:
        close_search()

print(f"Complete, sent to {successfully_sent} customers, time taken: {(time.time() - start_time):.2f}s -> {(time.time() - start_time)/60:.2f}min")

total_sent = sum(tracker['Message Status'].str.contains('Successfully Sent.*'))
total = len(tracker.index)
total_with_issues = sum(tracker['Message Status'].str.contains('cannot.*', case=False)) + sum(tracker['Message Status'].str.contains('Unable.*')) +sum(tracker['Message Status'].str.contains('No .*'))
Est_days_left = (total - total_sent - total_with_issues) / 150
users_left = total - total_sent - total_with_issues
print(f'Total sent across all sessions is {total_sent} out of {total}. Unable to send {total_with_issues} users. {users_left} users left. Estimated days left is {Est_days_left}')

# driver.quit() #to prevent memory leak issue chromedriver process doesnt get killed when closing browser manually



















