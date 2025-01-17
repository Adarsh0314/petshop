from django.urls import path
from.import views

urlpatterns = [
    path('',views.Readdata),
    path('one/<int:pk>',views.Readone),
    path('postdata',views.PostData),
    path('update/<int:pk>',views.UpdateData)
]