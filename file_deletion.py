import datetime
import sys
import os

# email:tengyue.zheng@mft.nhs.uk
# date: 2020-01-24

"""
Find all files and delete them based on modified date"
"""

"""
to run the script, execute the following:

$ python create_file_list.py <tmp_dir> <file_type> <days> <output_file>

<tmp_dir>
e.g./full/path/to/tmp_dir

<file_type>
e.g.".bam"

<days>
e.g.90

<output_file>
e.g.YYYY-MM-DD<file_type>.deletion.log

"""

def create_file_list(file_type, tmp_dir):

    # The following creates a list of a particular file type in in the specified directory.

    file_type = str(file_type)
    tmp_dir = os.path.abspath(tmp_dir)
    assert os.path.isabs(tmp_dir), "{} NOT absolute".format(tmp_dir)
    assert os.path.exists(tmp_dir), "{} DO NOT exist".format(tmp_dir)
    assert os.path.isdir(tmp_dir), "{} is NOT a directory".format(tmp_dir)

    file_list = []
    
    for root, dirname, filenames in os.walk(tmp_dir):
        for filename in filenames:
            #find all path to files
            if filename.endswith(file_type):
                file_list.append(os.path.join(root, filename))
            
    sorted_file_list = sorted(file_list)
    print ("list of files in {0} generated".format(tmp_dir))
    print ("file type: {0}".format(file_type))
    
    return sorted_file_list

def check_file_date(sorted_file_list, days):

	# check file date of files in tmp_ir, parse file paths to 4 lists based on modified date

	today = datetime.datetime.today()
	print ("Date of check:{}".format(today))
	days = int(days)
	
	over_duration = []
	under_duration = []
	equal_duration = []
	edge_case = []

	print ("START checking modified date of each file:")

	for f in sorted_file_list:

		modified_date = datetime.datetime.fromtimestamp(os.path.getmtime(f))
		duration = today - modified_date
		#print (duration)
	
		if duration.days > days:

			#WHEN READY UNCOMMENT THE FOLLOWING TO START TESTING DELETION
			os.remove(f)
			print ("over_duration: {0} {1} {2}".format(modified_date, f, "deleted"))
			over_duration.append("over_duration: {0} {1} {2}".format(modified_date, f, "deleted"))

			#WHEN READY COMMENT THE FOLLOWING
			#print ("over_duration: {0} {1}".format(modified_date, f))
			#over_duration.append("over_duration: {0} {1}".format(modified_date, f))

		elif duration.days < days:
			#print ("under_duration: {0} {1}".format(modified_date, f))
			under_duration.append("under_duration: {0} {1}".format(modified_date, f))
		elif duration.days == days:
			#print ("equal_duration:{0}".format(days))
			equal_duration.append("equal_duration:{0}".format(days))
		else:
			#print ("edge_case: {0} {1}".format(modified_date, f))
			edge_case.append("equal_duration:{0}".format(days))

	if not over_duration:
		print ("All files less than 90 days old")

	print ("check COMPLETE")

	return over_duration, under_duration, equal_duration, edge_case


def write_to_output(over_d, under_d, equal_d, edge_c, output_file):

	# Record the files checked, deleted in a log file

    output_file = str(output_file)

    sorted_file_list = [over_d, equal_d, edge_c, under_d]

    for due_file_list in sorted_file_list:
    	with open (output_file, "a") as fh:
        	for date_file in due_file_list:
        		fh.write(date_file+"\n")

    print ("LOG for modified dates and file paths created: {}".format(output_file))
    return output_file


def main(tmp_dir, file_type, days, output_file):

    sorted_file_list = create_file_list(file_type, tmp_dir)
    over_d, under_d, equal_d, edge_c = check_file_date(sorted_file_list, days)
    output = write_to_output(over_d, under_d, equal_d, edge_c, output_file)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

