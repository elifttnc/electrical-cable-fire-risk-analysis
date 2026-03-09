Electrical Cable Fire Risk Prediction and Early Warning System
Overview

This project presents a simulation-based fire risk estimation model for electrical cables using current behavior modeling, parametric harmonic representation, and thermal analysis. Excessive load currents and harmonic components increase conductor temperature due to I²R power losses. Prolonged thermal stress may degrade cable insulation and increase fire risk. The purpose of this study is to develop a multi-parameter risk scoring algorithm capable of classifying operating conditions before critical thermal limits are reached.

Project Objective

The objective of this project is to model electrical cable heating behavior under different load conditions, represent harmonic distortion effects in current signals, estimate fire risk using a normalized scoring algorithm, and classify operating states as SAFE, WARNING, or ALARM.

Methodology

The system evaluates three operating scenarios: Normal Load, Harmonic Load, and Overload Condition. The thermal model includes copper resistance approximation (ρ = 0.0175 Ω·mm²/m), cable length and cross-sectional area parameters, I²R power loss calculation, an iterative heating–cooling dynamic model, parametric harmonic current components, and overload ratio detection. Ambient temperature is assumed constant at 25°C throughout the simulation.

Cable temperature is calculated using a lumped-parameter thermal balance equation that considers both power dissipation and heat loss. This is a simplified dynamic model intended for risk estimation studies and does not represent a detailed finite-element heat-transfer simulation.

Harmonic Modeling

In the Python simulation, harmonic distortion is represented parametrically by adding a higher-frequency component to the fundamental current waveform. The THD value used in the simulation is a configurable parameter rather than a full FFT-based THD computation.

In MATLAB, frequency-domain validation is performed using THD analysis, FFT-based evaluation, and spectrogram visualization to observe harmonic behavior and confirm signal characteristics.

Risk Estimation Model

The normalized fire risk score (0–1) is computed as a weighted combination of current magnitude relative to allowable cable current, harmonic distortion parameter, cable temperature relative to a critical reference value, and overload ratio. The risk value is clipped between 0 and 1 to ensure normalization.

Risk classification is defined as follows:
0.00 – 0.30 → SAFE
0.30 – 0.60 → WARNING
0.60 – 1.00 → ALARM

This scoring approach enables early-stage risk identification before reaching extreme temperature conditions.

Technologies Used

Python was used for simulation and implementation of the risk estimation algorithm. MATLAB was used for signal processing analysis including THD evaluation and spectrogram visualization. Thermal modeling and signal processing techniques were applied throughout the study. The conceptual circuit schematic was designed using KiCad.

Conceptual Hardware Architecture

The proposed embedded system architecture includes an ACS712 current sensor, a DS18B20 digital temperature sensor, an ATmega328P microcontroller, a 16 MHz crystal oscillator, and required decoupling and filtering components. A physical prototype was not implemented within the scope of this study. The hardware design represents a conceptual architecture aligned with the simulation-based risk estimation model.

The circuit schematic is available in the hardware/ directory.

Results

Python simulation results demonstrate cable temperature evolution and corresponding fire risk scores under different load conditions. MATLAB analysis validates harmonic behavior and frequency-domain characteristics of the generated current signals. Generated figures are located in the figures/ directory. Detailed numerical simulation outputs are available in outputs/console_output.md.

Repository Structure

The repository is organized as follows:
python/ contains the simulation and risk estimation code.
matlab/ includes signal processing analysis scripts.
figures/ stores generated result visualizations.
hardware/ contains the conceptual circuit schematic.
outputs/ includes simulation console outputs.
data/ contains CSV data files used for MATLAB analysis.

Limitations

The system is based on simulation modeling and analytical signal evaluation. Ambient temperature is assumed constant at 25°C. No real-time embedded hardware validation or industrial testing was performed. The thermal model is a lumped-parameter approximation intended for risk estimation rather than precise physical heat-transfer modeling.

How to Run

- Running the Python Simulation
- Clone the repository:
git clone https://github.com/elifttnc/electrical-cable-fire-risk-analysis.git

- Navigate to the Python directory:
cd electrical-cable-fire-risk-analysis/python

- Install required dependencies:
pip install numpy matplotlib pandas

- Run the simulation:
python fire_risk_simulation.py

The script generates temperature and risk graphs and exports simulation data as a CSV file for MATLAB analysis.

Running MATLAB Analysis

- Open MATLAB.
- Navigate to the matlab/ directory.
- Ensure the generated CSV file (e.g., proje_verileri.csv) is located in the working directory.
- Run the MATLAB analysis script.

The MATLAB script performs FFT-based harmonic analysis, THD evaluation, and spectrogram visualization.

Author

Elif Tütüncü
Electrical & Electronics Engineering

Supervisor

Doç. Dr. Ümit Çiğdem Turhal
