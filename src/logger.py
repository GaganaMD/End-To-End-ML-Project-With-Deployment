import logging
import os
from datetime import datetime

# Generating a timestamp for the log file in the format 'month_day_year_hour_minute_second.log'
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Creating a directory path for logs
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)

# Creating the directory if it doesn't exist
os.makedirs(logs_path,exist_ok=True)

# Constructing the full path for the log file by joining the logs_path and LOG_FILE
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

# Configuring the logging module
logging.basicConfig(

    filename=LOG_FILE_PATH,
    # Setting the log file path

    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    # Defining the log message format

    level=logging.INFO,
    # Setting the logging level to INFO
    
)