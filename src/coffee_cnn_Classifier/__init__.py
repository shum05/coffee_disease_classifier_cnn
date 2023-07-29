import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
# %(asctime)s--> timestamp of the log message in the format "YYYY-MM-DD HH:MM:SS,sss" (e.g., "2023-07-25 14:30:45,123").
# %(levelname)s --> to include the log level of the message (e.g., "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL").
# %(module)s: This placeholder is used to include the name of the Python module where the log message originated.

log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath), #  FileHandler that directs log messages to a log file specified by the log_filepath variable.
        logging.StreamHandler(sys.stdout) #  a StreamHandler that directs log messages to the standard output (stdout), which typically displays them in the console.
    ]
)

logger = logging.getLogger("coffeeCnnLogger")