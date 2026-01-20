# Sales Analytics System

This project is a Sales Analytics System built using Python as part of a graded assignment.  
The main aim of this project is to work with raw sales transaction data, clean and validate it, perform basic sales analysis, enrich product information using an API, and generate a final sales report.

The project follows a step-by-step approach where data is first read from a file, processed, analyzed, and finally written into a report file.

## Project Structure

sales-analytics-system/
├── README.md  
├── main.py  
├── utils/  
│   ├── file_handler.py  
│   ├── data_processor.py  
│   └── api_handler.py  
├── data/  
│   └── sales_data.txt  
├── output/  
│   └── sales_report.txt  
└── requirements.txt  

## What This Project Does

- Reads sales data from a text file  
- Cleans and validates transaction records  
- Separates valid and invalid records  
- Calculates total revenue  
- Performs region-wise sales analysis  
- Finds top selling products  
- Enriches product data using an external API  
- Generates a final sales report  

## How to Run the Code

1. Make sure Python 3 is installed on your system  
2. Open the terminal or command prompt inside the project folder  
3. Install required dependencies using:  

   pip install -r requirements.txt  

4. Run the program using:  

   python main.py  

5. After execution, the output report will be generated inside the `output` folder.

## Output

- Console output showing processing details  
- A text file `sales_report.txt` containing the final sales analysis  

## Submission Details

- All files are pushed to a GitHub repository  
- Proper folder structure is maintained  
- This README explains how to run the code  
- The repository link is submitted for evaluation  
