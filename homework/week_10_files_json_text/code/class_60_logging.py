# Print 3 messages using logging (info, warning, error) with timestamps.
# Logging se 3 messages (info, warning, error) print karo timestamps ke saath.


import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

logging.info("Started")
logging.warning("Careful")
logging.error("Failed")

