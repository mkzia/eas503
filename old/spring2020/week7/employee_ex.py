from abc import ABC, abstractmethod


class Employee(ABC):

    def __init__(self, first_name, last_name, ssn):
        self.first_name = first_name
        self.last_name = last_name
        self.ssn = ssn

    @abstractmethod
    def earnings(self):
        pass

    def __repr__(self):
        return f'{self.first_name} {self.last_name}\nsocial security: {self.ssn}'


class SalariedEmployee(Employee):

    def __init__(self, first_name, last_name, ssn, salary):
        super().__init__(first_name, last_name, ssn)
        self.weekly_salary = salary

    def earnings(self):
        return self.weekly_salary

    def __repr__(self):
        # return 'salaried employee: ' + super().__repr__() + '\nweekly salary: $' + str(self.weekly_salary)
        return f'salaried employee: {super().__repr__()}\nweekly salary: ${self.weekly_salary}'


class HourlyEmployee(Employee):
    
    def __init__(self, first_name, last_name, ssn, hourly_wage, hours_worked):
        super().__init__(first_name, last_name, ssn)
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked


    def earnings(self):
        if self.hours_worked > 40:
            return (40 * self.hourly_wage) + (self.hours_worked-40) * 1.5 * self.hourly_wage
        else:
            return self.hours_worked * self.hourly_wage

    def __repr__(self):
        return f'hourly employee: {super().__repr__()}\nhourly wage: ${self.hourly_wage}; hours worked: {self.hours_worked}'



class CommissionEmployee(Employee):
    def __init__(self, first_name, last_name, ssn, sales, rate):
        super().__init__(first_name, last_name, ssn)
        self.sales = sales
        self.rate = rate


    def earnings(self):
       return self.sales * self.rate


    def __repr__(self):
        return f'commission employee: {super().__repr__()}\ngross sales: ${self.sales}; commission rate: {self.rate}'


class BasePlusCommissionEmployee(CommissionEmployee):
    def __init__(self, first_name, last_name, ssn, sales, rate, salary):
        super().__init__(first_name, last_name, ssn, sales, rate)
        self.salary = salary

    def earnings(self):
        earned = self.salary + super().earnings()
        return earned

    def __repr__(self):
        return f'base-salaried {super().__repr__()}; base-salary: ${self.salary}'

se1 = SalariedEmployee('john', 'doe', '111-22-3333', 1000)

he1 =  HourlyEmployee('Jane', 'Doe', '333-33-3333', 50, 75)

ce1 = CommissionEmployee('John', 'Smith', '444-44-4444', 80, 80)


print(se1, se1.earnings())
print(he1, he1.earnings())
print(ce1, ce1.earnings())
print()
