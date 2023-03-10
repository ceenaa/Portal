from bs4 import BeautifulSoup
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Course, Time, ChosenCourse


def extractTime(txt):
    startTime = ""
    endTime = ""
    temp = ""
    for iii in range(len(txt)):
        if txt[iii - 1] == "[":
            while txt[iii] != "-":
                temp += txt[iii]
                iii += 1
            startTime = temp
            iii = iii + 1
            temp = ""
            while txt[iii] != "]":
                temp += txt[iii]
                iii += 1
            endTime = temp

    return endTime, startTime


def extractDay(txt):
    res = ""
    for ii in range(len(txt)):
        if txt[ii] == "[":
            break
        res += txt[ii]
    return res


@api_view(['GET'])
def crawl(request):
    with open('./EducationalPortal.html', 'r') as html_file:
        content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    allTds = soup.findAll('td', class_='gridtic')

    for i in range(1, len(allTds), 21):

        ct1 = Time.objects.create(
            day=extractDay(allTds[i + 8].text),
            start_time=extractTime(allTds[i + 8].text)[0],
            end_time=extractTime(allTds[i + 8].text)[1]

        )

        name = allTds[i].text
        code = allTds[i + 1].text
        group = allTds[i + 3].text
        teacher = allTds[i + 7].text
        cts = [ct1]

        if allTds[i + 9].text != "":
            ct2 = Time.objects.create(
                day=extractDay(allTds[i + 9].text),
                start_time=extractTime(allTds[i + 9].text)[0],
                end_time=extractTime(allTds[i + 9].text)[1]
            )

            cts.append(ct2)
        if allTds[i + 10].text != "":
            ct3 = Time.objects.create(
                day=extractDay(allTds[i + 10].text),
                start_time=extractTime(allTds[i + 10].text)[0],
                end_time=extractTime(allTds[i + 10].text)[1]
            )
            cts.append(ct3)

        exam = Time.objects.create(
            day=extractDay(allTds[i + 11].text),
            start_time=extractTime(allTds[i + 11].text)[1],
            end_time=extractTime(allTds[i + 11].text)[0]
        )

        c = Course.objects.create(
            name=name,
            code=code,
            group=group,
            teacher=teacher,
            exam_time=exam
        )
        c.class_times.set(cts)
        c.save()
    return JsonResponse({'message': 'crawl done'})


def compareTime(t1, t2):
    h1 = t1.split(":")[0]
    m1 = t1.split(":")[1]
    h2 = t2.split(":")[0]
    m2 = t2.split(":")[1]
    if h1 > h2:
        return True
    elif h1 == h2:
        if m1 > m2:
            return True
        else:
            return False
    else:
        return False


# cct.start_time < ct.end_time <= cct.end_time

def checkCoherence(c):
    chosenCourses = ChosenCourse.objects.all()
    if c in chosenCourses:
        return False
    for cc in chosenCourses:

        if cc.course.exam_time.day == c.exam_time.day:
            if compareTime(cc.course.exam_time.start_time, c.exam_time.start_time) or \
                    compareTime(c.exam_time.end_time, cc.course.exam_time.end_time) \
                    or cc.course.exam_time.start_time == c.exam_time.start_time:
                return False
            if compareTime(cc.course.exam_time.end_time, c.exam_time.end_time) or \
                    compareTime(c.exam_time.start_time, cc.course.exam_time.start_time) \
                    or cc.course.exam_time.end_time == c.exam_time.end_time:
                return False

        for cct in cc.course.class_times.all():
            for ct in c.class_times.all():
                if cct.day == ct.day:
                    if compareTime(cct.end_time, ct.start_time) or compareTime(ct.end_time, cct.start_time)\
                            or cct.start_time == ct.start_time:
                        return False
                    if compareTime(cct.end_time, ct.end_time) or compareTime(ct.end_time, cct.start_time)\
                            or cct.end_time == ct.end_time:
                        return False

    return True
