import json
def read_json_data(name:str,encoding:str='utf8'):
    with open(name,encoding=encoding) as file:
        response = json.load(file)
    return response

def write_json_data(data:any,name:str,enconding:str='utf8'):
    with open(name,"w",encoding=enconding) as file:
        json.dump(data,file,ensure_ascii=False,indent=4)

