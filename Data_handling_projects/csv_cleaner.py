import csv
from pathlib import Path

INPUTFILE= "messy.csv"
OUTPUTFILE ="clean.csv"
def cleaner(input_file):
    if not Path(input_file).exists():
        print("Invalid File")
        return None, None
    rem_dup=set()
    data=[]
    with open(input_file,"r",newline="") as f:
        reader= csv.reader(f)
        header= next(reader)
        for line in reader:
            
            if len(line)==0 or all(value == "" for value in line) :
                continue
            if len(line) < len(header):
                continue
            if line[0] == "" or line[2] == "":
                continue
            if tuple(line) not in rem_dup: 
                rem_dup.add(tuple(line))
                data.append(tuple(line))

    return data, header

def save_to_clean(data,header): 
    with open(OUTPUTFILE,"w",newline="") as f:
        writer= csv.writer(f)
        writer.writerow(header)
        for line in data:
            writer.writerow(line)
        
        print(f"{INPUTFILE} is succesfully cleaned. ")
if __name__=="__main__":
    
    data,header=cleaner(INPUTFILE)
    if data is not None:
        save_to_clean(data,header)