csv_data = open('csv_data.txt', 'r')
lines = csv_data.readlines()
csv_data.close()

lines = [line.strip() for line in lines[1:]]

for line in lines:
    person_data = line.split(",")
    name = person_data[0].title()
    age = person_data[1]
    university = person_data[2].capitalize()
    degree = person_data[3].title()
    print(f'{name} is {age}, studying {degree} in {university}')


sample_csv_value = ','.join(['Rolf', '25', 'MIT', 'Computer Science'])
print(sample_csv_value)


# there are 2 other methods for reading and writing
# 1. csv reader - reads all the lines in the csv file and doesn't bother about headers, reads the headers also
# 2. csv writer - writes all the lines in the csv file and doesn't bother about headers, writes the headers also
# there are 2 other alternatives for csv reader and csv writer
# 1. csv DictReader
# 2. csv DictWriter
