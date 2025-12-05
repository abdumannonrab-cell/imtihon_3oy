from itertools import count


class Product:
    def __init__(self,name,price,hajmi,):
        self.name=name
        self.price=price
        self.hajmi=hajmi
p=Product("banan",10,100)
p1=Product("olma",5,100)
p2=Product("guruch",20,100)
class User:
    def __init__(self,username,balance,password):
        self.username=username
        self.balance=balance
        self.password=password
        self.is_admin=False
u=User("abdumannon",100,0000)
class Savat:
    def __init__(self,name,all_price,hajmi,price):
        self.name=name
        self.all_price=all_price
        self.hajmi=hajmi
        self.price=price
        self.usersavat=None
class Shop:
    def __init__(self,shopname):
        self.shopname=shopname
        self.shopbalance=0
        self.products=[]
        self.users=[]
        self.savat = []
    def shop_balance(self):
        print(f"shop_balance:{self.shopbalance}")
    def user_balance(self):
        username=u.username
        t=False
        for i in self.users:
            if username==i.username:
                print(f"user_balance:{i.balance}")
                t=True
        if not t:
            print('topilmadi')
    def add_product(self):
        name=input("namepoduct")
        price=int(input("narxi"))
        hajmi=int(input("omorda_hajmi"))
        if hajmi>0:
            p=Product(name,price,hajmi)
            self.products.append(p)
        else:
            print("xato")
    def delete_product(self):
        name=input("delete_name")
        count=0
        t=False
        for i in self.products:
            count+=1
            if name==i.name:
                t=True
                x=count
                self.products.pop(x-1)
                print("o'chdi")
                break
        if not t:
            print("topilmadi")
    def edit_product(self):
        name=input("edit_name")
        t=False
        for i in self.products:
            if name==i.name:
                yangi=i
                t=True
        if t:
            kod=input(" 1.name\n 2.price\n 3.hajmi\n 4.all")
            if kod=="1":
                new_name=input("new_namae")
                yangi.name=new_name
                print("o'zgardi")
            elif kod=="2":
                new_price=int(input("new_price"))
                yangi.price=new_price
                print("o'zgardi")
            elif kod=="3":
                new_hajmi=int(input("new_hajmi"))
                if new_hajmi>0:
                    yangi.hajmi=new_hajmi
                    print("o'zgardi")
            elif kod=="4":
                new_name = input("new_namae")
                new_price = int(input("new_price"))
                new_hajmi = int(input("new_hajmi"))
                if new_hajmi>0:
                    yangi.name = new_name
                    yangi.price = new_price
                    yangi.hajmi = new_hajmi
                    print("all_o'zgardi")
            else:
                print("xato")
        else:
            print("topilmadi")

    def view_product(self):
        count=0
        for i in self.products:
            count+=1
            print(f"{count} name:{i.name} price:{i.price} hajmi:{i.hajmi}")
    def add_user(self):
        username=input("username")
        balance=float(input("balance"))
        password=int(input("password"))
        u=User(username,balance,password)
        self.users.append(u)
    def add_balance(self,u:User):
        username=u.username
        t=False
        for i in self.users:
            if username==i.username:
                t=True
                yangi=i
                add_balance=int(input("balance_add"))
                yangi.balance=i.balance+add_balance
        if not t:
            print("topilmadi")
    def view_user(self):
        count=0
        for i in self.users:
            count+=1
            print(f"{count} username:{i.username} balance:{i.balance} password:{i.password}")

    def add_savat(self,u:User):
        count = 0
        for i in self.products:
            count += 1
            print(f"{count} name:{i.name} price:{i.price} hajmi:{i.hajmi}")
        t=False
        userismi=u.username
        for i in self.users:
            if userismi==i.username:
                usersavat=i.username
                name=input('name')
                for j in self.products:
                    if name==j.name:
                        t=True
                        hajmi=int(input("hajmi kg"))
                        if hajmi>0:
                            all_price=hajmi*j.price
                            price=j.price
                            sh=Savat(name,all_price,hajmi,price)
                            sh.usersavat=usersavat
                            self.savat.append(sh)
                        else:
                            print("hajmi_xato")
                        break
        if not t :
            print("topilmadi")
    def edit_Savat(self,u:User):
        name=input("nameproduct")
        userisim=u.username
        t=False
        for i in self.savat:
            if name==i.name and userisim==i.usersavat:
                t=True
                yangi=i
                new_hajmi=int(input("new_hajmi"))
                if new_hajmi>0:
                    yangi.hajmi=new_hajmi
                    yangi.all_price=i.price*new_hajmi
                    print("o'zgardi")
                else:
                    print("hajmi xato")
        if not t:
            print("topilmadi")
    def delete_savat(self,u:User):
        name=input("nameproduct")
        count=0
        t=False
        userismi=u.username
        for i in self.savat:
            count+=1
            if name==i.name and userismi==i.usersavat:
                self.savat.pop(count-1)
                t=True
        if not t:
            print('topilmadi')
    def view_savat(self, u:User):
        count=0
        t=False
        userismi=u.username
        for i in self.savat:
            if userismi==i.usersavat:
                count+=1
                print(f"{count} name:{i.name} all_price:{i.all_price} hajmi:{i.hajmi} price:{i.price}")
                t=True
        if not t:
            print("topilmadi")
    def shopping(self, u: User):
        userismi = u.username
        shop_price = 0

        for i in self.savat:
            if userismi == i.usersavat:
                shop_price += i.all_price

        if u.balance < shop_price:
            print("Mablag' yetarli emas")
            return
        for i in self.savat:
            if userismi == i.usersavat:
                for j in self.products:
                    if i.name == j.name:
                        if j.hajmi >= i.hajmi:
                            j.hajmi -= i.hajmi
                        else:
                            print("omborda yetmaydi")
                            return

        u.balance -= shop_price
        self.shopbalance += shop_price

        self.savat = [i for i in self.savat if i.usersavat != userismi]
        print("Xarid amalga oshdi!")
    def login(self):
        name = input("username: ")
        password = int(input("password: "))
        count=0
        for item in self.users:
            count+=1
            if item.username == name and item.password == password:
                return item, True
            else:
                if count==len(self.users):
                    return 0,False
shop=Shop("onlineshop")
admin=User("admin",0,1111)
admin.is_admin=True
shop.products.append(p)
shop.products.append(p1)
shop.products.append(p2)
shop.users.append(admin)
shop.users.append(u)
def admin_menejer(sh:Shop,u:User):
    while True:
        kod =input(" 1.add_product\n 2.delete_product\n 3.edit_product\n 4.view_product\n 5.view_user\n 6.shop_balance\n 7.break")
        if kod=="1":
            sh.add_product()
        elif kod=="2":
            sh.delete_product()
        elif kod=="3":
            sh.edit_product()
        elif kod=="4":
            sh.view_product()
        elif kod=="5":
            sh.view_user()
        elif kod=="6":
            sh.shop_balance()
        else:
            break
def user_menejer(sh:Shop,u:User):
    while True:
        kod=input(" 1.shoping\n 2.add_balance\n 3.add_savat\n 4.edit_savat\n 5.view_savat\n 6.user_balance\n 7.break")
        if kod=='1':
            sh.shopping(u)
        elif kod=='2':
            sh.add_balance(u)
        elif kod=='3':
            sh.add_savat(u)
        elif kod=="4":
            sh.edit_Savat(u)
        elif kod=='5':
            sh.view_savat(u)
        elif kod=="6":
            sh.user_balance()
        else:
            break
def menejer_shop(sh:Shop):
    while True:
        kod =input(" 1.login\n 2.kirish\n 3.braek")
        if kod=="1":
            item=sh.login()
            if item[1]:
                if item[0].is_admin:
                    admin_menejer(sh, item[0])
                else:
                    user_menejer(sh, item[0])
            else:
                print("xato1")
        elif kod=="2":
            sh.add_user()
menejer_shop(shop)

