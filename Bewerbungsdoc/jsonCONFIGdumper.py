import json
my_config = {
    "main_menu": ["Quit&Save","Show Data","Edit Data"],
    "create_menu": ["Quit&Save", "Main Menu", "Create Item", "Change Item", "Delete Item"],
    "show_menu": ["Quit&Save", "Main Menu","All", "ByIndex", "Search", "Sort after"],
    "csv_data": "data.csv",
    "sep": ";",
    "status__auswahl": sorted(["Bearbeitung","Anschauen","Wiedervorlage","Absage","Uninteressant"])
}
with open("config.json", "w") as f: 
    json.dump(my_config, f)
    