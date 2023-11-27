#tip calculator app
food_amount = float(input('enter the food amount $: '))
tip_percentage = float(input('enter the tip amount $: '))/ 100
tip_amount = food_amount * tip_percentage

total = food_amount + tip_amount
print('$' + str(total))
 