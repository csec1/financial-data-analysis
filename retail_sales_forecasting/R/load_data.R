# load_data.R
library(readxl)

# Load the data
data <- read_excel("data/Online_Retail.xlsx")

# Print the first few rows to confirm data is loaded
print(head(data))

# Save output
writeLines(c("First 5 rows of data:\n", capture.output(head(data))), "output/analysis_output.txt")
