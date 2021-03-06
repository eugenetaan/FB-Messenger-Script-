import os

chromedriver_path = 'C:/Program Files/chromedriver'
OS = 'Windows'       # accepts Mac and Windows os comment out import pyautoit if Mac (Capital - case sensitive)
QR_Code = False      # For non campaign broadcast
testing = False         # Use bobs cafe to test
manual_mode = False      # For instances where unable to automate typing into textbox, sending images (eg Aria Autocomplete fields)
user = "YK"             # Diff user acc to switch between YiKai and own acc
chatbox_element = 'textarea'  # accept textarea and div (div chatbox is unable to linebreak)

#-------For Desktop with D drive -------------------------------------------------------------------------------------
# template for Processed CSVs: f'D:/Pycharm Projects/DataSciCourse/venv/Processed_CSVs/{merchant_name}.csv'
# template for tracker_files: f'D:/Pycharm Projects/DataSciCourse/venv/Tracker_in_progress/{merchant_name}_tracker.csv'
# template for CSVs and Imgs Location: D:\\Downloads\\ChunyangImg.png
#-------For Laptop with C Drive --------------------------------------------------------------------------------------
# template for Processed CSVs: f'C:/Users/eugen/PycharmProjects/FBMessengerScript/Processed_CSVs/{merchant_name}.csv'
# template for tracker_files: f'C:/Users/eugen/PycharmProjects/FBMessengerScript/Tracker_in_progress/{merchant_name}_tracker.csv'
# template for CSVs and Imgs Location: 'C:\\Users\\eugen\\Downloads\\AI.png'
#QR code location : 'C:\\Users\\eugen\\PycharmProjects\\FBMessengerScript\\temp_qr_code.jpg'

# For csv_cleaning file, leave blank if not in use
original_csvs = ['C:\\Users\\eugen\\Downloads\\hxl.csv']

merchant_name = 'Ichiho'
if testing == False:
    if os.path.isfile(f'C:/Users/eugen/PycharmProjects/FBMessengerScript/Tracker_in_progress/{merchant_name}_tracker.csv'):
        customers_file_location = f'C:/Users/eugen/PycharmProjects/FBMessengerScript/Tracker_in_progress/{merchant_name}_tracker.csv'
    else:
        customers_file_location = f'C:/Users/eugen/PycharmProjects/FBMessengerScript/Processed_CSVs/{merchant_name}.csv' #if first time use customer file location template, else use save_to_file template
    save_to_file = f'C:/Users/eugen/PycharmProjects/FBMessengerScript/Tracker_in_progress/{merchant_name}_tracker.csv'
else:
    save_to_file = 'Testing.csv'
customer_sending_limit = 90

#----------------- Message Contents and Xpaths Below ------------------------------------------------------------------

if user == 'YK': # run FB Script
    if QR_Code:
        #-------------------CHUNYANG--------------------------------------------------
        promotion_text = ['New safety measures got you down? Turn that frown upside down with this promo. Buy 2 get 1 free for takeaway orders on your next visit AND get 10% cashback. We are also offering free next day delivery service for purchases above $15!',
                          '',
                          'Just present the QR Code below to claim your voucher!',
                          '',
                          'Valid for redemption at our outlet',
                          '- Orchard Rd, #02-25 25A, Singapore 238896',
                          '',
                          '*Valid till 16 June',
                          '*Vouchers are not redeemable for dine-in and delivery orders',
                          '*Free delivery excludes hot / warm drinks.',
                          '*Only redeemable for customers using Aimazing cashback',]
        imgs = ['C:\\Users\\eugen\\Downloads\\ChunyangPromo.png','C:\\Users\\eugen\\PycharmProjects\\FBMessengerScript\\temp_qr_code.jpg']

    else:
        promotion_text = ['1. Earn 10% cashback when you dine-in at HXL that is valid for buffet and alacarte \n 2. Those with cashback that was expired during 1st May - 20th June will be given extended expiry date until 21st July.'

        ]
        imgs = ['C:\\Users\\eugen\\Downloads\\hxl.jpeg']

#-----------------------------------------------------------------------------------------------------------------------
elif user=='Eugene':  # run FB Script New layout
    if QR_Code:
        promotion_text = [
            'New safety measures got you down? Turn that frown upside down with this promo. Get 30% off for Osmanthus Honey Green Tea on your next visit AND enjoy 5% cashback',
            '',
            'Just present the QR Code below to claim your voucher!',
            '',
            'Valid for redemption at our outlets',
            '- Lot One Shoppers Mall #B1-25',
            '-Jurong Point #01-45/46  (10am - 11.30pm)',
            '-HDB HUB Toa Payoh Central Lor 6, Blk 190 #01-536',
            '-Rivervale Mall #01-14',
            '-BLK 407 Ang Mo Kio Ave 10 #01-747',
            '',
            '*Valid till 16 June',
            '*Max 2 cups per transaction / per visit for every customers',
            '*Not applicable on Weekends',
            ]
        imgs = ['C:\\Users\\eugen\\PycharmProjects\\FBMessengerScript\\temp_qr_code.jpg']
    else:
        promotion_text = [
            'Testing',
                          ]
        imgs = ['C:\\Users\\eugen\\PycharmProjects\\FBMessengerScript\\temp_qr_code.jpg']

#------------------------------------------------Xpaths -----------------------------------------------------------

#RMB TO CHANGE Check duplicate xpath in f string in script file itself line 332
# for checking duplicates:
users_xpath = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/div[1]/div/div/div/li[@]'

# for close search function:
exit_button_xpath = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div[1]/div/div/div/a/i'

# chat history first user
first_user = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/div[1]/div/div/div/li[1]'

# messenger convo history
message_history_xpath = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/div[1]/div/div/div/div/div[2]'
convo_description_xpath = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/div[1]/div/div/div/div/div[1]'

# default
# file_upload_button_xpath = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div/div[3]/div[1]/div'

#HXL
file_upload_button_xpath = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div/div[3]/div[2]/div'
