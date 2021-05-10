class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def is_leap_year(self):
        if (self.year % 4 == 0 and not self.year % 100 == 0) or self.year % 400 == 0:
            return True
        else:
            return False

    def is_legal(self):
        if not (1800 <= self.year <= 2100 and 1 <= self.month <= 12 and 1 <= self.day <= 31):
            return False
        else:
            if self.month in [4, 6, 9, 11] and self.day > 30:
                return False
            if self.month == 2:
                if self.is_leap_year() and self.day > 29:
                    return False
                elif not self.is_leap_year() and self.day > 28:
                    return False
            return True

    def add_year(self):
        self.year = self.year + 1

    def add_month(self):
        if self.month == 12:
            self.month = 1
            self.add_year()
        else:
            self.month = self.month + 1

    def add_day(self):
        if not self.is_legal():
#            print('out')
            return False
        else:
            if self.day < 28:
                self.day = self.day + 1
            elif self.day == 28:
                if self.month == 2:
                    if self.is_leap_year():
                        self.day = 29
                    else:
                        self.day = 1
                        self.add_month()
                else:
                    self.day = self.day + 1
            elif self.day == 29:
                if self.month == 2:
                    self.day = 1
                    self.add_month()
                else:
                    self.day = 30
            elif self.day == 30:
                if self.month in [1, 3, 5, 7, 8, 10, 12]:
                    self.day = self.day + 1
                else:
                    self.day = 1
                    self.add_month()
            elif self.day == 31:
                self.day = 1
                self.add_month()
#            print(self.year, self.month, self.day)
            return True


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False


def get_month_days(year, month):
    if (month in (1, 3, 5, 7, 8, 10, 12)):
        return 31
    elif (month in (4, 6, 9, 11)):
        return 30
    elif (is_leap_year(year)):
        return 29
    else:
        return 28


def get_total_days(year, month, day):
    days = 0
    for i in range(1800, year):
        if (is_leap_year(i)):
            days += 366
        else:
            days += 365
    for j in range(1, month):
        days += get_month_days(year, j)
    days += day
    days -= 1
#    print(days)
    return days


def get_start_day(year, month, day):
    ans = (3 + get_total_days(year, month, day)) % 7
    #注入bug
    dict = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}
    return dict[ans]


def date_calculate(year, month, day):
    date = Date(year, month, day)
    if date.add_day():
#        print(get_start_day(date.year, date.month, date.day))
        string = str(date.year) + '/' + str(date.month) + '/' + str(date.day)
#        print(string)
        return get_start_day(date.year, date.month, date.day), string
    else:
#        print('error')
        return 'None', 'None'


if __name__ == "__main__":
    # 用于测试
    date_calculate(2021, 1, 1)
