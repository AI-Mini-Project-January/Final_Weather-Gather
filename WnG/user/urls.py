from django.urls import path
from .views import Join, Login, Logout, UploadProfile 
from . import views
<<<<<<< HEAD

=======
>>>>>>> e38e1c0fef9a6a69c3f500835f681bc3f09ecf03
# urls를 join이라고 해도 앱이름이 user이기 때문에 ~/user/join 으로 들어감
urlpatterns = [
    path('join', Join.as_view()),
    path('login', Login.as_view()),
    path('logout', Logout.as_view()),
    path('profile/upload', UploadProfile.as_view()),
    path('profile/delete/', views.profile_delete_view, name='profile_delete'),
]
