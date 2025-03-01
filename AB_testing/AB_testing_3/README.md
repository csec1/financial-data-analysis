A/B Testing for Email Campaign Effectiveness

This project performs an A/B test to compare the effectiveness of two different email marketing campaigns (Version A and Version B) on customer email open rates. It simulates a large customer dataset, performs statistical analysis, visualizes the results, and saves the findings for further review.
Project Overview
1.	Data Generation (Part 1):
o	Simulates customer data with demographics (age, gender) and email open rates for two email versions (A and B).
o	Generates a synthetic dataset for 50,000 customers and saves it as a CSV file (ab_test_email_campaign_data.csv).

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

2.	A/B Testing and Analysis (Part 2):
o	Reads the generated CSV file containing customer data.
o	Filters the data by email version (A and B) and performs a two-sample t-test to compare email open rates.
o	Visualizes the open rate distribution for both email versions and determines if there is a statistically significant difference.
o	Saves the analysis results in a new CSV file (ab_test_results_email_campaign.csv).
________________________________________
Libraries and Tools Used
•	NumPy: For data simulation and random number generation.
•	Pandas: For data manipulation, cleaning, and CSV handling.
•	SciPy: For statistical tests (t-test).
•	Matplotlib: For visualizing the results using histograms.

RESULTS ARE OF FORM
>>>>>>>>>>>>>>>>>>>>>
Conversion rate for Version A: 0.2023
Conversion rate for Version B: 0.2215
T-statistic: -5.2439

License: This project is licensed under the MIT License

P-value: 0.0000
The result is statistically significant, meaning there is a significant difference between A and B.


