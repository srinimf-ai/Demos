from datetime import date

# Take today's date
today = date.today()

# Input: birth date
birth_year = 1999
birth_month = 6
birth_day = 15

# Create date object for birth
birth_date = date(birth_year, birth_month, birth_day)

# Calculate age
age = today.year - birth_date.year

# If birthday hasn't occurred yet this year, reduce by 1
if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1

print("Age is:", age)