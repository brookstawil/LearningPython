#8/6/14
#read in pairs of data(Jilian date. temperature), check it for validity
#keep reading in until user says stop

total = 0.0
counter = 0

tot_temp = [0] * 366
count_slips = [0] * 366

user_date = input('Type in a Julian date or STOP ')

while(user_date.upper() != 'STOP'):
    #reads in and checks down the date
    user_date = int(user_date)
    if (user_date < 1 or user_date > 365):
        print('Bad date on input, retype')

    #reads and checks in the temperature
    else:
        temp = float(input('Now type in the temperature: '))
        if (temp < -70 or temp > 150):
            print('temperature out of range, retype')
        else:
            print('Day',user_date,'was',temp,'degrees farenheit')
            counter += 1
            total += temp
            tot_temp[user_date] += temp
            count_slips[user_date] += 1
    
    user_date = input('Type in a Julian date or STOP ')

if counter > 0 :
    avg = total/counter
    print('The average daily temperature was',avg,'degrees farenheit.')

average_hottest = -999
average_coldest = 999

for num in range(1,366):
    if count_slips[num] > 0:
        average_temp[num] = tot_temp[num]/count_slips[num]
        print('The average for day',num,'was',average_temp[num],'for',count_slips[num],'slips of paper')

        if average_temp[num] > average_hottest:
            average_hottest = average_temp[num]

        if average_temp[num] < average_coldest:
             average_coldest = average_temp[num]

print('The hottest average was',average_hottest)
print('The coldest average was',average_coldest)






        
