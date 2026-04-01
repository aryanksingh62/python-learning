import os
import json

INPUT_FILE="nested_data.json"
OUTPUT_FILE="flattened_data.json"

def flatten(data,parent_key=""):
    items={}
    for key in data:
        if parent_key=="":
            full_key=key
        else:
            full_key= parent_key + "." + key

        if isinstance(data[key],dict):
            items.update(flatten(data[key],full_key))
            
        elif isinstance(data[key],list):
            for i, j in enumerate(data[key]):
                list_key = full_key + "." + str(i)
                if isinstance(j,dict):
                    nested=flatten(j,list_key)
                    items.update(nested)  
                else:
                    items[list_key]=j
        else:
            items[full_key]= data[key]
    return items

def main():
    if not os.path.exists(INPUT_FILE):
        print("NO input file found")
        return
    try:
        with open(INPUT_FILE,"r",encoding="utf-8") as f:
            data =json.load(f)
        
        flatten_data = flatten(data)
        with open(OUTPUT_FILE,"w",encoding="utf-8") as f:
            json.dump(flatten_data,f,indent=2)
        print(f"flatten Json data {OUTPUT_FILE}")

    except Exception as e:
        print("Failed to flatten the data",e)

if __name__=="__main__":
    main()