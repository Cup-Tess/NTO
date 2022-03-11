from django.shortcuts import render, redirect
from .models import Records, Staistik, Sviz, marshrut
from json import dumps

'''
#Добавляет в таблицу данные некоторые необходимые (средние оценки, время, посещаемость..) 
marks = Records.objects.all()
ex = [[0, 0, 0, 0, 0, 0, 1000], [0, 0, 0, 0, 0, 0, 1000], [0, 0, 0, 0, 0, 0, 1000], [0, 0, 0, 0, 0, 0, 10000], [0, 0, 0, 0, 0, 0, 10000], [0, 0, 0, 0, 0, 0, 10000], [0, 0, 0, 0, 0, 0, 10000], [0, 0, 0, 0, 0, 0, 10000]]
for mark in marks:
    indeX = int(mark.exibitId)-1
    ex[indeX][0] += int(mark.visualFeedback)
    ex[indeX][1] += int(mark.description)
    ex[indeX][2] += int(mark.completeness)
    ex[indeX][3] += 1
    ex[indeX][4] += int(mark.timeSpentInFrontSec)
    ex[indeX][5] = max(ex[indeX][5], int(mark.timeSpentInFrontSec))
    ex[indeX][6] = min(ex[indeX][6], int(mark.timeSpentInFrontSec))
for i in range(len(ex)):
    pos = ex[i][3]
    staistik = Staistik.objects.get(exponat=(i+1))
    staistik.visualFeedback = ex[i][0]/pos
    staistik.description = ex[i][1]/pos
    staistik.completeness = ex[i][2]/pos
    staistik.posetit = pos
    staistik.timesred = ex[i][4]/pos
    staistik.timemin = ex[i][6]
    staistik.timemax = ex[i][5]
    staistik.save()
'''

def galery(request):
    return render(request, "museum/galery.html", {})


def main(request):
    return render(request, "museum/main.html", {})


def photoB(request):
    return render(request, "museum/photoB.html")


def portal(request):
    return render(request, "museum/portal.html")


def portal2(request):
    return render(request, "museum/portal2.html")


def statistica_polz(request):
    return render(request, "museum/statistica_polz.html", {})


def exp1(request):
    return render(request, "museum/exp1.html")


def exp2(request):
    return render(request, "museum/exp2.html")


def exp3(request):
    return render(request, "museum/exp3.html")


def exp4(request):
    return render(request, "museum/exp4.html")


def exp5(request):
    return render(request, "museum/exp5.html")


def exp6(request):
    return render(request, "museum/exp6.html")


def exp7(request):
    return render(request, "museum/exp7.html")


def exp8(request):
    return render(request, "museum/exp8.html")

def statCrit1(request):
    post = Staistik.objects.all()
    data = []
    for p in post:
        data.append(round(((float(p.visualFeedback)+ float(p.description) + float(p.completeness))/3),1))
    jdata1 = dumps(data)
    return render(request, "museum/statCrit1.html", {"data": jdata1})

def posesch(request):
    post = Staistik.objects.all()
    data = []
    for p in post:
        data.append(int(p.posetit))
    jdata = dumps(data)
    return render(request, "museum/posesch.html", {'data': jdata})

def statistica_polz(request):
    return render(request, "museum/statistica_polz.html")

def login(request):
    return render(request, "museum/login.html")

def admstat(request):
    post = Staistik.objects.all()
    data1 = []
    data2 = []
    data3 = []
    for p in post:
        data1.append(int(p.timesred))
        data2.append(int(p.timemin))
        data3.append(int(p.timemax))
    jdata1 = dumps(data1)
    jdata2 = dumps(data2)
    jdata3 = dumps(data3)
    return render(request, "museum/admstat.html", {'data1': jdata1, 'data2': jdata2, 'data3': jdata3})

def exponats(request):
    return render(request, "museum/exponats.html")


def navi(request):
    if request.method == "POST":
        nom = int(request.POST.get('nom'))
        p = marshrut()
        p.author = request.user
        p.way = nom
        p.save()
        return redirect('')
    return render(request, "museum/navi.html")


def gid(request):
    Array = ['Вы на месте', "Пройдите направо", "Пройдите налево", "Покиньте текущий зал",
             "Войдите в следующий зал", "2 раза ", "3 раза "]


    return render(request, "museum/gid.html", {})

