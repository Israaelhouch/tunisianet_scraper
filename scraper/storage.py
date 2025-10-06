
import json

def save_to_csv(products, csv_writer):
    for p in products:
        csv_writer.writerow([
            p["name"],
            p["price"],
            p["image"],
            p["availability"],
            p["description"],
            p["url"],
            p.get("main_category", ""),
            p.get("sub_category", "")
        ])

def save_to_json(products, json_file):
    try:
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)
    except:
        data = []
    data.extend(products)
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
