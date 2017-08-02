import random

class Bank():

    def info(self):

        self.name = input("Enter your name:")

        self.acc = input("Enter type of account u want:")
        self.age = int(input("Enter your age:"))
        print(self.age)
        print(self.name)

        print(self.acc)







    def bal(self):
        print("The minimum amount to be deposied intially is Rs.20000")

        self.amt = int(input(" Amount deposited:"))
        print(self.amt)
        while self.amt < 20000:
            print("Add more money")
            self.amt1 = int(input("More money deposited:"))
            self.amt = self.amt +self.amt1

        print("Amount in your account now",self.amt)


    def acc_id(self):
        self.id = random.randrange(1000,5000)
        print("Your unique account id is :",self.id)
    def file_create(self):
        self.fr = open(self.name + str(self.id),"w")
        self.fr.write("YOur name is:")
        self.fr.write(self.name)
        self.fr.write("\nHolder's age:")
        self.fr.write(str(self.age))
        self.fr.write("\nType of account:")
        self.fr.write(self.acc)
        self.fr.write("\nBalance in ur account:")
        self.fr.write(str(self.amt))

        self.fr.write("\nYour unique id:")
        self.fr.write(str(self.id))
        self.fr.close()



    def withdraw(self):

        self.code = input("ENTER  your name") + str(int(input("Enter you unique id:")))
        self.fs = open(self.code,"r")
        self.fw = self.fs.read()
        print(self.fw)
        self.fs.close()

        fz = open(self.code,"r")

        for line in fz.readlines():
            if line.startswith("Bal"):
                print(line)
                self.b = line.split(":")
                print(self.b)
                self.c = self.b[1]
                self.h  = int(self.c)
                self.balout = int(input("Enter amount to be withdrawn:"))
                if self.h < 5000:
                    print("limit crossed, minimum balance must be greater than Rs.5000")
                else:
                    self.h -= self.balout

                    print("Amount after withdrawal:")
                    print(self.h)

        fz.close()
        fg = open(self.code,"r")
        line = fg.readlines()
        print(line)

        res = line
        seps = [':','\n']
        for sep in seps:
            s, res = res, []
            for seq in s:
                res += seq.split(sep)

        print(res)
        res.remove(res[10])


        res.insert(10,str(self.h))
        print(res)

        fg.close()
        with open(self.code,"w") as gy :

            for fr in res:
                if fr == res[1] or fr == res[4] or fr == res[7] or fr == res[10] or fr == res[13]:
                    gy.write(":" + fr + "\n")
                else:
                    gy.write(fr)

    def deposit(self):

        self.meow = input("ENTER  your name") + str(int(input("Enter you unique id:")))
        self.js = open(self.meow, "r")
        self.jw = self.js.read()
        print(self.jw)
        self.js.close()

        jz = open(self.meow, "r")

        for lane in jz.readlines():
            if lane.startswith("Bal"):
                print(lane)
                self.we = lane.split(":")
                print(self.we)
                self.wr = self.we[1]
                self.mn = int(self.wr)
                self.balin = int(input("Enter amount to be deposited:"))
                self.mn += self.balin

                print("Amount after deposition:")
                print(self.mn)

        jz.close()
        jg = open(self.meow, "r")
        line = jg.readlines()


        res = line
        seps = [':', '\n']
        for sep in seps:
            s, res = res, []
            for seq in s:
                res += seq.split(sep)


        res.remove(res[10])


        res.insert(10, str(self.mn))


        jg.close()
        with open(self.meow, "w") as gy:

            for fr in res:
                if fr == res[1] or fr == res[4] or fr == res[7] or fr == res[10] or fr == res[13]:
                    gy.write(":" + fr + "\n")
                else:
                    gy.write(fr)












print("Welcome to Dota banking")
print("1:Open New Account \n2:Already Have an Account")
choice = int(input("Enter your option:"))
if choice == 1:
    bank1 = Bank()
    bank1.info()

    bank1.bal()
    bank1.acc_id()
    bank1.file_create()
elif choice == 2:


    print("1:Withdraw Amount \n2:Deposit amount \n3:Exit")

    chance = int(input("Enter your option:"))
    if chance == 1:
        bankai = Bank()

        bankai.withdraw()
    elif chance == 2:
        banku = Bank()
        banku.deposit()
    else:
        print("Thank You for choosing Dota banking")


