from flask import Flask, request

app = Flask(__name__)


@app.post('/zombie')
def zombie_risk():
    request_data = request.get_json()
    location = request_data["location"]

    # print(f"Checking risk for {location}")
    zombie_risk = calc_risk(location)
    return zombie_risk, 200

def calc_risk(location):

    # convert location to lower case
    location = location.lower()

    zombie_risk = {
        "message": "Sorry, I don't recognise your location, you're probably fine.",
        "risk": "0",
        "location": "Unknown"
    }

    match location:
        case "london":
            zombie_risk = {
                "message": "Keep calm and drink tea",
                "risk": "42",
                "location": "London, UK"
            }
        case "tokyo":
            zombie_risk = {
                "message": "Zero zombie cases reported in the last 90 days.",
                "risk": "0",
                "location": "Tokyo, Japan"
            }
        case "las vegas":
            zombie_risk = {
                "message": "Urgent, leave the city immediately, high likelihood of zombie attacks.",
                "risk": "95",
                "location": "Las Vegas, USA"
            }


    return zombie_risk


if __name__ == '__main__':
    app.run()
