import logging
import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:
    logging.info("Timer trigger executed at: %s", mytimer.schedule_status.last)

    # Your script logic here
    logging.info("Daily script executed successfully.")
