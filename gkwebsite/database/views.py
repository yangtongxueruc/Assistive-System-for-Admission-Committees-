# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, request, JsonResponse
from models import *
import student_backend as stu
import teacher_backend as tch
import volunteer_backend as vol
import register_backend as reg
from my_field import *


# Create your views here.


def search_student_by_name(request):
    # completed by evan69
    # by dqn14 Oct 12, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        t = []
        name = request.POST.get('name')
        stu_list = stu.getStudentbyField(Student.REAL_NAME, name)
        for item in stu_list:
            account = getattr(item, Student.ACCOUNT)
            stu_dic = stu.getStudentAllDictByAccount(account)
            dic = {'id': stu_dic[Student.ID],
                   'name': stu_dic[Student.REAL_NAME],
                   'gender': stu_dic[Student.SEX]['sexlist'][stu_dic[Student.SEX]['sex']],
                   'source': stu_dic[Student.PROVINCE]['provincelist'][stu_dic[Student.PROVINCE]['province']],
                   'school': stu_dic[Student.SCHOOL],
                   'id_card': stu_dic[Student.ID_NUMBER],
                   }
            t.append(dic)
        return JsonResponse(t, safe=False)  # must use 'safe=False'
    else:
        return HttpResponse('Access denied.')


def remove_student_by_id(request):
    # by dqn14 Oct 12, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        id = request.POST.get('id')
        account = stu.idToAccountStudent(id)
        stu.removeStudentAccount(account)
        return JsonResponse({})  # return nothing
    else:
        return HttpResponse('Access denied.')


def student_list_all(request):
    # completed by evan69
    # by dqn14 Oct 12, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        t = []
        stu_list = stu.getAllInStudent()
        # search for students in database
        for item in stu_list:
            account = getattr(item, Student.ACCOUNT)
            stu_dic = stu.getStudentAllDictByAccount(account)
            dic = {'id': stu_dic[Student.ID],
                   'name': stu_dic[Student.REAL_NAME],
                   'gender': stu_dic[Student.SEX]['sexlist'][stu_dic[Student.SEX]['sex']],
                   'source': stu_dic[Student.PROVINCE]['provincelist'][stu_dic[Student.PROVINCE]['province']],
                   'school': stu_dic[Student.SCHOOL],
                   'id_card': stu_dic[Student.ID_NUMBER],
                   }
            t.append(dic)
        return JsonResponse(t, safe=False)  # must use 'safe=False'
    else:
        return HttpResponse('Access denied.')


def get_teacher_name_by_id(request):
    '''
    通过id获得老师的名称
    :param request:
    :return:
    '''
    if request.is_ajax() and request.method == 'POST':
        id = request.POST.get('id')
        account = tch.idToAccountTeacher(id)
        t = {'name': tch.getTeacher(account, 'realName')}
        return JsonResponse(t)
    else:
        return HttpResponse('Access denied.')


def get_volunteer_name_by_id(request):
    # by dqn14 Oct 19, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        id = request.POST.get('id')
        account = vol.idToAccountVolunteer(id)
        t = {'name': vol.getVolunteer(account, 'realName')}
        return JsonResponse(t)
    else:
        return HttpResponse('Access denied.')


def search_volunteer_by_name(request):
    # by dqn14 Oct 15, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        t = []
        name = request.POST.get('name')
        volunteer_list = vol.getVolunteerbyField(Volunteer.REAL_NAME, name)
        for item in volunteer_list:
            account = getattr(item, Volunteer.ACCOUNT)
            vol_dic = vol.getVolunteerAllDictByAccount(account)
            dic = {'id': vol_dic[Volunteer.ID],
                   'name': vol_dic[Volunteer.REAL_NAME],
                   'department': vol_dic[Volunteer.MAJOR][0]['departmentlist'][vol_dic[Volunteer.MAJOR][0]['department']],
                   'class': vol_dic[Volunteer.CLASSROOM],
                   'student_id': vol_dic[Volunteer.STUDENT_ID],
                   }
            t.append(dic)
        return JsonResponse(t, safe=False)  # must use 'safe=False'
    else:
        return HttpResponse('Access denied.')


def remove_volunteer_by_id(request):
    # by dqn14 Oct 15, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        id = request.POST.get('id')
        vol.removeVolunteerAccount(vol.idToAccountVolunteer(id))
        return JsonResponse({})  # return nothing
    else:
        return HttpResponse('Access denied.')


def volunteer_list_all(request):
    # by dqn14 Oct 15, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        t = []
        vol_list = vol.getAllInVolunteer()
        print vol_list, '***********'
        for item in vol_list:
            account = getattr(item, Volunteer.ACCOUNT)
            vol_dic = vol.getVolunteerAllDictByAccount(account)
            dic = {'id': vol_dic[Volunteer.ID],
                   'name': vol_dic[Volunteer.REAL_NAME],
                   'department': vol_dic[Volunteer.MAJOR][0]['departmentlist'][vol_dic[Volunteer.MAJOR][0]['department']],
                   'class': vol_dic[Volunteer.CLASSROOM],
                   'student_id': vol_dic[Volunteer.STUDENT_ID],
                   }
            # 没注册的志愿者不显示出来
            if dic['name'] != '':
                t.append(dic)
        print t
        return JsonResponse(t, safe=False)  # must use 'safe=False'
    else:
        return HttpResponse('Access denied.')


def add_student(request):
    # by dqn14 Oct 15, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        num = request.POST.get('num')
        num = (int)(num)
        t = []
        codelist = []
        for i in range(0, num):
            code = str(reg.createNewRegisterCode())
            c = {'code': code}
            t.append(c)
            codelist.append(code)
        id = (str)(request.session['user_id'])
        generateExcel(request, id, '', '', 'sheet1', [codelist], [u'注册码'])
        return JsonResponse(t, safe=False)
    else:
        return HttpResponse('Access denied.')


def add_volunteer(request):
    # by dqn14 Oct 17, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        dic = {Volunteer.PASSWORD: password}
        if vol.createVolunteer(username, dic):
            flag = 'true'
        else:
            flag = 'false'
        print '-------' + username + ' ' + password + ' ' + str(flag)
        return JsonResponse({'success': flag, 'username': username})
    else:
        return HttpResponse('Access denied.')

def export_registration_code(request):
    # by dqn14 Oct 22, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        teacher = request.POST.get('id')
        length = request.POST.get('length')
        filename = "%s_teacher.xls" % teacher
        t = {'filename': filename}
        print 'file xls ' + filename
        return JsonResponse(t)
    else:
        return HttpResponse('Access denied.')
        
def get_teacher_alert_by_id(request):
    # by dqn14 Oct 22, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        t = {}
        t["message"]="15"
        t["score"]="4"
        return JsonResponse(t)
    else:
        return HttpResponse('Access denied.')


def test_list_all(request):
    # by dqn14 Oct 26, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        t = []
        c = {}
        c["year"]="2016年"
        c["place"]="全国II卷"
        c["subject"]="理科综合"
        #请注意，上面三个参数是直接显示在页面上的，请使其有可读性
        c["id"]="2016_全国II_理科综合"
        c["released"] = "N"
        t.append(c)
        return JsonResponse(t, safe=False)
    else:
        return HttpResponse('Access denied.')
        
def release_test(request):
    # by dqn14 Oct 26, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        id = request.POST.get('id')
        t = {}
        # t['success'] = 'Y'
        t['success'] = 'N'
        t['message'] = '管理员正忙'
        return JsonResponse(t)
    else:
        return HttpResponse('Access denied.')
        
def withdraw_test(request):
    # by dqn14 Oct 26, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        id = request.POST.get('id')
        t = {}
        # t['success'] = 'Y'
        t['success'] = 'N'
        t['message'] = '管理员正忙'
        return JsonResponse(t)
    else:
        return HttpResponse('Access denied.')
        
def remove_test(request):
    # by dqn14 Oct 26, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        id = request.POST.get('id')
        t = {}
        # t['success'] = 'Y'
        t['success'] = 'N'
        t['message'] = '管理员正忙'
        return JsonResponse(t)
    else:
        return HttpResponse('Access denied.')
        
def add_test(request):
    # by dqn14 Oct 26, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        year = request.POST.get('year')
        place = request.POST.get('place')
        subject = request.POST.get('subject')
        # 以上三个参数都是序号
        t = {}
        # t['success'] = 'Y'
        t['success'] = 'N'
        t['message'] = '管理员正忙'
        return JsonResponse(t)
    else:
        return HttpResponse('Access denied.')
        
def get_test_yearlist(request):
    # by dqn14 Oct 26, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        t = []
        t.append({'num':'0', 'str':'2017'})
        t.append({'num':'1', 'str':'2018'})
        t.append({'num':'2', 'str':'2019'})
        t.append({'num':'3', 'str':'2020'})
        return JsonResponse(t, safe=False)
    else:
        return HttpResponse('Access denied.')
        
def get_test_placelist(request):
    # by dqn14 Oct 26, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        t = []
        t.append({'num':'0', 'str':'北京卷'})
        t.append({'num':'1', 'str':'海南卷'})
        t.append({'num':'2', 'str':'上海卷'})
        t.append({'num':'3', 'str':'全国I卷'})
        return JsonResponse(t, safe=False)
    else:
        return HttpResponse('Access denied.')
        
def get_test_subjectlist(request):
    # by dqn14 Oct 26, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        t = []
        t.append({'num':'0', 'str':'语文'})
        t.append({'num':'1', 'str':'数学'})
        t.append({'num':'2', 'str':'英语'})
        t.append({'num':'3', 'str':'理科综合'})
        return JsonResponse(t, safe=False)
    else:
        return HttpResponse('Access denied.')