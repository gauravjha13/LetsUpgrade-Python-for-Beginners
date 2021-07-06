# ASSIGNMENT-4
# You all are pilots, you have to land a plane, the altitude required for landing a plane is 1000ft, if it is less than that tell pilot to land the plane, or it is more than that but less than 5000ft ask the pilot to “come down to 1000ft”, else if it is more than 5000ft ask the pilot to “go around and try later.”
# Example : Input - 1000 Output - Safe to land
# Example : Input - 4500 Output - Bring down to 1000
# Example : Input - 6500 Output - Turn Around

"""# ASSIGNMENT-4
# You all are pilots, you have to land a plane, the altitude required for landing a plane is 1000ft, if it is less than that tell pilot to land the plane, or it is more than that but less than 5000ft ask the pilot to “come down to 1000ft”, else if it is more than 5000ft ask the pilot to “go around and try later.”
# Example : Input - 1000 Output - Safe to land
# Example : Input - 4500 Output - Bring down to 1000
# Example : Input - 6500 Output - Turn Around
"""

#Landing a plane

altitude = int(input("Enter the altitude\n"))

if altitude <= 1000:
  print("Safe to land")
elif altitude > 1000 and altitude <= 5000:
  print("Bring down to 1000")
else:
  print("Turn Around")