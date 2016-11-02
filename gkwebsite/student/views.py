#encoding=utf-8
from django.http import JsonResponse
from django.shortcuts import render

from django.http import HttpResponse,JsonResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import redirect

from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt
import datetime

from database.models import *
from database.my_field import *
import database.student_backend as stu
import database.image_backend as pic
import database.teacher_backend as tch
import database.backend as back
import database.volunteer_backend as vol


# Create your views here.

def student_center(request):
    t = get_template('student/center.html')
    id = request.session.get('user_id', -1)
    c = {'id': id}
    return HttpResponse(t.render(c))


def student_score(request):
    t = get_template('student/score.html')
    id = request.session.get('user_id', -1)
    if id == -1:
        return HttpResponse('Access denied')
    c = {'id': id}
    return HttpResponse(t.render(c))


def student_rank(request):
    id = request.session.get('user_id', -1)
    if id == -1:
        return HttpResponse('Access denied')
    student_dic = stu.getStudentAllDictByAccount(stu.idToAccountStudent(str(id)))
    account = stu.idToAccountStudent(str(id))
    student = stu.getStudentAll(account)
    print stu.getStudentEstimateRank(student)
    rank, sum_rank = stu.getStudentEstimateRank(student)
    dict = {'name': student_dic[Student.REAL_NAME],
            'score': getStudentEstimateScore(student),
            'rank1': rank,
            'rank11':sum_rank,
            }
    return render(request, 'student/rank.html', {'dict': dict})


def student_admit(request):
    '''

    后端需要获取录取信息传给前端
    '''
    id = request.session.get('user_id', -1)
    if id == -1:
        return HttpResponse('Access denied')


    student_dic = stu.getStudentAllDictByAccount(stu.idToAccountStudent(str(id)))
    info = student_dic[Student.ADMISSION_STATUS]
    if info.strip() == '' or info.strip() == "0":
        info = u'暂时还没有您的录取信息，请耐心等待老师添加'
    admition = info
    return render(request,
                  'student/admit.html', {'admition': admition})


def student_contact(request):
    '''
                后端需要在这里改代码，从数据库读取正确的dict，并返回
    '''
    teacher_list = tch.getAllInTeacher()
    vol_list = vol.getAllInVolunteer()
    list = []
    for teacher in teacher_list:
        account = getattr(teacher, Teacher.ACCOUNT)
        name = tch.getTeacher(account, Teacher.REAL_NAME)
        phone = tch.getTeacher(account, Teacher.PHONE)
        email = tch.getTeacher(account, Teacher.EMAIL)
        address = tch.getTeacher(account, Teacher.AREA)
        dict = {'profession':u'老师','name':name, 'phone':phone,'email':email,'address':address}
        list.append(dict)

    for volunteer in vol_list:
        account = getattr(volunteer, Volunteer.ACCOUNT)
        tmp_dic = vol.getVolunteerAllDictByAccount(account)
        name = tmp_dic[Volunteer.REAL_NAME]
        if name.strip() == '':
            continue
        phone = tmp_dic[Volunteer.PHONE]
        email = tmp_dic[Volunteer.EMAIL]
        address = tmp_dic[Volunteer.ADDRESS]
        dict = {'profession':u'志愿者','name':name, 'phone':phone,'email':email,'address':address}
        list.append(dict)
    return render(request,'student/contact.html', {'dict': list})


def student_logout(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return redirect('/login')

@csrf_exempt
def profile(request):

    id = request.session.get('user_id', -1)
    if id == -1:
        return HttpResponse('Access denied')
    account = stu.idToAccountStudent(str(id))
    student = stu.getStudentAll(account)

    if request.method == 'POST':
        '''
        保存信息并返回json
        '''
        print "wp",request.POST

        info_dict = request.POST.copy()
        print info_dict
        for i in range(1, 7):
            if info_dict['majorSelect' + str(i)].strip() == '':
                info_dict['majorSelect' + str(i)] = '0'
        for i in range(1, 4):
            if info_dict['testScore' + str(i)].strip() == '':
                info_dict['testScore' + str(i)] = '0'
        for i in range(1, 4):
            if info_dict['rank' + str(i)].strip() == '':
                info_dict['rank' + str(i)] = '0'
        for i in range(1, 4):
            if info_dict['rank' + str(i)].strip() == '':
                info_dict['rank' + str(i)] = '0'
        for i in range(1, 4):
            if info_dict['rank' + str(i) + str(i)].strip() == '':
                info_dict['rank' + str(i) + str(i)] = '0'
        if info_dict['realScore'].strip() == '':
            info_dict['realScore'] = '0'

        dic = {
            'name': info_dict.get('name'),
            'identification': info_dict.get('identification'),
            'sex': info_dict.get('sex'),
            'nation': info_dict.get('nation'),
            'birth': info_dict.get('birth'),

            'type': int(info_dict.get('wenli')),
            'province': int(info_dict.get('province')),
            'phone': info_dict.get('phone'),
            'email': info_dict.get('email'),
            'address': info_dict.get('address'),

            'dadName': info_dict.get('dadName'),
            'dadPhone': info_dict.get('dadPhone'),
            'momName': info_dict.get('momName'),
            'momPhone': info_dict.get('momPhone'),
            'school': info_dict.get('school'),

            'stu_class': info_dict.get('stu_class'),
            'tutorName': info_dict.get('tutorName'),
            'tutorPhone': info_dict.get('tutorPhone'),

            'majorSelect1': int(info_dict.get('majorSelect1')),
            'majorSelect2': int(info_dict.get('majorSelect2')),
            'majorSelect3': int(info_dict.get('majorSelect3')),
            'majorSelect4': int(info_dict.get('majorSelect4')),
            'majorSelect5': int(info_dict.get('majorSelect5')),
            'majorSelect6': int(info_dict.get('majorSelect6')),

            'testScore1': int(info_dict.get('testScore1')),
            'testScore2': int(info_dict.get('testScore2')),
            'testScore3': int(info_dict.get('testScore3')),

            'rank1': int(info_dict.get('rank1')),
            'rank11': int(info_dict.get('rank11')),
            'rank2': int(info_dict.get('rank2')),
            'rank22': int(info_dict.get('rank22')),
            'rank3': int(info_dict.get('rank3')),
            'rank33': int(info_dict.get('rank33')),

            'realScore': int(info_dict.get('realScore')),
            # 'relTeacher': info_dict.get('relTeacher'),
            'comment': info_dict.get('comment'),
        }

        birth_list = info_dict['birth'].split('/')
        dic['birth'] = datetime.date(int(birth_list[2]), int(birth_list[0]), int(birth_list[1]))

        stu.setStudent(account, Student.REAL_NAME, dic['name'])
        stu.setStudent(account, Student.ID_NUMBER, dic['identification'])
        stu.setStudent(account, Student.SEX, dic['sex'])
        stu.setStudent(account, Student.NATION, dic['nation'])
        stu.setStudent(account, Student.BIRTH, dic['birth'])

        stu.setStudent(account, Student.TYPE, dic['type'])
        stu.setStudent(account, Student.PROVINCE, dic['province'])
        stu.setStudent(account, Student.PHONE, dic['phone'])
        stu.setStudent(account, Student.EMAIL, dic['email'])
        stu.setStudent(account, Student.ADDRESS, dic['address'])

        stu.setStudent(account, Student.MOM_NAME, dic['momName'])
        stu.setStudent(account, Student.DAD_NAME, dic['dadName'])
        stu.setStudent(account, Student.DAD_PHONE, dic['dadPhone'])
        stu.setStudent(account, Student.MOM_PHONE, dic['momPhone'])
        stu.setStudent(account, Student.SCHOOL, dic['school'])

        stu.setStudent(account, Student.CLASSROOM, dic['stu_class'])
        stu.setStudent(account, Student.TUTOR_NAME, dic['tutorName'])
        stu.setStudent(account, Student.TUTOR_PHONE, dic['tutorPhone'])

        stu.setStudent(account,
                       Student.MAJOR,
                       [dic['majorSelect1'],
                        dic['majorSelect2'],
                        dic['majorSelect3'],
                        dic['majorSelect4'],
                        dic['majorSelect5'],
                        dic['majorSelect6']])

        stu.setStudent(
            account, Student.TEST_SCORE_LIST, [
                dic['testScore1'], dic['testScore2'], dic['testScore3']])

        stu.setStudent(
            account, Student.RANK_LIST, [
                dic['rank1'], dic['rank2'], dic['rank3']])

        stu.setStudent(
            account, Student.SUM_NUMBER_LIST, [
                dic['rank11'], dic['rank22'], dic['rank33']])

        stu.setStudent(account, Student.REAL_SCORE, dic['realScore'])
        stu.setStudent(account, Student.COMMENT, dic['comment'])


        return JsonResponse(dict)
    else:
        '''
        获取信息并返回
        '''
        stu_dic = stu.getStudentAllDictByAccount(account)
        (rank, tmp) = stu.getStudentEstimateRank(student)
        dic = {
            'name': stu_dic[Student.REAL_NAME],
            'identification': stu_dic[Student.ID_NUMBER],
            'sex': stu_dic[Student.SEX],
            'nation': stu_dic[Student.NATION],
            'birth': stu_dic[Student.BIRTH].strftime("%m/%d/%Y"),
            'province': stu_dic[Student.PROVINCE],
            'phone': stu_dic[Student.PHONE],
            'email': stu_dic[Student.EMAIL],
            'wenli': stu_dic[Student.TYPE],
            'address': stu_dic[Student.ADDRESS],
            'dadName': stu_dic[Student.DAD_NAME],
            'dadPhone': stu_dic[Student.DAD_PHONE],
            'momName': stu_dic[Student.MOM_NAME],
            'momPhone': stu_dic[Student.MOM_PHONE],
            'school': stu_dic[Student.SCHOOL],
            'stu_class': stu_dic[Student.CLASSROOM],
            'tutorName': stu_dic[Student.TUTOR_NAME],
            'tutorPhone': stu_dic[Student.TUTOR_PHONE],
             Student.MAJOR: stu_dic[Student.MAJOR],
             Student.TEST_SCORE_LIST: stu_dic[Student.TEST_SCORE_LIST],
             Student.RANK_LIST: stu_dic[Student.RANK_LIST],
             Student.SUM_NUMBER_LIST: stu_dic[Student.SUM_NUMBER_LIST],
            'realScore': stu_dic[Student.REAL_SCORE],
            'relTeacher': stu_dic[Student.DUIYING_TEACHER],
            'comment': stu_dic[Student.COMMENT],
            'estimateScore': getStudentEstimateScore(stu.getStudentAll(account)),
            'estimateRank': rank
        }
        group_list = stu.getStudentGroupIDListString(student).split(' ')
        for i in range(1, 6):
            if i < len(group_list):
                dic['group' + str(i)] = group_list[i]
            else:
                dic['group' + str(i)] = '0'
        dic['grouplist'] = [' ']
        all_group = back.getGroupbyDict({})
        for item in all_group:
            dic['grouplist'].append(back.getGroupAllDictByObject(item)['id'])
        return render(request, 'student/userinfo.html', {'dict': dic})

@csrf_exempt
def get_all_tests(request):
    """
        后端应在此处返回该学生全部可以做的题目名称。名称无重复
        学生id由request.session中获取，同其他函数里的写法
        然后放到下面样例写好的dic的'tests'键对应的列表值中
    """
    id = request.session.get('user_id', -1)
    if id == -1:
        return HttpResponse('Access denied')
    print id
    account = stu.idToAccountStudent(str(id))
    stu_dic = stu.getStudentAllDictByAccount(account)
    year = datetime.datetime.now().strftime("%Y")

    year = int(year) - YEAR_LIST[1] + 1
    province = int(stu_dic[Student.PROVINCE]['province'])
    print 'pro ',province
    dic = {
        Picture.YEAR: year,
        Picture.PROVINCE: province,
    }
    global rec_dict
    rec_dict = dic

    ret_list = []
    subject_list = []
    pic_list = pic.getPicturebyDict(dic)
    for item in pic_list:
        pic_dic = pic.getPictureAllDictByObject(item)
        if pic_dic[Picture.SUBJECT] in subject_list:
            continue
        subject_list.append(pic_dic[Picture.SUBJECT])
        tao = u'%s_%s_%s' % (str(YEAR_LIST[pic_dic[Picture.YEAR]]),
                            str(PROVINCE_LIST[pic_dic[Picture.PROVINCE]]),
                            str(SUBJECT_LIST[pic_dic[Picture.SUBJECT]]))
        ret_list.append(tao)


    dic = {'tests' : ret_list}

    return JsonResponse(dic)

@csrf_exempt
def do_test(request):
    test_name = request.GET.get('test_name')
    t = get_template('student/do_test.html')
    return HttpResponse(t.render({'test_name': test_name}))
    # return render(request, 'student/do_test.html')
    # return HttpResponse(t.render({}))

@csrf_exempt
def get_problem_list(request):
    """
        后端应在此处返回某套题内包含的题目id列表，且需要按顺序
        试题名称由request.POST.get('test_name')获取，见下面样例
        然后放到下面样例写好的dic的'problem_list'键对应的列表值中
    """
    test_name = request.POST.get('test_name')
    # print 'test_name', test_name
    info = test_name
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

    if province == -1 or subject == -1:
        print 'ERROR !!!!!!!!!!!!!!!!!!!'

    id_list = []
    pic_list = pic.getPicturebyDict(dict)
    print 'len ', len(pic_list)
    for item in pic_list:
        pic_dic = pic.getPictureAllDictByObject(item)
        id_list.append(pic_dic[Picture.ID])

    dic = {'problem_list': id_list}
    print 'id_list ', id_list
    return JsonResponse(dic)

@csrf_exempt
def get_problem_info(request):
    """
        后端应在此处返回某道试题的全部信息，信息应转化为字符串
        试题id由request.POST.get('problem_id')获取，见下面样例
        然后放到下面样例写好的dic中
    """
    # print request.POST
    problem_id = request.POST.get('problem_id')

    picture = pic.getPicturebyField('id', int(problem_id))
    pic_dic = pic.getPictureAllDictByObject(picture[0])
    pic_name = get_picture_path(pic_dic[Picture.YEAR], pic_dic[Picture.PROVINCE],
                                pic_dic[Picture.SUBJECT], pic_dic[Picture.NUMBER],
                                pic_dic[Picture.SCORE], pic_dic[Picture.CATEGORY])
    # print pic_dic

    dic = {'problem_num': pic_dic[Picture.NUMBER],
       'problem_type': CATEGORY_LIST[pic_dic[Picture.CATEGORY]],
       'problem_full_score': pic_dic[Picture.SCORE],
       'problem_pic': '/static/images/'+pic_name}

    return JsonResponse({'problem_info': dic})

@csrf_exempt
def submit_test_result(request):
    """
        后端应在此处保存这次答题的结果
        学生id从request.session获取
        时间数据、分数数据、试题名称见下面样例
        返回空Json即可
    """
    id = request.session.get('user_id', -1)
    if id == -1:
        return HttpResponse('Access denied')
    print id
    print request.POST
    time_list = [int(item) for item in request.POST.get('time_list').split(",")]
    score_list = [int(item) for item in request.POST.get('score_list').split(",")]
    test_name = request.POST.get('test_name')
    account = stu.idToAccountStudent(str(id))
    tmp = (stu.getStudentAllDictByAccount(account))[Student.ESTIMATE_SCORE]
    if tmp.strip() == '':
        tmp = '{}'
    try:
        stu_dic = eval(tmp)
    except:
        stu_dic = {}
    stu_dic[test_name] = {'time': sum(time_list), 'score': sum(score_list)}
    stu.setStudent(account, Student.ESTIMATE_SCORE, str(stu_dic))
    return JsonResponse({})



