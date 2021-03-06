from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.student_center, name='student_center'),
    url(r'^score/$', views.student_score, name='student_score'),
    url(r'^contact/$', views.student_contact, name='student_contact'),
    url(r'^rank/$', views.student_rank, name='student_rank'),
    url(r'^admit/$', views.student_admit, name='student_admit'),
    url(r'^logout/$', views.student_logout, name='student_logout'),
    url(r'^profile/$', views.profile),

    url(r'^get_all_tests/$', views.get_all_tests),
    url(r'^do_test/$', views.do_test),
    url(r'^get_problem_list/$', views.get_problem_list),
    url(r'^get_problem_info/$', views.get_problem_info),
    url(r'^submit_test_result/$', views.submit_test_result),
    url(r'^message/$', views.message),
    url(r'^get_all_message/$', views.get_all_message),
    url(r'^get_message_info/$', views.get_message_info),
    #url(r'^static/(?P<path>.*)', 'django.views.static.serve', {'document_root': 'd:/wwwsite/office/static'}),

]
