from itertools import count
from datetime import datetime
from tabnanny import check


class Product:
    def __init__(self,name,price,hajmi,):
        self.name=name
        self.price=price
        self.hajmi=hajmi
p=Product("banan",10,100)
p1=Product("olma",5,100)
p2=Product("guruch",2,10)
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
class Check:
    def __init__(self,checkname,proname,allsom,allkg,date):
        self.checkname=checkname
        self.proname=proname
        self.allsom=allsom
        self.allkg=allkg
        self.date=date
class Shop:
    def __init__(self,shopname):
        self.shopname=shopname
        self.shopbalance=0
        self.products=[]
        self.users=[]
        self.savat = []
        self.usercheck=[]
    def user_check(self,u:User):
        found=False
        for item in self.savat:
            if item.usersavat==u.username:
                found=True
                checkname=u.username
                proname=item.name
                allsom=item.all_price
                allkg=item.hajmi
                date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                ch=Check(checkname,proname,allsom,allkg,date)
                self.usercheck.append(ch)
        if found:
            print("check saqlandi")
        else:
            print("xato")
    def view_check(self):
        count=0
        for i in self.usercheck:
            count+=1
            print(f"{count}   check\n checkname:{i.checkname}\n proname:{i.proname}\n allson:{i.allsom}\n allkg:{i.allkg}\n date:{i.date}")
    def name_check(self):
        count=0
        name=input("checkname:")
        for i in self.usercheck:
            if i.checkname==name:
                count+=1
                print(f"{count}  check\n checkname:{i.checkname}\n proname:{i.proname}\n allson:{i.allsom}\n allkg:{i.allkg}\n date:{i.date}")
    def u_check(self,u:User):
        count=0
        for i in self.usercheck:
            if i.checkname==u.username:
                count+=1
                print(f"{count}  check\n checkname:{i.checkname}\n proname:{i.proname}\n allson:{i.allsom}\n allkg:{i.allkg}\n date:{i.date}")
    def shop_balance(self):
        print(f"shop_balance:{self.shopbalance}")
    def user_balance(self,u:User):
        print(f"user_balance: {u.balance}")
    def add_product(self):
        name=input("namepoduct")
        price=int(input("narxi"))
        hajmi=int(input("omorda_hajmi"))
        for i in self.products:
            if i.name == name:
                print("bor")
                return
        if hajmi>0:
            p=Product(name,price,hajmi)
            self.products.append(p)
        else:
            print("xato")
    def delete_product(self):
        name=input("delete_name")
        count=0
        for i in self.products:
            count+=1
            if name==i.name:
                x=count
                self.products.pop(x-1)
                print("o'chdi")
                break
        else:
            print("topilmadi")
            return
    def edit_product(self):
        name=input("edit_name")
        for i in self.products:
            if name==i.name:
                yangi=i
                break
        else:
            print("topilmadi")
            return
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
            else:
                print("hajmi xato")
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
                print("hajmi xato")
        else:
            print("xato")
            return
    def view_product(self):
        count=0
        for i in self.products:
            if i.hajmi>0:
                count+=1
                print(f"{count} name:{i.name} price:{i.price} hajmi:{i.hajmi}")
    def add_user(self):
        username=input("username")
        balance=float(input("balance"))
        password=int(input("password"))
        for i in self.users:
            if i.username == username:
                print("Bu username band ")
                return
        u=User(username,balance,password)
        self.users.append(u)
    def add_balance(self,u:User):
        username=u.username
        for i in self.users:
            if username==i.username:
                yangi=i
                add_balance=int(input("balance_add"))
                if add_balance <= 0:
                    print("xato")
                    return
                yangi.balance=i.balance+add_balance
                break
        else:
            print("topilmadi")
            return
    def view_user(self):
        count=0
        for i in self.users:
            count+=1
            print(f"{count} username:{i.username} balance:{i.balance} password:{i.password}")
    def add_savat(self,u:User):
        self.view_product()
        name = input('name')
        for p in self.products:
            if p.name == name and p.hajmi>0:
                product = p
                break
        else:
            print("topilmadi")
            return
        hajmi = int(input("kg: "))
        if hajmi <= 0:
            print("0 bo‘la olmaydi")
            return
        if hajmi > product.hajmi:
            print(f"Omborda {product.hajmi} kg bor!")
            return
        for item in self.savat:
            if item.usersavat == u.username and item.name == name:
                item.hajmi += hajmi
                item.all_price = item.hajmi * item.price
                print("Savat yangilandi!")
                return
        new_sav = Savat(name, product.price * hajmi, hajmi, product.price)
        new_sav.usersavat = u.username
        self.savat.append(new_sav)
        print("Savatga qo‘shildi!")
    def edit_Savat(self,u:User):
        name=input("nameproduct")
        userisim=u.username
        for i in self.savat:
            if name==i.name and userisim==i.usersavat:
                yangi=i
                new_hajmi=int(input("new_hajmi"))
                if new_hajmi>0:
                    yangi.hajmi=new_hajmi
                    yangi.all_price=i.price*new_hajmi
                    print("o'zgardi")
                else:
                    print("hajmi xato")
                    break
        else:
            print("topilmadi")
            return
    def delete_savat(self,u:User):
        name=input("nameproduct")
        count=0
        userismi=u.username
        for i in self.savat:
            count+=1
            if name==i.name and userismi==i.usersavat:
                self.savat.pop(count-1)
                break
        else:
            print('topilmadi')
            return
    def view_savat(self, u:User):
        count=0
        found=False
        userismi=u.username
        for i in self.savat:
            if userismi==i.usersavat:
                found=True
                count+=1
                print(f"{count} name:{i.name} all_price:{i.all_price} hajmi:{i.hajmi} price:{i.price}")
        if not found:
            print("topilmadi")
    def shopping(self, u:User):
        userismi = u.username
        shop_price = 0
        user_items = [i for i in self.savat if i.usersavat == userismi]
        if not user_items:
            print("savat bo'sh")
            return
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
        self.user_check(u)
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
        kod =input(" 1.add_product\n 2.delete_product\n 3.edit_product\n 4.view_product\n 5.view_user\n 6.shop_balance\n 7.view_chek\n 8.name_check\n 9.break")
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
        elif kod=="7":
            sh.view_check()
        elif kod=="8":
            sh.name_check()
        else:
            break
def user_menejer(sh:Shop,u:User):
    while True:
        kod=input(" 1.shoping\n 2.add_balance\n 3.add_savat\n 4.edit_savat\n 5.view_savat\n 6.user_balance\n 7.u_check\n 8.break")
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
            sh.user_balance(u)
        elif kod=="7":
            sh.u_check(u)
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
# menejer_shop(shop)


list1=[1,2]
list2=[1,2]
list3=list1

print(f"{id(list1)}, \n {id(list2)}, \n {id(list3)}")