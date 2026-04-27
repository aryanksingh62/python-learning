import json
import csv
from pathlib import Path

def read_data(input_file):

    if not Path(input_file).is_file():
        print("Invalid file")
        return
    try:
        with open(input_file,"r",encoding="utf-8") as f:
            reader= csv.DictReader(f)
            data= list(reader)
            return data
    except Exception as e:
        print(f"failed to read the file\n{e}") 

def empty_remove(data):
    output_file="valid_details.json"
    count=1
    kept_row=[]
    for row in data:
        if not any(row[field]=="" for field in ["Email","Country","Company"]):
            row["Index"]=str(count)
            kept_row.append(row) 
            count+=1

    if len(kept_row)!=len(data):
        save_data(kept_row,output_file)
        print("✅ Succesfully clean details")
    else:
        print(f"There is no important detail which is empty")

def filter_by_country(data):

    output_file="filter_by_country.json"
    country= input("enter the country name:").lower().strip()
    result=[row for row in data if row["Country"].lower()==country]
    if result:
        save_data(result,output_file)
        print(f"total ={len(result)}, details saved successfully into {output_file}")
    else:
        print(f"no matching details found by the country name - {country}")

    
def save_data(data,output_file):
    with open(output_file,"w") as f:
        json.dump(data,f,indent=2)

def main():
    INPUT_FILE="sample.csv"
    data= read_data(INPUT_FILE)
    if data:
        print("what operation do you want to perform on the file")
        print("-"*20)
        print("1. clean and convert to json")
        print("2. Filter the details by country name")
        choice= int(input("Enter your choice between(1-2)").strip())
        match choice:
            case 1: empty_remove(data)
            case 2: filter_by_country(data)     
    else:
        print(f"{INPUT_FILE} file is emmpty")

if __name__=="__main__":
    main()
