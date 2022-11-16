from django.urls import path
from . import views as test_views


urlpatterns = [
	path('no-logging/', test_views.MockNoLoggingView.as_view()),
	path('logging/', test_views.MockLoggingView.as_view()),
	path('explicit-logging/', test_views.MockExplicitLoggingView.as_view()),
	path('custom-check-logging/', test_views.MockCustomCheckLoggingView.as_view()),
	path('session-auth-logging/', test_views.MockSessionAuthLoggingView.as_view()),
	path('sensitive-fields-logging/', test_views.MockSensitiveFieldsLoggingView.as_view()),
	path('invalid-cleaned-substitute-logging/', test_views.MockInvalidCleanedSubstituteLoggingView.as_view()),
]