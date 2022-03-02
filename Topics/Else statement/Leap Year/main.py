# put your python code here
year_type = ''
year_to_test = int(input())
ONE_HUNDRED = 100
FOUR_HUNDRED = 400
if year_to_test % 4 == 0 and not(year_to_test % ONE_HUNDRED == 0):
    year_type = 'Leap'
else:
    if year_to_test % FOUR_HUNDRED == 0:
        year_type = 'Leap'
    else:
        year_type = 'Ordinary'
print(year_type)
