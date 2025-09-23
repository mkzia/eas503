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
        return f'salaried employee: {super().__repr__()}\nweekly salary: ${self.weekly_salary}'


class HourlyEmployee(Employee):
    def __init__(self, first_name, last_name, ssn, hourly_wage, hours_worked):
        super().__init__(first_name, last_name, ssn)
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked

    def earnings(self):
        if self.hours_worked < 40:  # no overtime
            earned = self.hourly_wage * self.hours_worked
        else:
            earned = 40 * self.hourly_wage + \
                (self.hours_worked - 40) * self.hourly_wage * 1.5

        return earned

    def __repr__(self):
        return f'hourly employee: {super().__repr__()}\nhourly wage: ${self.hourly_wage}; hours worked: {self.hours_worked}'


class CommissionEmployee(Employee):
    def __init__(self, first_name, last_name, ssn, sales, rate):
        super().__init__(first_name, last_name, ssn)
        self.sales = sales
        self.rate = rate

    def earnings(self):
        earned = self.sales * self.rate
        return earned

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


print('Employees processed individually:\n')
salaried_employee = SalariedEmployee('John', 'Smith', '111-11-1111', 800)
print(salaried_employee)
print(f'earned: ${salaried_employee.earnings()}')

print()
hourly_employee = HourlyEmployee('Karen', 'Price', '222-22-2222', 16.75, 40)
print(hourly_employee)
print(f'earned: ${hourly_employee.earnings()}')

print()
commission_employee = CommissionEmployee('Sue', 'Jones', '333-33-3333', 10000, 0.06)
print(commission_employee)
print(f'earned: ${commission_employee.earnings()}')


print()
base_plus_commission_employee = BasePlusCommissionEmployee('Bob', 'Lewis', '444-44-4444', 5000, 0.04, 300)
print(base_plus_commission_employee)
print(f'earned: ${base_plus_commission_employee.earnings()}')


employees = [salaried_employee, hourly_employee,
             commission_employee, base_plus_commission_employee]

for employee in employees:
    print()
    print(employee)
    if employee.__class__.__name__ == 'BasePlusCommissionEmployee':
        employee.salary = 1.10 * employee.salary
        print(f'new base salary with 10% increase is {employee.salary}')
    print(f'earned: ${employee.earnings()}')

