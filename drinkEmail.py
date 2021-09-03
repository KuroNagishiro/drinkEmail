import smtplib
import time
import random
from imgData import arr
from email.mime.text import MIMEText
from email.header import Header

#获取当前时间
curTime = time.strftime("%H:%M:%S", time.localtime())

#发送的内容
mail_msg = """
    <p>现在的时间是:%s</p>
    <h2 style="color:#f00">距离上一次喝水已经过了一小时了，可以暂时停下手中的游戏和工作喝一杯水啦</h2>
    """%(curTime)
#生成随机数
i = random.randint(0,3294)
#拼接图片的url
imgUrl1 = '<img src="https://steamuserimages-a.akamaihd.net/ugc/'
imgUrl2 = arr[i]
imgUrl3 = '">'
imgUrl = imgUrl1 + imgUrl2 + imgUrl3
#将图片和发送的内容拼接在一起
mail_msg = mail_msg + imgUrl

message = MIMEText(mail_msg,'html','utf-8')

message['From'] = Header("提醒喝水机器人",'utf-8')

message['To'] = Header("需要喝水的大家❤",'utf-8')

subject = '该喝水啦'
message['Subject'] = Header(subject,'utf-8')

sender = 'xxx@qq.com'
receiver = ['xxx@qq.com']

smtpObj = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 此处使用的是qq的smtp服务发送邮件
smtpObj.login(sender, "xxx")  # 此处填入获取到发件人邮箱的授权码
smtpObj.sendmail(sender,receiver,message.as_string())
smtpObj.quit()
print("邮件发送成功")