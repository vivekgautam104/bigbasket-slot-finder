# Big Basket Home Delivery Slot Finder
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-2-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
A cross platform tool that finds available delivery slots for Big Basket Home delivery site.

****
Users in United States can use our other tool for the ["Amazon Fresh" delivery tool](https://github.com/ojasvi92/Amazon-Fresh-Delivery-Slot-Notifier-COVID-19)
****
Last Updated - April 20,2020. If downloaded your executable on or before April 20,2020, please download the new executable to benefit from the new features released.
****

## Pre-requisites: 

1. Please make sure that you have Google Chrome browser installed on your system. The tools works only with Google Chrome.

2. Fill up your cart/basket with your complete order before running the tool so as to quickly proceed with checkout as soon as a slot is found. However, you can fill up your cart after launching the application as well.

3. Turn up the volumne of your system for the voice notification.



## Option 1 - Download and run the executables

1. Download the respective executable file for MAC OS and Windows OS:
	* MAC - Click [here](https://github.com/vivekgautam104/bigbasket-slot-finder/files/4507568/bigbasket_slotfinder_macOS.zip)
	* Windows - Click [here](https://github.com/vivekgautam104/bigbasket-slot-finder/files/4507569/bigbasket_slotfinder_win.zip)

2. Unzip the file

3. Run the respective executable file.

## Option 2 - Execution of Source Code 

1. Make sure Python 3.x is installed on your system

2. Clone the repo

3. Run `pip3 install -r requirements.txt`

4. Run `python3 bigbasket_slotfinder.py`

## Instructions:

1. Run the executable file. Click on “Launch Big Basket” to proceed.

![GUILaunch](https://raw.githubusercontent.com/vivekgautam104/bigbasket-slot-finder/master/SlotFinder/images/DeliverySlotFinderLaunchBigBasket.png)

2. The tool will automatically download the compatible Google Chrome driver during the first run in line with your browser version. If promted, click allow access.

3. A new incognito Google Chrome window will be launched and redirected to Big Basket sign in page. Login to your Big Basket account and select your delivery location:

![BigBasket Login](https://raw.githubusercontent.com/vivekgautam104/bigbasket-slot-finder/master/SlotFinder/images/login.png)

4. Fill up your Big Basket cart/basket with your complete order, reach the checkout page which would look like this:

![BasketPage](https://raw.githubusercontent.com/vivekgautam104/bigbasket-slot-finder/master/SlotFinder/images/basketpage.png)

5. Click on “Notify Me” button on the tool and turn up the volume of your system.

![GuiNotifyMe](https://raw.githubusercontent.com/vivekgautam104/bigbasket-slot-finder/master/SlotFinder/images/DeliverySlotFinderNotifyMe.png)

6. The application will keep running in the background, checking for available slots. The voice notification will be sent out once a slot is found.

7. DO NOT explicitly close the launched window if you want to keep the tool running in the background. 

8. Once you're notified, quickly select a slot and finish checking out because available slots disappear almost instantly.


## Inspiration and idea behind this tool:

The Coronavirus 2019 pandemic caused a surge in demand for grocery delivery services, making it nearly impossible to find an open delivery slot. My intention in providing this tool is to help people get the essentials at their doorsteps without having to step out of home. The idea sprang up when I saw my friends and family struggling to get groceries and essentials due to unavailability of slots.

## Notes:
1. The script will stop running if you navigate elsewhere from the checkout page. You need to re-run the tool and re-login for the code to continue finding the slots.

2. If you are logged out due to inactive session, you need to re-run the tool.


## Disclaimer:
The tool does not guarantee a definite slot. It avoids the manual work of having to check for slots countless number of times in order to get one. The tool runs in background and checks for available slots for you and alerts you when a slot is found.

Please keep trying and eventually a slot should work! 

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/ojasvi92"><img src="https://avatars3.githubusercontent.com/u/4646567?v=4" width="100px;" alt=""/><br /><sub><b>Ojasvi Maleyvar</b></sub></a><br /><a href="#design-ojasvi92" title="Design">🎨</a> <a href="#infra-ojasvi92" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="#maintenance-ojasvi92" title="Maintenance">🚧</a></td>
    <td align="center"><a href="https://github.com/shivangimgupta"><img src="https://avatars3.githubusercontent.com/u/32472018?v=4" width="100px;" alt=""/><br /><sub><b>shivangimgupta</b></sub></a><br /><a href="#userTesting-shivangimgupta" title="User Testing">📓</a> <a href="https://github.com/vivekgautam104/bigbasket-slot-finder/commits?author=shivangimgupta" title="Documentation">📖</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!