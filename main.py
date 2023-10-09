##################### Hard Starting Project ######################
import smtplib
import datetime as dt
import pandas
import random

# getting the day
now = dt.datetime.now()
day = now.day
month = now.month

# Setting up the smtp

my_email = "onehundreddaysofcode86@gmail.com"
password = "mfyyedxmejkjecuy"

# turning csv file into dictionary

df = pandas.read_csv("birthdays.csv")

birthday_dict = df.to_dict(orient="records")

# turning the txt files int a list:


with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as file:
    letter = file.read()

print(letter)

# sending the email

for person in birthday_dict:
    if person["day"] == day and person["month"] == month:
        NAME = person["name"]
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=f"{person['email']}",
                                msg=f"Subject: Happy Birthday {NAME}\n\n"
                                    f"{letter.replace('[NAME]', NAME)}")


# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



