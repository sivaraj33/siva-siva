from django.urls import path
from .views import  *

urlpatterns=[
    path('appdisplay/',appdisplay,name='appdisplay'),
    path('showall/',showall,name='showall'),
    path('insert/',add,name='add'),
    path('update/<int:id>/',update_detail,name='update_detail'),
    path('delete/<int:id>/',delete_detail,name='delete_detail')

]