
-------------------------
E-commerce Sales Analysis
-------------------------

This project uses R and Spark to clean, transform, and analyze e-commerce sales data. The analysis generates insightful visualizations, including sales trends and category-based distributions. The main script, script.R, performs all operations, from data processing to visualization. Key results are stored as plot files in the plots/ directory.

Tools Used
---------------
R: For data processing, visualization, and scripting.
Sparklyr: To integrate R with Apache Spark.
ggplot2: For creating visualizations.
dplyr: For efficient data manipulation.
Apache Spark: To handle large datasets.

Details and Files
-------------------
script.R: Main script for the analysis.
Plot Outputs:
total_sales_by_category.jpg: Bar chart of total sales by category.
total_products_by_category.jpg: Bar chart of total products by category.
sales_distribution.jpg: Boxplot of sales distribution.
total_sales_trend_by_category.jpg: Line chart of sales trends by category.
proportion_of_total_sales_by_category.jpg: Pie chart of sales proportions.
Generated plot files are saved in the plots/ directory and updated with every script run.


All other files, including raw data and processed CSV outputs, are ignored for these purposes but were executed in the actual runs.

Output
------
Processed Data: A CSV file containing cleaned and aggregated sales data.

Visualizations:
--------------
Total sales and products by category.
Sales distribution as a boxplot.
Sales trend over categories.
Proportional sales distribution as a pie chart.

Troubleshooting
---------------
Spark connection issues: Ensure SPARK_HOME is correctly set and Spark is installed.
Missing libraries: Run install.packages() to install any missing R packages.
File not found: Verify the paths to generated_data.csv in the script.

License
-------
This project is available under the MIT License.


