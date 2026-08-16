"""
EV-Experimenter
First Boost Converter Experiment

Target:
    12 V -> 450 V
"""

from ev_experimenter.physics.boost_converter import BoostConverter


def main():
    # Target system
    vin = 12.0
    target_vout = 450.0

    # Calculate the theoretical duty cycle
    duty_cycle = 1.0 - (vin / target_vout)

    converter = BoostConverter(
        vin=vin,
        duty_cycle=duty_cycle,
        switching_frequency=50_000,
        inductance=100e-6,
        capacitance=220e-6,
        load_resistance=202.5,
    )

    print("=" * 50)
    print("EV-EXPERIMENTER")
    print("First Boost Converter Experiment")
    print("=" * 50)

    print(f"Input Voltage      : {converter.vin:.2f} V")
    print(f"Duty Cycle         : {converter.duty_cycle:.4f}")
    print(f"Duty Cycle         : {converter.duty_cycle * 100:.2f} %")
    print(f"Switching Frequency: {converter.switching_frequency / 1000:.1f} kHz")

    print("-" * 50)

    print(f"Output Voltage     : {converter.output_voltage():.2f} V")
    print(f"Output Current     : {converter.output_current():.2f} A")
    print(f"Output Power       : {converter.output_power():.2f} W")
    print(f"Input Current      : {converter.input_current():.2f} A")
    print(f"Efficiency         : {converter.efficiency() * 100:.2f} %")

    print("=" * 50)


if __name__ == "__main__":
    main()
