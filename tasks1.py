from celery import Celery
celery = Celery('tasks', backend='redis://', broker='pyamqp://mj3:2018year@172.31.21.127/mj3_vhost')

celery.send_task('tasks.add', (2,2))
