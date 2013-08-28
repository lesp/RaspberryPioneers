def traffic():
    import datetime
    now = datetime.datetime.now()
    green = now.replace(hour=8, minute=30, second=0, microsecond=0)
    amber = now.replace(hour=8, minute=45, second=0, microsecond=0)
    red = now.replace(hour=9, minute=0, second=0, microsecond=0)
    if now <= green:
        print("You are on time, well done")
    elif now >= amber:
        print("You are running late")
    elif now >= red:
        print("You are very late")

while True:
    traffic()
else:
    print("Error")



                    
