from .base_mixins import BaseLoggingMixin
from .models import APIRequestLog

class LoggingMixin(BaseLoggingMixin):
	def handle_log(self):
		APIRequestLog(**self.log).save()
