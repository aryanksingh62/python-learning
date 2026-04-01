import os 
import csv
import json

INPUT_FILE= "raw_data.csv"
OUTPUT_FILE= "coverted_data.json"

def load_csv_data(filename):
    if not os.path.exists(filename):
        print("no data to convert")
        return []
    try:
        with open(filename,"r",encoding="utf-8") as f:
            reader= csv.DictReader(f)
            data= list(reader)
            return data
    except:
        print("Invalid csv format")

def convert_data(data,output_file):
    if not data:
        print("no data to convert")
        return
    with open(output_file,"w",encoding="utf-8") as f:
        json.dump(data,f)
        print(f"converted {len(data)} records to {output_file}")
    
def preview_data(data,count=3):
    for row in data[:count]:
        print(json.dumps(row,indent=2))
    print(".......")


def main():
    print("csv to json")
    data=load_csv_data(INPUT_FILE)
    convert_data(data,OUTPUT_FILE)
    preview_data(data)
if __name__=="__main__":
    main()