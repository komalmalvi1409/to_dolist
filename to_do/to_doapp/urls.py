from django.urls import path
from. import views
from .views import To_dooCreate
from .views import To_dooList
from .views import To_dooUpdate,To_dooDelete

urlpatterns=[

    path('login',views.login,name="login"),
    path('to_doocreate', To_dooCreate.as_view()),
    path('to_doolist', To_dooList.as_view()),
    path('<pk>/update', To_dooUpdate.as_view()),
    path('<pk>/delete', To_dooDelete.as_view()),
]