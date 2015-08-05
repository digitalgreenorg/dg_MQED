from django.core.management import setup_environ
import dg.settings
setup_environ(dg.settings)
import csv
grd_file = open('path_adoptions_errors.csv', 'wb')
wrtr = csv.writer(grd_file, delimiter=',', quotechar='"')
from activities.models import PersonAdoptPractice
import openpyxl as xl
wb = xl.load_workbook(filename='PathAdoptions.xlsx')
ws = wb.worksheets[0]
i=0
for row in ws.rows[1:]:
    i = i + 1
    print i
    try:
        adoption = PersonAdoptPractice(user_created_id = 127, partner_id = 13, person_id = row[1].value, video_id = row[3].value, date_of_adoption = row[2].value)
        adoption.save()
    except Exception as e:
        wrtr.writerow([i, row[0].value, row[1].value, row[2].value, row[3].value, e] )
        grd_file.flush()
grd_file.close()
