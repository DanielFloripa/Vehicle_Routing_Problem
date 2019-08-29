import csv


class LoadData(object):
    def __init__(self, class_type, file, has_header=False):
        self.csv_file = file
        self.has_header = has_header
        self.header = []
        self.list_of_lines = self.__load_file()
        self.list = self.object_creator(class_type)

    def __repr__(self):
        return repr(self.list)

    def object_creator(self, class_type):
        self.header = self.list_of_lines.pop(0) if self.has_header else []
        return [class_type(obj) for obj in self.list_of_lines]

    def __load_file(self):
        with open(self.csv_file, "r") as fp:
            loading = csv.reader(fp)
            return [line for line in loading]
