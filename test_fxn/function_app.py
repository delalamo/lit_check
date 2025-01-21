import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()


@app.timer_trigger(
    schedule="0 * * * * *", arg_name="myTimer", run_on_startup=False, use_monitor=False
)
def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().isoformat()
    logging.info("Timer trigger executed at: %s", utc_timestamp)

    if mytimer.past_due:
        logging.info("The timer is past due!")

    # Your script logic here
    logging.info("Daily script executed successfully.")
