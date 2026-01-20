from utils.file_handler import read_sales_file
from utils.data_processor import (
    parse_transactions,
    validate_transactions,
    total_revenue,
    region_wise_sales,
    top_products,
    generate_sales_report
)
from utils.api_handler import (
    fetch_all_products,
    create_product_mapping,
    enrich_sales_data
)


def main():
    print("Sales Analytics System Started")

    # Read sales data
    lines = read_sales_file("data/sales_data.txt")
    transactions = parse_transactions(lines)

    # Validate data
    valid_records, invalid_records = validate_transactions(transactions)
    print(f"Valid records: {len(valid_records)}")
    print(f"Invalid records: {len(invalid_records)}")

    # Basic analysis
    print("Total Revenue:", total_revenue(valid_records))
    print("Region-wise Sales:", region_wise_sales(valid_records))
    print("Top Products:", top_products(valid_records))

    # API integration
    products = fetch_all_products()
    product_mapping = create_product_mapping(products)
    enriched_data = enrich_sales_data(valid_records, product_mapping)

    # Generate report
    generate_sales_report(valid_records, enriched_data)

    print("Sales report generated successfully in output/sales_report.txt")


if __name__ == "__main__":
    main()
