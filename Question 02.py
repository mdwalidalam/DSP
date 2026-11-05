import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# Question 2(a): Exponential Signals Convolution
# ==========================================
a = 0.5
n = np.arange(0, 11)  # n from 0 to 10

x_a = a ** n
h_a = a ** n

# Convolve and truncate to n = 0 to 10
y_a = np.convolve(x_a, h_a)[:11]

# Display Output Table
print("--- Question 2(a) Output Table ---")
print("n\tx[n]\th[n]\ty[n]")
print("-" * 32)
for i in range(11):
    print(f"{n[i]}\t{x_a[i]:.4f}\t{h_a[i]:.4f}\t{y_a[i]:.6f}")

# Stem Plots for 2(a)
plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.stem(n, x_a, linefmt='b-', markerfmt='bo')
plt.title('Input Signal x[n] = (0.5)^n u[n]')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.stem(n, h_a, linefmt='g-', markerfmt='go')
plt.title('Impulse Response h[n] = (0.5)^n u[n]')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.stem(n, y_a, linefmt='r-', markerfmt='ro')
plt.title('Output Signal y[n] = x[n] * h[n]')
plt.grid(True)

plt.tight_layout()
plt.show()

# ==========================================
# Question 2(b): Manual Nested Loops Convolution
# ==========================================
def manual_convolution(x, h):
    Nx = len(x)
    Nh = len(h)
    Ny = Nx + Nh - 1
    y = np.zeros(Ny)
    
    for n_idx in range(Ny):
        for k in range(Nx):
            if 0 <= (n_idx - k) < Nh:
                y[n_idx] += x[k] * h[n_idx - k]
    return y

# ==========================================
# Question 2(c): Convolution of [1,2,3] and [1,1,1]
# ==========================================
x_c = np.array([1, 2, 3])
h_c = np.array([1, 1, 1])

y_builtin = np.convolve(x_c, h_c)
y_manual = manual_convolution(x_c, h_c)

print("\n--- Question 2(b) & (c) Results ---")
print(f"Built-in np.convolve result : {y_builtin}")
print(f"Manual nested loop result   : {y_manual.astype(int)}")

# ==========================================
# Question 2(d): Step-by-Step Manual Display
# ==========================================
print("\n--- Question 2(d) Step-by-Step Calculations ---")
Nx = len(x_c)
Nh = len(h_c)
Ny = Nx + Nh - 1

for n_idx in range(Ny):
    terms = []
    val = 0
    for k in range(Nx):
        if 0 <= (n_idx - k) < Nh:
            terms.append(f"({x_c[k]} * {h_c[n_idx - k]})")
            val += x_c[k] * h_c[n_idx - k]
    calculation_str = " + ".join(terms)
    print(f"y[{n_idx}] = {calculation_str} = {val}")