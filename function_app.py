import logging
import azure.functions as func
from datetime import datetime

app = func.FunctionApp()


@app.timer_trigger(
    schedule="0 * * * * *", arg_name="myTimer", run_on_startup=False, use_monitor=False
)
def timer_trigger2(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info("The timer is past due!")

    # Use datetime.now() to get the current time
    # current_execution = datetime.now(datetime.timezone.utc).isoformat()  # Use UTC time
    current_execution = datetime.utcnow().isoformat()  # Use UTC time
    logging.info("Timer trigger executed at: %s", current_execution)
    logging.info("Python timer trigger function executed.")
