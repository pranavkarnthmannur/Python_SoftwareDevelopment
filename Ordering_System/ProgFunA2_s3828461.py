import os
from datetime import datetime

class Customer:
    #Customer class to support attributes such as ID, name and value
    discount = 0

    def __init__(self, ID=None, name=None, value=0):
        self.ID = ID
        self.name = name
        self.value = value

    def get_ID(self):
        return self.ID

    def set_ID(self, ID):
        self.ID = ID

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_discount(self, price):
        return Customer.discount, price

    def display_info(self):

        return "{:<3} {:<10} {:<7} {:<7}".format(str(self.ID),self.name,str(Customer.discount),str(self.value))


c = Customer()

class Member(Customer):
    #Member class to support attributes such as ID, name, value and discount
    discount = 5

    def __init__(self, ID=0, name=None, value=None, discount=5):
        Customer.__init__(self, ID, name, value)
        # super(Member, self).__init__()
        self.discount = discount

    def set_rate(self, discount):
        self.discount = discount

    def get_rate(self):
        return self.discount

    def get_discount(self, price):
        total = float(price) - float(Member.discount/100 * price)
        return Member.discount, total

    def display_info(self):

        return "{:<3} {:<10} {:<7} {:<7}".format(str(self.ID), self.name, str(self.discount), str(self.value))


m = Member()

class VIPMember(Customer):
    #VIP Member class to support attributes such as ID, name, value and discount, second discount and threshold value
    discount = 10
    discountextra = 15
    thresh = 1000

    def __init__(self, ID=None, name=None, value=None, discount=10):
        Customer.__init__(self, ID, name, value)
        self.discount = discount

    def set_firstrate(self, firstdiscount):
        self.discount = firstdiscount

    def get_firstrate(self):
        return self.discount

    def set_secondrate(self, seconddiscount):
        self.discountextra = seconddiscount

    def get_secondrate(self):
        return self.discountextra

    def set_threshold(self, newthresh):
        self.thresh = newthresh

    def get_threshold(self):
        return self.thresh

    def get_discount(self, price):
        """ Sets the discount value for the price according to the threshold value"""
        if price <= self.thresh:
            totaldiscount = self.discount
            total = float(price) - float(self.discount/100 * price)

        elif float(price) > self.thresh:
            totaldiscount = float(5 + self.discount)
            total = float(price) - float(totaldiscount/100 * price)

        return totaldiscount, total

    def display_info(self):

        return "{:<3} {:<10} {:<7} {:<7}".format(str(self.ID), self.name, str(self.discount), str(self.value))


vip = VIPMember()


class Product():
    #Product class to support attributes such as ID, name, price and stock

    def __init__(self, prodID=None, prodName=None, prodPrice=0, prodStock=0):
        self.prodID = prodID
        self.prodName = prodName
        self.prodPrice = prodPrice
        self.prodStock = prodStock

    def get_prodID(self):
        return self.prodID

    def set_prodID(self, prodID):
        self.prodID = prodID

    def get_prodName(self):
        return self.prodName

    def set_prodName(self, prodName):
        self.prodName = prodName

    def get_prodPrice(self):
        return self.prodPrice

    def set_prodPrice(self, prodPrice):
        self.prodPrice = prodPrice

    def get_prodStock(self):
        return self.prodStock

    def set_prodStock(self, prodStock):
        self.prodStock = prodStock

    def displayProduct(self):

        return "{:<3} {:<10} {:<7} {:<7}".format(str(self.prodID), self.prodName, str(self.prodPrice), str(self.prodStock))

    def updateproductquantity(self, productID, productStock): #This method supports the quantity of the product to be changed/updated
        for updateobject in r.list_products:
            if (type(updateobject).__name__) == 'Product':
                if productID == updateobject.prodName or productID == updateobject.prodID:
                    updateobject.prodStock = updateobject.prodStock - productStock

                else:
                    pass

p = Product()

class Bundle:
    #Bundle class to allow the customer to order a bundle and supports attributes such as ID, name, products, quantity

    def __init__(self, bID = None, bName = None, bProducts = None, bqty = 0, discount = 0.20):
        self.bID = bID
        self.bName = bName
        self.bProducts = bProducts
        self.bqty = bqty
        self.discount = discount

    def get_bID(self):
        return self.bID

    def get_bName(self):
        return self.bName

    def get_bProducts(self):
        return self.bProducts

    def get_discount(self, bundleproducts):
        pass

    def displayBundle(self):

        pstring = ','.join(self.bProducts)
        return "{:<3} {:<10} {:<7} {:<7}".format(self.bID,self.bName ,str(pstring),str(self.bqty))

    def updatebundlequantity(self, bID, bqty): #This method supports the quantity of the bundle to be changed/updated

        for updatebundleobject in r.list_products:
            if (type(updatebundleobject).__name__) == 'Bundle':
                if bID == updatebundleobject.bName or bID == updatebundleobject.bID:
                    updatebundleobject.bqty = int(updatebundleobject.bqty) - int(bqty)

                else:
                    pass


b = Bundle()

class Order:
    def __init__(self, name=None, product=None, quantity=None, date=datetime.now()):

        self.name = name
        self.product = product
        self.date = date
        self.quantity = quantity

    def set_name(self, name):
        self.name = name

    def set_product(self, product):
        self.product = product

    def set_quantity(self,quantity):
        self.quantity = quantity

    def get_name(self):
        return self.name

    def get_product(self):
        return self.product

    def get_quantity(self):
        return self.quantity

o = Order()

class Records:

    list_customers = [] #list of existing Customers
    list_products = [] #list of existing Products

    def read_customers(self):
        #read the comma-separated file called customers.txt and add the customers in this file to the customer list of the class
        try:
            file = open('customers.txt', 'r')
            for line in file.readlines():
                read_customer = line.strip().split(',')
                if (len(read_customer) > 3):
                    for i in range(1):
                        #creating objects for customer, memeber and vipmemeber class
                        c = Customer()
                        m = Member()
                        vip = VIPMember()

                        #reading and appending customer details into the list of customers
                        if read_customer[0][0] == 'C':
                            c.ID = read_customer[i].strip()
                            c.name = read_customer[i + 1].strip()
                            c.discount = float(read_customer[i + 2].strip())
                            c.value = read_customer[i + 3]
                            r.list_customers.append(c)
                        if read_customer[0][0] == 'M':
                            m.ID = read_customer[i].strip()
                            m.name = read_customer[i + 1].strip()
                            m.discount = float(read_customer[i + 2].strip())
                            m.value = read_customer[i + 3]
                            r.list_customers.append(m)
                        if read_customer[0][0] == 'V':
                            vip.ID = read_customer[i].strip()
                            vip.name = read_customer[i + 1].strip()
                            vip.discount = float(read_customer[i + 2].strip())
                            vip.value = read_customer[i + 3]
                            r.list_customers.append(vip)

                        else:
                            file.close()

        except IOError:
            print('file not found')

    def read_products(self):
        # read the comma-separated file called products.txt and add the products in this file to the products list of the class
        try:
            file = open('products.txt', 'r')

            for line in file.readlines():
                read_products = line.strip().split(',')
                # reading and appending product and bundle details into the list of products
                if (len(read_products) > 1):
                    if(read_products[0][0]=='P'):
                        for i in range(1):

                            p = Product()
                            p.prodID = read_products[i].strip()
                            p.prodName = read_products[i + 1].strip()
                            p.prodPrice = read_products[i + 2].strip()
                            p.prodStock = int(read_products[i + 3])
                            r.list_products.append(p)
                    else:
                        for i in range(1):
                            b = Bundle()
                            b.bID = read_products[i].strip()
                            b.bName = read_products[i+1].strip()
                            b.bProducts = read_products[2:-1]
                            b.bqty = read_products[-1]
                            r.list_products.append(b)
            file.close()
        except IOError:
            print('file not found')

    def customeridgeneration(self, type):
        # To generate a unique ID for a new customer and add to the existing customer list
        new = 0
        for x in range(len(r.list_customers)):
            id = r.list_customers[x].ID
            new = id[1:]
        return type + str(int(new) + 1)


    def find_customer(self):
        #To search through the list of customers and find out if the given customer exists or not
        global newcustomername
        global custnameorid
        cnt = 0

        custnameorid = input('Enter customer name or id \n')

        for obj_cust in r.list_customers:
            if custnameorid == obj_cust.name or custnameorid == obj_cust.ID:
                global customername
                customername = obj_cust.name
                return (obj_cust.ID, obj_cust.name, 0) #return ID, name and 0 for existing customer

            else:
                cnt+=1
                if cnt == len(r.list_customers):
                    global newcustomername
                    print('You are a new Customer!')
                    newcustomername = input('Welcome!, enter your name please \n')
                    return ("", newcustomername,1) #return empty ID (string), name and 1 for existing customer


    def find_product(self):
        #To search through the list of products and find out if the given product exists or not

        while True:
            global  prodnameorid
            prodnameorid = input('Please Enter a valid product name or id \n')
            for prodobjj in r.list_products:

                if (type(prodobjj).__name__) == 'Product': #If the product is a normal product

                    if prodnameorid == prodobjj.prodName or prodnameorid == prodobjj.prodID:

                        if int(prodobjj.prodStock) == 0:
                            print('BUT not enough quantity, try again')
                            break
                        if str(prodobjj.prodPrice) == '':
                            print('The price is invalid, try again')
                            break
                        if float(prodobjj.prodPrice) == 0:
                            print('The price is invalid, try again')
                            break

                        return prodobjj

                if (type(prodobjj).__name__) == 'Bundle': #If the product is a bundle

                    if prodnameorid == prodobjj.bName or prodnameorid == prodobjj.bID:

                        if int(prodobjj.bqty) == 0:
                            print('BUT not enough quantity, try again')
                            break

                        if len(prodobjj.bProducts) == 0:
                            print('BUT not enough quantity, try again')
                            break

                        return prodobjj
                else:
                    continue

    def listallcustomers(self): #To list all the existing customers on screen

        for name in r.list_customers:
            print(name.display_info())

    def listallproducts(self): #To list all the existing products on screen

        print()
        for x in r.list_products:
            if type(x).__name__ == 'Product':
                print(x.displayProduct())

            if type(x).__name__ == 'Bundle':
                print(x.displayBundle())

r = Records()

def adj_discount():

    #To adjust the discount value of the VIP members

    customer_id, customer_name, Flag = r.find_customer()
    if customer_id[0]=='V':
        while True:
            # To make sure the user is entering a valid value
            newdiscount = input('enter new discount \n')
            try:
                newdiscount = float(newdiscount)
                if newdiscount<0:
                    print('enter a valid discount value')
                    continue
                else:
                    vip.set_firstrate(newdiscount) #set_rate method from the VIP member class
                    vip.discount = float(newdiscount)
                    vip.discountextra = float(newdiscount+5)
                    break
            except ValueError:
                print('invalid value, please enter a decimal value for discount')

    else:
        print('Invalid Customer')


def adj_threshhold():

    #To adjust the threshold value of the VIP memebers
    while True:
        newthreshold = input('enter new threshold \n')
        try:
            #To make sure the user is entering a valid value
            newthreshold = float(newthreshold)
            if newthreshold < 0:
                print('enter a valid threshhold value')
                continue
            else:
                vip.set_threshold(newthreshold) #set_threshold method from the VIP member class
                vip.thresh = float(newthreshold)
                break
        except ValueError:
            print('enter a valid number for threshold')


def customerorderhistory():
    #To Display all the orders of a specific customer

    custnameorid = input('Enter customer name or id \n')
    for obj_cust in r.list_customers:
        if custnameorid == obj_cust.name or custnameorid == obj_cust.ID:
            global customername
            customername = obj_cust.name
            customerID = obj_cust.ID

    #Checks if the customer name or id is in the orders file and prints the same.
    with open("orders.txt") as openfile:
        for line in openfile:
            if customername in line:
                print(line)
            if customerID in line:
                print(line)

def mostvaluablecustomer():
    #To display the most valuable customer
    mostvalcust = {}
    for obj_cust in r.list_customers:
        if obj_cust.name or obj_cust.ID not in mostvalcust.keys():
            mostvalcust[obj_cust.name] = float(obj_cust.value)
        else:
            mostvalcust[obj_cust.name] += float(obj_cust.value)

    print(max(mostvalcust, key=mostvalcust.get))




class Operations:

    product_quantity = {} #Product name and Quantity of the products ordered
    mvp = {} #Most valuable product Dictionary
    file_customers = "customers.txt"
    file_products = "products.txt"

    if os.path.isfile(file_customers) and os.path.isfile(file_products): #Looks for both the files in the local directory

        r.read_customers()
        r.read_products()

    else: # Display error message if the file is not found
        if os.path.isfile(file_customers) == False:
            print("Customer File not exist")
        if os.path.isfile(file_products) == False:
            print("Products File not exist")
        exit()

    while True:
        #Display menu for the user
        print("Welcome to Easy Appliances Store")
        print('Choose from the following')
        print('--------------------------------------------------')
        print("1. Place an order \n"
              "2. Display existing customers \n"
              "3. Display existing products \n"
              "4. Adjust the discount rate of a VIP member \n"
              "5. Adjust the threshold rate of a VIP member \n"
              "6. Display all orders \n"
              "7. Display all orders of a specific customer \n"
              "8. Display the most valuable customer \n"
              "9. Display the most valuable product \n"
              "10. Summarize all the orders \n"
              "0. Exit the program \n")
        print('--------------------------------------------------')

        choice = input('enter your choice \n')
        if choice == '1':
            #Allowing the customer to make an order
            customer_id, customer_name, Flag = r.find_customer() #Flag variable to check if user exists or not
            netprice = 0
            while True:
                print('choose from the following \n')
                r.listallproducts()
                products = r.find_product()

                while True:
                    quantity = input('enter quantity of the chosen product \n')
                    try:
                        quantity = int(quantity)
                        if (type(products).__name__) == 'Product':
                            if (quantity > int(products.prodStock) or quantity == 0 or quantity < 0): #to check if user has entered a valid quantity for product
                                print('please enter a valid quantity for the product')
                                continue
                            else:
                                if products.prodName in product_quantity.keys() or products.prodID in product_quantity.keys():
                                    product_quantity[products.prodName][0] += quantity #updating the price and quantity of the product_quantity dictionary
                                    netprice = netprice + float(products.prodPrice) * quantity #Calculating the net price

                                    if str(products.prodName) in mvp.keys() or str(products.prodID) in mvp.keys():
                                        mvp[products.prodName]+=1 #updating most valuable product based on orders
                                    else:
                                        mvp[products.prodName]=1

                                else:
                                    product_quantity[products.prodName] = [quantity, products.prodPrice]
                                    netprice = netprice + float(products.prodPrice) * quantity #Calculating the net price

                                    if str(products.prodName) in mvp.keys() or str(products.prodID) in mvp.keys():
                                        mvp[products.prodName]+=1
                                    else:
                                        mvp[products.prodName]=1

                            p.updateproductquantity(products.prodID, quantity) #updating product quantity

                        if (type(products).__name__) == 'Bundle':
                            if(quantity > int(products.bqty)): #to check if user has entered a valid quantity for Bundle
                                print('pleaase enter valid quantity for product')
                                continue
                            if (len(products.bProducts)<1):
                                print('pleaase enter valid quantity for product')
                                continue
                            else:
                                #Calculating the individual cost of the bundle
                                cost = 0
                                bundlelist = products.bProducts
                                for product_id in bundlelist:
                                    for prodobj in r.list_products:
                                        if type(prodobj).__name__ == 'Product':
                                            if product_id.strip() == prodobj.prodID:
                                                cost = cost + float(prodobj.prodPrice)
                                        else:
                                            break

                                if products.bName in product_quantity.keys() or products.bID in product_quantity.keys():
                                    product_quantity[products.bName][0] += quantity #Updating the product and its respective quantity
                                    netprice = cost * quantity

                                    if str(products.bName) in mvp.keys() or str(products.bID) in mvp.keys():
                                        mvp[products.bName]+=1 #Most valuable product based on orders
                                    else:
                                        mvp[products.bName]=1

                                else:
                                    product_quantity[products.bName] = [quantity, cost]
                                    netprice = cost * quantity

                                    if str(products.bName) in mvp.keys() or str(products.bID) in mvp.keys():
                                        mvp[products.bName]+=1
                                    else:
                                        mvp[products.bName]=1

                            b.updatebundlequantity(products.bID, quantity) #updating bundle quantity

                        break

                    except ValueError:
                        print('enter a valid integer value')


                one_more = input('Do you want to continue shopping? enter y or n \n') #Asking the user whether they want to continue their shopping
                while one_more != 'y' and one_more != 'n':
                    one_more = input('please enter it correctly: y or n \n')
                if one_more == 'y':
                    continue
                else:

                    if Flag == 1: #For new user
                        print('VIP Membership costs 200$ and we do not charge you for a normal Membership')
                        memb_type = 'C'
                        while True: #Asking the new user whether they want to become a member
                            doyouwantamembership = input('So, would you like to become a member? (y/n) \n')
                            if doyouwantamembership == 'y' or doyouwantamembership == 'n':
                                break
                            else:
                                print('please enter only y or n')
                                continue

                        if (doyouwantamembership == 'y'):
                            while True: #Asking the user whether they want a normal membership or a VIP membership
                                memb_type = input('Enter membership type: V or M \n')
                                if memb_type == 'V' or memb_type == 'M':
                                    break
                                else:
                                    print('please enter either V or M')
                                    continue

                            if (memb_type == 'V' or memb_type == 'M'):
                                customer_id = r.customeridgeneration(memb_type)


                            else: #If the user did not opt for a membership

                                print('you have not selected a membership \n'
                                      'Would you like to proceed without a membership \n')
                                proceed = input('y or n')
                                if proceed == 'n':
                                    while True:
                                        memb_type = input('Enter membership type: V or M \n')
                                        if (memb_type == 'V' or memb_type == 'M'):
                                            customer_id = r.customeridgeneration(memb_type) #Generating new ID for customer - Member or VIP ID

                                else:
                                    customer_id = r.customeridgeneration(memb_type) #Generating new ID for Customer

                        elif (doyouwantamembership == 'n'):
                            customer_id = r.customeridgeneration(memb_type) #Generating new ID for customer - normal customer


                        #Reading and appending the details of the new customer to the list of customers
                        customertype = customer_id[0]
                        if customertype == 'C':
                            c1 = Customer()
                            customerdiscount, customerdiscountamount = c1.get_discount(netprice)
                            c1.name = customer_name
                            c1.ID = customer_id
                            c1.value = customerdiscountamount
                            c1.discount = float(customerdiscount/100)
                            r.list_customers.append(c1)


                        elif customertype == 'M':
                            m1 = Member()
                            customerdiscount, customerdiscountamount = m1.get_discount(netprice)
                            m1.name = customer_name
                            m1.ID = customer_id
                            m1.value = customerdiscountamount
                            m1.discount = float(customerdiscount/100)
                            r.list_customers.append(m1)


                        elif customertype == 'V':
                            v1 = VIPMember()
                            customerdiscount, customerdiscountamount = v1.get_discount(netprice)
                            v1.name = customer_name
                            v1.ID = customer_id
                            v1.value = customerdiscountamount + 200
                            v1.discount = float(customerdiscount/100)
                            r.list_customers.append(v1)



                    else:
                        #Updating the details of the existing customer to the list of customers
                        customertype = customer_id[0]
                        if customertype == 'C':

                            for obj_cust in r.list_customers:
                                if customer_name == obj_cust.name:
                                    c2 = Customer()
                                    customerdiscount, customerdiscountamount = c2.get_discount(netprice)
                                    obj_cust.value = float(obj_cust.value) + float(customerdiscountamount)
                            r.list_customers.append(obj_cust)

                        elif customertype == 'M':

                            for obj_cust in r.list_customers:
                                if customer_name == obj_cust.name:
                                    m2 = Member()
                                    customerdiscount, customerdiscountamount = m2.get_discount(netprice)
                                    obj_cust.value = float(obj_cust.value) + float(customerdiscountamount)
                            r.list_customers.append(obj_cust)

                        elif customertype == 'V':

                            for obj_cust in r.list_customers:
                                if customer_name == obj_cust.name:
                                    v2 = VIPMember()
                                    customerdiscount, customerdiscountamount = v2.get_discount(netprice)
                                    obj_cust.value = float(obj_cust.value) + float(customerdiscountamount)
                            r.list_customers.append(obj_cust)


                    file_orders = "orders.txt"
                    #Checking if the orders file exists, else throwing an error message
                    if os.path.isfile(file_orders):
                        file = open('orders.txt', 'a')
                        file.write(custnameorid + ", " + prodnameorid + ", " + str(quantity) + ", " + str(datetime.now()) + '\n') #Appending all the order details to the orders text file
                        file.close()

                    else:
                        if os.path.isfile(file_orders) == False:
                            print("Cannot load the order file. Run as if there is no order previously.")

                    #Printing the customer bill
                    print("-----------------------------------------------")
                    for name,qty in product_quantity.items():
                        print("{}   purchases   {}  *   {}".format(customer_name, qty[0], name))
                        print("Unit price         {} (AUD)".format(qty[1]))
                    if customertype == 'V' and Flag == 1:
                        print("VIP Membership \t        {}".format(200))
                        print("{} gets a discount of    {}%".format(customer_name, customerdiscount))
                        print("Total price      {} (AUD) \n\n".format(customerdiscountamount+200))
                    else:
                        print("{} gets a discount of    {}%".format(customer_name, customerdiscount))
                        print("Total price      {} (AUD) \n\n".format(customerdiscountamount))
                    print("-----------------------------------------------")
                    product_quantity.clear()
                    break

        if choice == '2': #To list all existing customers
            print(r.listallcustomers())

        if choice == '3': #To list all the existing products
            print(r.listallproducts())

        if choice == '4': # To adjust the discount value of the VIP member
            adj_discount()

        if choice == '5': #To adjust the threshold value of the VIP member
            adj_threshhold()

        if choice == '6': #To print all the orders
            a_file = open("orders.txt")
            lines = a_file.readlines()
            for line in lines:
                print(line)
            a_file.close()

        if choice == '7': #To print the orders of a specific customer
            customerorderhistory()

        if choice == '8': #To print the most valueable customer
            mostvaluablecustomer()

        if choice == '9': #To print the most valueable product based on orders

            print(max(mvp, key=mvp.get))

        if choice == '0': #To exit the program

            print('Thank you for shopping with us, hoping to see you soon!')
            exit()

op = Operations()

"""
------------Documentation:-------------- 
1. The code has be explained in a neat and succinct manner via comments. 



2. Requirements not met by the program: 
-> High distinction level was Challenging 
-> Summarizing all orders
-> Writing to the orders file when multiple orders
-> As the user places orders, the most valuable product gets calculated



3. analysis/discussion/reflection of the Program: 
-> High distinction level was very challenging 
-> Code quality is good, can be improved with more time
-> Modularity is good, can be improved with more time
-> Creating and raising exceptions can be implemented 

"""