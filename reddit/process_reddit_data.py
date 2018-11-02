import csv


# extr
def process_reddit_data():
    # the header for the final file
    all_comments = [["hurricane name", "time", "title", "comment"]]
    # from the reddit cleaned data , extract the name of the hurricane, time, the title and the comment
    with open("./reddit_cleaned_data.csv", 'r') as file:
        reader = csv.reader(file, delimiter=',')
        reddit_cleaned = list(reader)
        # column 1: hurricane name
        # column 7: comment time
        # column 2: tht title the comment is under
        # column 6: the comment
        ll = [[line[1], line[7], line[2], line[6]] for line in reddit_cleaned[1:]]
        all_comments.extend(ll)
        # save as csv file
        with open("./reddit_data.csv", 'w') as save_file:
            writer = csv.writer(save_file, delimiter=',')
            writer.writerows(all_comments)
    return


if __name__ == "__main__":
    process_reddit_data()
