import math

# Precompute the angles for each iteration
# These are the angles corresponding to arctan(2^-i)
angles = [math.atan(1 / 2**i) for i in range(30)]

def cordic(theta, iterations=30):
    # Initialize the vector (1, 0) and angle 0
    x = 1.0
    y = 0.0
    z = theta

    # Iterate through the precomputed angles
    for i in range(iterations):
        # Determine the direction of rotation (either clockwise or counter-clockwise)
        if z < 0:
            d = -1
            z += angles[i]
        else:
            d = 1
            z -= angles[i]

        # Apply the rotation
        x_new = x - d * y * 2**-i
        y = y + d * x * 2**-i
        x = x_new

    # Return the results for sine and cosine
    return x, y  # x is cosine, y is sine

# Example usage:
theta = math.pi / 4  # 45 degrees
cosine, sine = cordic(theta)
print(f"cos({theta}) = {cosine}, sin({theta}) = {sine}")
