# Imports packages
import logging
import argparse
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options


# Logical switch for debugging
debug = False

# Defines logger format
LOG_FORMAT = "[%(asctime)s] %(levelname)s - %(message)s"

# Collects and parse arguments from users
parser = argparse.ArgumentParser(description="")
parser.add_argument(
    "-n",
    "--registration-number",
    help="KKM registration number to validate",
    required=True,
)

# Extracts and stores arguments
arguments, _ = parser.parse_known_args()
arguments = vars(arguments)

# Defines chrome options for non-debug mode
chrome_options = Options()
chrome_options.add_argument("--headless")


def main():
    """
    Returns boolean.
    True if registration number exists, and False if does not exist.

    param: registration: KKM registration number to validate.
    """
    # Defines registration_number
    registration_number = arguments["registration_number"]
    # Defines logger basis config
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

    logging.info(f"Product Registration Number: {registration_number}")

    # KKM regiatration number validation page
    url = "https://quest3plus.bpfk.gov.my/pmo2/index.php"

    # Begins try block for error handling
    try:
        # Initializes driver
        if not debug:
            # If not debug, runs headleass
            driver = webdriver.Chrome(
                service=Service(ChromeDriverManager().install()), options=chrome_options
            )

        else:
            # If debug, runs with ui
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        logging.info(f"Begin validating...")
        # Goes to url provided
        driver.get(url)

        # Click on search by box
        select = Select(driver.find_element("id", "searchBy"))

        # select by visible text
        select.select_by_visible_text("Product Registration Number")

        # Clicks on search box
        search_type = driver.find_element("id", "searchType")
        search_type.click()
        time.sleep(0.25)
        search_type.click()
        time.sleep(0.25)

        # Enter registartion number
        actions = ActionChains(driver)
        actions.send_keys(registration_number)
        actions.perform()
        time.sleep(0.25)

        # First element in list should exact match
        first_element = driver.find_element("id", "select2-searchTxt-results").text

        # Quites driver
        driver.quit()

        # Returns boolean for app usage
        if first_element == registration_number:
            # Surfaces results to humans
            logging.info(f"{registration_number} IS LISTED")
            return True
        else:
            # Surfaces results
            logging.info(f"{registration_number} IS NOT LISTED")
            return False

    # In case of error. Prompt user
    except:
        logging.error("Rerun program or debug. Ensure stable internet connection.")


if __name__ == "__main__":
    # Defines start time to surface later on
    start_time = time.time()

    # Begins main program
    main()

    # Log completed
    logging.info(f"Completed")
    # Surcase executatios time
    logging.info("Execution time: %s seconds" % (time.time() - start_time))
