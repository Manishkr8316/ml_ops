import logging
import os
from datetime import datetime
from pathlib import Path

# 1. Define the directory and filename separately
LOG_DIR = Path.cwd() / "logs"
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
LOG_FILE_PATH = LOG_DIR / LOG_FILE

# 2. Create the directory (not the file path)
LOG_DIR.mkdir(parents=True, exist_ok=True)

# 3. Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
)

if __name__ == "__main__":
    logging.info("Logging has started")