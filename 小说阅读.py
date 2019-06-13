
#题目：精分少女的小说阅读器
#作者：moyu
#写这么长原因：沉迷小说，不可自拔
#存在问题：
        # 1 文件不能为空
        # 2 好多地方不能退出（太晚了，不能再熬夜了QAQ，不想写了）
        # 3 打赏和推荐没有跳转到充值页面（(⊙﹏⊙)其实应该和排行榜的跳转到登陆差不多，然而还有好多作业等着我宠幸呢）
        # 4 里面有好多import没有删
        # 5 其他的暂时没发现，不想发现，好晚了QAQ
#畅想：
        # 1 套个android外壳，可以吗（期待）？
        # 2 拉一波web端的小说接口，然后我就可以不掏钱还没广告的看小说了。不过暂时不会写python调用接口的方法QAQ




import pickle,operator
#用户信息
class User:
    #账号(userID 000累加)昵称(userName),密码(userPw),userCount默认为空）
    userID=0
    userName='null'
    userPw='null'
    #账户建立之出金额为0
    userCount=0
    #注册不需userID userCount 登陆只需userID userPw
    def __init__(self,userPw,userID=0,userName='null',userCount=0):
        self.userID=userID
        self.userName=userName
        self.userPw=userPw
        self.userCount=userCount
    def setUserID(self,userID):
        #传入列表中最后一个账户的ID加1
        self.userID=userID+1
class UserAction:
    #注册
    def regist(self,reg):
        import pickle
        #print(reg.userName)
        u=[reg.userName,reg.userPw,reg.userCount]
        #print(u)
        fi=open(r"user.txt","rb")
        list1=[]
        list1=pickle.load(fi)
        #print(list1)
        #最后一位用户的ID
        reg.setUserID(list1[len(list1)-1][0])
        u.insert(0,reg.userID)
        list1.append(u)
        fi.close()
        f=open(r"user.txt","wb")
        pickle.dump(list1,f)
        f.close()
        print(reg.userName,'您的账号是',reg.userID,'请妥善保管')
    #登陆 
    def login(self,logi):
        import pickle
        #取值
        fi=open(r"user.txt","rb")
        list1=[]
        list1=pickle.load(fi)
        #print(list1)
        fi.close()
        for i in list1:
            if logi.userID==i[0]:
                if logi.userPw==i[2]:
                    logi.userName=i[1]
                    logi.userCount=i[3]
                    print(logi.userName,'欢迎进入书的海洋')
                    return True
        print('账号或用户名错误，请重新登录')
        return False
    #充值 userID 充值账号 money 充值金额
    def giveMoney(self,userID,money):
        import pickle
        #取值
        fi=open(r"user.txt","rb")
        list1=[]
        list1=pickle.load(fi)
        fi.close()
        #print(list1)
        for i in list1:
            if userID==i[0]:
                #取值并改变
                print('账号存在，充值中')
                list1[list1.index(i)][3]+=money
                print(i[0],'已成功充值',money,'元；','现有余额：',list1[list1.index(i)][3])
        #重新装入
        f=open(r"user.txt","wb")
        pickle.dump(list1,f)
        f.close()
#第二个页面
#书籍类     书籍ID？从零累加（每个文件累加自己的）   
class Book:
    bookID=0
    bookName='null'
    #打赏金额 1：1 人民币
    daShang=0
    #推荐票数 1：1 人民币
    tuiJian=0
    #书页内容
    bookContents=[]
    #点击量
    bookClick=0
    def __init__(self,bookName,bookContents,daShang=0,tuiJian=0,bookClick=0,bookID=0):
        self.bookName=bookName
        self.bookContents=bookContents
        self.daShang=daShang
        self.tuiJian=tuiJian
        self.bookClick=bookClick
        self.bookID=bookID
    def setBookID(self,bookID):
        #传入列表中最后一个书的ID加1
        self.bookID=bookID+1
class Books:
    def addBook(self,book,sort):
        import pickle
        u=[book.bookName,book.daShang,book.tuiJian,book.bookContents,book.bookClick]
        #print(u)
        fi=open(sort,"rb")
        list1=[]
        list1=pickle.load(fi)
        #print(list1)
        #累加bookID,同userID
        book.setBookID(list1[len(list1)-1][5])
        u.insert(5,book.bookID)
        list1.append(u)
        fi.close()
        f=open(sort,"wb")
        pickle.dump(list1,f)
        f.close()
    #填充一本书
    def creatBook(self):
        print('少年/少女，快拿起你的御笔，写下这篇江山')
        bookName=input("请输入要添加的书籍名字：")
        bo=1
        bookContents=[]
        print('开始添加书籍内容，按Enter继续下一页，按0结束编辑')
        while bo:
            print("请输入第",bo,"页的内容")
            bookContent=input("")
            bo=bo+1
            bookContents.append(bookContent)
            ex=int(input("按0结束，按1进入下一页："))
            if ex==0:
                bo=0
            elif ex==1:
                pass
        book=Book(bookName,bookContents)
        return book
    #添加书籍前，选择书籍分类
    def addBookSorts(self,sort):
        if sort==1:
            #调用古典仙侠
            book=self.creatBook()
            self.addBook(book,r"gudian.txt")
        elif sort==2:
            book=self.creatBook()
            self.addBook(book,r"dongfang.txt")
        elif sort==3:
            book=self.creatBook()
            self.addBook(book,r"badao.txt")
        elif sort==4:
            book=self.creatBook()
            self.addBook(book,r"dushi.txt")
     #file为所调用文件地址
    def sorts(self,file,user):
        import pickle
        fi=open(file,"rb")
        list1=[]
        list1=pickle.load(fi)
        fi.close()
        num=0
        print('看第几本书按几：')
        #输出书籍名称供用户选择
        for i in list1:
            num+=1
            print('第',num,'本书：',i[0])
        print()
        bookNum=int(input('爱卿，今天想看哪本书：'))
        self.sortBook(list1[bookNum-1],user,file)
    #选择书的种类
    def switchSorts(self,sort,user):
        if sort==1:
            #调用古典仙侠
            self.sorts(r"gudian.txt",user)
        elif sort==2:
            self.sorts(r"dongfang.txt",user)
        elif sort==3:
            self.sorts(r"badao.txt",user)
        elif sort==4:
            self.sorts(r"dushi.txt",user)
    #打赏，和充值相反
    def daShang(self,user,book,file):
        fi=open(r"user.txt","rb")
        list1=[]
        list1=pickle.load(fi)
        fi.close()
        #print(list1)
        #找到书籍现有列表
        ##
        ###这个比较大欸
        fbi=open(file,"rb")
        list2=[]
        list2=pickle.load(fbi)
        fbi.close()
        for i in list1:
            if user.userID==i[0]:
                #取值并改变
                mo=int(input("请输入要打赏金额（1：1）："))
                if list1[list1.index(i)][3]-mo>=0:
                    list1[list1.index(i)][3]-=mo
                    #print(book[5])
                    list2[book[5]][1]+=mo
                    print(i[1],'已成功打赏',mo,'元；','现有余额：',list1[list1.index(i)][3])
                    #重新装入
                    f=open(r"user.txt","wb")
                    pickle.dump(list1,f)
                    f.close()
                    bi=open(file,"wb")
                    pickle.dump(list2,bi)
                    bi.close()
                else:
                    print('您的余额不足，不能打赏')
                
    #投推荐票
    def tuiJian(self,user,book,file):
        fi=open(r"user.txt","rb")
        list1=[]
        list1=pickle.load(fi)
        fi.close()
        #print(list1)
        #找到书籍现有列表
        ##
        ###这个比较大欸
        fbi=open(file,"rb")
        list2=[]
        list2=pickle.load(fbi)
        fbi.close()
        for i in list1:
            if user.userID ==i[0]:
                #取值并改变
                mo=int(input("请输入要投票数（1：1）："))
                if list1[list1.index(i)][3]-mo>=0:
                    list1[list1.index(i)][3]-=mo
                    list2[book[5]][2]+=mo
                    print(i[1],'已成功投出',mo,'票；','现有余额：',list1[list1.index(i)][3])                
                    #重新装入
                    f=open(r"user.txt","wb")
                    pickle.dump(list1,f)
                    f.close()
                    bi=open(file,"wb")
                    pickle.dump(list2,bi)
                    bi.close()
                else:
                    print('您的余额不足，买不起推荐票')
    #更新点击量
    def bookClick(self,book,file):
        fbi=open(file,"rb")
        list2=[]
        list2=pickle.load(fbi)
        fbi.close()
        #print(list2[book[5]])
        #print(list2[book[5]][4])
        list2[book[5]][4]+=1
        bi=open(file,"wb")
        pickle.dump(list2,bi)
        bi.close()

    #书籍详细页,file判断是哪类书 ,进入开始看书   
    def sortBook(self,book,user,file):
        print('书名：',book[0])
        print('打赏：',book[1])
        print('推荐票：',book[2])
        print('点击量：',book[4])
        da=input("客官，不来点小费吗（Y/N）：")
        if da=='Y':
            self.daShang(user,book,file)
            print("谢过客官")
        elif da=='N':
            print('讨厌~~~')
        tui=input("美丽的小仙女/小哥哥，投我一票好不好嘛（Y/N）：")
        if tui=='Y':
            self.tuiJian(user,book,file)
            print("mua")
        elif tui=='N':
            print('qaq~~~')
        #更改点击量
        self.bookClick(book,file)
        #浏览过书页
        page=0
        #当前页
        nowPage=-1
        #更新账户信息至最新
        fi=open(r"user.txt","rb")
        list1=[]
        list1=pickle.load(fi)
        for i in list1:
            if i[0]==user.userID:
                user.userCount=i[3]
                print('余额：',user.userCount)
        #总页数    
        numPage=len(book[3])
        #退出不想看了
        exx=1
        while numPage>nowPage+1 and exx:
            nex=input("爱卿，想看这一页吗？(Y / N):")
            if nex=='Y':
                #判断此页之前是否读过，读过不用交钱
                if user.userCount>0 or nowPage+1<page:
                    if nowPage+1<page:
                        nowPage+=1
                    else:
                        user.userCount-=1
                        page+=1
                        nowPage+=1
                    print(book[3][nowPage])
                    if numPage==nowPage+1:
                        print('本书已读完，爱卿退朝吧')
                        print()
                        
                else:
                    gm=int(input("爱卿，余额不足了，还想看的话，快给朕国库交银子："))
                    ua=UserAction()
                    ua.giveMoney(user.userID,gm)
                    user.userCount+=gm
            elif nex=='N':
                pre=input("爱卿，是想看上一页吗？(Y / N)")
                if nowPage>0 or pre=='N':
                    if pre=='Y':
                        nowPage-=1
                        print(book[3][nowPage])
                    elif pre=='N':
                        print('无本启奏，就退朝吧')
                        exx=0
                        print()
                else:
                    print('爱卿已经翻到头了')
                    print()

        for i in list1:
            if i[0]==user.userID:
                #看完后，更新账户余额
                list1[list1.index(i)][3]=user.userCount
        f=open(r"user.txt","wb")
        pickle.dump(list1,f)
        f.close()
    #选择排行榜中的哪一本书
    def diaoBang(self,book,user):
        file='null'
        ind=book[6]
        if ind=='古典仙侠':
            #print(book)
            file=r"gudian.txt"
        elif ind=='东西玄幻':
            file=r"dongfang.txt"
        elif ind=='霸道总裁':
            file=r"badao.txt"
        elif ind=='都市人生':
            file=r"dushi.txt"
        self.sortBook(book,user,file)

    #排行榜，bookKinds为排行榜类别（如点击榜按book[4]排序）
    #将所有文件都读取一下，合并成一个列表，排序
    #可能存在问题：排行榜只是一个花架子，并没有和书连接
    def paiHangBang(self,bookKinds,user=0):
        if bookKinds==3:
            bookKinds=4
        f1=open(r"gudian.txt","rb")
        list1=pickle.load(f1)
        for i in list1:
            list1[list1.index(i)].append('古典仙侠')
        f1.close()
        f2=open(r"dongfang.txt","rb")
        list2=pickle.load(f2)
        for i in list2:
            list2[list2.index(i)].append('东西玄幻')
        f2.close()
        f3=open(r"badao.txt","rb")
        list3=pickle.load(f3)
        for i in list3:
            list3[list3.index(i)].append('霸道总裁')
        f3.close()
        f4=open(r"dushi.txt","rb")
        list4=pickle.load(f4)
        for i in list4:
            list4[list4.index(i)].append('都市人生')
        f4.close()
        #合在一块
        list5=[]
        list5.extend(list1)
        list5.extend(list2)
        list5.extend(list3)
        list5.extend(list4)
        #降序排序
        list5.sort(key=operator.itemgetter(bookKinds),reverse=True)
        num=0
        while num<201 and num<len(list5):
            for i in list5:
                num+=1
                print(num,i[0],i[6])
        print()
        like=input('少年/少女，有你喜欢的书吗？有的话，请输入你想看的书前的数字；没有的话请按 N：')
        if like=='N':
            pass
        elif user==0:
            print('少年/少女，想看书先登陆')
            print()
            #调用登陆
            like=int(like)-1
            book=list5[like]
            user=self.diaoLogin(book)
        else:
            like=int(like)-1
            book=list5[like]
            self.diaoBang(book,user)
        return user
    #调用登陆
    def diaoLogin(self,like=0,user=0):
        if user==0:
            print('=====欢迎来到登陆页面=====')
            #账号
            uID=int(input('请输入您的账号：'))
            #密码
            uPw=input('请输入您的密码：')
            user=User(userID=uID,userPw=uPw)
        ua=UserAction()
        #登陆动作
        if ua.login(user):
            print()
            #登陆之前没有进入排行榜
            if like==0:               
                sort=6
                while sort!='q':
                    sort=input('请选择图书分类，古典仙侠请按1；东西玄幻请按2；霸道总裁请按3；都市人生请按4,添加书籍请按5，查看榜单请按6，退出请按q：')
                    if sort!='q':
                        sort=int(sort)
                    if sort==5:
                        #添加书籍
                        addSort=int(input('请选择要添加图书分类，古典仙侠请按1；东西玄幻请按2；霸道总裁请按3；都市人生请按4：'))
                        print()
                        self.addBookSorts(addSort)
                    elif sort==6:
                        #查看排行榜
                        bookKinds=10
                        while bookKinds!='q':
                            if bookKinds!='q':
                                bookKinds=int(bookKinds)
                                self.paiHangBang(bookKinds)
                    elif sort=='q':
                        user=0
                    else:
                        self.switchSorts(sort,user)
            else:
                self.diaoBang(like,user)
        return user
                
        

        
class Demo:
    first=5
    user=0
    while first:
        if first!=2 or user==0:
            first=int(input('请根据需要按：1 注册；2 登陆看书系统；3 充值；4 查看榜单：点击榜、推荐榜、打赏榜；0 退出：'))
        print()
        if first==1:
            print('=====欢迎来到注册页面=====')
            #用户名
            uName=input('请输入您的昵称：')
            #密码
            uPw=input('请输入您的密码：')
            user=User(userName=uName,userPw=uPw)
            ua=UserAction()
            #注册动作
            ua.regist(user)
            user=0
            print()
        elif first==2:
            bk=Books()
            #判断是否已登陆（调用排行榜后）
            if user==0:
                bk.diaoLogin()
            else:
                user=bk.diaoLogin(user=user)
        elif first==3:
            print('=====欢迎来到充值页面=====')
            #账号
            uID=int(input('请输入您的账号：'))
            #充值金额
            money=int(input('请输入您的充值金额：'))
            ua=UserAction()
            ua.giveMoney(uID,money)
            print()
        elif first==4:
            print('=====排行榜=====')
            books=Books()
            bookKinds=10
            while bookKinds!='q':
                bookKinds=input('请选择要查看的排行榜：打赏榜请按1；推荐榜请按2；点击榜请按3；退出请按q：')
                print()
                if bookKinds!='q':
                    bookKinds=int(bookKinds)
                    books=Books()
                    #判断user是否定义过
                    #if not 'user' in dir():
                    if user==0:
                        user=books.paiHangBang(bookKinds)
                    #调用排行榜时登陆过了
                    books.paiHangBang(bookKinds,user)
                else:
                    if user!=0:
                        first=2
            print()
            
d=Demo()


            
