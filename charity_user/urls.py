
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home, name='home'),#it is different from basic home
    path('logout', views.user_logout, name='logout'), #charity login
    path('login', views.user_login, name='login'), #charity logout
    path('verify/<token>', views.verify, name='verify'), #charity logout
    path('signup', views.signup, name='signup'), #charity signup wiyh validation
    path('edit_info', views.edit_info, name='edit_info'),
    # path('create_charity_user', views.create_charity_user, name='create_charity_user'),
    path('home', views.home, name='home'), #it is different from basic home 
    path('display_complaint', views.display_complaint, name='display_complaint'),  #Show the all compliant
    path('blogs', views.blogs, name='blogs'),#edit te blog here
    path('write_blog', views.write_blog, name='write_blog'),#edit te blog here
    path('about', views.about, name='about'), #blog will same 
    path('events', views.event_registration, name='event_registration'),#add event and its discription
    # path('upcoming_events', views.upcoming_events, name='upcoming_events'),#Add events
    path('help', views.help, name='help'),#in this we show help for how to use website
    path('donation_details', views.donation_details, name='donation_details'), #in this we show the total donation collected
    
    
]
