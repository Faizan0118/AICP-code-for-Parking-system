#!/usr/bin/env python
# coding: utf-8

# In[31]:


import datetime

# Initialize daily total payment and user data dictionary
daily_total = 0
user_data = {}

# Function to calculate parking price
def calculate_price(day, arrival_time, hours, frequent_parker_number):
    if day == 'Sunday':
        max_hours = 8
    elif day == 'Saturday':
        max_hours = 4
    elif day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
        max_hours = 2
    else:
        print("Invalid day.")
        return

    if hours > max_hours:
        print(f"Maximum parking hours allowed on {day} is {max_hours}.")
        return None

    if day == 'Sunday':
        if 8 <= arrival_time < 16:
            price_per_hour = 2
        else:
            price_per_hour = 2
    elif day == 'Saturday':
        if 8 <= arrival_time < 16:
            price_per_hour = 3
        else:
            price_per_hour = 2
    elif day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
        if 8 <= arrival_time < 16:
            price_per_hour = 10
        else:
            price_per_hour = 2
    else:
        print("Invalid day.")
        return

    discount = 0
    if frequent_parker_number == "FREQUENT123":
        discount = 0.10  # 10% discount

    total_price = price_per_hour * hours * (1 - discount)

    return total_price

now = datetime.datetime.now()
hour = now.hour

while True:
    if 0 <= hour < 8:
        print("Parking is not allowed between midnight and 08:00.")
    else:
        user_id = input("Enter user ID (or press Enter to finish): ")
        if not user_id:
            break
        day = input("Enter the day: ")
        hours = int(input("Enter the number of hours: "))
        frequent_parker_number = input("Enter frequent parking number (or leave blank): ")

        price = calculate_price(day, hour, hours, frequent_parker_number)
        if price is not None:
            daily_total += price
            print(f"Total amount to pay: ${price:.2f}")

        user_data[user_id] = {"day": day, "hours": hours, "frequent_parker_number": frequent_parker_number, "total_price": price}

    print(f"Daily Total Payment: ${daily_total:.2f}")

print("User Data:")
for user_id, data in user_data.items():
    print(f"User ID: {user_id}, Day: {data['day']}, Hours: {data['hours']}, Frequent Parker: {data['frequent_parker_number']}, Total Price: ${data['total_price']:.2f}")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




