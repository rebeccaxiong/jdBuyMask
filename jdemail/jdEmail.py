# -*- coding=utf-8 -*-
'''
发送邮件模块
'''
import traceback


def sendMail(mail, url, isOrder):
    try:
        import smtplib
        from email.mime.text import MIMEText
        # email 用于构建邮件内容
        from email.header import Header

        # 用于构建邮件头
        # 发信方的信息：发信邮箱，QQ 邮箱授权码
        from_addr = '540518514@qq.com'
        password = 'kytjhosonkldbajg'

        # 收信方邮箱
        to_addr = 540518514@qq.com
        # 发信服务器
        smtp_server = 'smtp.qq.com'
        # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
        if isOrder:
            msg = MIMEText(url + ' 类型口罩，已经下单了。24小时内付款', 'plain', 'utf-8')
        else:
            msg = MIMEText(url + ' 类型口罩，下单失败了，快去抢购！', 'plain', 'utf-8')
        # 邮件头信息
        # msg['From'] = Header(from_addr)
        msg['From'] = Header(u'from Mark<{}>'.format(from_addr), 'utf-8')
        msg['To'] = Header(to_addr)
        msg['Subject'] = Header('京东口罩监控','utf-8')
        # 开启发信服务，这里使用的是加密传输
        server = smtplib.SMTP_SSL(host=smtp_server)
        server.connect(smtp_server, 465)
        # 登录发信邮箱
        server.login(from_addr, password)
        # 发送邮件
        server.sendmail(from_addr, to_addr, msg.as_string())
        # 关闭服务器
        server.quit()
    except Exception as e:
        print(traceback.format_exc())
