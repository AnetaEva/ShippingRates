# 2.0 pounds or less = $1.50
# over 2 pounds (which is 2.1 or higher) but not more than 6 (which is 6.0 or lower) = $3.00
# over 6 pounds (which is 6.1 or higher) but not more than 10(which is 9.9 or lower) = $4.00
# over 10 pounds (which is 10.0 or higher) = $4.75

weight = float(input('Enter package weight in pounds: '))

if weight < 0:
    print('Invalid input value!')
else:
    if weight >= 10:
        shipping_price = '$4.75'
    else:
        if weight >= 6.1:
            shipping_price = '$4.00'
        else:
            if weight >= 2.1:
                shipping_price = '$3.00'
            else:
                shipping_price = '$1.50'

    print('Shipping charge:', shipping_price)

# using elif
if weight < 0:
    print('Invalid input value!')
else:
    if weight >= 10:
        shipping_price = '$4.75'
    elif weight >= 6.1:
        shipping_price = '$4.00'
    elif weight >= 2.1:
        shipping_price = '$3.00'
    else:
        shipping_price = '$1.50'
    print('Shipping charge:', shipping_price)

# in order using if, and
if weight < 0:
    print('Invalid input value!')
else:
    if weight > 10:
        shipping_price = '$4.75'
    if weight < 10 and weight >= 6.1:
        shipping_price = '$4.00'
    if weight < 6.0 and weight >= 2.1:
        shipping_price = '$3.00'
    if weight < 2.0:
        shipping_price = '$1.50'
    print('Shipping charge:', shipping_price)
