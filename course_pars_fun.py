import requests
from bs4 import BeautifulSoup


def usd_pars():
    url = 'https://kurs.com.ua/valyuta/usd'

    headers = {
        "Accept": "*/*",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.83"
    }

    req = requests.get(url, headers=headers)
    src = req.text
    with open("usd.html", "w", encoding="utf-8") as file:
        file.write(src)

    with open("usd.html", encoding="utf-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")

    usd_course = []

    course_usd = soup.find_all(class_="course")
    for course_usd in course_usd:
        course_usd = course_usd.text.strip().split("\n")
        usd_course.append(course_usd)

    usd_buy = round((float(usd_course[0][0])), 2)
    usd_sell = round((float(usd_course[1][0])), 2)
    usd_black = round((float(usd_course[2][0])), 2)
    return [usd_buy, usd_sell, usd_black]

def eur_pars():
    url = 'https://kurs.com.ua/valyuta/eur'

    headers = {
        "Accept": "*/*",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.83"
    }

    req = requests.get(url, headers=headers)
    src = req.text
    with open("eur.html", "w", encoding="utf-8") as file:
        file.write(src)

    with open("eur.html", encoding="utf-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")

    eur_course = []

    course_eur = soup.find_all(class_="course")
    for course_eur in course_eur:
        course_eur = course_eur.text.strip().split("\n")
        eur_course.append(course_eur)

    eur_buy = round((float(eur_course[0][0])), 2)
    eur_sell = round((float(eur_course[1][0])), 2)
    eur_black = round((float(eur_course[2][0])), 2)
    return [eur_buy, eur_sell, eur_black]


# def gbfunt_pars():
#     url = 'https://kurs.com.ua/valyuta/gbp'
#
#     headers = {
#         "Accept": "*/*",
#         "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.83"
#     }
#
#     req = requests.get(url, headers=headers)
#     src = req.text
#     with open("gbfunt.html", "w", encoding="utf-8") as file:
#         file.write(src)
#
#     with open("gbfunt.html", encoding="utf-8") as file:
#         src = file.read()
#
#     soup = BeautifulSoup(src, "lxml")
#
#     gbfunt_course = []
#
#     course_gbfunt = soup.find_all(class_="course")
#     for course_gbfunt in course_gbfunt:
#         course_gbfunt = course_gbfunt.text.strip().split("\n")
#         gbfunt_course.append(course_gbfunt)
#
#     gbfunt_buy = round((float(gbfunt_course[0][0])), 2)
#     gbfunt_sell = round((float(gbfunt_course[1][0])), 2)
#     gbfunt_black = round((float(gbfunt_course[2][0])), 2)
#     return [gbfunt_buy, gbfunt_sell, gbfunt_black]