from cgitb import reset

arg = ''

menu = {
    1:"Enter 1 to view product list",
    2:'Enter 2 to add all product to the cart',
    3:'Enter 3 to remove a product from the cart',
    4:'Enter 4 to remove all products from the cart',
    5:'Enter 5 to view the cart',
    6:'Enter 6 to sort all products from the list',
    7:'Enter 7 to view the menu again',
    8:'Enter 8 to exit the program',
    }

productList = [
    {'id':11,'type':'Laptop','brand':'Asus'},
    {'id':12,'type':'Mobile','brand':'iPhone'},
    {'id':13,'type':'Mobile','brand':'Samsung'},
    {'id':14,'type':'Laptop','brand':'Mac'}
]

cart = productList

def getRequestUser(n):
    if int(n) == 1 :
        showProduct()
    elif int(n) == 2:
        cart = productList
        print(f"your cart = {cart}")
    elif int(n) == 3:
        deleteItemCart()
    elif int(n) == 4:
        cart = []
        print("Your cart is empty ...")      
    elif int(n) == 5:
        for item in cart:
            print(item)
    elif int(n) == 6:
        print('\nUnder Construction')
    elif int(n) == 7:
        showMenu()
    elif int(n) == 8:
        exit()
    else :
        print('\nThe value entered is incorrect!')
        showMenu()


def showProduct():
    for item in productList:
        print(item)
    print("\nWhat do you want to do? Add Product or View Menu. Please Enter A or M!") 
    requestUser =  input()
    if (requestUser == "A" or requestUser == "a"):
        print("-------------------------------------------------")
        addProcut()
    elif (requestUser == "M" or requestUser == "m"):
        print("-------------------------------------------------")        
        showMenu()
    else:
        print("\nInput is incorrect!")
        exit()    
           
def addProcut():
    print("\nHow many items do you need?")
    number = int(input())
    i= 0
    if number <= len(productList):
        while i < number: 
            print(f"\nEnter the product ID {i+1}!")
            Id = int(input())   
            searchList = [x for x in productList if x['id'] == Id]
            if searchList != [] :
                selectProduct = next(item for item in productList if item["id"] == Id)
                cart.append(selectProduct)
            i+=1
        showCart()
    else:
        print("Entered number is not allowed!")
        exit()

def showCart():
    for item in cart:
        print(item)

def deleteItemCart():
    showCart()
    print('\nWhich item do you want to remove from the cart? Enter its ID:')
    itemId = int(input())
    searchList = [x for x in cart if x['id'] == itemId]
    if searchList != [] :
        selectProduct = next(item for item in productList if item["id"] == itemId)
        cart.remove(selectProduct)
        showCart()

def showMenu():
    for key, value in menu.items():
        print(key, ' : ', value)
    print("Enter the desired menu number:")
    arg = int(input())
    getRequestUser(arg)

showMenu()
