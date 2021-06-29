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
QR Code will be required] for promotions that are limited to current AImazing Customers / Promotions that can only be reedemed once

If a qr code is required, you will need to send the processed CSV to Xavier Liew or one of the engineers to update into database before broadcasting can start.


#### Broadcasting ####
1.Before broadcasting, you will need to ensure that the XPaths / CSS selectors (usually CSS selectors won't have issues) are working for the merchant facebook page. To do this use chrome dev tools to inspect the elements stated in the variables file and click on copy full xpath to compare. This requires regular maintenance as full xpath is the absolute position of the element in the HTML file structure and any maintenance / update by FB may break it. At the same time ensure that your FB Business Suite UI is the same as what is coded for as FB might overhaul the UI and you might have to change some parts of the code.<br>
2.Next update the merchant name, the CSV you are sending from and the number of users to send to (capped at 150 / day due to FB regulations, not a hard cap but try not to go above 250-300 a day). Also fill in the message and imgs to be sent. <br>
3. Run the script

Sending generally takes anywhere from 40mins to 1hr10mins for 150 users, depending on img file size and complexity of message as well as rate of error. Generally there will be 5% error rate for reasons such as user not found, name in DB is not full name, etc etc. Look at code for more details. Do take note that you will be unable to use your machine effectively during broadcast.

#### Post-Broadcast ####
Update excel sheet upon completion of the broadcast for the day.


#### Additional Good to Know ####
Theres many hidden functions in the CSV_processing file including get status which will return a more detailed progress report. Read the code to find out more

There are also functions to dynamically change a placeholder value in variables promotion text. Read code to find out more

There might be error occuring when duplicates are being sent due to the first index in the list somehow registering as a different number. Running the code again usually solves the issue. Else change the csv file directly.

Compress images before sending to reduce time duration

Sending too many of the same link will cause message to not be sent and all prev messages to be revoked.

Any additional upgrades is welcome and you can push to your own github repo :). 
(idea for you to input all merchants and text at once and the script will go down the list)


## Requirements ##
#### Required Libraries (not in Python Standard Library) ####
* pandas
* selenium
* qrcode
* PyAutoIt (Windows) - Comment out this import statement if using Mac
* PyAutoGui (Mac)   


### Variables control file ###
* OS - to delcare os type for which send img function to be used 
* QR_code - for promotions requiring QR code 
* testing - use pre written dictionary to test dataset
* manual_mode - for FB text boxes that are unable to be automated ie aria autocomplete fields instead of textarea fields
* user - which account to be used, update in username_pw file as well
* chatbox_element - used to determine if the chatbox uses a textarea element or div element for input
