# ⚡ EV-Experimenter

### An open-source AI laboratory for discovering, modeling, and optimizing electric-vehicle powertrains through intelligent experimentation.

**EV-Experimenter** is an open-source research and engineering platform that combines **power electronics, EV system modeling, machine learning, physics-based modeling, and active learning** to create an intelligent experimentation loop for electric-vehicle powertrains.

Instead of asking an engineer to manually run hundreds or thousands of simulations, EV-Experimenter aims to let an intelligent system determine:

> **What should we experiment with next?**

The system runs an experiment, analyzes the result, updates its understanding of the system, estimates uncertainty, and chooses the next experiment.

The long-term goal is to create a **free, reproducible, local-first alternative to fragmented EV engineering experimentation workflows**.

---

## 🚀 Why EV-Experimenter?

Modern EV development requires engineers to work across many different tools and domains:

* MATLAB/Simulink
* PLECS
* SPICE
* battery modeling frameworks
* motor simulation
* CAN data
* laboratory instruments
* hardware-in-the-loop systems
* optimization software
* machine-learning frameworks

These tools are powerful, but the engineering workflow is often fragmented.

An engineer may have to manually:

1. create a model
2. choose parameters
3. run a simulation
4. collect results
5. analyze the results
6. decide what to change
7. run another simulation
8. repeat hundreds or thousands of times

EV-Experimenter explores a different approach.

```text
                  ENGINEERING GOAL
                         │
                         ▼
                ┌─────────────────┐
                │ Experiment      │
                │ Planner         │
                └────────┬────────┘
                         │
                         ▼
                  Select experiment
                         │
                         ▼
              ┌──────────────────────┐
              │ Simulation / Hardware │
              └──────────┬───────────┘
                         │
                         ▼
                       DATA
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
       Physics Model          ML Model
              │                     │
              └──────────┬──────────┘
                         ▼
                  Uncertainty
                         │
                         ▼
              Next Best Experiment
                         │
                         └───────────────┐
                                         │
                                         ▼
                                   Repeat / Learn
```

---

# 🎯 The Core Problem

The first question EV-Experimenter attempts to solve is:

> **How can an AI system intelligently identify the behavior of an EV power-electronics system using the smallest useful number of experiments?**

Consider a DC-DC converter.

An engineer might need to investigate the effects of:

* input voltage
* output voltage
* load
* switching frequency
* duty cycle
* inductance
* capacitance
* ESR
* temperature
* semiconductor characteristics

A conventional parameter sweep might require thousands of simulations.

EV-Experimenter instead attempts to learn from each experiment.

For example:

```text
Experiment 001
      ↓
Observe response
      ↓
Update model
      ↓
Estimate uncertainty
      ↓
Select Experiment 002
      ↓
Observe response
      ↓
Update model
      ↓
...
```

The objective is not simply to find a good parameter.

The objective is to **learn the system intelligently.**

---

# 🧠 Core Concept

EV-Experimenter is based on four ideas:

### 1. Physics

The system should understand the electrical system through equations, models, constraints, and engineering knowledge.

### 2. Machine Learning

ML models learn relationships between:

```text
System parameters
       ↓
Electrical behavior
       ↓
Performance
```

### 3. Active Learning

The system identifies which experiment would provide the most useful information.

### 4. Optimization

Once sufficient knowledge has been acquired, the system searches for better designs or operating conditions.

Together:

```text
Physics
   +
Machine Learning
   +
Active Learning
   +
Optimization
   =
Intelligent Engineering Experimentation
```

---

# ⚡ Initial Target: EV Power Electronics

The first implementation will focus on power electronics because it provides a well-defined environment for experimentation and directly connects to EV powertrain architecture.

The initial target system is:

```text
       DC Battery
           │
           ▼
     ┌───────────┐
     │  DC-DC    │
     │ Converter │
     └─────┬─────┘
           │
           ▼
        DC Link
           │
           ▼
      ┌─────────┐
      │ Inverter│
      └────┬────┘
           │
           ▼
      Electric Motor
```

The first prototype will begin with a **Boost Converter**.

---

# 🧪 First Demonstration

The first major demonstration will be:

## 12 V → 450 V Boost Converter

Example target:

```text
Input voltage:       12 V
Output voltage:      450 V
Power:               500 W – 2 kW
Target efficiency:   >95%
Output ripple:       <2%
```

The exact specifications will remain configurable.

The system will explore parameters such as:

```text
Vin
Vout
Duty cycle
Switching frequency
Inductance
Capacitance
Load
ESR
```

and measure:

```text
Efficiency
Output ripple
Inductor current ripple
Peak current
Switch stress
Voltage stress
Power loss
Transient response
```

---

# 🔬 Example Experiment

Suppose the user specifies:

```text
Goal:

Vout = 450 V
Pout = 1 kW
Efficiency > 95%
Minimize component stress
```

EV-Experimenter may begin with:

```text
Experiment #1

L  = 100 µH
C  = 220 µF
Fs = 50 kHz
D  = 0.73
```

The simulator returns:

```text
Efficiency = 92.4%
Ripple     = 3.8%
```

The model learns from the experiment.

It then decides which parameter is most useful to investigate.

For example:

```text
Experiment #2

L  = 150 µH
C  = 220 µF
Fs = 50 kHz
D  = 0.73
```

The system continues learning.

Eventually:

```text
                  500 experiments

                         ↓

                 Learned surrogate
                      model

                         ↓

                  Optimization

                         ↓

                 Candidate designs

                         ↓

               High-fidelity validation
```

The result might be:

```text
Recommended region

L  = 143 µH
C  = 330 µF
Fs = 67 kHz

Predicted efficiency = 96.1%
Predicted ripple     = 1.4%
```

The final result must be validated against the original physics/simulation model.

---

# 🧠 Neural Network Layer

The project will not begin by blindly adding a neural network.

The ML architecture will evolve as the engineering problem requires it.

Possible models include:

* Gaussian Processes
* Bayesian optimization
* Random Forest
* Gradient Boosting
* MLP
* Autoencoder
* LSTM
* Transformer
* Neural surrogate models
* Physics-informed neural networks
* Reinforcement learning

The first objective is not to use the most complicated model.

The objective is:

> **Use the simplest model that solves the engineering problem reliably.**

---

# 🔄 The Learning Loop

The central algorithm can be represented as:

```text
Initialize system
       │
       ▼
Define engineering objective
       │
       ▼
Generate initial experiments
       │
       ▼
Run simulations
       │
       ▼
Collect measurements
       │
       ▼
Train/update model
       │
       ▼
Estimate uncertainty
       │
       ▼
Choose next experiment
       │
       ▼
Run experiment
       │
       ▼
Compare prediction vs reality
       │
       ▼
Update model
       │
       └───────────────► Repeat
```

This creates a closed-loop learning system.

---

# 🔮 Long-Term Vision

The Boost Converter is only the starting point.

The platform is designed to eventually support:

### Power Electronics

* Boost converters
* Buck converters
* Buck-boost converters
* Interleaved converters
* Dual-active bridges
* LLC converters
* Multilevel converters
* Inverters

### Electric Machines

* PMSM
* BLDC
* induction motors
* motor-drive systems

### EV Systems

* battery
* DC-DC converter
* inverter
* motor
* regenerative braking
* thermal systems

### Charging

* onboard charger
* DC fast charging
* charging optimization
* V2G

---

# 🧩 Simulation Backends

The architecture will be backend-agnostic.

The initial system will prioritize open and reproducible tools.

Potential integrations include:

* Python-based models
* SciPy
* PyBaMM
* SPICE-compatible simulators
* OpenModelica
* PLECS
* MATLAB/Simulink where users have access to them

The core platform should not depend on a proprietary simulator.

---

# 🔌 Hardware-in-the-Loop

A long-term objective is to connect EV-Experimenter to real hardware.

The architecture will eventually support:

```text
                 EV-Experimenter
                        │
             ┌──────────┴──────────┐
             ▼                     ▼
        Simulation             Hardware
             │                     │
             └──────────┬──────────┘
                        ▼
                      Data
                        │
                        ▼
                 Learning Engine
```

Potential hardware could include:

* STM32
* ESP32
* Raspberry Pi
* low-cost DAQ devices
* custom converter boards

This would allow the same experiment definition to move from simulation toward physical experimentation.

---

# 🧬 System Identification

One of the most important future capabilities is **system identification**.

The software should eventually be able to observe:

```text
Voltage
Current
Temperature
RPM
Torque
```

and infer unknown system properties.

For example:

```text
Unknown:

Inductance
Resistance
Capacitance
Thermal resistance
Switching losses
Motor parameters
```

The system performs experiments and estimates them.

This transforms EV-Experimenter from a simulation optimizer into an **experimental engineering system**.

---

# 🤖 Active Experiment Selection

The most important research component is the experiment planner.

Instead of:

```text
Run everything
```

the system should ask:

> **Which experiment will teach me the most?**

Possible approaches:

### Random exploration

Simple baseline.

### Grid search

Traditional engineering baseline.

### Bayesian optimization

Efficient optimization of expensive simulations.

### Active learning

Select experiments based on model uncertainty.

### Reinforcement learning

Learn an experiment-selection policy.

The project will compare these approaches experimentally.

---

# 📊 Reproducibility

Every experiment should be reproducible.

An experiment will contain:

```text
experiment/
├── config.yaml
├── model/
├── parameters/
├── dataset/
├── results/
├── plots/
├── metrics.json
└── README.md
```

Someone should be able to clone the repository and reproduce an experiment with a single command.

For example:

```bash
evexp run experiments/boost_converter/basic
```

---

# 🌍 Open-Source Philosophy

EV-Experimenter is intended to be:

### Free

The core platform will remain free.

### Local-first

Data should not need to leave the user's machine.

### Reproducible

Experiments should be reproducible from source.

### Hardware-independent

Users should be able to start without an expensive EV laboratory.

### Extensible

Researchers should be able to add models, algorithms, simulators and hardware interfaces.

### Research-friendly

Experiments should produce datasets and results that can be used in academic research.

---

# 🛠️ Proposed Architecture

```text
ev-experimenter/
│
├── core/
│   ├── experiment.py
│   ├── parameter_space.py
│   ├── objective.py
│   └── runner.py
│
├── physics/
│   ├── converters/
│   ├── motors/
│   ├── batteries/
│   └── thermal/
│
├── simulators/
│   ├── python/
│   ├── spice/
│   ├── pybamm/
│   ├── openmodelica/
│   └── plecs/
│
├── ml/
│   ├── surrogate/
│   ├── active_learning/
│   ├── uncertainty/
│   └── neural/
│
├── optimization/
│   ├── bayesian/
│   ├── evolutionary/
│   └── reinforcement_learning/
│
├── hardware/
│   ├── stm32/
│   ├── esp32/
│   └── daq/
│
├── experiments/
│   ├── boost_converter/
│   ├── inverter/
│   └── battery/
│
├── datasets/
│
├── visualization/
│
├── examples/
│
├── tests/
│
└── docs/
```

The architecture will evolve as the project develops.

---

# 🗺️ Development Roadmap

## Phase 0 — Foundations

* [ ] Repository architecture
* [ ] Python environment
* [ ] Experiment definition format
* [ ] Parameter-space abstraction
* [ ] Objective-function abstraction
* [ ] Dataset format

---

## Phase 1 — First Power-Electronics Model

* [ ] Boost converter model
* [ ] Electrical equations
* [ ] Numerical simulation
* [ ] Parameter sweeps
* [ ] Performance metrics
* [ ] Visualization

**Milestone:**

> A user can define a converter and automatically run experiments.

---

## Phase 2 — Experiment Engine

* [ ] Experiment scheduler
* [ ] Parameter sampling
* [ ] Parallel experiments
* [ ] Result database
* [ ] Experiment comparison
* [ ] Reproducibility

**Milestone:**

> Hundreds of experiments can be automatically executed and analyzed.

---

## Phase 3 — Optimization

* [ ] Random search baseline
* [ ] Grid search baseline
* [ ] Bayesian optimization
* [ ] Multi-objective optimization
* [ ] Pareto-front visualization

**Milestone:**

> EV-Experimenter can find better converter configurations automatically.

---

## Phase 4 — Machine Learning

* [ ] Surrogate model
* [ ] Neural-network surrogate
* [ ] Model evaluation
* [ ] Uncertainty estimation
* [ ] Prediction vs simulation comparison

**Milestone:**

> The ML model learns the relationship between engineering parameters and system behavior.

---

## Phase 5 — Active Learning

* [ ] Uncertainty-driven experiment selection
* [ ] Information-gain strategies
* [ ] Active-learning benchmark
* [ ] Experiment-efficiency comparison

**Milestone:**

> The system can decide which experiment should be performed next.

---

## Phase 6 — EV Powertrain

* [ ] Battery model
* [ ] DC-DC converter
* [ ] DC-link
* [ ] Inverter
* [ ] PMSM model
* [ ] Drive cycle
* [ ] Power-flow analysis

**Milestone:**

> The system can intelligently experiment with a simplified EV powertrain.

---

## Phase 7 — Hardware

* [ ] STM32 interface
* [ ] Sensor interface
* [ ] Data acquisition
* [ ] Hardware experiment definition
* [ ] Simulation-to-hardware comparison

**Milestone:**

> A simulated experiment can be transferred toward physical hardware.

---

# 📈 Benchmarking

EV-Experimenter will not claim that AI is automatically better.

Every intelligent method should be compared against traditional approaches.

For example:

```text
Method                  Experiments    Best efficiency
-------------------------------------------------------
Grid Search             10,000         95.1%
Random Search            2,000         95.4%
Bayesian Optimization      300         95.8%
Neural Surrogate           200         95.9%
Active Learning            150         96.0%
```

The actual numbers will come from experiments.

The project should always report:

* number of experiments
* computational cost
* accuracy
* uncertainty
* optimization quality
* reproducibility

---

# 🔬 Research Questions

EV-Experimenter is also intended to support research.

Possible research questions include:

### RQ1

Can active learning reduce the number of EV power-electronics simulations required to reach a target design?

### RQ2

Can neural surrogate models accurately reproduce converter performance?

### RQ3

Can physics-informed models outperform purely data-driven models when training data is limited?

### RQ4

Can an experiment-selection algorithm identify unknown powertrain parameters efficiently?

### RQ5

How well does a learned model transfer from simulation to real hardware?

### RQ6

How much computational effort can intelligent experimentation save compared with conventional parameter sweeps?

---

# 📚 Example Applications

## Example 1 — Converter Optimization

```text
Goal:

maximize efficiency
minimize ripple
minimize component stress
```

EV-Experimenter searches the design space.

---

## Example 2 — Unknown Parameter Identification

```text
Given:

Vin
Iin
Vout
Iout

Find:

L
C
R
loss parameters
```

The system chooses experiments to reduce uncertainty.

---

## Example 3 — Fault Investigation

Possible hypotheses:

```text
H1: capacitor degradation
H2: inductor saturation
H3: switching loss increase
H4: sensor error
```

The experiment planner selects the experiment that best distinguishes between the hypotheses.

---

## Example 4 — Battery Experimentation

Given limited battery data:

```text
Find:

SOC
SOH
internal resistance
thermal parameters
```

The system identifies the most informative operating conditions.

---

# 🛡️ Safety

EV-Experimenter is primarily a **simulation and research platform**.

It must not directly control a road-going vehicle.

Hardware interfaces will include safety mechanisms such as:

* operating limits
* voltage limits
* current limits
* temperature limits
* emergency shutdown
* simulation-first validation
* explicit hardware confirmation

The project will prioritize safe experimentation over autonomous physical control.

---

# 🤝 Contributing

Contributions are welcome.

Potential contribution areas:

* EV models
* converter models
* motor models
* battery models
* optimization algorithms
* ML algorithms
* simulation backends
* datasets
* hardware interfaces
* documentation
* visualization
* benchmarks

A good contribution should include:

1. reproducible experiment
2. documentation
3. tests where applicable
4. benchmark results
5. explanation of assumptions

---

# 🌟 Long-Term Vision

The long-term vision is much larger than a converter optimizer.

We want to build:

> **An open-source experimentation layer for electric-vehicle engineering.**

Eventually:

```text
                 EV-EXPERIMENTER
                        │
       ┌────────────────┼────────────────┐
       │                │                │
    BATTERY          POWER             MOTOR
       │            ELECTRONICS          │
       │                │                │
       └────────────────┼────────────────┘
                        │
                 EXPERIMENT ENGINE
                        │
                 MACHINE LEARNING
                        │
                 ACTIVE LEARNING
                        │
                 OPTIMIZATION
                        │
                 HARDWARE / HIL
```

The ultimate goal is:

> **Make advanced EV experimentation accessible to anyone with a computer.**

A student should be able to reproduce an experiment.

A researcher should be able to publish a new algorithm.

An engineer should be able to test a design.

A hardware developer should be able to connect a prototype.

And all of them should be able to build on the same open-source foundation.

---

# 🚧 Current Status

**Early research / development**

The project is currently at the concept and architecture stage.

The first implementation will focus on:

> **Intelligent experimentation and optimization of a DC-DC converter.**

The project will expand toward complete EV powertrain experimentation only after the core experimentation engine is validated.

---

# 📜 License

The initial implementation is intended to use a permissive open-source license.

The exact license will be selected before the first public release.

---

# ⭐ If you find this useful

Star the repository, reproduce an experiment, report your results, and contribute improvements.

The goal isn't to build another closed engineering tool.

The goal is to build an **open laboratory for EV engineering.**

---

## ⚡ EV-Experimenter

**Simulate. Experiment. Learn. Optimize.**

> *Let the machine decide what to test next.*
