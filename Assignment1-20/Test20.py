class car:

    def __init__(self, Owner, Company, Model_type, Model_name, Color, CC, Mileage, Cost):
        self.Owner = Owner
        self.Company = Company
        self.Model_type = Model_type
        self.Model_name = Model_name
        self.Color = Color
        self.CC = CC
        self.Mileage = Mileage
        self.Cost = Cost

user = car('Sivaram', 'Kia', 'Hatch Back' ,"Seltos", "Harbor grey", "1497","20 km/l", "19,50,000")
print("\n",user.Owner,"\n", user.Company, "\n", user.Model_type, "\n",user.Model_name,"\n", user.Color,"\n", user.CC,"\n", user.Mileage,"\n", user.Cost)        
