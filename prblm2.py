meal_cost = float(input())

tip_percent = int(input())

tax_percent = int(input())
total_cost=0
meal_cost=float(meal_cost)
tip=meal_cost*(tip_percent/100)
tax=meal_cost*(tax_percent/100)
total_cost=meal_cost+tip+tax
print(tip,tax,total_cost)
print(int(total_cost))
