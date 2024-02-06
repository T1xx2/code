import numpy as np

# Define evaluation criteria
criteria = ['Y1', 'Y2', 'Y3', 'Y4']

# Define the judgment matrix
matrix = np.array([
    [1, 2, 3, 5],
    [1/2, 1, 2, 3],
    [1/3, 1/2, 1, 2],
    [1/5, 1/3, 1/2, 1]
])

# Values of Random Index (RI)
RI = [0, 0, 0.58, 0.9, 1.12, 1.24, 1.32, 1.41, 1.45, 1.49]

# Function for consistency check
def consistency_check(matrix):
    # Calculate the eigenvalues and eigenvectors of the matrix
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    # Get the maximum eigenvalue
    max_eigenvalue = max(eigenvalues)
    # Dimension of the matrix
    n = len(matrix)
    # Calculate Consistency Index (CI)
    ci = (max_eigenvalue - n) / (n - 1)
    # Calculate Consistency Ratio (CR)
    cr = ci / RI[n - 1]

    # Check consistency based on CR value
    if cr < 0.1:
        print("Consistency check passed, CR =", round(cr, 2))
    else:
        print("Consistency check failed, CR =", round(cr, 2))

# Function to calculate weights
def calculate_weights(matrix):
    # Calculate the eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    # Find the index corresponding to the maximum eigenvalue
    max_eigenvalue = max(eigenvalues)
    index = np.argmax(eigenvalues)
    # Extract the corresponding eigenvector and normalize it to obtain weights
    weights = eigenvectors[:, index].real
    weights /= weights.sum()

    return weights

# Perform consistency check
consistency_check(matrix)
# Calculate and print weights
weights = calculate_weights(matrix)

for i in range(len(criteria)):
    print(criteria[i], "weight:", round(weights[i], 3))



#This step is the first time to calculate the weights of the four evaluation factors in the historical and cultural value, and then the community leader gives each evaluation factor a score. The score is multiplied by the corresponding weight to obtain the score of the historical and cultural value. And so on, calculate four times to get four scores. Then multiply these four scores by the weights corresponding to the four criteria to obtain the total score, which is the building protection score.
