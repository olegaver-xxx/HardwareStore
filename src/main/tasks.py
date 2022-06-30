from .celery import app
import time


@app.task
def test_task(x=None):
    print(x)
    time.sleep(2)
    print('COMPLETE')
