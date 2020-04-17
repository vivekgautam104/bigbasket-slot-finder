# Big Basket Home Delivery Slot Finder
A cross platform tool that finds available delivery slots for Big Basket Home delivery site.

## Pre-requisites: 

1. Please make sure that you have Google Chrome browser installed on your system. The tools works only with Google Chrome
2. Fill up you cart/basket with you complete order before running the process.
3. Turn up the volumne of your system for the voice notification.

## Instructions:

1. Download the respective executable file for MAC OS and Windows OS
	MAC - SlotFinder/mac/dist/bigbasket_slotfinder
	Windows - SlotFinder/win/dist/bigbasket_slotfinder.exe
2. Run the respective executable file
3. The tool will automatically download the compatible Google Chrome driver during the first run in line with you browser version. If promted, click allow access
4. A new incognito Google Chrome window will be launched. Login to your Big Basket account and select your delivery location within 60 seconds
![BigBasket Login](/images/login.png)
Format: ![Alt Text](url) 
5. After 60 seconds, the launched Google Chrome window will be minimized and process will keep running the background. You can always open the Google Chrome window and check the status. DO NOT explicitly close the launched window if you want to keep the process running in the background. 
6. Your Big Basket cart/basket with complete order at checkout page would look like this:
![BigBasket Login](/images/mybasket.png)
Format: ![Alt Text](url) 
7. You will be alerted once a slot is found. 
8. The voice notification will be sent out when a slot is found.
9. Once you're notified, quickly select a slot and finish checking out because available slots disappear almost instantly.

## Inspiration and idea behind this tool:

The Coronavirus 2019 pandemic caused a surge in demand for grocery delivery services, making it nearly impossible to find an open delivery slot. My intention in providing this tool is to help people getting the essentials at their doorsteps without having to step out of home. The idea sprang up when I saw my friends and family struggling to get groceries and essentials due to unavailability of slots.

## Notes:
The script will stop running if you navigate elsewhere from the checkout page. You need to re-run the process and re-login for the code to continue finding the slots.
If you are unable to login and select a delivery address within 60 seconds, you need to re-run the process.
If you are logged out due to inactive session, you need to re-run the process.


## Disclaimer:
The tool does not guarantee a definite slot. It avoids the manual work of having to check for slots countless number of times in order to get one. The tool runs in background and checks for available slots for you and alerts you when a slot is found.

Please keep trying and eventually a slot should work! 
