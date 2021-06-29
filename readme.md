# FB Business Suite Messenger Script  #

## Goal ## 
Automate broadcasting of messages/promotions through FB Business Suite to relevant Aimazing Customers 

## Description ##
This is a script using selenium to broadcast messages through a FB Page to a list of relevant customers. Selenium was used for the script as there is no relevant API available for messenger broadcast at the time of development.

The general flow of events would look like this: <br>
Broadcast Request (Customer Service/Success) -->  Generation and cleaning of CSVs --> Broadcast --> Post Broadcast Updates 

The script will be used for 2 parts, generation of processed CSVs and broadcasting. 

#### Broadcast Request ####
Customer Success / Service and Marketing will generally be contacting you to broadcast. Theres a excel sheet for them to fill up and for you to update namely, Merchant Broadcasting Requests.

#### Generation and cleaning of CSVs ####
1. Query the list of customers from the AImazing Database and download it in the csv format. Do take note that for merchants with different outlets eg. Whaletea you will need to query and download multiple csvs.
2. Next head to the variable files and place all the filepaths of the downloaded CSVs in the original CSVs array as well as fill in the merchant name.
3. Head over to the CSV processing file and run the code to clean, sort and combine (if applicable) the csvs


Csvs will be sorted by customers with the most lifetime visits
QR Code will be required for promotions that are limited to current AImazing Customers / Promotions that can only be reedemed once

If a qr code is required, you will need to send the processed CSV to Xavier Liew or one of the engineers to update the UUIDs into the database before broadcasting can start.


#### Broadcasting ####
1. Before broadcasting, you will need to ensure that the XPaths eg <br>`xpath='/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/div[1]/div/div/div/li[1]' `<br> and CSS selectors eg <br> `chatbox = driver.find_element_by_css_selector('textarea[placeholder="Write a reply…"]')`<br> are working for the merchant facebook page. To do this use chrome dev tools to inspect the elements stated in the variables file and right click and copy full xpath to compare xpath. 
2. Next update the merchant name, the CSV you are sending from and the number of users to send to (capped at 150 / day due to FB regulations, not a hard cap but try not to go above 250-300 a day). Also fill in the message and imgs to be sent. 
3. Run the script

Sending generally takes anywhere from 40mins to 1hr10mins for 150 users, depending on img file size and complexity of message as well as rate of error. Generally there will be 5% error rate for reasons such as user not found, name in DB is not full name, etc etc. Look at code for more details. Do take note that you will be unable to use your machine effectively during broadcast. 

Xpaths requires regular maintenance as full xpath is the absolute position of the element in the HTML file structure and any slight UI changes by FB may break it. On the other hand CSS Selectors tend to have less issues. However Xpaths is still used as certain functions eg check_duplicate makes use of the li[@] element in the xpath to iterate through the list, moreover some elements do not have any styling and hence CSS selector cannot be used.

Most of the xpath variables will be found in the variables file however there is an f string variable in the actual script so remember to change this as well <br> 
`user = driver.find_element_by_xpath(f'/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/div[1]/div/div/div/li[{customer_position}]')`

#### Post-Broadcast ####
Update excel sheet upon completion of the broadcasts for the day.


#### Additional Good to Know ####
Functions in the CSV_processing file including get status which will return a more detailed progress report. 

There are also functions to dynamically change a placeholder value in variables promotion text. 

There might be error occuring when duplicates are being sent due to the first index in the list somehow registering as a different number. Running the code again usually solves the issue. Else change the csv file directly.

Compressing images before sending to reduce broadcasting time duration

Sending too many of the same link will cause message to not be sent and all prev messages to be revoked.

In the event the facebook UI change drastically you will need to restructure the code to the accomodate the new UI

#### Controlling Variables in variables file ####
* OS - to delcare os type for which send img function to be used 
* QR_code - for promotions requiring QR code 
* testing - use pre written dictionary to test dataset
* manual_mode - for FB text boxes that are unable to be automated ie div fields instead of textarea fields
* user - which account to be used, update in username_pw file as well
* chatbox_element - used to determine if the chatbox uses a textarea element or div element for input
  * textarea elements look like this <br> `<textarea type="text" class="_1p7p _5id1 _4dv_ _58al uiTextareaAutogrow" placeholder="Write a message…"></textarea>`
  * div elements look like this <br> `<div class="_1p1v" id="placeholder-bjaas" style="white-space: pre-wrap;">Write a reply…</div>`<br> or this <br> `<div aria-autocomplete="list" aria-controls="js_353" aria-describedby="placeholder-bjaas" aria-expanded="false" aria-label="Write a reply…" class="notranslate _5rpu" contenteditable="true" role="combobox" spellcheck="true" style="outline: none; user-select: text; white-space: pre-wrap; overflow-wrap: break-word;"><div data-contents="true"><div class="" data-block="true" data-editor="bjaas" data-offset-key="c8uua-0-0"><div data-offset-key="c8uua-0-0" class="_1mf _1mj"><span data-offset-key="c8uua-0-0"><br data-text="true"></span></div></div></div></div>`


## Requirements ##
#### Required Libraries (not in Python Standard Library) ####
* pandas
* selenium
* qrcode
* PyAutoIt (Windows) - Comment out this import statement if using Mac
* PyAutoGui (Mac)   

The script requires a facebook account with access to the relevant FB page. Insert the FB account credentials under username_pw.py before starting broadcast

PyAutoIt is able to directly control the windows GUI but for Mac Users PyAutoGui works by clicking at predetermined coordinates on the screen. Hence different Mac users may need to reconfigure the send_image_mac function for their own screens by using `pyautoit.position()`
