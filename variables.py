chromedriver_path = 'C:/Program Files/chromedriver'
QR_Code = True           # For non campaign broadcast
testing = False          # Use bobs cafe to test
manual_mode = False      # For instances where unable to automate typing into textbox, sending images (eg Aria Autocomplete fields)
user = "YK"              # Diff user acc to switch between YiKai and own acc

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
original_csvs = []

merchant_name = 'Chunyang'
if testing == False:
    # customers_file_location = f'C:/Users/eugen/PycharmProjects/FBMessengerScript/Processed_CSVs/{merchant_name}.csv' #if first time use customer file location template, else use save_to_file template
    customers_file_location = f'C:/Users/eugen/PycharmProjects/FBMessengerScript/Tracker_in_progress/{merchant_name}_tracker.csv'
    save_to_file = f'C:/Users/eugen/PycharmProjects/FBMessengerScript/Tracker_in_progress/{merchant_name}_tracker.csv'
else:
    save_to_file = 'Testing.csv'
customer_sending_limit = 150

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

        #-----------------ICHIHO---------------------------------------------------------
        # promotion_text = ['New safety measures got you down? Turn that frown upside down with one of the following promotions!',
        #                   '1) 10% off voucher for self-collection orders',
        #                   '2) 20% off voucher for 2nd Donburi, 30% off voucher for 3rd and additional Donburi',
        #                   '3) $88+ Family Package promotion, available for pre-order only (For next day collection/delivery) with last orders each day at 7:00 pm.',
        #                   '',
        #                   'Visit http://bit.ly/ichihofb or contact us at 8202 8168 to place your order!',
        #                   '',
        #                   'Just present the QR Code below to claim your voucher!',
        #                   '',
        #                   'Self-collection at our outlet:',
        #                   '- 12 Kallang Ave, Aperia Mall, #02-07/08, 339511',
        #                   '',
        #                   '*Valid till 16 June',
        #                   '*Customers may only redeem 1 promotion',
        #                   '*Discount on Donburi will be applied on lower priced items',
        #                   '*10% voucher for self-collection is not applicable for promotional packages',
        #                   '*Promotion cannot be stacked with cashback',
        #                   '*Exclusive of delivery and tax charges'
        #                   ]
        # imgs = ['C:\\Users\\eugen\\Downloads\\Ichiho.jpeg','C:\\Users\\eugen\\PycharmProjects\\FBMessengerScript\\temp_qr_code.jpg']

    else:
        promotion_text = []
        imgs = []

    # RMB TO CHANGE Check duplicate xpath in code which uses f string
    #for checking duplicates:
    users_xpath = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div[1]/div/div/div/li[@]'

    #for close search function:
    exit_button_xpath = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div[1]/div/div[1]/div/div[1]/div/div/div/div/a'

    #search button
    search_button_xpath = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div/div/div/div[3]/div'

    #chat history first user
    first_user = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div[1]/div/div/div/li'

    # messenger convo history
    message_history_xpath = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div[1]/div/div/div/div/div[2]'
    convo_description_xpath = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div[1]/div/div/div/div/div[1]'

    # default
    file_upload_button_xpath = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div[3]/div[1]/div/div'

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
        promotion_text = [ "Hi <Customer name>, in the light of the Covid-19 restrictions, we have extended your cashback expiry date to 13 August (Does not apply to Cashbacks expiring after 13 August). However, do note that this cashback can only be used for dine-in, not takeaways. We hope to see you soon!"
                          ]
        imgs = []

    #RMB TO CHANGE Check duplicate xpath in f string
    # for checking duplicates:
    users_xpath = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/div[1]/div/div/div/li[@]'

    # for close search function:
    exit_button_xpath = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div[1]/div/div/div/a'

    # chat history first user
    first_user = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/div[1]/div/div/div/li'


    # messenger convo history
    message_history_xpath = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/div[1]/div/div/div/div/div[2]'
    convo_description_xpath = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/div[1]/div/div/div/div/div[1]'

    # default
    # file_upload_button_xpath = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div[2]/div/div[1]/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div/div[3]/div[1]/div/div'

    # for pages with send products button (whaletea)
    file_upload_button_xpath = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div/div[3]/div[2]/div/div'



