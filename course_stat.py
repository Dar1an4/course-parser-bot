from course_pars_fun import *
import datetime
import time
import csv

def save_course(usd_pars, eur_pars, gbfunt_pars):
    myData = [[datetime.datetime.today().strftime("%d.%m %H:%M"), f'{usd_pars()}', f'{eur_pars()}', f'{gbfunt_pars()}']]

    myFile = open('example2.csv', 'a')
    with myFile:
        writer = csv.writer(myFile, lineterminator='\n')
        writer.writerows(myData)
    print("Writing complete")
while True:
    save_course(usd_pars, eur_pars, gbfunt_pars)
    time.sleep(10)
