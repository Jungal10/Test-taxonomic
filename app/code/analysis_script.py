#!/usr/bin/env python3
"""
analysis_script.py

Reads a taxonomic dataset and produces:
1. A summary CSV with total and average species counts per phylum.
2. A bar chart visualization of total species counts per phylum.

Input file is expected to be in the `data/raw` folder. Outputs are written to:
- `data/intermediate` for intermediate steps.
- `data/output` for final results.

Usage:
    python code/analysis_script.py --input data/raw/taxonomic_data.csv --output_dir data
"""

import argparse
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # Imported for improved aesthetics

def load_data(input_file):
    """Load taxonomic data."""
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file {input_file} not found.")
    return pd.read_csv(input_file)

def validate_data(df):
    """Validate and clean the input data."""
    required_cols = {'phylum', 'species', 'count'}
    if not required_cols.issubset(df.columns):
        raise ValueError(f"Missing required columns: {required_cols - set(df.columns)}")
    df = df.dropna(subset=['phylum', 'species'])
    df['count'] = pd.to_numeric(df['count'], errors='coerce').fillna(0).astype(int)
    return df

def compute_statistics(df):
    """Compute total and average species counts per phylum."""
    grouped = df.groupby('phylum').agg(
        total_count=('count', 'sum'),
        avg_count_per_species=('count', 'mean')
    ).reset_index()
    return grouped

def save_results(df, intermediate_dir, output_dir):
    """Save intermediate and final results."""
    intermediate_path = os.path.join(intermediate_dir, 'validated_taxonomic_data.csv')
    final_output_path = os.path.join(output_dir, 'phylum_summary.csv')
    
    df.to_csv(intermediate_path, index=False)
    print(f"Intermediate results saved to {intermediate_path}")

    df.to_csv(final_output_path, index=False)
    print(f"Final results saved to {final_output_path}")

def plot_bar_chart(summary_df, output_dir):
    """Plot and save an elegant bar chart of total species counts per phylum."""
    # Set Seaborn style for better aesthetics
    sns.set(style="whitegrid")

    # Sort the DataFrame by total_count in descending order for better readability
    summary_df = summary_df.sort_values(by='total_count', ascending=False)

    plt.figure(figsize=(12, 8))  # Increased figure size for better visibility

    # Create a color palette
    palette = sns.color_palette("viridis", len(summary_df))

    # Create the bar plot using Seaborn for enhanced aesthetics
    barplot = sns.barplot(
        x='total_count',
        y='phylum',
        data=summary_df,
        palette=palette,
        edgecolor='black' 
    )

    # Set titles and labels
    plt.title('Total Species Count per Phylum', fontsize=16, weight='bold')
    plt.xlabel('Total Species Count', fontsize=14)
    plt.ylabel('Phylum', fontsize=14)

    # Add data labels to each bar for precise information
    for index, value in enumerate(summary_df['total_count']):
        plt.text(
            value + max(summary_df['total_count']) * 0.01,  
            index,
            str(value),
            va='center',
            fontsize=12
        )

    # Rotate y-axis labels if needed
    plt.yticks(fontsize=12)

    # Adjust layout for better spacing and fit
    plt.tight_layout()

    # Save the figure with high resolution suitable for reports or presentations
    chart_path = os.path.join(output_dir, 'phylum_counts_bar_chart.png')
    plt.savefig(chart_path, dpi=300)
    plt.close()  # Close the figure to free memory
    print(f"Bar chart saved to {chart_path}")

def main():
    parser = argparse.ArgumentParser(description="Analyze taxonomic data.")
    parser.add_argument('--input', required=True, help="Path to input CSV file (e.g., data/taxonomic_data.csv)")
    parser.add_argument('--output_dir', default='data', help="Path to output directory: data")
    args = parser.parse_args()

    # Define directories for intermediate and final outputs
    intermediate_dir = os.path.join(args.output_dir, 'intermediate')
    output_dir = os.path.join(args.output_dir, 'output')
    os.makedirs(intermediate_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)

    try:
        # Load the data from the input CSV file
        df = load_data(args.input)
        
        # Validate and clean the data
        df = validate_data(df)
        
        # Compute the required statistics
        summary_df = compute_statistics(df)
        
        # Save the intermediate and final results
        save_results(summary_df, intermediate_dir, output_dir)
        
        # Plot and save the enhanced bar chart
        plot_bar_chart(summary_df, output_dir)
    except Exception as e:
        print(f"Error: {e}")
        exit(1)

if __name__ == '__main__':
    main()
