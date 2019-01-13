# import smtplib
# from email.mime.text import MIMEText
# smtpserver="smtp.qq.com"
# port="465"
# sender="446816637@qq.com"
# psw="oupahyapzqikbgce"
# receiver="gaotianming3@jd.com"
# body="<pre><h1>测试报告，请查收~</h1></pre> "
#
# #邮件内容
#
# msg =MIMEText(body,"html","utf-8")
# msg["from"]=sender
# msg["to"]=receiver
# msg["subject"]="自动化测试报告"
#
# #调用发件服务
#
# smtp=smtplib.SMTP_SSL(smtpserver,port)
# smtp.login(sender,psw)
# smtp.sendmail(sender,receiver,msg.as_string())
# smtp.quit()


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
smtpserver="smtp.qq.com"
port=465
sender="446816637@qq.com"
receiver="gaotianming3@jd.com"
psw="oupahyapzqikbgce"
#body="<pre><h1>测试报告，请查收~</h1></pre> "
# #填写邮件内容,发送文本
# msg = MIMEText(body,"html","utf-8")
# msg["form"]=sender
# msg["to"]=receiver
# msg["subject"]="主题是测试报告"


#发送附件
msg = MIMEMultipart()
msg["from"]=sender
msg["to"]=receiver
msg["subject"]="主题是测试报告"
b=open(r"2019-01-13 15_01_51-report.html","rb")
mail_body=b.read()
b.close()
#正文
body=MIMEText(mail_body,"html","utf-8")
msg.attach(body)
#附件
att = MIMEText(mail_body ,"base64", "utf-8")
att["Content-Type"] = "application/octet-stream"
att["Content-Disposition"] = 'attachment; filename= "test_report.html"'
msg.attach(att)


#调用发件服务QQ邮箱
smtp=smtplib.SMTP_SSL(smtpserver,port)
smtp.login(sender,psw)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()

#企业邮箱
