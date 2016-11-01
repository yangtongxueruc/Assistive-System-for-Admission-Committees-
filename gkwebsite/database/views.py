# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, request, JsonResponse
from models import *
import student_backend as stu
import teacher_backend as tch
import volunteer_backend as vol
import register_backend as reg
import image_backend as pic
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
        # print vol_list, '***********'
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
        # print t
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
        t["message"] = "15"
        t["score"] = "4"
        return JsonResponse(t)
    else:
        return HttpResponse('Access denied.')


def test_list_all(request):
    # by dqn14 Oct 26, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        t = []
        pic_list = pic.getPicturebyDict({Picture.IS_TITLE: 1})
        for item in pic_list:
            c = {}
            dic = pic.getPictureAllDictByObject(item)
            c['id'] = '%s_%s_%s' % (str(YEAR_LIST[dic[Picture.YEAR]]),
                                    SHITI_LIST[dic[Picture.PROVINCE]],
                                    SUBJECT_LIST[dic[Picture.SUBJECT]])
            c["year"] = str(YEAR_LIST[dic[Picture.YEAR]])
            c["place"] = SHITI_LIST[dic[Picture.PROVINCE]]
            c["subject"] = SUBJECT_LIST[dic[Picture.SUBJECT]]
            
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
        print 'fabu ',id
        list = id.split('_')
        year = find_item_index_in_list(int(list[0]), YEAR_LIST)
        province = find_item_index_in_list(list[1], SHITI_LIST)
        subject = find_item_index_in_list(list[2], SUBJECT_LIST)
        dic = {
            Picture.YEAR: year,
            Picture.PROVINCE: province,
            Picture.SUBJECT: subject,
        }
        pic_list = pic.getPicturebyDict(dic)
        print 'pic_list len', len(pic_list)
        t = {}
        for item in pic_list:
            flag = pic.setPicture(item, Picture.IS_DELEVERED, 1)
            if flag is False:
                t['success'] = 'N'
                t['message'] = '管理员正忙'
                return JsonResponse(t)

        t['success'] = 'Y'
        t['message'] = 'ok'
        return JsonResponse(t)
    else:
        return HttpResponse('Access denied.')


def withdraw_test(request):
    # by dqn14 Oct 26, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        id = request.POST.get('id')
        print 'chehui ', id
        list = id.split('_')
        year = find_item_index_in_list(int(list[0]), YEAR_LIST)
        province = find_item_index_in_list(list[1], SHITI_LIST)
        subject = find_item_index_in_list(list[2], SUBJECT_LIST)

        dic = {
            Picture.YEAR: year,
            Picture.PROVINCE: province,
            Picture.SUBJECT: subject,
        }
        pic_list = pic.getPicturebyDict(dic)
        t = {}
        for item in pic_list:
            flag = pic.setPicture(item, Picture.IS_DELEVERED, 0)
            if flag == False:
                t['success'] = 'N'
                t['message'] = '管理员正忙'
                return JsonResponse(t)

        t['success'] = 'Y'
        t['message'] = 'ok'
        return JsonResponse(t)
    else:
        return HttpResponse('Access denied.')


def remove_test(request):
    # by dqn14 Oct 26, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        id = request.POST.get('id')
        list = id.split('_')
        year = find_item_index_in_list(int(list[0]), YEAR_LIST)
        province = find_item_index_in_list(list[1], SHITI_LIST)
        subject = find_item_index_in_list(list[2], SUBJECT_LIST)
        dic = {
            Picture.YEAR: year,
            Picture.PROVINCE: province,
            Picture.SUBJECT: subject,
        }
        pic.removePictureIDByDic(dic)
        t={}
        t['success'] = 'Y'
        t['message'] = 'ok'
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
        dict = {
            Picture.YEAR : int(year),
            Picture.PROVINCE: int(place),
            Picture.SUBJECT: int(subject),
            Picture.IS_TITLE: 1,
        }
        flag = pic.createPicturebyDict(dict)
        t = {}
        if flag:
            t['success'] = 'Y'
            t['message'] = 'ok'
        else:
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
        year_len = len(YEAR_LIST)
        for i in range(0, year_len):
            t.append({'num': str(i), 'str': str(YEAR_LIST[i])})

        return JsonResponse(t, safe=False)
    else:
        return HttpResponse('Access denied.')


def get_test_placelist(request):
    # by dqn14 Oct 26, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        t = []
        yiti_len = len(SHITI_LIST)
        for i in range(0, yiti_len):
            t.append({'num': str(i), 'str': str(SHITI_LIST[i])})
        return JsonResponse(t, safe=False)
    else:
        return HttpResponse('Access denied.')


def get_test_subjectlist(request):
    # by dqn14 Oct 26, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        t = []
        kemu_len = len(SUBJECT_LIST)
        for i in range(0, kemu_len):
            t.append({'num': str(i), 'str': str(SUBJECT_LIST[i])})
        return JsonResponse(t, safe=False)
    else:
        return HttpResponse('Access denied.')

def list_question(request):
    # by dqn14 Oct 27, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        test_id = request.POST.get('id')
        list = test_id.split('_')
        year = find_item_index_in_list(int(list[0]), YEAR_LIST)
        province = find_item_index_in_list(list[1], SHITI_LIST)
        subject = find_item_index_in_list(list[2], SUBJECT_LIST)
        dic = {
            Picture.YEAR: year,
            Picture.PROVINCE: province,
            Picture.SUBJECT: subject,
        }
        pic_list = pic.getPicturebyDict(dic)
        t = []
        for item in pic_list:
            pic_dic = pic.getPictureAllDictByObject(item)
            c = {}
            c['num'] = pic_dic[Picture.NUMBER]
            c['type'] = CATEGORY_LIST[pic_dic[Picture.CATEGORY]]
            c['maxscore'] = pic_dic[Picture.SCORE]
            t.append(c)
        return JsonResponse(t, safe=False)
    else:
        return HttpResponse('Access denied.')
        
def remove_question(request):
    # by dqn14 Oct 27, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        test_id = request.POST.get('test_id')
        list = test_id.split('_')
        year = find_item_index_in_list(int(list[0]), YEAR_LIST)
        province = find_item_index_in_list(list[1], SHITI_LIST)
        subject = find_item_index_in_list(list[2], SUBJECT_LIST)
        num = int(request.POST.get('num'))
        dic = {
            Picture.YEAR: year,
            Picture.PROVINCE: province,
            Picture.SUBJECT: subject,
            Picture.NUMBER: num,
        }
        pic.removePictureIDByDic(dic)

        t = {}
        t['success']='Y'
        t['message']='ok'
        return JsonResponse(t)
    else:
        return HttpResponse('Access denied.')
        
def get_next_question_num(request):
    # by dqn14 Oct 27, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        test_id = request.POST.get('test_id')
        info = test_id
        info_list = info.split('_')
        print info_list
        year = int(info_list[0]) - YEAR_LIST[1] + 1
        province = find_item_index_in_list(info_list[1], PROVINCE_LIST)
        subject = find_item_index_in_list(info_list[2], SUBJECT_LIST)
        dict = {
            Picture.YEAR: year,
            Picture.PROVINCE: province,
            Picture.SUBJECT: subject,
        }
        pic_list = pic.getPicturebyDict(dict)
        num_list = []
        for picture in pic_list:
            info_dic = pic.getPictureAllDictByObject(picture)
            num_list.append(info_dic[Picture.NUMBER])
        num = 1
        for i in range(1, 99999):
            if i not in num_list:
                num = i
                break
        t = {'num':num}
        return JsonResponse(t)
    else:
        return HttpResponse('Access denied.')
        
def move_question_up(request):
    # by dqn14 Oct 27, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        test_id = request.POST.get('test_id')
        num = request.POST.get('num')
        # Caution: please check the boundary
        t = {}
        t['success']='N'
        t['message']='管理员正忙，没空上移'
        return JsonResponse(t)
    else:
        return HttpResponse('Access denied.')
        
def move_question_down(request):
    # by dqn14 Oct 27, 2016
    # use this if-else to block violent access
    if request.is_ajax() and request.method == 'POST':
        test_id = request.POST.get('test_id')
        num = request.POST.get('num')
        # Caution: please check the boundary
        t = {}
        t['success']='N'
        t['message']='管理员正忙，没空下移'
        return JsonResponse(t)
    else:
        return HttpResponse('Access denied.')