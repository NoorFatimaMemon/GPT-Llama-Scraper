import time
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GPT_Scrapper():
    def login(self, driver, main_url, email, password):
        while True:
            try:
                logging.info(f"Accessing URL: {main_url}")
                driver.get(main_url)
                driver.implicitly_wait(30)
                time.sleep(3)

                # Perform login process
                login = WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="login-button"]')))
                login_button = driver.find_element(By.XPATH, '//button[@data-testid="login-button"]')
                login_button.click()
                time.sleep(3)

                google_button = driver.find_element(By.XPATH, '//span[text()="Continue with Google"]//parent::button')
                google_button.click()
                time.sleep(3)

                # Enter the email
                email_input = driver.find_element(By.XPATH, '//input[@type="email"]')
                email_input.click()
                email_input.send_keys(email)
                time.sleep(3)

                next_button = driver.find_element(By.XPATH, '//span[text()="Next"]//parent::button')
                next_button.click()
                time.sleep(3)

                # Enter the password
                password_input = driver.find_element(By.XPATH, '//input[@type="password"]')
                password_input.click()
                password_input.send_keys(password)
                time.sleep(3)

                next_button = driver.find_element(By.XPATH, '//span[text()="Next"]//parent::button')
                next_button.click()
                time.sleep(20)
                driver.implicitly_wait(50)

                # Check if login was successful
                if driver.current_url == main_url: 
                    logging.info("Login successful!")
                    break 
                else:
                    logging.warning("Login failed. Please try again.")

            except TimeoutException as e:
                logging.error(f"Timeout while trying to access the page: {e}")
            except NoSuchElementException as e:
                logging.error(f"Element not found: {e}")
            except Exception as e:
                logging.error(f"An unexpected error occurred: {e}")

    def get_session_url(self, driver, session_url):
        while True:
            if session_url.lower() == 'quit':
                logging.info("User chose to quit the program.")
                break

            # Basic validation to check if the URL starts with 'http://' or 'https://'
            if session_url.startswith(('http://', 'https://')):
                logging.info(f"Accessing URL: {session_url}")
                driver.get(session_url)
                driver.implicitly_wait(50)  
                time.sleep(2)

                # Check if the current URL matches the session URL
                try:
                    current_url = driver.current_url
                    if current_url == session_url:
                        logging.info("Page loaded successfully.")
                        break
                    else:
                        logging.warning(f"Loaded page URL '{current_url}' does not match expected URL '{session_url}'.")
                        print(f"Failed to load the expected URL. Loaded: {current_url}, Expected: {session_url}")
                except TimeoutException:
                    logging.error("Page load timed out.")
                    print("The page took too long to load. Please try again.")
            else:
                print("Invalid URL. Please ensure it starts with 'http://' or 'https://'.")

    def get_response(self, driver, prompt):
        """Scrapes the output based on the input prompt from the ChatGPT-like page."""
        try:
            # Find the input area and type the prompt
            input_box = driver.find_element(By.XPATH, '//*[@id="prompt-textarea"]/p')
            input_box.click()
            input_box.send_keys(prompt)
            logging.info(f"Prompt submitted: {prompt}")
            time.sleep(5)

            # Click the submit button
            try:
                submit_button = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Send prompt"]')))
                submit_button.click()
                logging.info("Clicked the submit button.")
            except TimeoutException:
                logging.error("Timed out waiting for the submit button to be clickable.")
                return None
            except NoSuchElementException:
                logging.error("Submit button not found.")
                return None

            # Wait until the copy button is clickable
            WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, '(//button[@aria-label="Copy"])[last()]')))     
            
            # Wait for and retrieve the response
            try:
                message_ = WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH, '(//div[@data-message-author-role="assistant"])[last()]')))
                time.sleep(5)
                message_element = driver.find_element(By.XPATH, '(//div[@data-message-author-role="assistant"])[last()]')
                time.sleep(5)
                message = message_element.text
                time.sleep(5)
                logging.info("Received response from the assistant.")
                return message

            except TimeoutException:
                logging.error("Timed out waiting for the message element.")
            except NoSuchElementException:
                logging.error("Message element not found.")
        except TimeoutException as e:
            logging.error(f"Timeout while trying to access the page: {e}")
        except NoSuchElementException as e:
            logging.error(f"Element not found: {e}")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")

        return None