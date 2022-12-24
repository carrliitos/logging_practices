"""
Sample script for logging and string cleaning.
"""

import logging
import csv
import json

from datetime import date
from project_logs import logger

with open("../project_info.json", "r") as proj_info:
    data = json.load(proj_info)
    proj = (data["project_start_date"] + " " + data["project_name"]) \
            .lower() \
            .replace("-", "") \
            .replace(" ", "_") \
            .replace("__", "_")
    file_name = proj + ".csv"
    logging.info("Porject information extracted.")

with open(file_name, "a+", newline="") as csv_file:
    writer = csv.writer(csv_file)
    # writer.writerow(["SN", "Movie", "Protagonist"])
    writer.writerow([12, "Lord of the Hinges", "Frodo GangGangs"])
    writer.writerow([4, "Henry Potter", "Berry Potter"])
    logging.info("Written to CSV file.")
