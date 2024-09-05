# utils/logger.py

import logging
import logging.handlers
import sys
from pathlib import Path

def setup_logging(log_level=logging.INFO, log_file='logs/application.log'):
    """
    Sets up logging configuration for the application.

    :param log_level: The logging level (default: logging.INFO).
    :param log_file: The file path for logging output.
    """
    # Ensure the log directory exists
    log_path = Path(log_file).parent
    log_path.mkdir(parents=True, exist_ok=True)

    # Create handlers
    console_handler = logging.StreamHandler(sys.stdout)
    file_handler = logging.handlers.RotatingFileHandler(
        log_file, maxBytes=5*1024*1024, backupCount=5
    )

    # Create formatters
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Get the root logger
    logger = logging.getLogger()
    logger.setLevel(log_level)

    # Add handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    # Optional: Silence third-party loggers if needed
    logging.getLogger('some_third_party_module').setLevel(logging.WARNING)
