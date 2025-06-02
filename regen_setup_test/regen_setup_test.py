import sys
import pandas as pd
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from asf_levies_model.levies import Levy

levy = Levy(
    name="demo",
    short_name="d",
    electricity_weight=1,
    gas_weight=0,
    tax_weight=0,
    electricity_variable_weight=1,
    electricity_variable_rate=0.1,
    revenue=100,
    electricity_fixed_weight=0,
    electricity_fixed_rate=0,
    gas_variable_weight=0,
    gas_variable_rate=0,
    gas_fixed_weight=0,
    gas_fixed_rate=0,
    general_taxation=0,
    price_cap_period= pd.Interval(left=0, right=1, closed="left")  # <--- need to work out what this is, but this should work
)

if __name__ == '__main__':
    print(levy.calculate_levy(electricity_consumption=3.0, gas_consumption=0.0, electricity_customer=True, gas_customer=True))