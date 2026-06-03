import csv 


def old_faithful_stats(csv_file):
    # Read the CSV file
    data = csv.read_csv(csv_file)

    
    eruption_length = data["eruptions length"]
    eruption_wait = data["Eruption wait"]

  
    print("Average eruption length:", eruption_length.mean())
    print("Longest eruption time:", eruption_length.max())
    print("Shortest eruption time:", eruption_length.min())

    print("Average eruption wait:", eruption_wait.mean())
    print("Shortest eruption wait:", eruption_wait.min())
    print("Longest eruption wait:", eruption_wait.max())


    longest_wait_row = data.loc[eruption_wait.idxmax()]
    print(
        "Eruption time of the longest eruption wait:",
        longest_wait_row["eruptions"]
    )


old_faithful_stats("faithful.csv")
