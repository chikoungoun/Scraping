import datetime
from datetime import datetime
import smtplib


""" confirmation par mails """
def confirmation_mail(scrape_file):
    t = datetime.now()
    day = str(t.day) +"/"+str(t.month)+"/"+str(t.year)
    hour = str(t.hour)+":"+str(t.minute)+":"+str(t.second)
    temps = str(day)+"    "+str(hour)

    EMAIL_ADDRESS = 'gharwissen@gmail.com'
    EMAIL_PASSWORD = 'Alabasta_44'


    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)

        subject = str(scrape_file) + " du "+str(temps)
        body = 'Mail de confirmation de scraping réussi pour : '+ str(scrape_file)

        msg = (f'Subject:{subject}\n\n{body}').encode('utf-8')

        smtp.sendmail(EMAIL_ADDRESS,EMAIL_ADDRESS,msg)
