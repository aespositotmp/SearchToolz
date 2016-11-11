from datetime import datetime
import json


class PayloadOutPut:
    def query_output_txt(result, search_term):
        today = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        parsed = json.dumps(result, indent=4)

        output_name = search_term + ' ' + today + '.txt'

        with open(output_name, "wt") as out_file:
            out_file.write(parsed)
