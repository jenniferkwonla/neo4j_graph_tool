
""" myutils module: has class CleanData with functions delete_symbols, remove_empty_cells
                    and class DataFile to write file,
                    and functions word_count
"""

class CleanData:
    def __init__(self):
        pass

    def delete_symbols(self, rows):
        """
        delete_symbol(self, rows): passes a list of dictionaries and deletes
        values with double quotes.
        Ex {'insights': ""Vitamin D.." Also, the patient..."}
        """
        symbols = ['"']
        for row in rows:
            for i, (key, value) in enumerate(row.items()):
                for s in symbols:
                    if s in str(value):

                        value = value.replace(s, '')
                        row[key] = value
        return rows

    def remove_empty_cell(self, rows):
        """
        remove_empty_cell(self, rows): passes a list of dictionaries and removes
        keys with "" or empty strings. This is done for implementing graphs in neo4j later.
        """

        return rows

class DataFile:
    def __init__(self, file_name):
        self.__file = open(file_name, 'w')
        self.__file.write('***** Start Data File *****\n\n')
        
    def write(self, str):
        self.__file.write(str)

    def writelines(self, str_list):
        self.__file.writelines(str_list)

    def __del__(self):
        self.close()

    def close(self):
        if self.__file:
            self.__file.write('\n\n***** End Data File *****')
            self.__file.close()
            self.__file = None

            
occurrences = {}
def word_count(text):
    occurrences_in_header = {}
    for word in text.split():
        occurrences [word] = occurrences.get(word, 0) + 1 
