import json

def show_profile():
    profile_data = json.loads(open('profile.json',).read())
    portfolio_lenght = len(profile_data["having"])

    print("")
    print(profile_data["username"] + ',')
    print("Current Balence: " + profile_data["current-balence"])
    print("")
    print("Portfolio")

    i = 0
    while i < portfolio_lenght:
        print("")
        print(profile_data["having"][i]["bought-company"])
        print("Bought Price: ₹" + profile_data["having"][i]["bought-price"])
        print("Quantity: " + profile_data["having"][i]["bought-price"])
        i += 1
