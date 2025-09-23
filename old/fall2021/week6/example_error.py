def calculate_bmi(height, weight):

    if type(height) not in [float, int]:
        raise TypeError('Height has to be float or an int')

    if type(weight) not in [float, int]:
        raise TypeError('Weight has to be float or an int')

    if height <= 0:
        raise ValueError('Height cannot be less than or equal to 0')

    if weight <= 0:
        raise ValueError('Weight cannot be less than or equal to 0')

    return 703 * weight / height**2

calculate_bmi('1000', 100)