import sys
import os

from  selenium.webdriver.common.by import By

SYSTEM =sys.platform
PATH_PROJECT = os.path.dirname(os.path.abspath(__file__))

if SYSTEM == "win32":
    CHROME_DRIVER = "chromedriver.exe"
else:
    CHROME_DRIVER = "chromedriver"

DRIVER_PATH = os.path.join(PATH_PROJECT, "../driver", CHROME_DRIVER)
IMPLICITLY_WAIT = 8
EXPLICITLY_WAIT = 30

DEFAUND_LOCATOR_TYPE = By.XPATH

if SYSTEM == "windows":
    CHROME_DRIVER = "chromedriver.exe"
else:
    CHROME_DRIVER = "chromedriver"
