name = input('What is your name: ')

days = 0
sum = 0

while True:
    answer = int(input('how many cups taken on day ' + str(days + 1) + ': '))
    
    if answer is -1:
        break
    else:
        sum = sum + answer
        days = days + 1


average = sum/ days
message = ''
if average < 5:
    message = 'Drink More'
elif average == 5:
    message = 'Good'
else:
    message = "You drank too much"

print('User: ' + name)
print('Days: ' + str(days))
print('Total # of cups: ' + str(sum) )
print('Average: ' + str(average))
print(message)