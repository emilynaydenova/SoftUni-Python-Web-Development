from calendar import month_name


class DVD:
    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_month = creation_month
        self.creation_year = creation_year
        self.age_restriction = age_restriction

        self.is_rented = False

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        dd, mm, yy = [int(x) for x in date.split('.')]
        month = month_name[mm]
        return cls(name, id, yy, month, age_restriction)

    def __repr__(self):
        flag = 'rented' if self.is_rented else 'not rented'
        return f'{self.id}: {self.name} ({self.creation_month} {self.creation_year}) ' \
               f'has age restriction {self.age_restriction}. ' \
               f'Status: {flag}'
