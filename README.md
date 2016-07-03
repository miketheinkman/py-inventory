# py-inventory
py-inventory generates a shopping list based on the barcodes of the items you throw away. This is a pet project of mine that I did mainly for my own entertainment, and because I can never remember what I need from the store. 

## Installation:
I recommend deploying to Heroku and using a raspberry pi with a touch-screen and a barcode scanner to keep things simple. I also use a barcode keyboard on Android to do some scanning in and out and product configuration. Deploying to Heroku is easy with Git and Heroku toolbelt since I already have a Procfile and requirements.txt. Basically just login to the toolbelt, create a project with 'heroku create <project-name>', and 'git push heroku master'

## Instructions:
Configure at least one vendor. After you have a vendor, you can start to configure and track items. That's basically it. You scan items in and out from the add and remove pages. To see your shopping list, click Shopping List, and choose a vendor. The list will also have an email option if you want to email the list to the vendor or yourself.

To configure email, edit the email related settings in the py_inventory/settings.py file. Once you enter your email info there, you should be able to email the lists.

I bookmark the vendors page on my phone desktop for easy access when I am at the store. The lists are done with dismissable div tags, so you can dismiss each item as you find it in the store. The items will not be added to inventory however until you scan them in from the add page
