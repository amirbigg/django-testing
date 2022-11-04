

class BaseLoggingMixin:
	def initial(self, request, *args, **kwargs):
		print('='*90)
		print('initial')
		return super().initial(request, *args, **kwargs)

	def finalize_response(self, request, response, *args, **kwargs):
		print('finalize response')
		return super().finalize_response(request, response, *args, **kwargs)
