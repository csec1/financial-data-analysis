### README: A/B Testing for Website Layout Comparison

This project simulates an A/B test to compare the performance of two website layouts (Version A and Version B) based on their conversion rates (percentage of visitors who make a purchase). The test generates simulated data for 1,500 visitors in each group, with Version A having a 3% conversion rate and Version B having a 5% conversion rate. The test performs a two-sample t-test to determine whether the difference in conversion rates is statistically significant.

#### Libraries and Tools Used:
- **NumPy**: For generating random data and statistical operations.
- **SciPy**: For performing the two-sample t-test to check statistical significance.
- **Matplotlib**: For visualizing the data in histograms.
- **Pandas**: For saving the results to a CSV file for further analysis.

The key steps include:
1. Simulating the visitor and purchase data.
2. Calculating the conversion rates.
3. Performing a two-sample t-test.
4. Visualizing the results in a histogram.
5. Saving the results in a CSV file.

**Results**: Version B significantly outperforms Version A with a p-value of 0.0000.