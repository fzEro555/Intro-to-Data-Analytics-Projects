import csv
from Main.extract_reddit import leanify_reddit as process_reddit
from Main.combine_lean_data import combine_lean_data

if __name__ == "__main__":
    # fpds_clean = "FPDS_final.csv"
    # reddit_clean = "../reddit/reddit_cleaned_data.csv"
    # nytimes_clean = "nytimes_cleaned.csv"
    # guardian_clean = "the_guardian_cleaned.csv"

    # process reddit data
    reddit_clean = "../reddit/reddit_cleaned_data.csv"
    process_reddit(reddit_clean, "../reddit/reddit_lean.csv")

    # combine all data together, and aggregate data for each day
    reddit_lean = "../reddit/reddit_lean.csv"
    nytimes_lean = "../news_further_cleaning/nytimes_lean.csv"
    guardian_lean = "../news_further_cleaning/the_guardian_lean.csv"
    with open(reddit_lean, 'r') as reddit:
        with open(nytimes_lean, 'r') as nytimes:
            with open(guardian_lean, 'r') as guardian:
                combined = combine_lean_data(reddit, nytimes, guardian)

    # sort and save combined data into csv
    with open("./counts_combined.csv", 'w') as combined_save:
        writer = csv.writer(combined_save, delimiter=',')
        writer.writerows(combined)



