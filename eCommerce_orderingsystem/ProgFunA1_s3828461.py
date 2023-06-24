l1_allcustomers = ['Drake','Derrik','Pranav'] #predefined list for all the customers
l2_members = ['Mike','Michael','Melody','Pranav'] #predefined list for the members
product_dict = {'table':100,'chair':50,'cutlery':40,'placemat':20} #store the list of items and price
mostValueCustomer = {'Mannur': 500, 'Jack': 200} #store the most valueable customer
option = 0 #variable stores user input action
dict_customer = {} #store customer details: product and quantity
order_history = {} #store the the customer order history

def valuecustomer(): #calculates most valueable customer
    for name in mostValueCustomer:
        mostValueCustomer[name] += final_amt

while True:
    # display Menu
    print("""    
        Welcome to MyStore
        1: Place an order
        2: Add/Update products and prices
        3: Display all existing customers
        4: Display all customers with membership
        5: Display all existing products with their prices
        6: Display the most valuable customer
        7: Display a customer order history
        0: Exit the program
        """)
    option = input("Choose an option between 1 and 7 or 0 to exit:\n")
    try: #user enters a valid option
        option = int(option)
        if (option >= 8 or option < 0):
            print('please enter a number between 1 and 7 or 0 to exit:\n')
            continue
    except ValueError:
        print("Please only enter a number\n")

    if option == 1:
        amt = 0
        cart = {} #store product and quantity (shopping cart)
        name = str(input('Hello there!, enter your name please \n'))

        if name not in l1_allcustomers:
            l1_allcustomers.append(name)
            mostValueCustomer[name] = 0 #initialising name with 0 expenditure to the most valueable customer record
        while True:
            while True:
                print('Choose from the following products') #user buying product
                for pro,pri in product_dict.items():
                    print(pro,pri)
                product = str(input('Enter the product name \n'))
                if product not in product_dict.keys():
                    print('Sorry invalid product')
                else:
                    break
            if product_dict[product] == 0: #checking product is valid
                print('Sorry invalid product')
                qty=0
            else:
                while True:

                    qty = int(input('enter the quantity \n')) #check for valid Quantity to be entered
                    if int(qty) <= 0:
                        print('Sorry invalid quantity')
                    else:
                        break
                if product not in product_dict.keys():
                    print('Sorry invalid product')

            one_more = input('Do you want to continue shopping? enter y or n \n') #user can choose to continue shopping
            while one_more != 'y' and one_more != 'n':
                one_more = input('please enter it correctly: y or n \n')
            if one_more == 'y':
                cart[product] = qty
                amt += qty * product_dict[product] #calculating initial amount before discount
                if name in dict_customer:
                    if product in dict_customer[name]: #updating customer dictionary
                        dict_customer[name][product] += qty
                    else:
                        dict_customer[name][product] = qty
                else:
                    dict_customer[name] = {product: qty}
            if one_more == 'n':
                print('user is done')
                break


        cart[product]=qty

        if name not in order_history.keys(): #update order history
            order_history[name] = []
        order_history[name].append(cart)
        amt += qty * product_dict[product]
        if name in dict_customer:
            dict_customer[name][product] = qty
        else:
            dict_customer[name] = {product: qty}

        while True:
            if name in l2_members: #output invoice
                for products in cart.keys():
                    print("{} purchases {} x {}. \n Unit price: {} (AUD)".format(name, cart[products], products,product_dict[products] * cart[products]))
                final_amt = amt - (amt * 0.05)
                print(name, 'gets a discount of 5% \n Total Price is', final_amt)
                valuecustomer()
                break

            if name not in l2_members: #output invoice
                l2_members.append(name)
                member_Q = str(input('Customer does not have a membership. Does the customer want to have a membership [enter y or n]? \n'))
                while member_Q != "y" and member_Q != "n": #handling wrong answer
                    member_Q = input('Please enter only y/n')
                for products in cart.keys():
                    print("{} purchases {} x {}. \n Unit price: {} (AUD)".format(name, cart[products], products,product_dict[products] * cart[products]))
                if member_Q == 'y': #apply discount to the initial amount calculated for members
                    final_amt = amt - (amt * 0.05)
                    print(name, 'gets a discount of 5% \n Total Price is',final_amt)
                    valuecustomer()
                    break
                if member_Q == 'n': #no discount for non-members
                    final_amt = amt
                    print(name, 'gets a discount of 0% \n Total Price is', final_amt)
                    valuecustomer()
                    break
                else:
                    continue

    if option == 2: #adding and updating the products and prices
        prod_update = str(input('Enter the products to update \n'))
        price_update = str(input('Enter the price of products \n'))
        prod_update_list = prod_update.split(',')
        price_update_list = price_update.split(',')

        for i in range(len(price_update_list)):
            if price_update_list[i] == '':
                price_update_list[i] = 0
        price_update_list = [int(x) for x in price_update_list]
        product_dict_updated = dict(zip(prod_update_list,price_update_list))
        product_dict.update(product_dict_updated)
        print(product_dict)

    if option == 3: #display all existing customers
        print(l1_allcustomers)

    if option == 4: #display all existing members
        print(l2_members)

    if option == 5: #display all existing products with their prices
        print(product_dict)

    if option == 6: #display the most valueable customer
        x = list(sorted(mostValueCustomer.items())[-1])
        print("The most valueable customer is {} with an expenditure of {}".format(x[0],x[1]))

    if option == 7: #to print the order history of the user
        name = input("Enter a customer name : ")
        while name not in l1_allcustomers: #handling valid customer name
            name = input("Enter an existing customer name :")
        for key1, prod in dict_customer.items():
            print(key1,prod)
            if name == key1:
                #displaying order history in the required format
                print("This is the order history of {} \n".format(name))
                print("           ", end='')
                if name in order_history.keys():

                    for product in product_dict.keys(): #product name
                        print(product + '\t', end='')

                    index = 1
                    print()
                    for purchase in order_history[name]: #purchase number
                        print('Purchase', index, '\t', end='')
                        for product in product_dict.keys(): #Quantity of products
                            if product in purchase.keys():
                                print(purchase[product], '\t\t', end='')
                            else:
                                print(0, '\t\t', end='')
                        print()
                        index += 1

    if option == 0: #user exits the application
        print('Thank you for shopping with us!')
        input("Press Enter to LogOut")
        exit()
