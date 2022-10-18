import smtplib as s
ob = s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login('sidqazwsx801@gmail.com','nxacvwwdcqjufjws')
sub = "test python"
body = "i love python"
message = "subject:{}\n\n{}".format(sub,body)
lst = ['cowos65359@inkmoto.com']
ob.sendmail('sidqazwsx801@gmail.com',lst,message)
print('mail sent')
ob.quit()