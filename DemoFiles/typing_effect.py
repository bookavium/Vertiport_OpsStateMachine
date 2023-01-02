import time
import colorama
from colorama import init, Fore, Back, Style
colorama.init(autoreset=False)



def slow_print(msg):
    for c in msg:
        print(c, end="", flush=True)
        time.sleep(0.01)
    print()

print(Fore.LIGHTBLUE_EX, end="")
slow_print("""

                    {
                        "UPLOADING THE FLIGHT PLAN": {
                        "VTOLId": "0x1bf29d1fd7",
                        "VTOLModel": "eBEE",
                        "VTOLType": "143GM",
                        "VTOLPropulsion": "tilt",
                        "VTOLTaxi": "hoover",
                        "nOfPaxMax": 4,
                        "flightRulesCapabilities": "VFR",
                        "flightControl": "remote"
                      },
                      "FlightPlan": {
                        "DepVertiport": "KVTOL",
                        "ArrVertiport": "KVTOM",
                        "EstimatedDepartureTime": "07:34:45.6",
                        "EstimatedFlightTime": 23,
                        "EstimatedArrivalTime": "07:32:21.4"
                      },
                      "Arrival": {
                        "ArrivalPoint": "Sierra_2",
                        "Est_TimeOverPoint": "07:35:23.1"
                      },
                      "ApproachLanding": {
                        "LandingFATO": "Pad_2",
                        "Est_LandingTime": "07:35:27.4"
                      },
                      "TaxiPark": {
                        "Taxiway": "Sierra_4",
                        "Stand": "Stand_3",
                        "Est_TimeAtStand": "07:35:34.2"
                      },
                      "TurnAround": {
                        "DeVTOLTime": "07:35:49.1",
                        "ChargingTime": 48,
                        "OnVTOLTime": "07:45:23.2"
                      }
                    }

        
        
        
""")
print(Style.RESET_ALL, end="")
