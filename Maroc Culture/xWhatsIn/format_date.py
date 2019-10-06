
""" Formatage des dates """
import dateparser

from datetime import datetime



def format_date(num_date):
    x =datetime.now()

    if num_date =="NO DATE":
        return num_date

    old = dateparser.parse(num_date)
    print(old)
    #convertir en datetime object
    date_obj = datetime.strptime(str(old),'%Y-%m-%d  %H:%M:%S')
    #formater
    print(date_obj.strftime('%d.%m.%Y'))


a = 'July 4 1999'
format_date(a)

b = 'Dimanche 6 Octobre'
format_date(b)
