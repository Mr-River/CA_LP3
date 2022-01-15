weight = 20
# Ground Shipping
cost = 0
ground_flat_rate = 20.00

print("Shipping Rates:")

if weight <= 2:
  cost = weight * 1.50 + ground_flat_rate
elif weight <= 6:
  cost = weight * 3.00 + ground_flat_rate
elif weight <= 10:
  cost = weight * 4.00 + ground_flat_rate
else:
  cost = weight * 4.75 + ground_flat_rate

print("Ground:            ", cost)

# Premium Shipping
premium_rate = 120.00
print("Premium Flat Rate: ",premium_rate)

# Drone Shipping
warning = "This package exceeds the drone's weight limit and cannot be shipped via this method. We apologize for any inconenience."
if weight <= 2:
  cost = 4.50 * weight
elif weight <= 6:
  cost = 9.00 * weight
elif weight <= 10:
  cost = 12.00 * weight
else:
  cost = 14.25 * weight

if weight >= 50:
  print("Drone: ", warning)
else:
  print("Drone:             ", cost)
