def is_right(test_sample, func):
    predict = test_sample[-1]
    test = func(test_sample[:-1])
    if predict == test:
        return True, predict, test
    else:
        return False, predict, test




type_of_triangle = {
    0: 'Out of range',
    1: 'Not triangle',
    2: 'Scalene',
    3: 'Isosceles',
    4: 'Equilateral'
}

description = r'''Input the three sides of the triangle to judge whether it can form a triangle. If a triangle is formed, judge the type of the triangle.'''

def decide_triangle_type(test_sample):
    a, b, c = test_sample

    if not (1 <= a <= 100 and 1 <= b <= 100 and 1 <= c <= 100):
        return 0
    elif a+b <= c or b + c <= a or a + c <= b:
        return 1
    else:
        if a == b and b == c and a == c:
            return 4
        elif a == b or b == c or a == c:
            return 3
        else:
            return 2
