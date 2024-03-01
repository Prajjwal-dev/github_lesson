print("Welcome to my Calculator app")
first = input("Enter the first number: ")
operator = input("Enter the operator(+/-/*///%/^)")
second = input("Enter the second number: ")
if (operator == "+"):
    sum = int(first) + int(second)
    print("The sum of two numbers is ",sum)
elif (operator == "-"):
    difference=int(first)-int(second)
    print("The difference of two numbers is ",difference)
elif (operator=="*") :
    product=int(first)*int(second)
    print ("The product of two numbers is " ,product )
elif (operator=="/") :
    quotient=(float)(first)/((float)(second))
    print('The Quotient of two numbers is ',quotient)
elif (operator=="%") :
    modulus=int(first)%int(second)
    print ('The modulus of two numbers is',modulus)
elif(operator=="^") :
    power=int(first)**int(second)
    print("The Power of two numbers is ",power)
   # power=pow(((float)(first)), ((float)(second)))
else :
    print("Invalid Operator")
print("Thank you for using calculator")
     

    