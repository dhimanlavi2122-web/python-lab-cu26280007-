import csv
import glob


def program_30():
    pattern = input("Enter CSV file pattern [*.csv]: ") or "*.csv"
    output_name = input("Enter output file name [combined.csv]: ") or "combined.csv"

    filenames = [
        name for name in sorted(glob.glob(pattern))
        if name != output_name
    ]

    if not filenames:
        print("No matching CSV files found.")
        return

    header = None
    all_rows = []

    for filename in filenames:
        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            file_header = next(reader, None)

            if file_header is None:
                continue

            if header is None:
                header = file_header
            elif file_header != header:
                print(f"Skipped {filename}: its header does not match.")
                continue

            all_rows.extend(reader)

    if header is None:
        print("No CSV data found.")
        return

    with open(output_name, "w", newline="", encoding="utf-8") as output:
        writer = csv.writer(output)
        writer.writerow(header)
        writer.writerows(all_rows)

    print(f"CSV files combined into {output_name}.")


program_30()