"""Boost converter physics model."""
"""
Ideal Boost Converter Model
===========================

First physics model for EV-Experimenter.

This model calculates the ideal steady-state behavior of a
Boost Converter operating in Continuous Conduction Mode (CCM).

Initial target:
    12 V DC -> 450 V DC

The model will later be extended with:
    - Inductor current ripple
    - Capacitor voltage ripple
    - Semiconductor losses
    - Inductor losses
    - Switching losses
    - Thermal effects
    - Dynamic/transient simulation
"""


from dataclasses import dataclass


@dataclass
class BoostConverter:
    """Ideal steady-state Boost Converter model."""

    vin: float
    duty_cycle: float
    switching_frequency: float
    inductance: float
    capacitance: float
    load_resistance: float

    def output_voltage(self) -> float:
        """
        Calculate ideal output voltage.

        Vout = Vin / (1 - D)
        """

        if not 0 < self.duty_cycle < 1:
            raise ValueError("Duty cycle must be between 0 and 1.")

        return self.vin / (1.0 - self.duty_cycle)

    def output_current(self) -> float:
        """Calculate output current using Ohm's law."""

        vout = self.output_voltage()

        return vout / self.load_resistance

    def input_current(self) -> float:
        """
        Calculate ideal average input current.

        For an ideal converter:

            Pin = Pout

        Therefore:

            Iin = Pout / Vin
        """

        vout = self.output_voltage()
        iout = self.output_current()

        pout = vout * iout

        return pout / self.vin

    def input_power(self) -> float:
        """Calculate input power."""

        return self.vin * self.input_current()

    def output_power(self) -> float:
        """Calculate output power."""

        return self.output_voltage() * self.output_current()

    def efficiency(self) -> float:
        """
        Calculate converter efficiency.

        The ideal converter has no losses.
        Therefore efficiency = 100%.
        """

        return 1.0
