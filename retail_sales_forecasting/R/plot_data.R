# plot_data.R
library(ggplot2)

# Load data
data <- read_excel("data/Online_Retail.xlsx")

# Plot data (e.g., plot sales per country)
plot <- ggplot(data, aes(x = Country, fill = Country)) +
  geom_bar() +
  theme(axis.text.x = element_text(angle = 90, hjust = 1)) +
  labs(title = "Sales by Country", x = "Country", y = "Sales Count")

# Save plot as PNG
ggsave("output/sales_by_country.png", plot)
