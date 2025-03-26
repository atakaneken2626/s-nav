
def main():
    phone = input("enter phone number")
    
    phone_number = convert(phone)
    
    print(phone_number)
    
def convert(phone_string):
    
    phone_dict = {2:('A','B','C'),3:('D','E','F'),
                  4:('G','H','I'),5:('J','K','L'),
                  6:('M','N','O'),7:('P','Q','R','S'),
                  8:('T','U','V'),9:('W','X','Y','Z')}
    
    phone_number = phone_string[0: 4] # 555-
    first_part = phone_string[4: 7] #GET
    second_part = phone_string[8:] #FOOD
    
    for c in first_part:
        for key,value in phone_dict.items():
            if c in value:
                print(key)
                phone_number+=str(key)
                
    phone_number+='-'
    
    for c in second_part:
        for key,value in phone_dict.items():
            if c in value:
                print(key)
                phone_number+=str(key)
                
    return phone_number

main()