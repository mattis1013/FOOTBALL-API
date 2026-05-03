import logging
import azure.functions as func
from main import run_pipeline

app = func.FunctionApp()

@app.timer_trigger(schedule="0 */1 * * * *", arg_name="myTimer", run_on_startup=True)
def ingestion_football(myTimer: func.TimerRequest) -> None:

    logging.info("Start pipeline")

    if myTimer.past_due:
        logging.warning("Timer en retard")

    try:
        run_pipeline()
        logging.info("OK pipeline")

    except Exception as e:
        logging.error(f"ERROR: {e}")
        raise