#cell1
# Load required libraries
Sys.setenv(SPARK_HOME = "/opt/spark/spark-3.5.3-bin-hadoop3")

library(sparklyr)
library(dplyr)
library(ggplot2)

# Connect to Spark
sc <- spark_connect(master = "local")

#cell2
# Load the CSV data into Spark
raw_data <- spark_read_csv(
  sc,
  name = "raw_data",
  path = "/home/cybersec/python_projects/R/E-commerce_Sales_Analysis2/generated_data.csv",  # Replace with your CSV file path
  infer_schema = TRUE,
  header = TRUE
)

# Print column names for reference
print(colnames(raw_data))

# Data cleaning: Remove missing values, remove duplicates, and filter invalid rows
# Assuming 1 USD = 150 JPY, adjust as needed for real-time data
exchange_rate <- 150  # Example exchange rate from JPY to USD

cleaned_data <- raw_data %>% 
  filter_all(any_vars(!is.na(.))) %>%                    # Remove rows with missing values
  distinct() %>%                                         # Remove duplicate rows
  mutate(actual_price = as.numeric(actual_price)) %>%    # Convert 'actual_price' to numeric
  filter(actual_price > 0) %>%                           # Filter rows with valid sales amounts
  mutate(actual_price_usd = actual_price / exchange_rate)  # Convert 'actual_price' from JPY to USD

# Collect cleaned data into R for viewing the head
cleaned_data_r <- collect(cleaned_data)

# Print the head of the cleaned data
head(cleaned_data_r)

#cell3
# Data transformation: Aggregate total sales and total products
transformed_data <- cleaned_data %>% 
  group_by(main_category) %>%                             # Group by 'main_category' as there is no 'order_date'
  summarise(
    total_sales = sum(actual_price_usd, na.rm = TRUE),    # Aggregate sales in USD
    total_products = n()                                  # Count number of products per category
  )

#cell4
# Create a batch pipeline to process data automatically (e.g., store processed data)
batch_data_pipeline <- function() {
  # Clean and transform data
  cleaned_data <- spark_read_csv(
    sc,
    name = "batch_data",
    path = "/home/cybersec/python_projects/R/E-commerce_Sales_Analysis2/generated_data.csv",  # Path to your dataset
    infer_schema = TRUE,
    header = TRUE
  ) %>% 
    filter_all(any_vars(!is.na(.))) %>%                    # Remove rows with missing values
    distinct() %>%                                         # Remove duplicates
    mutate(actual_price = as.numeric(actual_price)) %>%    # Ensure 'actual_price' is numeric
    filter(actual_price > 0) %>%                           # Filter invalid rows
    mutate(actual_price_usd = actual_price / exchange_rate)  # Convert 'actual_price' to USD

  # Aggregate data by 'main_category'
  cleaned_data <- cleaned_data %>% 
    group_by(main_category) %>% 
    summarise(
      total_sales = sum(actual_price_usd, na.rm = TRUE),  # Aggregate sales in USD
      total_products = n()                                # Count products by category
    )
  
  # Save the cleaned and transformed data
  spark_write_csv(cleaned_data, path = "/home/cybersec/python_projects/R/E-commerce_Sales_Analysis2/processed_data.csv", mode = "overwrite")
}

# Execute the batch data pipeline
batch_data_pipeline()

#cell5
# Collect the processed data into R
plot_data <- transformed_data %>% collect()


# Plot 1: Total Sales over Categories (Bar plot)
plot1 <- ggplot(plot_data, aes(x = main_category, y = total_sales)) +
  geom_bar(stat = "identity", fill = "blue") +
  labs(title = "Total Sales by Category", x = "Category", y = "Total Sales (USD)") +
  theme_minimal() +
  theme(
    plot.title = element_text(size = 16, face = "bold", hjust = 0.5, color = "black"),
    axis.title.x = element_text(size = 14, color = "black"),
    axis.title.y = element_text(size = 14, color = "black"),
    axis.text.x = element_text(angle = 45, hjust = 1),
    panel.background = element_rect(fill = "white"),
    plot.background = element_rect(fill = "white")
  )
ggsave("/home/cybersec/python_projects/R/E-commerce_Sales_Analysis2/total_sales_by_category.jpg", plot = plot1, width = 10, height = 6)

# Plot 2: Total Products over Categories (Bar plot)
plot2 <- ggplot(plot_data, aes(x = main_category, y = total_products)) +
  geom_bar(stat = "identity", fill = "orange") +
  labs(title = "Total Products by Category", x = "Category", y = "Total Products") +
  theme_minimal() +
  theme(
    plot.title = element_text(size = 16, face = "bold", hjust = 0.5, color = "black"),
    axis.title.x = element_text(size = 14, color = "black"),
    axis.title.y = element_text(size = 14, color = "black"),
    axis.text.x = element_text(angle = 45, hjust = 1),
    panel.background = element_rect(fill = "white"),
    plot.background = element_rect(fill = "white")
  )
ggsave("/home/cybersec/python_projects/R/E-commerce_Sales_Analysis2/total_products_by_category.jpg", plot = plot2, width = 10, height = 6)

# Plot 3: Boxplot for Sales Distribution (Outliers in red)
plot3 <- ggplot(plot_data, aes(y = total_sales)) +
  geom_boxplot(fill = "lightblue", outlier.color = "red", outlier.size = 2) +
  labs(title = "Sales Distribution", y = "Total Sales (USD)") +
  theme_minimal() +
  theme(
    plot.title = element_text(size = 16, face = "bold", hjust = 0.5, color = "black"),
    axis.title.y = element_text(size = 14, color = "black"),
    axis.text.y = element_text(size = 12, color = "black"),
    panel.background = element_rect(fill = "white"),
    plot.background = element_rect(fill = "white")
  )
ggsave("/home/cybersec/python_projects/R/E-commerce_Sales_Analysis2/sales_distribution.jpg", plot = plot3, width = 10, height = 6)

# Plot 4: Line Graph for Total Sales Trend by Category
plot4 <- ggplot(plot_data, aes(x = main_category, y = total_sales, group = 1)) +
  geom_line(color = "blue", linewidth = 1.5) +  # Use 'linewidth' instead of 'size'
  geom_point(color = "red", size = 3) +        # Keep 'size' for points
  labs(title = "Total Sales Trend by Category", x = "Category", y = "Total Sales (USD)") +
  theme_minimal() +
  theme(
    plot.title = element_text(size = 16, face = "bold", hjust = 0.5, color = "black"),
    axis.title.x = element_text(size = 14, color = "black"),
    axis.title.y = element_text(size = 14, color = "black"),
    axis.text.x = element_text(angle = 45, hjust = 1),
    panel.background = element_rect(fill = "white"),
    plot.background = element_rect(fill = "white")
  )
ggsave("/home/cybersec/python_projects/R/E-commerce_Sales_Analysis2/total_sales_trend_by_category.jpg", plot = plot4, width = 10, height = 6)

# Plot 5: Pie Chart for Proportion of Total Sales by Category with Labels
pie_data <- plot_data %>%
  mutate(proportion = total_sales / sum(total_sales) * 100,
         label = paste0(main_category, " (", round(proportion, 1), "%)"))  # Create labels

plot5 <- ggplot(pie_data, aes(x = "", y = proportion, fill = main_category)) +
  geom_bar(stat = "identity", width = 1, color = "white") +
  coord_polar(theta = "y") +
  geom_text(aes(label = label), position = position_stack(vjust = 0.5), size = 4, color = "black") +  # Add labels
  labs(title = "Proportion of Total Sales by Category") +
  theme_void() +
  theme(
    plot.title = element_text(size = 16, face = "bold", hjust = 0.5, color = "white")
  )

# Save the updated plot
ggsave("/home/cybersec/python_projects/R/E-commerce_Sales_Analysis2/proportion_of_total_sales_by_category.jpg", plot = plot5, width = 10, height = 6)

