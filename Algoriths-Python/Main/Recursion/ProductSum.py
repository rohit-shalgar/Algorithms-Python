# input - [5, 2, [7, -1], 3, [6, [-13, 8], 4]] is = 12 as this is calculated by the formula
# 1*(5+2)+2*(7-1)+3+2*(6+ 3*(-13+8)+4)
# 7+12+3+(-10) = 12
# as the degree of array increases we multiply by degree


def get_product_sum_helper(multiplier, number_array):
    product_sum: int = 0
    for number in number_array:
        if isinstance(number, list):
            product_sum = product_sum + get_product_sum_helper(multiplier + 1, number)
        else:
            product_sum = product_sum + number
    return product_sum * multiplier


def get_product_sum(number_array):
    return get_product_sum_helper(1, number_array)
