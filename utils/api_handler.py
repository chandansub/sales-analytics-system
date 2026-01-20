import requests


def fetch_all_products():
    url = "https://dummyjson.com/products?limit=100"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("products", [])
    except Exception:
        return []


def create_product_mapping(products):
    mapping = {}
    for p in products:
        pid = p.get("id")
        if pid is not None:
            mapping[pid] = {
                "category": p.get("category"),
                "brand": p.get("brand"),
                "rating": p.get("rating"),
            }
    return mapping


def enrich_sales_data(transactions, product_mapping):
    enriched = []

    for t in transactions:
        new_t = t.copy()
        try:
            pid = int("".join(filter(str.isdigit, t.get("ProductID", ""))))
        except Exception:
            pid = None

        if pid in product_mapping:
            new_t["API_Category"] = product_mapping[pid]["category"]
            new_t["API_Brand"] = product_mapping[pid]["brand"]
            new_t["API_Rating"] = product_mapping[pid]["rating"]
            new_t["API_Match"] = True
        else:
            new_t["API_Category"] = None
            new_t["API_Brand"] = None
            new_t["API_Rating"] = None
            new_t["API_Match"] = False

        enriched.append(new_t)

    return enriched
