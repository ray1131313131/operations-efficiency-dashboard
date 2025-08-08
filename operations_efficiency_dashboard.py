import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
Operations Efficiency Dashboard

This script creates a synthetic operations dataset with daily records for three machines.
For each day and machine, the script randomly generates the number of operations performed
and the total delay in minutes. It then aggregates the data to compute total operations
and total delay minutes per machine, calculates a delay rate, and produces a bar chart
of delay rate by machine.

To run this script:
    python operations_efficiency_dashboard.py

It will output a summary printed to the console and save a plot called
`operations_delay_rate.png` in the current directory.
"""

def main():
    np.random.seed(0)
    machines = ['Machine_A', 'Machine_B', 'Machine_C']
    dates = pd.date_range('2024-01-01', '2024-06-30', freq='D')
    data = []
    # Generate synthetic data
    for date in dates:
        for machine in machines:
            operations = np.random.randint(80, 120)  # number of operations for the day
            delay = np.random.poisson(lam=10)        # delay in minutes for the day
            data.append({'Date': date, 'Machine': machine, 'Operations': operations, 'DelayMinutes': delay})
    df = pd.DataFrame(data)
    
    # Compute summary metrics
    summary = df.groupby('Machine').agg({'Operations': 'sum', 'DelayMinutes': 'sum'})
    summary['DelayRate'] = summary['DelayMinutes'] / summary['Operations']
    
    print("Summary metrics by machine:")
    print(summary)
    
    # Plot delay rate by machine
    summary['DelayRate'].plot(kind='bar')
    plt.title('Delay Rate by Machine')
    plt.xlabel('Machine')
    plt.ylabel('Delay Rate (minutes per operation)')
    plt.tight_layout()
    plt.savefig('operations_delay_rate.png')
    plt.close()

if __name__ == '__main__':
    main()
