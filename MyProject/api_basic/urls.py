from django.urls import path
from .views import article_list, article_detail,ArticaleAPIView, ArticalDetails, GenericAPIView


urlpatterns = [
    #path('article/', article_list),
    path('article/',ArticaleAPIView.as_view()),
    #path('detail/<int:pk>/', article_detail),
    path('detail/<int:id>/', ArticalDetails.as_view()),
    path('generic/article/<int:id>/', GenericAPIView.as_view()),
]