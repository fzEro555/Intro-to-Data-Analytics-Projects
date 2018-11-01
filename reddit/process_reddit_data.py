import csv


def process_reddit_data():
    all_comments = [["hurricane name", "time", "title", "comment"]]
    with open("./reddit_cleaned_data.csv", 'r') as file:
        reader = csv.reader(file, delimiter=',')
        reddit_cleaned = list(reader)
        ll = [[line[1], line[7], line[2], line[6]] for line in reddit_cleaned[1:]]
        all_comments.extend(ll)
        with open("./reddit_data.csv", 'w') as save_file:
            writer = csv.writer(save_file, delimiter=',')
            writer.writerows(all_comments)
    return


if __name__ == "__main__":
    process_reddit_data()
