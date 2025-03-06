import logging

class CustomFormatter(logging.Formatter):
    """Custom log formatter with color support for console output."""

    COLORS = {
        "DEBUG": "\033[92m",  # Green
        "INFO": "\033[94m",   # Blue
        "WARNING": "\033[93m",  # Yellow
        "ERROR": "\033[91m",  # Red
        "CRITICAL": "\033[41m"  # Red Background
    }
    RESET = "\033[0m"

    def format(self, record):
        log_format = "%(asctime)s - [%(levelname)s] - %(name)s - %(message)s"
        date_format = "%Y-%m-%d %H:%M:%S"
        formatter = logging.Formatter(log_format, datefmt=date_format)

        log_message = formatter.format(record)
        return f"{self.COLORS.get(record.levelname, self.RESET)}{log_message}{self.RESET}"

def get_logger(name="app_logger", level=logging.DEBUG):
    """Creates and returns a logger with the custom formatter."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(CustomFormatter())
        logger.addHandler(console_handler)

    return logger
