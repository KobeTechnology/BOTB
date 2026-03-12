def check_product_data(ai_value, real_value):
    if ai_value != real_value:
        print("Mismatch detected between AI data and official data.")
        return False
    else:
        print("AI data matches official product data.")
        return True

if __name__ == "__main__":
    ai_battery = "16 hours"
    real_battery = "10 hours"

    check_product_data(ai_battery, real_battery)
