# Class  to register workers
class Registration:
    def __init__(self):
      self.name = str(input("Enter your name : "))
      self.pin = str(input("Enter your pin : "))
      self.phoneNum = str(input("Enter your phone number : "))
      self.accountBal = int(input("Enter your account balance : "))
      print("Registration successful!") 

userRegister = Registration()          

# Class Deposit inherits class Registration
class Deposit:
   def __init__(self,objectRegistration):
    self.userRegister = objectRegistration
    
    self.deposit = int(input("Enter amount to deposit : "))
    self.pin = str(input("Enter your pin : "))

    if self.pin == self.userRegister.pin :
     
      self.userRegister.accountBal += self.deposit
      print("Deposit successful!")
      print("Your have deposited Ksh", self.deposit," to your account. Your account balance is Ksh" , self.userRegister.accountBal)

    else:
      print("Invalid Pin input")
      print("Deposit not successful!")

Deposit(userRegister)  

class SendMoney:
  def __init__(self,objectRegistration):
    self.userRegister = objectRegistration

    self.receiversContact = str(input("Enter receiver's contact : "))
    self.amountToSend = int(input("Enter amount to send : "))
    self.pin = str(input("Enter your pin : "))

    if self.pin == self.userRegister.pin and self.userRegister.phoneNum != self.receiversContact and self.userRegister.accountBal > self.amountToSend:
      self.userRegister.accountBal -= self.amountToSend
      print("Transaction successful!")
      print("You have sent Ksh ",self.amountToSend,"to account number ",self.receiversContact,".Your account balance is Ksh",self.userRegister.accountBal)
    else:
      print("Transaction unsuccessful!")
      print("Please verify your pin and check your account balance.") 

SendMoney(userRegister)      

   
         
    



          
       


