from celery import Celery

app = Celery('tasks',broker='pyamqp://mj:2018year@34.201.106.87//')

@app.task
def hello(msg):
  open('./hello', 'a+').write('%s\n' % msg)
  return msg

