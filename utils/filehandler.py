def read_sales_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return file.readlines()
    except Exception as e:
        print("Error reading file:", e)
        return []


def write_file(filepath, content):
    try:
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)
    except Exception as e:
        print("Error writing file:", e)
