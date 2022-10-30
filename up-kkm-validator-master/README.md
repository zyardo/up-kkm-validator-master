# KKM Registration Validator
An app to verify if a Product Registration Number is listed under [KKM](https://quest3plus.bpfk.gov.my/pmo2/index.php).

Please ensure a stable internet connection to run this app.

## Setup
1. Install packages.
    * Run `pip install -r requirements.txt`.
2. Running the app.
    * Run `python app.py -n <Product Registration Number>`.

***NOTE:** It is advisable to setup in a virtual environment. This app is developed and tested using `python==3.9.13`.*

## Example
1. KKM listed registration number:

   **Command:**
   ```
   python app.py -n MAL20021402ACRZ
   ```

   **Output:**
   ```
   [2022-10-30 17:21:28,639] INFO - Product Registration Number: MAL20021402ACRZ
   [2022-10-30 17:21:28,639] INFO - ====== WebDriver manager ======
   [2022-10-30 17:21:28,757] INFO - Get LATEST chromedriver version for google-chrome 107.0.5304
   [2022-10-30 17:21:29,059] INFO - Driver [/Users/awahid/.wdm/drivers/chromedriver/mac64/107.0.5304/chromedriver] found in cache
   [2022-10-30 17:21:30,128] INFO - Begin validating...
   [2022-10-30 17:21:32,570] INFO - MAL20021402ACRZ IS LISTED
   [2022-10-30 17:21:32,570] INFO - Completed
   [2022-10-30 17:21:32,570] INFO - Execution time: 3.9313998222351074 seconds
   ```
2. KKM non-listed registration number:

   **Command:**
   ```
   python app.py -n BSHBXNSBSN99J
   ```

   **Output:**
   ```
   [2022-10-30 17:27:53,418] INFO - Product Registration Number: BSHBXNSBSN99J
   [2022-10-30 17:27:53,419] INFO - ====== WebDriver manager ======
   [2022-10-30 17:27:53,660] INFO - Get LATEST chromedriver version for google-chrome 107.0.5304
   [2022-10-30 17:27:53,952] INFO - Driver [/Users/awahid/.wdm/drivers/chromedriver/mac64/107.0.5304/chromedriver] found in cache
   [2022-10-30 17:27:55,306] INFO - Begin validating...
   [2022-10-30 17:27:59,060] INFO - BSHBXNSBSN99J IS NOT LISTED
   [2022-10-30 17:27:59,060] INFO - Completed
   [2022-10-30 17:27:59,061] INFO - Execution time: 5.6416239738464355 second
   ```


