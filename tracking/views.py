from rest_framework.views import APIView
from rest_framework.response import Response
from .mixins import LoggingMixin


class Home(LoggingMixin, APIView):
	def post(self, request):
		return Response('hello')
