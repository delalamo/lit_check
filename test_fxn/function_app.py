import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().isoformat()
    logging.info("Timer trigger executed at: %s", utc_timestamp)

    # Your script logic here
    logging.info("Daily script executed successfully.")
