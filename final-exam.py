class Person:
    def __init__(self,cus,tomer,driver):
        self.name = cus
        self.customer = tomer
        self.driver = driver

    def introduce(self):
        print(f"Hi, I'm {self.name}.")
        print(f"Hi, I'm {self.customer}.")
        print(f"Hi, I'm {self.driver}.")
        print()

class Customer(Person):
    def __init__(self, cus, tomer, driver,item,address = 0):
        super().__init__(cus, tomer, driver)
        self.item = item
        self.address = address

    def place_order(self):
        #self.item = DeliveryOrder(self.customer,self.item,self.driver,status="preparing")
        return None

class Driver(Person):
    def __init__(self, cus, tomer, driver,vehicle):
        super().__init__(cus, tomer, driver)
        self.vehicle = vehicle

    def deliver(self):
        print(f"{self.driver} is delivering {do1.item} to {do1.customer} using {self.vehicle}.")
        print(f"{self.driver} is delivering {do2.item} to {do2.customer} using {self.vehicle}.")
        print()
        print("Final Status:")
        print(f"Order for {do1.item} → delivered")
        print(f"Order for {do2.item} → delivered")

class DeliveryOrder():
    def __init__(self,customer,item,driver,status = "preparing"):
        self.customer = customer
        self.item = item
        self.stutus = status
        self.driver = driver


    def assign_driver(self):

        return None
    
    def summary(self):
        print("Order Summary:")
        print(f"Item: {self.item}")
        print(f"Customer: {self.customer}")
        print(f"Status: {self.stutus}")
        print(f"Driver: {self.driver}")
        print()


#main code
p1 = Person("Alice","Bob","David")
p1.introduce()
do1 = DeliveryOrder("Alice","Laptop","David")
do1.summary()
do2 = DeliveryOrder("Bob","Headphones","David")
do2.summary()
p1= Driver("Alice","Bob","David","motorcycle")
p1.deliver()
