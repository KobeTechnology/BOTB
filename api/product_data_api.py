def get_product_data(company_profile):
    company = company_profile["company"]

    if company == "Dell":
        return {
            "company": "Dell",
            "product": "Dell Inspiron 15",
            "battery_life": "10 hours",
            "price": "$699",
            "availability": "In Stock"
        }

    elif company == "HP":
        return {
            "company": "HP",
            "product": "HP Pavilion 15",
            "battery_life": "9 hours",
            "price": "$649",
            "availability": "In Stock"
        }

    elif company == "Lenovo":
        return {
            "company": "Lenovo",
            "product": "Lenovo IdeaPad 3",
            "battery_life": "8 hours",
            "price": "$599",
            "availability": "In Stock"
        }

    return {
        "company": company,
        "product": company_profile["product"],
        "battery_life": "Unknown",
        "price": "Unknown",
        "availability": "Unknown"
    }
