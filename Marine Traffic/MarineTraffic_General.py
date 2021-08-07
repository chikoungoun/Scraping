import pandas as pd
import requests
from datetime import datetime

# fetch Vessel infos
def get_ship_info(ship_id):

    url ="https://www.marinetraffic.com/en/vesselDetails/vesselInfo/shipid:{}".format(ship_id)

    headers = {
        "accept": "application/json",
        "accept-encoding": "gzip, deflate",
        "user-agent": "Mozilla/5.0",
        "x-requested-with": "XMLHttpRequest"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    return response.json()

#fetch voyage infos
def get_ship_voyage(ship_id):

    url ="https://www.marinetraffic.com/vesselDetails/voyageInfo/shipid:{}".format(ship_id)

    headers = {
        "accept": "application/json",
        "accept-encoding": "gzip, deflate",
        "user-agent": "Mozilla/5.0",
        "x-requested-with": "XMLHttpRequest"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    return response.json()

# fetch vessel position data
def get_ship_position(ship_id):

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


    info = get_ship_info("371441")
    voyage = get_ship_voyage("371441")
    position = get_ship_position("371441")


    print("\n\n Info : ### \n",pd.Series(info))
    print("\n\n Voyage : ### \n",pd.Series(voyage))
    print("\n\n Position : ### \n",pd.Series(position))



    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
