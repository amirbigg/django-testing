from rest_framework.views import APIView
from rest_framework.response import Response
from tracking.mixins import LoggingMixin


class MockNoLoggingView(APIView):
	def get(self, request):
		return Response('no logging')


class MockLoggingView(LoggingMixin, APIView):
	def get(self, request):
		return Response('with logging')
