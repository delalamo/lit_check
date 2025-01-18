from copy import deepcopy
import logging
import azure.functions as func
from datetime import datetime

from azure.communication.email import EmailClient
import os

app = func.FunctionApp()


@app.timer_trigger(
    schedule="0 * * * * *", arg_name="myTimer", run_on_startup=False, use_monitor=False
)
def main(myTimer: func.TimerRequest) -> None:
    for s in ["CONNECTION_STRING", "MY_EMAIL", "SENDER_EMAIL"]:
        logging.info(s, os.environ[s])

    connection_string = os.environ["CONNECTION_STRING"]
    email_client = EmailClient.from_connection_string(connection_string)

    message = {
        "content": {
            "subject": "This is the subject",
            "plainText": "This is the body",
            "html": "<html><h1>This is the body</h1></html>",
        },
        "recipients": {
            "to": [
                {"address": os.environ["MY_EMAIL"], "displayName": "Diego del Alamo"}
            ]
        },
        "senderAddress": os.environ["SENDER_EMAIL"],
    }

    if myTimer.past_due:
        logging.info("The timer is past due!")

    # Use datetime.now() to get the current time
    # current_execution = datetime.now(datetime.timezone.utc).isoformat()  # Use UTC time
    current_execution = datetime.utcnow().isoformat()  # Use UTC time
    logging.info("Timer trigger executed at: %s", current_execution)
    local_message = deepcopy(message)
    local_message["content"]["html"] = f"<html><h1>{current_execution}</h1></html>"
    poller = email_client.begin_send(local_message)
    logging.info("Email sent")
    result = poller.result()
    logging.info(result)
