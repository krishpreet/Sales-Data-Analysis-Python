import pandas as pd
import matplotlib.pyplot as plt

def load_data(sales_data.csv):
    """Load sales data from CSV file."""
    try:
        data = pd.read_csv(sales_data.csv)
        return data
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None

def explore_data(data):
    """Explore the loaded data."""
    # Display the first few rows of the DataFrame
    print("First 5 rows of the data:")
    print(data.head())

    # Display basic info about the DataFrame
    print("\nData Info:")
    print(data.info())

    # Summary statistics
    print("\nSummary Statistics:")
    print(data.describe())

def analyze_sales(data):
    """Perform basic sales analysis."""
    # Total sales
    total_sales = data['TotalAmount'].sum()
    print("\nTotal Sales: ${:.2f}".format(total_sales))

    # Monthly sales trends
    data['SaleDate'] = pd.to_datetime(data['SaleDate'])  # Convert SaleDate to datetime
    data['Month'] = data['SaleDate'].dt.to_period('M')  # Extract month
    monthly_sales = data.groupby('Month')['TotalAmount'].sum()
    
    # Plot monthly sales
    monthly_sales.plot(kind='line', marker='o')
    plt.title('Monthly Sales Trends')
    plt.xlabel('Month')
    plt.ylabel('Total Sales ($)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    # Load data
    file_path = 'sales_data.csv'
    data = load_data(sales_data.csv)
    if data is None:
        return
    
    # Explore data
    explore_data(data)
    
    # Perform analysis
    analyze_sales(data)

if __name__ == "__main__":
    main()
