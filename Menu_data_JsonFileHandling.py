import json
import pprint
import logging
from datetime import datetime

log_filename = f"Menu_data_JsonFileHandling_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

logging.basicConfig(
    level=logging.INFO,  
    format="%(levelname)s : %(message)s",
    handlers=[
        logging.FileHandler(log_filename, mode='w'),  # Save logs in file
        logging.StreamHandler()                       # Also show logs in console
    ]
)

logging.info("Program started")


try:
    with open(r"C:/Users/joshi/Downloads/menu_items.json",mode='r') as file:
        data = json.load(file) 
    logging.info("JSON file loaded successfully")

except FileNotFoundError:
    logging.error("Error: The JSON file was not found.")
    exit()

except json.JSONDecodeError:
    logging.error("Error: The file is not a valid JSON format.")
    print("Error: The file is not a valid JSON format.")
    exit()
   
except Exception as e:
    logging.exception(f"Unexpected error while loading JSON: {e}")
    print("An unexpected error occurred:", e)
    exit()

else:
    # 1.
    # Get all the Categories in the menu
    def all_menu_categories():
        try:
            menu_list=[]
            for menu in data:
                menu_list.append(menu['name'])
                return menu_list
        except Exception as e:
            logging.exception("Error fetching menu categories: %s", e)
            return []
        
    AllCategories=all_menu_categories()
    pprint.pprint(AllCategories)

    # 2. Find All Appetizers 
    # Extract and print the name of every menu item that belongs to the "Appetizers" category. 
    def Find_All_Appetizers(Appetizers={}, app_list=[]):
        try:
            for i in data:
                if i['name']=="Appetizers":
                    for j in i["menuItems"]:
                        print(j["name"])
                        app_list.append(j["name"])
                Appetizers["Appetizers"]=app_list
                return Appetizers
        except Exception as e:
            logging.exception("Error finding appetizers: %s", e)
            return {}

    AllAppetizers=Find_All_Appetizers()
    pprint.pprint(AllAppetizers)


    # 3.Find Average Price of Non-Alcoholic Beverages
    
    def NonAlcoholicBeverages(Non_Alcoholic_Beverages=[]):
        try:
            for B in data:
                if B["name"]=="Beverages":
                    for items in B["subCategories"]:
                        if items["name"]=="Non Alcoholic Beverages":
                            for k in items["menuItems"]:
                                Non_Alcoholic_Beverages.append(k['customConfigs'][0]["itemPrice"])
            avg=sum(Non_Alcoholic_Beverages)/len(Non_Alcoholic_Beverages)
            logging.info("Average Non-Alcoholic Beverage price calculated successfully")
            return avg
        except Exception as e:
            logging.exception("Error calculating Non-Alcoholic Beverage average: %s", e)
            return 0
    
    NAB=NonAlcoholicBeverages()
    print(NAB)

    #4. Find Items with Multiple Sizes 
    # Some menu items, like "Chkn Tender Bskt," come in different sizes (e.g., "SM" and "LG"). Write 
    # a script to find and print the name of all items that have more than one size option in their 
    # customConfigs.
    def Find_Items_with_Multiple_Sizes():
        try:
            Multy_Items={}
            for a in data:
                if a["menuItems"]:
                    for menu_list_items in a["menuItems"]:
                        if menu_list_items["customConfigs"] and len(menu_list_items["customConfigs"])>1:
                            if a['name'] not in Multy_Items:
                                Multy_Items[a["name"]]=[menu_list_items["name"]]
                            else:
                                Multy_Items[a["name"]].append(menu_list_items["name"])
            
                elif a["subCategories"]:
                    for menu_list_items in a["subCategories"]:
                        if menu_list_items["menuItems"]:
                            # pprint.pprint(menu_list_items["customConfigs"])
                            for k in menu_list_items["menuItems"]:
                                if len(k["customConfigs"])>1:
                                    if len(k["customConfigs"]) not in Multy_Items:
                                        # pprint.pprint(len(k["customConfigs"]))
                                        Multy_Items[a["name"]]=[k["name"]]
                                    else:
                                        Multy_Items[a["name"]].append(k["name"])
            logging.info("Items with multiple sizes fetched successfully")
            return Multy_Items
        except Exception as e:
            logging.exception("Error finding multiple size items: %s", e)
            return {}

    MultyItems=Find_Items_with_Multiple_Sizes()
    pprint.pprint(MultyItems)


    # 5. List All Wing Flavors 
    # The "Chicken Wings" item has several flavor options. Extract and print the name of each 
    # "Wing Flavor" available. 

    def Chicken_Wings_flavours():
        try:
            flavours=[]
            for menu_items in data:
                if menu_items["menuItems"]:
                    for chick_wing in menu_items["menuItems"]:
                            if chick_wing["name"]=="Chicken Wings":
                                for config in chick_wing["customConfigs"]:
                                        for k in config["mandatoryModifiers"]:
                                            if k["name"]=="Wing Flavor":
                                                for res in k.get("modifiers",[]):
                                                    flavours.append(res["name"])
            logging.info("Chicken wing flavors fetched successfully")
            return flavours
        except Exception as e:
            logging.exception("Error fetching chicken wing flavors: %s", e)
            return []

    CWF=Chicken_Wings_flavours()
    print(CWF)

    # 6.Identify Items with Mandatory Modifiers 
    # Some menu items require the customer to make a choice (e.g., a dipping sauce). Find and 
    # print the name of all menu items that have at least one mandatory modifier. 

    def  Mandatory_Modifiers():
        try:
            mandatoryModifiers={}
            for menu_items in data:
                if menu_items["menuItems"]:
                    for items in menu_items["menuItems"]:
                        if items["customConfigs"]:
                            for x in items["customConfigs"]:
                                if len(x["mandatoryModifiers"])>=1:
                                    if len(x["mandatoryModifiers"]):
                                        items["name"]=[len(x["mandatoryModifiers"])]
                                    else:
                                        items["name"].append(len(x["mandatoryModifiers"]))
            logging.info("Mandatory modifier items fetched successfully")
            return mandatoryModifiers
        except Exception as e:
            logging.exception("Error finding mandatory modifiers: %s", e)
            return {}
    User_mandatoryModifiers=Mandatory_Modifiers()
    pprint.pprint(User_mandatoryModifiers)

    # # mandatoryModifiers={}
    # for menu_items in data:
    #     if menu_items["menuItems"]:
    #         for items in menu_items["menuItems"]:
    #             if items["havingMandatoryModifier"]:
    #                 print(items["name"])

    # 7.Count the Number of Salads 
    # Count and print the total number of unique menu items available in the "Salads & Soups" 
    # category. 

    def Count_the_Number_of_Salads():
        try:
            salads_soups_menu=[]
            for menu_items in data:
                if menu_items["name"]=="Salads & Soups":
                    for sal_soup in menu_items["menuItems"]:
                        if sal_soup["name"] not in salads_soups_menu:
                            salads_soups_menu.append(sal_soup["name"])
            logging.info("Salad count fetched successfully")
            return len(salads_soups_menu)
        except Exception as e:
            logging.exception("Error counting salads: %s", e)
            return 0

    count_salads=Count_the_Number_of_Salads()
    pprint.pprint(count_salads)


    # 8. Find the Most Expensive Item 
    # Iterate through all menu items across all categories and find the one with the highest 
    # itemPrice. Print the item's name and its price. 
    def Find_the_Most_Expensive_Item(max_p=0):
        try:
            max_price=[]
            for menu_items in data:
                if menu_items["menuItems"]:
                    for items in menu_items["menuItems"]:
                        if items["customConfigs"]:
                            for x in items["customConfigs"]:
                                max_p=x["itemPrice"]
                                if max_price==[]:
                                    max_price.append((items["name"],x["itemPrice"]))
                                elif max_price!=[] and max_p<x["itemPrice"]:
                                    max_price=(items["name"],x["itemPrice"])
            logging.info("Most expensive item fetched successfully")
            return max_price
        except Exception as e:
            logging.exception("Error finding most expensive item: %s", e)
            return None, 0

    ExpensiveItem=Find_the_Most_Expensive_Item()
    print(ExpensiveItem)

    # 9.Group Items by Price Range 
    # Create a Python script that categorizes all menu items into three price ranges: 
    # ● Cheap: Under $8.00 
    # ● Moderate: $8.00 - $12.00 
    # ● Expensive: Over $12.00 

    def Group_Items_by_Price_Range(cheap={},moderate={},Expensive={}):
        for a in data:
            if a["menuItems"]:
                for menu_list_items in a["menuItems"]:
                    if menu_list_items["customConfigs"]:
                        for price_data in menu_list_items["customConfigs"]:
                            if price_data["itemPrice"]/100<8:
                                cheap[menu_list_items["name"]]=price_data["itemPrice"]
                            elif 12>price_data["itemPrice"]/100>8:
                                moderate[menu_list_items["name"]]=price_data["itemPrice"]
                            elif price_data["itemPrice"]/100>12:
                                Expensive[menu_list_items["name"]]=price_data["itemPrice"]
            
            elif a["subCategories"]:
                for menu_list_items in a["subCategories"]:
                    if menu_list_items["menuItems"]:
                        for k in menu_list_items["menuItems"]:
                            for price_data in k["customConfigs"]:
                                if price_data["itemPrice"]/100<8:
                                    cheap[k["name"]]=price_data["itemPrice"]
                                elif 12>price_data["itemPrice"]/100>8:
                                    moderate[k["name"]]=price_data["itemPrice"]
                                elif price_data["itemPrice"]/100>12:
                                    Expensive[k["name"]]=price_data["itemPrice"]
        return print(f"cheap:\n {cheap}\n Moderate:\n {moderate}\n Expensive:\n {Expensive}")
    ArangedAsPrice=Group_Items_by_Price_Range()


    # 10. Create a Simple Menu Dictionary 
    # Write a script to transform the JSON data into a simpler dictionary where the keys are the 
    # main category names (e.g., "Appetizers," "Beverages") and the values are a list of the menu 
    # item names in that category. Print the resulting dictionary. 
    def Simple_Menu_Dictionary():
        try:
            menu={}
            for items in data:
                if items["menuItems"]:
                    for item_name in items["menuItems"]:
                        if items["name"] not in menu:
                            menu[items["name"]]=[item_name["name"]]
                        else:
                            menu[items["name"]].append(item_name["name"])
            logging.info("Simple menu dictionary created successfully")
            return menu
        except Exception as e:
            logging.exception("Error creating simple menu dictionary: %s", e)
            return {}
            
    MENU=Simple_Menu_Dictionary()
    pprint.pprint(MENU)
logging.info("Program finished successfully")