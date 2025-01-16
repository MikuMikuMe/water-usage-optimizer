Certainly! Below is a complete Python program for the "Water-Usage-Optimizer" project. It focuses on analyzing household water consumption patterns and providing personalized recommendations for reducing waste and conserving resources.

Assumptions for the program:
- The water usage data is stored in a CSV file.
- Each row in the CSV file represents daily water usage in liters for various activities.
- Columns in the CSV include 'date', 'shower', 'toilet', 'tap', 'washing_machine', 'dishwasher', 'other'.

We'll use pandas for data manipulation and basic statistics to recommend potential savings.

```python
import pandas as pd
import numpy as np

def load_data(file_path):
    """
    Load water usage data from a CSV file.
    
    Parameters:
    file_path (str): Path to the CSV file containing water usage data.
    
    Returns:
    pd.DataFrame: DataFrame containing the water usage data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError as e:
        print(f"Error: The file {file_path} was not found.")
        raise e
    except pd.errors.EmptyDataError:
        print("Error: The file is empty or not readable.")
        return pd.DataFrame()

def analyze_data(data):
    """
    Analyze the water usage data and provide recommendations.
    
    Parameters:
    data (pd.DataFrame): DataFrame containing the water usage data.
    
    Returns:
    dict: Recommendations based on the data analysis.
    """
    if data.empty:
        print("Error: No data to analyze.")
        return {}

    # Calculate average usage per activity
    avg_usage = data[['shower', 'toilet', 'tap', 'washing_machine', 'dishwasher', 'other']].mean()

    # Calculate potential savings
    # Let's assume the optimal average consumption should be 20% below the current average
    savings_potential = avg_usage * 0.2

    recommendations = {
        'shower': f"Reduce shower usage by {savings_potential['shower']:.2f} liters per day.",
        'toilet': f"Reduce toilet usage by {savings_potential['toilet']:.2f} liters per day.",
        'tap': f"Reduce tap usage by {savings_potential['tap']:.2f} liters per day.",
        'washing_machine': f"Reduce washing machine usage by {savings_potential['washing_machine']:.2f} liters per day.",
        'dishwasher': f"Reduce dishwasher usage by {savings_potential['dishwasher']:.2f} liters per day.",
        'other': f"Reduce other usage by {savings_potential['other']:.2f} liters per day."
    }

    return recommendations

def display_recommendations(recommendations):
    """
    Display the recommendations in a user-friendly format.
    
    Parameters:
    recommendations (dict): Recommendations based on the data analysis.
    """
    if not recommendations:
        print("No recommendations available.")
        return

    print("Personalized Water Usage Recommendations to Reduce Waste:")
    for activity, suggestion in recommendations.items():
        print(f"- {activity.capitalize()}: {suggestion}")

def main():
    # Define the path to the data file
    file_path = 'water_usage_data.csv'

    # Load the data
    data = load_data(file_path)
    
    # Analyze the data
    recommendations = analyze_data(data)
    
    # Display recommendations
    display_recommendations(recommendations)

if __name__ == "__main__":
    main()
```

### Explanation:
1. **load_data**: This function reads water usage data from a CSV file and handles `FileNotFoundError` and empty data errors.
2. **analyze_data**: It calculates the average water usage for different activities and proposes a 20% reduction for optimal savings.
3. **display_recommendations**: This function formats and displays the conservation tips.
4. **main**: The main function orchestrates loading, analyzing, and displaying the data.

### Error Handling:
- The program includes error handling for file operations and checks for empty data.
- Recommendations are displayed in a user-friendly manner, even if the dataset is empty, with appropriate messages.

Please ensure you have a CSV file named `water_usage_data.csv` with the outlined structure before running the program.