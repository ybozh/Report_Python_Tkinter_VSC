import os
import datetime

dt = datetime.datetime.now()
dt = str(dt.year)+'_'+str(dt.month)+'_'+str(dt.day)+'_'+str(dt.hour)+'_'+str(dt.minute)+'_'+str(dt.second)
path_to_reports_folder = '/home/bozhko/Документи/Reports/'
path_to_report_folder = path_to_reports_folder + 'BT_' + str(dt)

if os.path.exists(path_to_reports_folder):
    pass
else: os.mkdir(path_to_reports_folder)

if os.path.exists(path_to_report_folder):
    pass
else: os.mkdir(path_to_report_folder)

