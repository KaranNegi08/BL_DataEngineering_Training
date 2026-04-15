import random

class CouponNumbers:
    def __init__(self, coupon_number):
        self.coupon_number= coupon_number
        self.count=0
        self.coupons= set()
    
    def generate_coupons(self):
        while len(self.coupons) < self.coupon_number:
            number= random.randint(1,self.coupon_number)
            self.count += 1

            if number not in self.coupons:
                self.coupons.add(number)
            else:
                continue
        
        print(f"Total random numbers generated to get {self.coupon_number} distinct coupons: {self.count} ")


coupon_number= int(input("Enter the number of coupons you want: "))
coupon_obj= CouponNumbers(coupon_number)
coupon_obj.generate_coupons()