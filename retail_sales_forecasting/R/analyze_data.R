# analyze_data.R
library(dplyr)

# Load data
data <- read_excel("data/Online_Retail.xlsx")

# Data analysis: Total sales by country
total_sales_by_country <- data %>%
  group_by(Country) %>%
  summarise(TotalSales = sum(Quantity, na.rm = TRUE))

# Print summary
print(total_sales_by_country)

# Save analysis output
write.table(total_sales_by_country, "output/total_sales_by_country.csv", sep = ",", row.names = FALSE)
