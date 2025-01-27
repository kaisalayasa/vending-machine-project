
total = 0
def yes_or_no():
    while True:  
        y_n_input = input("yes/no:").lower()
        
        if y_n_input not in ("yes", "no"): 
            print("Please answer with Yes or No.")
        elif y_n_input == "no":  
            print("Thank You!")
            return False
        elif y_n_input == "yes": 
            return True


    

    
    #---------------------

choices = {                                                  #items a use can chose from
    "A1": ("WATER", 1.50),            
    "A2": ("SODA", 2.00),              
    "A3": ("SUGAR FREE SODA", 1.80), 
     
      
    "B1": ("CHOCOLATEBAR", 1.20),     
    "B2": ("CHIPS", 1.00),            
    "B3": ("CANDY", 0.90),     
           
    "C1": ("SANDWICH", 3.50),         
    "C2": ("WRAP", 3.00),             
    "C3": ("SALAD", 2.50)             
}




choicelist = list(choices.items())                      #create a list with the items  (keys)

def pickitem():

    
    for i in range(0, len(choicelist), 3):
        print(f"{choicelist[i][1][0]:<20} ${choicelist[i][1][1]:<5}  {choicelist[i+1][1][0]:<20} ${choicelist[i+1][1][1]:<5}  {choicelist[i+2][1][0]:<20} ${choicelist[i+2][1][1]:<5}")
        print(f"{choicelist[i][0]:<27}  {choicelist[i+1][0]:<27}  {choicelist[i+2][0]:<27}")
    loopcon = True
    while loopcon:
        userpick = input("Please Chose An Item (A1,B1,C1...)").upper()

        if userpick in choices:                           #checks keys
            print(f'You Picked {choices[userpick][0]} for ${choices[userpick][1]}  . Confirm?(yes/no) ')
            conf_check =yes_or_no()                       #checks if user want to continue with the item
            if conf_check == True:
                confirmed_pick= choices[userpick][1]          
                return confirmed_pick
            else:                                          #If user does not confirm (no)
                print("Let's pick another item. ")           #Loop continues to let them pick another item
                
                
        else:
            print("Invalid Choice Please Pick From The Avaliable Items ")
            
        


def change(n):
    global total
    remaining_change = 0
    amount_needed = 0
    if n == total:
        print("thank you for shopping! ")
        exit() 
        
    elif n> total:
        remaining_change = round(n- total,3)
        print(f'please take the your change {remaining_change} from the box. Thank You For Shopping ')
        exit()
    elif n < 0:
        print("REALLY NEGITIVE MONEY?!. RESTART")
        exit()
        
    
    while n < total:
        amount_needed = round(total - n, 3)
        order_status = input(f'Please Insert The remaining ${amount_needed} or cancel Order ')   # either how much is lefr / cancel
        if order_status.lower() in ("cancel"):
            print("thank you for shopping! ")
            exit()              # to exit the whole program

        elif float(order_status) < 0:  
            print("REALLY NEGATIVE MONEY?! RESTART")
            exit()

        else:
            if float(order_status) == amount_needed:                        
                print("thank you for shopping! ")
                exit()
                
            
            else:
                while amount_needed > 0 and float(order_status) < amount_needed :
                    amount_needed = amount_needed - float(order_status)     
                    order_status = input(f'Please Insert The remaining ${amount_needed} or cancel Order ')
                    if order_status.lower() in ("cancel"):
                        print("thank you for shopping! ")
                        exit()  
                            
                    elif float(order_status) < 0:  
                        print("REALLY NEGATIVE MONEY?! RESTART")
                        exit()
                    
                    else:
                        if float(order_status) == amount_needed:                        
                            print("thank you for shopping! ")
                            exit()

                else: 
                    float(order_status) > amount_needed
                    remaining_change = float(order_status) - amount_needed
                    print(f'please take the your change {remaining_change} from the box. Thank You For Shopping ')
                    exit()
                





    
  

def start():
    global total
    print("Do You Want To Use This Machine? (Yes/No)")
    cont = yes_or_no()
    
    while cont:
        
        amount_from_fun = pickitem()                                          # returns amount
        total += amount_from_fun
        print("Do You Want To Continue Using The Machine? (yes/no)")
        user_cont =yes_or_no()
        if user_cont == False:
            print(f'Your Total Is ${total}. Please Insert ${total} Into The Machine ')
            change(float(input("pay for the goods! ")))
        

        
        
      




