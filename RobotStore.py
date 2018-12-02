class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity # how many are in stock

    def isAvailable(self, count):
        #  takes an integer count and determines whether that many of the product are in stock.
        return count <= self.quantity


    def purchaseCost(self, count):
        # takes a count and returns the total cost of that many of the product
        return count * self.price

    def removeStock(self, count):
        # takes a count and removes that many of the product from the stock.
        self.quantity = self.quantity - count


products = [Product("Ultrasonic range finder", 2.50, 4),
            Product("Servo motor", 14.99, 10),
            Product("Servo controller", 44.95, 5),
            Product("Microcontroller Board", 34.95, 7),
            Product("Laser range finder", 149.99, 2),
            Product("Lithium polymer battery", 8.99, 8)]


def printStock():
    print()
    print("Available Products")
    print("------------------")
    for i in range(0, len(products)):
        if products[i].quantity > 0:
            print(str(i)+")", products[i].name, "$", products[i].price)
    print()


def main():
    cash = float(input("How much money do you have? $"))
    while cash > 0:
        printStock()

        vals = input("Enter product ID and quantity you wish to buy: ").split(" ")

        if vals[0] == "quit":
                break

        prodId = int(vals[0])
        count = int(vals[1])

        product = products[prodId]

        if product.isAvailable(count):
            if product.purchaseCost(count) <= cash:
                product.removeStock(count)
                print("You purchased", count, product.name + ".")
                cash -= product.price * count
                print("You have $", "{0:.2f}".format(cash), "remaining.")
            else:
                print("Sorry, you cannot afford that product.")
        else:
            print("Sorry, we do not have that many", product.name)


main()