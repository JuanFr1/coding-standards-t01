"""Module providing a Vacation Package Cost Estimator."""


class MyClass:
    """Class representing validations"""
    def __init__(self):
        self.my_fav = {'Paris': 500, 'NYC': 600}

    def get_extra_cost(self, dist):
        """Getter for the extra cost."""
        return self.my_fav.get(dist, 0)

    def valid_this(self, dist):
        """Function validating the instance."""
        return isinstance(dist, str)


class Passenger:
    """Class representing passengers"""
    def __init__(self, num):
        self.num = num

    def valid_number(self):
        """Function validating the number of passengers."""
        print("this working here")
        return isinstance(self.num, int) and self.num > 0

    def for_here_discount(self):
        """Function validating the discount."""
        if 4 < self.num < 10:
            return 0.1
        elif self.num >= 10:
            return 0.2
        else:
            return 0.0


class TotalTime:
    """Class representing the total time of vacation"""
    def __init__(self, dur):
        self.dur = dur

    def is_valid_total_time(self):
        """Function validating total time."""
        return isinstance(self.dur, int) and self.dur > 0

    def get_fee(self):
        """Getter for the fee."""
        return 200 if self.dur < 7 else 0

    def get_best_promo(self):
        """Getter for the best promo."""
        return 200 if self.dur > 30 else 0

    def get_weekend(self):
        """Getter for the weekend."""
        return 100 if self.dur > 7 else 0


class Vacation:
    """Class representing the vacation"""
    costBas = 1000

    def __init__(self, dist, num, dur):
        self.my_class = MyClass()
        self.passenger = Passenger(num)
        self.total_time = TotalTime(dur)
        self.dist = dist

    def sum(self):
        """Function summing the cost of the vacation package."""
        valid_class = self.my_class.valid_this(self.dist)
        valid_passenger = self.passenger.valid_number()
        valid_total_time = self.total_time.is_valid_total_time()
        if not valid_class or not valid_passenger or not valid_total_time:
            return -1

        # sum the total cost
        number_total = self.costBas
        number_total += self.my_class.get_extra_cost(self.dist)
        number_total += self.total_time.get_fee()
        number_total -= self.total_time.get_best_promo()

        discount = self.passenger.for_here_discount()
        number_total = number_total - (number_total * discount)

        return max(int(number_total), 0)


def destination_validator():
    """Function validating the destination."""
    valid_input = False
    while not valid_input:
        user_input = input("Write the destination of your vacation: ")

        while not user_input.isalpha():
            print("The destination is invalid.")
            user_input = input("Write the destination of your vacation: ")

        valid_input = True

    dist = user_input
    return dist


def passenger_number_validator():
    """Function validating the passenger numer."""
    valid_input = False
    while not valid_input:
        user_input = input("Write the number of passengers: ")

        while not user_input.isnumeric():
            print("The number of passengers is invalid.")
            user_input = input("Write the number of passengers: ")

        valid_input = True

    num = int(user_input)
    return num


def duration_validator():
    """Function validating the duration of the vacation."""
    valid_input = False
    while not valid_input:
        user_input = input("Write the duration of the vacation in days: ")

        while not user_input.isnumeric():
            print("The number of days is invalid.")
            user_input = input("Write the duration of the vacation in days: ")

        valid_input = True

    dur = int(user_input)
    return dur


# this is main function
def main():
    """Function initializing the program."""
    # this are the inputs
    dist = destination_validator()
    num = passenger_number_validator()
    dur = duration_validator()

    # this are the outputs
    calculator = Vacation(dist, num, dur)
    cost = calculator.sum()

    print(f"The total cost of the vacation package is: ${cost}")


# main event function
if __name__ == "__main__":
    main()
