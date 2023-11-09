def pay_calculation(num_of_hours, normal_pay):
    if (num_of_hours > 1) and (num_of_hours < 60):
        if num_of_hours > 37.5:
            new_pay = 12 * 1.5 * num_of_hours
            return(new_pay)
        else:
            new_pay = 12 * num_of_hours
            return(new_pay)
    else:
        return("Invalid Input. Number of hours must be over 1 and under 60")

num_of_hours = float(input("Enter the number of hours you work per week:\n"))
normal_pay = 12
print(pay_calculation(num_of_hours, normal_pay))
