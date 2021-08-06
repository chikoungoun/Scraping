def get_ship_position(ship_id):
    import requests

    url = "https://www.marinetraffic.com/vesselDetails/latestPosition/shipid:{}".format(ship_id)

    headers = {
        "accept": "application/json",
        "accept-encoding": "gzip, deflate",
        "user-agent": "Mozilla/5.0",
        "x-requested-with": "XMLHttpRequest"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    return response.json()


def main():

    from datetime import datetime

    data = get_ship_position("371441")
    print(data)
    ts = datetime.utcfromtimestamp(data["lastPos"])
    print("Last known position: {} / {} @ {}".format(data["lat"], data["lon"], ts))
    print("Speed : ",data['speed'])
    print("Status : ",data['shipStatus'])
    print("Area : ",data['areaCode'])
    print("Area Name : ",data['areaName'])


    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
