from celery import Celery

class Factory():
    """celery Instance for API."""
    def set_celery(self):
        self.celery = Celery(__name__, backend='rpc://', broker='pyamqp://localhost//')
        return self.celery


    def make_celery(self, app):
        self.celery = Celery(
          __name__,
          backend=app.config['CELERY_RESULT_BACKEND'],
          broker=app.config['CELERY_BROKER_URL']
        )
        self.celery.conf.update(app.config)
        class ContextTask(self.celery.Task):
            def __call__(self, *args, **kwargs):
                with app.app_context():
                    return self.run(*args, **kwargs)
        self.celery.Task = ContextTask
        return self.celery    
