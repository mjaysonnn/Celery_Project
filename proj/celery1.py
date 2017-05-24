from __future__ import absolute_import, unicode_literals
from celery import Celery
app = Celery('proj',
             broker='pyamqp://mj2:2018year@127.0.0.1/mj2_vhost',
             backend='redis://127.0.0.1',
             include=['proj.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()
