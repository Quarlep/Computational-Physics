# Exercise 2.1 : Another ball dropped from a tower

g = 9.81  # in m/s^2
h = float(input("Enter the height of the tower: "))
t = (2 * h / g) ** (1 / 2)
print("The time it takes until the ball hits the ground:", "%0.3f" % t, "second")
