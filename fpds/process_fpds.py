import csv


def tally(ll, hurricane, amount):
    if hurricane == "HURRICANE IRMA 2017":
        ll[1] += 1
        ll[5] += float(amount)
    elif hurricane == "HURRICANE HARVEY 2017":
        ll[2] += 1
        ll[6] += float(amount)
    elif hurricane == "HURRICANE MARIA 2017":
        ll[3] += 1
        ll[7] += float(amount)
    elif hurricane == "HURRICANE IRENE 2011":
        ll[4] += 1
        ll[8] += float(amount)
    else:
        # raise Exception("Unknown hurricane name in FPDS data. ")
        pass
    return


def process_fpds():
    # read in FPDS file
    with open("./FPDS_final.csv", 'r') as file:
        reader = csv.reader(file, delimiter=',')
        fpds = list(reader)
    # prepare dictionary, this will be a dictionary of date and a list
    # list = [date, number of contract for irma, number of contract for harvey,
    # number of contract for maria, number of contract for irene,
    # amount for irma, amount for harvey, amount for maria, amount for irene]
    all_days = {}
    # i_agency = 1
    i_date = 2
    i_hurricane = 6
    i_amount = 7
    for transaction in fpds[1:]:
        date = transaction[i_date].split(" ")[0]
        if date in all_days:
            tally(all_days[date], transaction[i_hurricane], transaction[i_amount])
        else:
            # this date doesn't exist in dictionary, insert this date
            all_days[date] = [date, 0, 0, 0, 0, 0, 0, 0, 0]
            tally(all_days[date], transaction[i_hurricane], transaction[i_amount])
    # save all items to csv
    all_days = list(all_days.values())
    header = ["date", "number of contract for irma", "number of contract for harvey",
              "number of contract for maria", "number of contract for irene",
              "amount for irma", "amount for harvey", "amount for maria", "amount for irene"]
    all_days.insert(0, header)
    with open("./FPDS.csv", 'w') as save_file:
        writer = csv.writer(save_file, delimiter=',')
        writer.writerows(all_days)
    return


if __name__ == "__main__":
    process_fpds()
