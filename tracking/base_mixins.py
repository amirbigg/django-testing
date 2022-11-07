from django.utils.timezone import now
import ipaddress
import traceback
from .app_settings import app_settings


class BaseLoggingMixin:
	logging_methods = '__all__'

	def initial(self, request, *args, **kwargs):
		self.log = {'requested_at':now()}
		return super().initial(request, *args, **kwargs)

	def handle_exception(self, exc):
		response = super().handle_exception(exc)
		self.log['errors'] = traceback.format_exc()
		return response

	def finalize_response(self, request, response, *args, **kwargs):
		response = super().finalize_response(request, response, *args, **kwargs)
		if self.should_log(request, response):
			user = self._get_user(request)
			self.log.update({
				'remote_addr': self._get_ip_address(request),
				'view': self._get_view_name(request),
				'view_method': self._get_view_method(request),
				'path': self._get_path(request),
				'host': request.get_host(),
				'method': request.method,
				'user': user,
				'username_persistent': user.get_username() if user else 'Anonymous',
				'response_ms': self._get_response_ms(),
				'status_code': response.status_code,
			})
			self.handle_log()
		return response

	def handle_log(self):
		raise NotImplementedError

	def _get_ip_address(self, request):
		ipaddr = request.META.get('HTTP_X_FORWARDED_FOR', None)
		if ipaddr:
			ipaddr = ipaddr.split(',')[0]
		else:
			ipaddr = request.META.get('REMOTE_ADDR', '').split(',')[0]

		possibles = (ipaddr.lstrip('[').split(']')[0], ipaddr.split(':')[0])

		for addr in possibles:
			try:
				return str(ipaddress.ip_address(addr))
			except:
				pass

		return ipaddr

	def _get_view_name(self, request):
		method = request.method.lower()
		try:
			attribute = getattr(self, method)
			return (type(attribute.__self__).__module__ + "." + type(attribute.__self__).__name__)
		except AttributeError:
			return None

	def _get_view_method(self, request):
		if hasattr(self, 'action'):
			return self.action or None
		return request.method.lower()

	def _get_path(self, request):
		return request.path[:app_settings.PATH_LENGTH]

	def _get_user(self, request):
		user = request.user
		if user.is_anonymous:
			return None
		return user

	def _get_response_ms(self):
		response_timedelta = now() - self.log['requested_at']
		response_ms = int(response_timedelta.total_seconds() * 1000)
		return max(response_ms, 0)

	def should_log(self, request, response):
		return (
			self.logging_methods == '__all__' or request.method in self.logging_methods
		)
