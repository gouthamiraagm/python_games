import calendar
def check_leap(y):
    if y%100==0: #for centuary year
        if y%400==0:
            return True
        else:
            return False
    else:
        if y%4==0: #for normal years
            return True
        else:
            return False
def check_valid_date(dt,m,y,l):
    if l:
        if m==2:
            if dt<30:
                return True
            else:
                return False
        else:  
            if m<8:
                if m%2==1:
                    if dt<32:
                        return True
                    else:
                        return False 
                else:
                    if dt<31:
                        return True
                    else:
                        return False
            else:
                if m%2==0:
                    if dt<32:
                        return True
                    else:
                        return False 
                else:
                    if dt<31:
                        return True
                    else:
                        return False
    else:
        if m==2:
            if dt<29:
                return True
            else:
                return False
        else:  
            if m<8:
                if m%2==1:
                    if dt<32:
                        return True
                    else:
                        return False 
                else:
                    if dt<31:
                        return True
                    else:
                        return False
            else:
                if m%2==0:
                    if dt<32:
                        return True
                    else:
                        return False 
                else:
                    if dt<31:
                        return True
                    else:
                        return False
def get_day(day_index):
    list_of_days=['monday','tuesday','wednesday','thursady','friday','saturday','sunday']
    return list_of_days[day_index]
    
            
while(1):#true
    year=int(input("enter year 1970-2020"))
    if year<1970:
        print("enter a valid year(1970-2020)")
    else:
        break
while(1):#true
    month=int(input("enter month 1-12"))
    if month<=12 and month>0:
        break
    else:
        print("enter a valid month(1-12)")

leap=check_leap(year)   

while(1):#true
    date=int(input("enter date"))
    if date>0 and check_valid_date(date,month,year,leap):
        break
    else:
         print("enter a valid date")
         
day_index=calendar.weekday(year,month,date)
day=get_day(day_index)

print(date,"/",month,"/",year,"falls on ",day)

