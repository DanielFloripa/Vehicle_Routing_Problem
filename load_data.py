import csv


class LoadData(object):
    def __init__(self, class_type, file):
        self.csv_file = file
        self.list_from_file = self.__load_file()
        self.list = self.object_creator(class_type)

    def __repr__(self):
        return repr(self.list)

    def object_creator(self, class_type):
        return [class_type(obj) for obj in self.list_from_file[1:]]

    def __load_file(self):
        with open(self.csv_file, "r") as fp:
            load = csv.reader(fp)
            return [line for line in load]