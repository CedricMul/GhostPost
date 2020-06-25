from django.urls import path
from ghostapp import views

urlpatterns = [
    path('', views.index, name='home'),
    path('boasts/', views.boast_view),
    path('roasts/', views.roast_view),
    path('gpost_submit/', views.gpost_submit),
    path('upvote/<int:id>/', views.upvote_view),
    path('downvote/<int:id>/', views.downvote_view),
    path('sort_by_score/', views.sort_by_score),
    path('sort_by_date/', views.sort_by_date)
]