from django.urls import path
from .import views
app_name='Myapp'
urlpatterns = [
        path('', views.index, name='index'),
    path('indexkk',views.indexkk, name='indexkk'),
    path('indexjj',views.indexjj, name='indexjj'),
    path('indexcse',views.indexcse, name='indexcse'),
    path('indexce',views.indexce, name='indexce'),
    path('indexee',views.indexee, name='indexee'),
    path('indexme',views.indexme, name='indexme'),
    path('indexec',views.indexec, name='indexec'),
    path('stuRegister',views.stuRegister, name='stuRegister'),
	path('stuDelete',views.stuDelete, name='stuDelete'),
	path('stuDetail', views.stuDetail, name='stuDetail'),
	path('stuEdit', views.stuEdit, name='stuEdit'),
	path('stuUpdate', views.stuUpdate, name='stuUpdate'),
	path('stuResult',views.stuResult, name='stuResult'),
]

