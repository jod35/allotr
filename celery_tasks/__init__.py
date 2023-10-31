from celery import Celery

app = Celery(
    'Hello',
    broker ="redis://127.0.0.1:6379/0"
)

@app.task
def hello():
    return "Hello world"

    