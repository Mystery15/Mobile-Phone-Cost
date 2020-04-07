from dataclasses import dataclass

@dataclass
class MobilePhoneCost:
    blue: int
    pink: int
    bluePhone: int = 20
    pinkPhone: int = 40

    @property
    def NoOfPhones(self):
        return(self.blue + self.pink)

    @property
    def TotalPrice(self):
        return((self.blue*self.bluePhone) + (self.pink*self.pinkPhone))

price = MobilePhoneCost(2, 5)

message = "Congratulations! You have purchased " + str(price.NoOfPhones) + " phones.\nPrice total: $" + str(price.TotalPrice)

print(message)
