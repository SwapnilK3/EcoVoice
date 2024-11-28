
from django.contrib import admin
from django.urls import path
from charity_user import views as c_views
from .views import *



urlpatterns = [
    # path('admin/', admin.site.urls),#just for testing purposes at last delete it when project is done 
    path('', home, name='home'),
    path('logout', user_logout, name='logout'),
    path('login', user_login, name='login'),
    path('signup', c_views.signup, name='signup'),
    path('verify/<token>', c_views.verify, name='verify'), #charity logout
    path('edit_info', edit_info, name='edit_info'),

    path('home', home, name='home'),
    path('complaint', complaint, name='complaint'),   
    path('anonymouscomplaint', anonymouscomplaint, name='anonymouscomplaint'),   
    path('blogs', blogs, name='blogs'),
    path('write_blog', write_blog, name='write_blog'),
    path('about', about_us, name='about_us'),
    # path('upcoming_events', upcoming_events, name='upcoming_events'),
    path('help', help, name='help'),
    path('news', news, name='news'),
    path('donation', donation, name='donation'),
    
    
]
