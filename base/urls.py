from django.urls import path
from  .import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    #TokenRefreshView,
    )

urlpatterns = [

    path('',views.endpoints),
    path('advocates/', views.advocates_list),
    #path('advocates/<str:username>', views.advocate_detail),
    path('advocates/<str:username>',views.AdvocateDetails.as_view()),

    path('companies/',views.companies_list),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
