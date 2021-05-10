def calculate_computer_commission(test_sample):
    host = test_sample[0]
    shower = test_sample[1]
    affliate = test_sample[2]
    payment = 0
    if host <= 0 or host > 70 or shower <= 0 or shower > 80 or affliate <= 0 or affliate > 90:
        return payment
    else:
        costs = host * 25 + shower *30 + affliate*45

    # costs = host * 25 + shower * 30 + affliate * 45
    
    if costs <= 1000:
        payment = 0.1 * costs
    elif 1000 < costs <= 1800:
        payment = 0.15 * costs
    elif costs > 1800:
        payment = 0.2 * costs
    return payment


if __name__ == "__main__":
    print(calculate_computer_commission([10,9,10]))
