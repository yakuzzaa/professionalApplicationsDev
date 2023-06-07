import csv
from datetime import datetime


class Reference:
    def __init__(self, number, date, fio, grant, destination):
        self.number = number
        self.date = date
        self.fio = fio
        self.grant = grant
        self.destination = destination


class CSVReader:
    def __init__(self):
        self._file_name = "data.csv"
        self._data: list[Reference] = []

        self._read_file(self._file_name)
        self._current_row = 0

    @classmethod
    def build_from_dict(cls, data: list[Reference]):
        instance = cls()
        instance._data = data
        return instance

    def __iter__(self):
        return self

    def __getitem__(self, item):
        return self._data[self._current_row].get(item)

    def __next__(self):
        if self._current_row >= len(self._data):
            self._current_row = 0
            raise StopIteration
        self._current_row += 1
        return self._data[self._current_row - 1]

    def generator(self):
        while self._current_row < len(self._data):
            yield self._data[self._current_row]
            self._current_row += 1

    def __repr__(self):
        return f'Row: {self._current_row}: {self._data[self._current_row]}'

    def _read_file(self, file_path):
        with open(file_path) as file:
            reader = csv.reader(file, delimiter=",")
            next(reader)  # skip header
            for row in reader:
                self._data.append(
                    {
                        "number": int(row[0]),
                        "data": datetime.strptime(row[1], "%d.%M.%Y"),
                        "fio": str(row[2]),
                        "grant": str(row[3]),
                        "destination": str(row[4]),
                    }
                )

    def new_entry(self, fio, grant, destination):
        self._data.append(Reference(number=len(self._data),
                                    data=datetime.now()),
                          fio=fio,
                          grant=grant,
                          destination=destination)

    def save(self):
        with open("new.csv", "w") as file:
            writer = csv.DictWriter(file, ['number', 'data', 'fio', 'grant', 'destination'])
            writer.writeheader()
            writer.writerows(self._data)

    def fio_sorting(self, key: str) -> list[Reference]:
        return sorted(self._data, key=lambda f: f["fio"])

    def grant_sorting(self, key: str) -> list[Reference]:
        return sorted(self._data, key=lambda f: f["grant"], reverse=True)

    def grant_more_than_sorting(self, key: str, value) -> list[Reference]:
        return [grant for grant in self._data if grant[key] > value]
