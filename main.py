import json

INPUT_FILE = "input.csv"

# TODO реализовать конвертер из csv в json

def csv_to_list_dict() -> list[dict]:
    list_dik = []
    list_rows = []
    with open (filename, 'r') as f:
        result = f.readlines()
        headers = result[0].rstrip.split(sep=",")
        for row in result[1:]:
            list.rows.append(row.rstrip().split(sep=','))

        for element in list_rows:
            a={k:v for k, v in zip(headers, element)}
            list_dik.append(a)


    return list_dik
print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
