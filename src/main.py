"""
Sample script for logging and string cleaning.
"""

import logging
import csv

from datetime import date
from project_logs import logger

project_name = "Benzon - Test Project"
project_date = "2022-12-24"

proj = (project_date + " " + project_name) \
        .lower() \
        .replace("-", "") \
        .replace(" ", "_") \
        .replace("__", "_")
file_name = proj + ".csv"

with open(file_name, "a+", newline="") as csv_file:
    writer = csv.writer(csv_file)
    # writer.writerow(["SN", "Movie", "Protagonist"])
    writer.writerow([12, "Lord of the Hinges", "Frodo GangGangs"])
    writer.writerow([4, "Henry Potter", "Berry Potter"])
    logging.info("Written to CSV file.")
