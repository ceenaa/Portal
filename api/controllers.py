from bs4 import BeautifulSoup
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Course, Time


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
            start_time=extractTime(allTds[i + 8].text)[1],
            end_time=extractTime(allTds[i + 8].text)[0]

        )

        name = allTds[i].text
        code = allTds[i + 1].text
        group = allTds[i + 3].text
        teacher = allTds[i + 7].text
        cts = [ct1]

        if allTds[i + 9].text != "":

            ct2 = Time.objects.create(
                day=extractDay(allTds[i + 9].text),
                start_time=extractTime(allTds[i + 9].text)[1],
                end_time=extractTime(allTds[i + 9].text)[0]
            )

            cts.append(ct2)
        if allTds[i + 10].text != "":
            ct3 = Time.objects.create(
                day=extractDay(allTds[i + 10].text),
                start_time=extractTime(allTds[i + 10].text)[1],
                end_time=extractTime(allTds[i + 10].text)[0]
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
