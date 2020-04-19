# Big Basket Home Delivery Slot Finder
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-2-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
A cross platform tool that finds available delivery slots for Big Basket Home delivery site.

****
Users in United States can use our other tool for the ["Amazon Fresh" delivery website] (https://github.com/ojasvi92/Amazon-Fresh-Delivery-Slot-Notifier-COVID-19)
****


## Pre-requisites: 

1. Please make sure that you have Google Chrome browser installed on your system. The tools works only with Google Chrome.

2. Fill up your cart/basket with your complete order before running the process.

3. Turn up the volumne of your system for the voice notification.



## Option 1 - Download and run the executables

1. Download the respective executable file for MAC OS and Windows OS:
	* MAC - Click [here](https://github.com/vivekgautam104/bigbasket-slot-finder/releases/download/v1.0/bigbasket_slotfinder_macOS.zip)
	* Windows - Click [here](https://github.com/vivekgautam104/bigbasket-slot-finder/releases/download/v1.0/bigbasket_slotfinder_windows.zip)

2. Unzip the file

3. Run the respective executable file.

## Option 2 - Execution of Source Code 

1. Make sure Python 3.x is installed on your system

2. Clone the repo

3. Run `pip3 install -r requirements.txt`

4. Run `python3 bigbasket_slotfinder.py`

## Instructions:

1. The tool will automatically download the compatible Google Chrome driver during the first run in line with your browser version. If promted, click allow access.

2. A new incognito Google Chrome window will be launched. Login to your Big Basket account and select your delivery location within 60 seconds:

![BigBasket Login](https://raw.githubusercontent.com/vivekgautam104/bigbasket-slot-finder/master/SlotFinder/images/login.png)

3. After 60 seconds, the launched Google Chrome window will be minimized and process will keep running in the background. You can always open the Google Chrome window and check the status. DO NOT explicitly close the launched window if you want to keep the process running in the background. 

4. Your Big Basket cart/basket with complete order at checkout page would look like this:

![BigBasket Cart](https://raw.githubusercontent.com/vivekgautam104/bigbasket-slot-finder/master/SlotFinder/images/mybasket.png)

5. You will be alerted once a slot is found. 

6. The voice notification will be sent out when a slot is found.

7. Once you're notified, quickly select a slot and finish checking out because available slots disappear almost instantly.


## Inspiration and idea behind this tool:

The Coronavirus 2019 pandemic caused a surge in demand for grocery delivery services, making it nearly impossible to find an open delivery slot. My intention in providing this tool is to help people getting the essentials at their doorsteps without having to step out of home. The idea sprang up when I saw my friends and family struggling to get groceries and essentials due to unavailability of slots.

## Notes:
1. The script will stop running if you navigate elsewhere from the checkout page. You need to re-run the process and re-login for the code to continue finding the slots.

2. If you are unable to login and select a delivery address within 60 seconds, you need to re-run the process.

3. If you are logged out due to inactive session, you need to re-run the process.


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