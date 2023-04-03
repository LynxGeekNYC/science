import matplotlib.pyplot as plt

# r = (2 * G * M) / c^2 - The equation that calculates the minimum mass required to form a black hole is known as the Schwarzschild radius equation. It gives the radius of a non-rotating black hole as a function of its mass:
# Define constants
G = 6.67430e-11  # gravitational constant in m^3/kg*s^2
c = 299792458  # speed of light in m/s

# Define function to calculate Schwarzschild radius
def schwarzschild_radius(mass):
    radius = (2 * G * mass) / (c**2)
    return radius

# Define masses to compare
earth_mass = 5.972e24  # mass of the Earth in kg
sun_mass = 1.989e30  # mass of the Sun in kg
black_hole_masses = [0.1 * sun_mass, sun_mass, 10 * sun_mass, 100 * sun_mass, 1000 * sun_mass, 1e7 * sun_mass, 1e8 * sun_mass]
labels = ['0.1 M\u2609', '1 M\u2609', '10 M\u2609', '100 M\u2609', '1000 M\u2609', '10,000,000 M\u2609', '100,000,000 M\u2609']

# Calculate Schwarzschild radii
radii = [schwarzschild_radius(m) for m in black_hole_masses]

# Plot results
plt.plot(black_hole_masses, radii, 'bo-', markersize=8)
plt.plot([earth_mass, sun_mass], [schwarzschild_radius(earth_mass), schwarzschild_radius(sun_mass)], 'ro', markersize=10)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Mass (kg)')
plt.ylabel('Schwarzschild radius (m)')
plt.title('Schwarzschild Radii of Different Masses')
plt.grid(True, which='both')
plt.annotate('Earth', xy=(earth_mass, schwarzschild_radius(earth_mass)), xytext=(earth_mass/10, schwarzschild_radius(earth_mass)*10),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12)
plt.annotate('Sun', xy=(sun_mass, schwarzschild_radius(sun_mass)), xytext=(sun_mass/2, schwarzschild_radius(sun_mass)/10),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12)
for i in range(len(black_hole_masses)):
    plt.annotate(labels[i], xy=(black_hole_masses[i], radii[i]), xytext=(black_hole_masses[i], radii[i]*2),
                 ha='center', fontsize=12)
plt.show()
