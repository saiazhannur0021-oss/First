import logging
from dotenv import load_dotenv
import os
import io
logging.basicConfig(
    level = logging.INFO,
    format =  "%(asctime)s - %(levelname)s - %(message)s",
    filename = "main-log.log",
    filemode = 'a'
)


load_dotenv()




def file_open(defult_text_name):
    Securiti_code1 = os.getenv("Secrit_one")
    logging.info(f"SC code :{Securiti_code1}")    
    
    with io.open(defult_text_name, "r", encoding = "utf-8") as file:
        text_in_file = file.read()
        logging.info(f"IN defult_text_name : {text_in_file}")
    if text_in_file != Securiti_code1:
        logging.error(f"text in file wrong")
        return "incorrect"
    elif text_in_file == Securiti_code1:
        logging.info(f"text correct")
        return "correct"
defult_text_name = "pytester.txt"
file_open(defult_text_name)