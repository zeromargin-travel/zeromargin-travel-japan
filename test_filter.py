def is_match(spot_category, category_param):
    c = spot_category.lower()
    if category_param == 'Café' and not ('café' in c or 'bistro' in c or 'restaurant' in c):
        return False
    return True

print("Result:", is_match("Landmark", "Café"))
