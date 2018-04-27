from django.urls import path, re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('course/<category>', views.courseCategory, name='single_category'),
    path('course/<category>/<level>', views.drawing_course, name='drawing_course'),
    path('<category>/course/<course>', views.course, name='single_course'),
    path('all-courses', views.all_course, name='all_course'),
    path('popular-courses', views.popular_course, name='popular_course'),
    path('resent-courses', views.recent_course, name='recent_course'),
    path('event/<event_id>', views.event, name='single_event_page'),
    path('contact', views.contact, name='contact_page'),
    path('about-us', views.about_us, name='about_page'),
    path('faq', views.faq, name='faq_page'),
    path('login', views.get_login, name='login'),
    path('logout', views.get_logout, name='logout'),
    path('profile', views.get_user_profile, name='profile'),
    path('sign-up', views.signup, name='sign-up'),
    path('user-message', views.user_message, name='user_message'),
    # path('activate/<uidb64>/<token>', views.activate, name='activate'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
     views.activate, name='activate'),
]
