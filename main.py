"""
Student Grades


A Team effort!
Hannah
Rachael

11/09/20

Reads in names and scores for students in a class and then calculates percentages and grades

Allows user to update the records after entry
"""

#create class to store records
class Student():
	def __init__(self, record, record_id):
		self.id = record_id
		self.name = record[0]
		self.score = record[1]

#main function of the program. Uses the other functions
def main():
    students = get_records()
    calc_percentage(students)
    calc_grade(students)
    display_records(students)

    user_choice = 0

	# Loop until user chooses 'Exit'
    while user_choice != 2:
        user_choice = int(input('\nOptions\n1 - Change an entry\n2 - Exit\n> '))

        if user_choice == 1:
            student_id = int(
			    input(f'\nPlease enter the student you want to update (1 - {len(students)})\n> '))

			# Update selected record and display again
            update_record(students, student_id)
            print()
            display_records(students)

def get_records():
	# List to store records
	records = []
    # For each student
	for x in range(3):
		# Get record and add to list
		records.append(Student(get_record_data(), x))

	return records

#input the students information(name an dscore)
def get_record_data():
    #Read in details of one record
    name = input("Name: ")
    score = int(input("Score: "))

    #Return details of record
    return [name, score]

def calc_percentage(records):
	#Calculate percentages and store in records
  for x in range(len(records)):
    records[x].percentage = round(records[x].score/1.5 ,2)

def calc_grade(records):
  for x in range(len(records)):
    #Calculate grades and store in records
    if records[x].percentage >= 85:
        records[x].grade = "A"
        
    elif records[x].percentage >= 70 and records[x].percentage <= 84:
        records[x].grade = "B"

    elif records[x].percentage >= 55 and records[x].percentage <= 69:
        records[x].grade = "C"

    elif records[x].percentage >= 40 and records[x].percentage <= 54:
        records[x].grade = "D"
    else:
        records[x].grade = "Fail"
        
# Update information of an entry of your choice
def update_record(records, record_id):
  record = get_record_data()
	# Update percentages and grades for new data
  records[record_id] = Student(record, record_id)
  calc_percentage([records[record_id]])
  calc_grade([records[record_id]])


# Print the headings for the table formatted
def display_records(records):
	print(f'{"ID":7}{"Name":20}{"Score":10}{"Percentage":15}Grade')
  # Loop for number of records and print information
	for record in records:
		print(
		    f'{record.id:<7}{record.name:<20}{record.score:<10}{record.percentage:<15}{record.grade}'
		)


main()