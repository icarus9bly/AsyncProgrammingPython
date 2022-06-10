from celery import Celery
import time
app = Celery('tasks', broker="redis://localhost", backend="redis://localhost")

@app.task
def my_intensive_function(name):
    time.sleep(2)
    return name

# celery -A tasks worker --loglevel=info
# redis-cli
# KEYS *
# get celery-task-meta-c9bf6edb-461b-4167-92a9-3badd5a46685
# "{\"status\": \"SUCCESS\", \"result\": \"Aditya\", \"traceback\": null, \"children\": [], \"date_done\": \"2022-06-06T12:21:45.334069\", \"task_id\": \"c9bf6edb-461b-4167-92a9-3badd5a46685\"}"
