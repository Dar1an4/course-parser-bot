from course_pars_fun import *
import datetime
import time
import csv

def save_course(usd_pars, eur_pars):
    usd_pars_list = usd_pars()
    eur_pars_list = eur_pars()
    myData = [[datetime.datetime.today().strftime("%d.%m %H:%M"), usd_pars_list[0], usd_pars_list[1], usd_pars_list[2], eur_pars_list[0], eur_pars_list[1], eur_pars_list[2] ]]
    myFile = open('sheet_course.csv', 'a')
    with myFile:
        writer = csv.writer(myFile, lineterminator='\n')
        writer.writerows(myData)
    print("Writing complete")


def forward_stats(usd_pars, eur_pars):
    with open('sheet_course.csv') as f:
        reader = csv.reader(f)
        stat_list_str = []
        for row in reader:
            stat_list_str.append(row)
        stat_list_str = stat_list_str[-1]
        stat_list_str = stat_list_str[1:]
        stat_list_float = []
        now_course_list_noround = []
        now_course_list_round = []
        usd_pars_list = usd_pars()
        eur_pars_list = eur_pars()
        now_course_list_noround.extend(usd_pars_list)
        now_course_list_noround.extend(eur_pars_list)

    for i in stat_list_str:
        stat_list_float.append(round(float(i), 2))
    for i in now_course_list_noround:
        now_course_list_round.append(round(float(i), 2))

    print(stat_list_float)
    print(now_course_list_round)
    print(usd_pars_list, eur_pars_list)

    if stat_list_float != now_course_list_round:
        save_course(usd_pars, eur_pars)
        print('The course was changed. BD was refreshed')
        return False
    else:
        print('The course did not changed, allright')
        return True

