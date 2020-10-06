from django.urls import path
# 사용자에게 보여줄 화면 처리 함수 view.py도 연결
from . import views

urlpatterns = [
	path('', views.index)
]
