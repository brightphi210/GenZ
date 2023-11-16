

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [
    path('api/', views.enpoint, name="enpoint"),

    # ==================== User ==================================
    path('api/user', views.UserGetCreate.as_view(), name="api"),
    path('api/user/<str:pk>', views.UserGetUpdateDelete.as_view(), name="user_update"),
    path('api/userprofile/update/<str:pk>', views.UserProfileGetUpdate.as_view(), name="user_profile"),


    # =========================== NEWS ==============================
    path('api/newsLetter', views.NewsLetterView.as_view(), name="newsLetter"),
    
    path('api/news', views.NewsGet.as_view(), name="news"),
    path('api/stories', views.StoryGet.as_view(), name="stories"),


    # ======================== subsribe =================================
    path('api/subMonthly', views.BasicSubscriptionPlanViewSet.as_view(), name="subBasic"),
    path('api/subYearly', views.BasicSubscriptionPlanViewSet.as_view(), name="subBasic"),
    path('api/subYealyPrint', views.BasicSubscriptionPlanViewSet.as_view(), name="subBasic"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)