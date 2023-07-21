import re

class DataController:

    def prepare_datatype(self, element):
        joined_list = ' '.join([str(part) for part in element])

        joined_list = joined_list.replace('"', '')
        joined_list = joined_list.replace("'", "")
        joined_list = joined_list.replace("`", "")
        joined_list = joined_list.replace("{", "")
        joined_list = joined_list.replace("}", "")

        joined_list = re.sub(' +', ' ', joined_list)

        return str(joined_list)

