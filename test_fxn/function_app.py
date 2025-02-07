import os
import azure.functions as func
import datetime
import json
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = func.FunctionApp()


@app.timer_trigger(
    schedule="0 * * * * *", arg_name="myTimer", run_on_startup=False, use_monitor=False
)
def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().isoformat()
    logging.info("Timer trigger executed at: %s", utc_timestamp)

    if mytimer.past_due:
        logging.info("The timer is past due!")

    message = MIMEMultipart()
    message["From"] = os.environ.get("MY_EMAIL")
    message["To"] = os.environ.get("MY_EMAIL")
    message["Subject"] = f"Papers {datetime.now()}"
    message.attach(MIMEText("TEST TEST", "plain"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(os.environ.get("MY_EMAIL"), os.environ.get("MY_PW"))
        server.sendmail(
            os.environ.get("MY_EMAIL"), os.environ.get("MY_EMAIL"), message.as_string()
        )

    # Your script logic here
    logging.info("Daily script executed successfully.")
