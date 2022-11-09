from rest_framework.views import APIView
from rest_framework.response import Response
from .mixins import LoggingMixin


class Home(LoggingMixin, APIView):
	sensitive_fields = {'pass'}
	def get(self, request):
		return Response('hello')
