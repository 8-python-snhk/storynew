import random
when = ['很久以前','昨天','今天','一年前','一月一号']
who = ['兔子','老鼠','学生','老师','猫']
name = ['levi','zhou','liu','wang','chen']
residence = ['一个房子里','武汉','北京','上海']
went = ['学校','电影院','书店','朋友家','公园']
happened = ['摔了一跤','调皮被老师发现','考试没考好','打乒乓球']
print(random.choice(when)+ ',' +random.choice(who) + 'ta住在' + random.choice(residence) + ',去了' + random.choice(went) + ' 然后' + random.choice(happened))
input("按任意键结束...")

