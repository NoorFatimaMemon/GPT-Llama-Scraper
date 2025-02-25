from gptScrpper import GPT_Scrapper
from llama_model import llama_model
from seleniumbase import Driver
import logging
import time

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Main():
    Scrapper, llama = GPT_Scrapper(), llama_model()

    def main(self):
        main_url = "https://chatgpt.com/"
        email = 'mohammaddanial767@gmail.com'
        password = 'Family.123'
        session_url = 'https://chatgpt.com/g/g-HxPrv1p8v-code-tutor'

        logging.info("Starting browser instance 1")
        driver = Driver(uc=True, headless2=False)

        logging.info("Starting login process")
        self.Scrapper.login(driver, main_url, email, password)
        logging.info("Ending login process")
        driver.implicitly_wait(10)

        logging.info("Getting session URL")
        self.Scrapper.get_session_url(driver, session_url)
        logging.info("Got session URL")

        while True:
            prompt = input("Enter a prompt or quit to exit: ")

            if prompt.lower() == 'quit':
                logging.info("Exiting the prompt loop.")
                break 

            # Send the prompt to the browser and collect response
            logging.info(f"Sending prompt to browser instance 1: {prompt}")
            response_from_instance = self.Scrapper.get_response(driver, prompt)
            if response_from_instance:
                print(f"Response from browser 1: {response_from_instance}")
            else:
                print(f"No response received from browser 1")

            time.sleep(5)
            # Send the prompt to the LLAMA model to collect response
            response_from_llama = self.llama.llama_model(prompt=prompt)
            time.sleep(5)
            if response_from_llama:
                print(f"Response from LLAMA model: {response_from_llama}")
            else:
                print(f"No response received from LLAMA model")

        driver.quit()    
        
test = Main()
test.main()
