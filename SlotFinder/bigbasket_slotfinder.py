import argparse
import logging
import os
import re
import subprocess
import sys
import time
import zipfile
from io import BytesIO
from sys import exit
from xml.etree import ElementTree

import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

__author__ = 'Vivek Gautam <vigsvivekgautam@gmail.com>'
__credits__ = ['Ojasvi Maleyvar', 'Anshuli Bisen', 'Shivangi Gupta']


# Function set_log_level
def set_log_level(log_level):
    is_level_set = True
    if log_level == 'DEBUG':
        logging.getLogger().setLevel(logging.DEBUG)
    elif log_level == 'INFO':
        logging.getLogger().setLevel(logging.INFO)
    elif log_level == 'WARNING':
        logging.getLogger().setLevel(logging.WARNING)
    elif log_level == 'ERROR':
        logging.getLogger().setLevel(logging.ERROR)
    elif log_level == 'CRITICAL':
        logging.getLogger().setLevel(logging.CRITICAL)
    else:
        is_level_set = False
        logging.info('Can not set requested log level to %s, please provide correct logging level', log_level)

    if is_level_set:
        logging.info('Log level set to %s', log_level)
# End set_log_level

def get_chrome_driver_filename():
    """
    Returns the filename of the binary for the current platform.
    :return: Binary filename
    """
    if sys.platform.startswith('win'):
        return 'chromedriver.exe'
    return 'chromedriver'

def get_chromedriver_url(version):
    """
    Returns the chrome drive url for the current platform.
    :return: Download URL for chromedriver
    """
    base_url = 'https://chromedriver.storage.googleapis.com/'
    platform, architecture = get_system_os()
    return base_url + version + '/chromedriver_' + platform + architecture + '.zip'


def load_google_chrome_webdriver():
    """
    Returns the chrome selenium webdriver.
    :return: google chrome selenium webdriver
    """
    try:
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        chrome_driver_filepath = download_chrome_drive(cwd=False)
        chrome_driver_dir = os.path.dirname(chrome_driver_filepath)
        driver = webdriver.Chrome(executable_path=chrome_driver_dir+'/chromedriver', options=chrome_options)
        return driver
    except Exception as e:
        logging.error("Unable to load Google Chrome Driver.")
        logging.error(str(e))
        exit(1)


def get_system_os():
    """
    Returns the OS and architecture for the platform
    :return: platform and architecture bit
    """
    try:
        if sys.platform.startswith('linux') and sys.maxsize > 2 ** 32:
            platform = 'linux'
            architecture = '64'
        elif sys.platform == 'darwin':
            platform = 'mac'
            architecture = '64'
        elif sys.platform.startswith('win'):
            platform = 'win'
            architecture = '32'
        return platform, architecture
    except Exception as e:
        logging.error("Could not determine the System Operating System")
        logging.error(str(e))
        exit(1)

def check_version(binary, required_version):
    try:
        version = subprocess.check_output([binary, '-v'])
        version = re.match(r'.*?([\d.]+).*?', version.decode('utf-8'))[1]
        if version == required_version:
            return True
    except Exception:
        return False
    return False

def get_chrome_version():
    """
    :return: the version of chrome installed on client
    """
    try:
        platform, architecture = get_system_os()
        if platform == 'mac':
            process = subprocess.Popen(['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', '--version'],
                                       stdout=subprocess.PIPE)
            version = process.communicate()[0].decode('UTF-8').replace('Google Chrome', '').strip()
        elif platform == 'win':
            process = subprocess.Popen(
                ['reg', 'query', 'HKEY_CURRENT_USER\\Software\\Google\\Chrome\\BLBeacon', '/v', 'version'], \
                stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
            version = process.communicate()[0].decode('UTF-8').strip().split()[-1]
        elif platform == 'linux':
            with subprocess.Popen(['chromium-browser', '--version'], stdout=subprocess.PIPE) as proc:
                version = proc.stdout.read().decode('utf-8').replace('Chromium', '').strip()
        return version
    except Exception as e:
        logging.error("Could not get the Google Chrome Version")
        logging.error(str(e))
        exit(1)


def get_major_version(version):
    """
    :param version: the version of chrome
    :return: the major version of chrome
    """
    return version.split('.')[0]

def get_matched_chromedriver_version(version):
    """
    :param version: the version of chrome
    :return: the version of chromedriver
    """
    try:
        doc = requests.get('https://chromedriver.storage.googleapis.com')
        # root = elemTree.fromstring(doc)
        root = ElementTree.fromstring(doc.content)
        for k in root.iter('{http://doc.s3.amazonaws.com/2006-03-01}Key'):
            if k.text.find(get_major_version(version) + '.') == 0:
                return k.text.split('/')[0]
        return
    except Exception as e:
        logging.error("Error in getting matched google chrome driver version")
        logging.error(str(e))
        exit(1)

def download_chrome_drive(cwd=False):
    """
    Downloads, unzips and installs chromedriver.
    If a chromedriver binary is found in PATH it will be copied, otherwise downloaded.
    :param cwd: Flag indicating whether to download to current working directory
    :return: The file path of chromedriver
    """
    try:
        chrome_version = get_chrome_version()
        if not chrome_version:
            logging.error("Chrome not installed. This application works only with Google Chrome")
            exit(1)
        chrome_driver_version = get_matched_chromedriver_version(chrome_version)
        if not chrome_driver_version:
            logging.error("Cannot find chromedriver for currently installed chrome version")
            exit(1)
        major_version = get_major_version(chrome_driver_version)
        if cwd:
            chrome_river_dir = os.path.join(
                os.path.abspath(os.getcwd()),
                major_version
            )
        else:
            chrome_driver_dir = os.path.join(
                os.path.abspath(os.path.dirname(__file__)),
                major_version
            )

        chrome_driver_filename = get_chrome_driver_filename()
        chrome_driver_filepath = os.path.join(chrome_driver_dir, chrome_driver_filename)

        if not os.path.isfile(chrome_driver_filepath) or \
                not check_version(chrome_driver_filepath, chrome_driver_version):
            logging.info('Downloading chromedriver ({chrome_driver_version})...')
            if not os.path.isdir(chrome_driver_dir):
                os.mkdir(chrome_driver_dir)
            download_endpoint = get_chromedriver_url(version=chrome_driver_version)
            try:
                response = requests.get(download_endpoint)
                if response.status_code != 200:
                    logging.error("Download URL not found")
                    exit(1)
            except Exception as e:
                logging.error('Failed to download chromedriver archive: {download_endpoint}')
            archive = BytesIO(response.content)
            with zipfile.ZipFile(archive) as zip_file:
                zip_file.extract(chrome_driver_filename, chrome_driver_dir)
        else:
            logging.info("Chrome Driver is already installed.")
        if not os.access(chrome_driver_filepath, os.X_OK):
            os.chmod(chrome_driver_filepath, 0o744)
        return chrome_driver_filepath

    except Exception as e:
        logging.error("Unable to download the Google Chrome Driver")
        logging.error(str(e))
        exit(1)


def send_voice_notifications(slot_found):
    """
    sends the notification if the slot is found or not found. It sends out voice notification on your system. So make sure system speakers are on
    """
    try:
        platform, architecture = get_system_os()
        if platform == 'mac':
            try:
                if slot_found:
                    os.system("say 'Slot found. Please reserve your slot. Slot not guaranteed.'")
                else:
                    os.system("say - 'Slot Not found. Please rerun the process.'")
            except Exception as e:
                logging.error("Unable to send notifications for MacOS. However please reserve the slot.")
                logging.error(str(e))
                exit(1)
        elif platform == 'win':
            try:
                from win32com.client import Dispatch
                speak = Dispatch("SAPI.SpVoice")
                if slot_found:
                    speak.Speak("Slot found. Please reserve your slot. Slot not guaranteed.")
                else:
                    speak.Speak("Slot Not found. Please rerun the process")
            except Exception as e:
                logging.error("Unable to send notifications for Windows OS. However please reserve the slot.")
                logging.error(str(e))
                exit(1)
        elif platform == 'linux':
            try:
                if slot_found:
                    os.system("spd-say 'Slot found. Please reserve your slot. Slot not guaranteed.'")
                else:
                    os.system("spd-say 'Slot Not found. Please rerun the process.'")
            except Exception as e:
                logging.error("Unable to send notifications for Linux OS. However please reserve the slot.")
                logging.error(str(e))
                exit(1)
    except Exception as e:
        logging.error("Unable to send out notifications. Please reserve your slot.")
        logging.error(str(e))
        exit(1)


def big_basket_slot_finder(driver, web_url):
    """
    master function which navigates the checkout process and sends out notification if the slot is found or not
    """
    try:
        driver.get(web_url)
        slot_found = False
        logging.info("Please login and do not forget to choose your delivery location in next 60 seconds")
        logging.info("Running the process in background. Chrome Window will be minimized")
        time.sleep(60)
        driver.minimize_window()
        while True:
            driver.get(web_url)
            time.sleep(30)  # Time to refresh the cart page
            logging.info("Looking for a Slot")
            try:
                checkout = driver.find_element_by_xpath("//button[@id = 'checkout']").click() # Clicking the checkout page
                time.sleep(10)
            except NoSuchElementException:
                send_voice_notifications(slot_found)
                logging.error("You are not logged in or a page refresh failure. Please rerun the process and login")
                exit(1)

            if 'checkout' in driver.current_url and 'Delivery Options' in driver.page_source:
                time.sleep(10)
                try:
                    slot_found = True
                    logging.info("Slot Found!")
                    driver.maximize_window()
                    num_of_retries_for_notification = 3
                    while num_of_retries_for_notification > 0:
                        try:
                            num_of_retries_for_notification -= 1
                            send_voice_notifications(slot_found)
                            time.sleep(10)
                        except Exception as e:
                            logging.error("Error in calling the notification Function")
                            logging.error(str(e))
                            exit(1)
                    logging.info('Job ended')
                    logging.info('Job ended on: ' + time.strftime('%Y-%m-%d %I:%M:%S %p'))
                    exit(0)

                except Exception as e:
                    logging.error("Error in finding the slot. Please retry running this process")
                    logging.error(str(e))
                    exit(1)


    except Exception as e:
        send_voice_notifications(slot_found)
        logging.error("Error in big_basket_slot_finder function")
        logging.error(str(e))
        exit(1)


def main(args):
    log_level = args.level.upper()

    if len(log_level) > 0:
        set_log_level(log_level)

    source_page_url = 'https://www.bigbasket.com/basket/?ver=1'
    web_driver = load_google_chrome_webdriver()
    big_basket_slot_finder(web_driver, source_page_url)


if __name__ == '__main__':
    print('\n')
    logging.basicConfig(format='[ %(asctime)s ] - %(levelname)s -: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                        level=logging.INFO)
    logging.info('Job started on: ' + time.strftime('%Y-%m-%d %I:%M:%S %p'))
    # Parse the parameters
    parser = argparse.ArgumentParser(description="")
    # Optional parameters
    parser.add_argument("-loglevel", "--level", help="Log level for logging configuration", default='')
    args = parser.parse_args()
    main(args)
