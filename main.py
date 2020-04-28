import section_1
import section_2

if __name__ == '__main__':
    # Init section_1
    section_1.collect(count=10, csv_filename='movies_data.csv')

    # Init section_2
    section_2.analyze(csv_filename='movies_data.csv')

