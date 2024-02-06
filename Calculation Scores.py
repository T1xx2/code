#The code for calculating scores is as follows (example values are based on data from St. Mark's Square)



import numpy as np

# Example scores for each standard (modify based on actual values)
standard_1 = 9.242
standard_2 = 8.714
standard_3 = 8.547
standard_4 = 5.431

# Assume there are 4 standards
building_standards = np.array([standard_1, standard_2, standard_3, standard_4])

# Array of importance weights for each standard (fill in calculated weights)
building_weights = np.array([0.483, 0.272, 0.157, 0.088])

# Calculate the protection value of the building
building_protection_value = np.dot(building_weights, building_standards)

print("The protection value of the building is:", building_protection_value)

# Print the protection values for each building
for i, value in enumerate(building_protection_value):
    print(f"Building {i + 1} Protection Value: {value}")
