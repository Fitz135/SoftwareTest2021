import math


def calculate_comm_fee(test_sample):
    minutes, n_overdue, discount = test_sample
    
    #注入bug
    # if minutes <= 0 or minutes >= 44640:
    #     return -1

    max_overdue = math.ceil(minutes/60)
    if 1 <= max_overdue <= 6:
        max_overdue = max_overdue
    else:
        max_overdue = 6

    basic_part, comm_part = 25, 0
    # 逾期次数少于限额,可以享受折扣

    if 0 <= n_overdue <= 11:
        if n_overdue <= max_overdue:
            comm_part = 0.15 * (1 - discount) * minutes
        else:
            comm_part = 0.15 * 1 * minutes
        total_part = basic_part + comm_part
        return total_part
    else:
        return -1


if __name__ == "__main__":
    print(calculate_comm_fee([60, 0, 0.01]))
    print(calculate_comm_fee([60, 6, 0]))
