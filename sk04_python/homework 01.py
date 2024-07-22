print("Hello,World")
name = input("Моля, въведете вашето име: ")
age = input("Моля, въведете вашите години: ")
favorite_color = input("Моля, въведете вашия предпочитан цвят: ")
birth_year = int(input("What year were you born in?"))
current_age = 2024 - birth_year
output = "You are " + str(current_age) + " years old."
# output = f"You are {str(current_age)} years old."  # f-string, we will discuss them later
print(output)