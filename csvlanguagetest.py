import csv


def write_to_csv(user_name, callback_data):

    my_data = [["User_name", "Language"],
              [user_name, callback_data]]

    my_file = open('example2.csv', 'w')
    with my_file:
        writer = csv.writer(my_file)
        writer.writerows(my_data)

    print("Writing complete")


def read_from_csv(user_name):
    with open('example2.csv') as File:
        reader = csv.reader(File, delimiter=',', quotechar=',',
                            quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            if not row:
                continue

            if row[0] == str(user_name):
                return row[1]
        print("not found")
