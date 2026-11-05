import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# Question 1(a): Sampling & Aliasing
# ==========================================
# xa(t) = 3 * cos(100 * pi * t) -> Analog frequency f = 50 Hz
f_analog = 50 
t_continuous = np.linspace(0, 0.05, 1000)
xa_continuous = 3 * np.cos(2 * np.pi * f_analog * t_continuous)

sampling_rates = [400, 100, 60]

plt.figure(figsize=(12, 8))

for idx, fs in enumerate(sampling_rates, 1):
    # Sampled time vectors
    t_sampled = np.arange(0, 0.05, 1 / fs)
    xa_sampled = 3 * np.cos(2 * np.pi * f_analog * t_sampled)
    
    plt.subplot(3, 1, idx)
    plt.plot(t_continuous, xa_continuous, label='Original Continuous Signal (50 Hz)', color='lightblue', linestyle='--')
    plt.stem(t_sampled, xa_sampled, linefmt='r-', markerfmt='ro', basefmt='k-', label=f'Sampled Signal (fs = {fs} Hz)')
    plt.title(f'Sampling at fs = {fs} Hz')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.legend(loc='upper right')
    plt.grid(True)

plt.tight_layout()
plt.show()

# ==========================================
# Question 1(b): Nyquist Rate Determination
# ==========================================
# xa(t) = 3*cos(2000*pi*t) + 5*sin(6000*pi*t) + 10*cos(12000*pi*t)
f1 = 2000 / 2  # 1000 Hz
f2 = 6000 / 2  # 3000 Hz
f3 = 12000 / 2 # 6000 Hz

f_max = max(f1, f2, f3)
nyquist_rate = 2 * f_max
fs_given = 15000

print(f"--- Question 1(b) Results ---")
print(f"Component Frequencies: {f1} Hz, {f2} Hz, {f3} Hz")
print(f"Maximum Frequency (f_max): {f_max} Hz")
print(f"Nyquist Rate: {nyquist_rate} Hz")

if fs_given >= nyquist_rate:
    print(f"At fs = {fs_given} Hz: No aliasing occurs because fs >= Nyquist Rate.")
else:
    print(f"At fs = {fs_given} Hz: Aliasing occurs because fs < Nyquist Rate.")