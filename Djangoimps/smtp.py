import smtplib
content="Hello World"
mail=smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
sender='225003055@sastra.ac.in'
recipient='beerakajaivanth15@gmail.com'
mail.login('225003055@sastra.ac.in','********')
header='To:'+recipient+'\n'+'From:' \
+sender+'\n'+'subject:testmail\n'
content=header+content
mail.sendmail(sender, recipient, content)
mail.close()
