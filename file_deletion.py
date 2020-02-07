import datetime
import sys
import os
import argparse


# email:tengyue.zheng@mft.nhs.uk
# date: 2020-02-07

"""
Find all bam files in whitelisted dir /mnt/cmftgen5/temp/ and delete them based on modified date"
"""

"""
to run the script, execute the following:

$ python create_file_list.py <tmp_dir> <file_type> <days> <white_list_dirs><output_file>

<tmp_dir>
e.g./full/path/to/tmp_dir

<file_type>
e.g.".bam"

<days>
e.g.90

<white_list_dirs>
e.g.white_listed_dirnames.txt

<output_file>
e.g.YYYY-MM-DD<file_type>.deletion.log

"""

temp_dir = "/mnt/cmftgen5/temp"

def temp_dir_deletion_whitelist():

	# whitelisted dirs to search files for deletion

	directories = [
	"APC",
	"APC_MUTYH",
	"BEST1_LLM",
	"BRCA",
	"Breast_cancer_LLM",
	"CAH",
	"Cancer_Pharmacogenomics",
	"Cardiac",
	"Cataract",
	"CF_LLM",
	"CORE",
	"Exome_NGS",
	"FE_Full",
	"FFPE_BRCA",
	"FFPE_Lynch",
	"FFPE_Overgrowth",
	"GLA",
	"HIV",
	"HRD",
	"Inherited_cancer",
	"Kabuki_syndrome",
	"KATNA1",
	"Lynch_syndrome",
	"LZTR1",
	"LZTR1_SMARCB1",
	"Macular_dystrophy_LLM",
	"Meningococcal",
	"Metabolic",
	"MiSeq",
	"Myeloid",
	"NF1",
	"NF1_DNA",
	"NF2",
	"OCA",
	"Ophthalmic",
	"ORF15",
	"Overgrowth",
	"Progressive_joint_contractures",
	"PTCH1",
	"PTEN",
	"QIAseq_BRCA",
	"QIAseq_Core",
	"QIAseq_HRD",
	"QIAseq_KTP",
	"QIAseq_RNA_fusion",
	"RB1",
	"RD",
	"Research",
	"Retinal_dystrophy",
	"RNASeq",
	"Schwannomatosis",
	"Schwannomatosis_validation",
	"Severe_Pre_eclampsia",
	"SLD",
	"SLE",
	"SMARCB1",
	"TARG",
	"Thymoma",
	"UrinaryTractExomes",
	"X_linked_RP_LLM"
	]

	return directories

def check_tmp_dir(tmp_dir, log_file):

	# check the temp dir supplied is correct

	tmp_dir = os.path.abspath(tmp_dir) + "/"
	assert os.path.isabs(tmp_dir), "{} NOT absolute".format(tmp_dir)
	assert os.path.exists(tmp_dir), "{} DO NOT exist".format(tmp_dir)
	assert os.path.isdir(tmp_dir), "{} is NOT a directory".format(tmp_dir)
	#print (tmp_dir)

	if tmp_dir == "{0}".format(temp_dir):
		print ("CORRECT tmp_dir: {0}".format(tmp_dir))
		with open (log_file, "a") as log:
			log.writelines("CORRECT tmp_dir: {0}\n".format(tmp_dir))
		return tmp_dir
	else:
		print ("WRONG tmp_dir: {0}, check path in /mnt/cmftgen5/temp/".format(tmp_dir))
		with open (log_file, "a") as log:
			log.writelines("WRONG tmp_dir: {0}, check path in /mnt/cmftgen5/temp/".format(tmp_dir)+"\n")
		sys.exit()

def check_dir(dirpath, log_file):
	
	# check each dir path exist, and is a dir

	dirpath = os.path.abspath(dirpath) + "/"
	try:
		assert os.path.isabs(dirpath), "{} NOT absolute".format(dirpath)
	except AssertionError as a:
		with open (log_file, "a") as log:
			log.writelines("{0}".format(a)+"\n")
		sys.exit()
	
	try:
		assert os.path.exists(dirpath), "{} DO NOT exist".format(dirpath)
	except AssertionError as e:
		with open (log_file, "a") as log:
			log.writelines("{0}".format(e)+"\n")
		sys.exit()
	
	try:
		assert os.path.isdir(dirpath), "{} is NOT a directory".format(dirpath)
	except AssertionError as d:
		with open (log_file, "a") as log:
			log.writelines("{0}".format(d)+"\n")
		sys.exit()

	if dirpath:
		print ("CORRECT dirpath: {0}".format(dirpath))
		with open (log_file, "a") as log:
			log.writelines("CORRECT dirpath: {0}\n".format(dirpath))
		return dirpath	
	
	else:
		print ("WRONG dirpath: {0}, check path in /mnt/cmftgen5/temp/".format(dirpath))
		with open (log_file, "a") as log:
			log.writelines("WRONG dirpath: {0}, check path in /mnt/cmftgen5/temp/".format(dirpath)+"\n")
		sys.exit()

def create_file_list(file_types, tmp_dir, log_file):

    # The following creates a list of a BAM and BAM.BAI in the specified directory.

    file_list = []

    print ("file types: {0}".format(file_types))
    print ("generate a list of files with above file types")

    for file_type in file_types:

	    for root, dirname, filenames in os.walk(tmp_dir):
	        for filename in filenames:
	            #find all path to files
	            if filename.endswith(file_type):
	                file_list.append(os.path.join(root, filename))
	            
    print ("list of files in {0} generated".format(tmp_dir))
    with open(log_file, "a") as log:
    	log.writelines("file types: {0}\n".format(file_types))
    	log.writelines("list of files in {0} generated\n".format(tmp_dir))
    
    return file_list

def check_files_against_whitelist(sorted_file_list, tmp_dir, log_file):

	# check the list of file paths generated against whitelist dirs

	whitelist = ["{0}{1}".format(tmp_dir, str(x)) for x in temp_dir_deletion_whitelist()]	

	# check whitelist dirs exists

	for dirs in whitelist:
		if check_dir(dirs, log_file):
			continue
		else:
			sys.exit()

	new_filtered_file_list = []
	
	print ("Checking file paths against whitelist")
	with open (log_file, "a") as log:
		log.writelines("Checking file paths against whitelist\n")

	for folder in whitelist:
		[new_filtered_file_list.append(f) for f in sorted_file_list if folder in f]
	
	sorted_unique_file_list = sorted(set(new_filtered_file_list))

	return sorted_unique_file_list

def check_file_date(sorted_file_list,expiry_period, log_file, file_types):

	# check file date of files in tmp_ir, parse file paths to 4 lists based on modified date

	today = datetime.datetime.today()
	print ("Time of check:{}".format(today))
	days = int(expiry_period)
	
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
			#os.remove(f)
			print ("over_duration: {0} {1} {2}".format(modified_date, f, "deleted"))
			over_duration.append("over_duration(deleted): {0} {1}".format(modified_date, f))

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
			edge_case.append("unknown:{0}".format(days))

	if not over_duration:
		print ("All files < 90 days old")
		with open(log_file, "a") as log:
			log.writelines("All files < 90 days old")
			sys,exit()
	else:
		log_file = write_to_output(over_duration, log_file)
		log_file = write_to_output(equal_duration, log_file)
		log_file = write_to_output(under_duration, log_file)
		log_file = write_to_output(edge_case, log_file)

	remain_list = equal_duration + under_duration + edge_case

	for ft in file_types:
		ft_delete_list = [f for f in over_duration if f.endswith(ft)]
		ft_remain_list = [f for f in remain_list if f.endswith(ft)]
		print ("number of {0} files deleted: {1}".format(ft, len(ft_delete_list)))
		print ("number of {0} files remain: {1}".format(ft, len(ft_remain_list)))
		with open (log_file, "a") as log:
			log.writelines("number of {0} files deleted: {1}\n".format(ft, len(ft_delete_list)))
			log.writelines("number of {0} files remain: {1}\n".format(ft, len(ft_remain_list)))

	print ("CHECK COMPLETE")
	print ("LOG for modified dates and file paths created: {}".format(log_file))
	
	with open(log_file, "a") as log:
		log.writelines("number of files in total deleted: {0}\n".format(len(over_duration)))
		log.writelines("number of files in total remain: {0}\n".format(len(remain_list)))
		log.writelines("CHECK COMPLETE\n")
		log.writelines("LOG for modified dates and file paths created: {}\n".format(log_file))

	return log_file

def write_to_output(file_list, log_file):

	# Record the files checked, deleted in a log file

    for date_file in file_list:
    	if not date_file:
    		continue
    	else:
    		with open (log_file, "a") as log:
        		log.writelines(date_file + "\n")

    return log_file

def parse_arguments():

	parser = argparse.ArgumentParser("script to parse certain file types from a temp_dir, and delete them if over expiry date")

	parser.add_argument("dir", nargs="?", help="temp directory where the files are located")
	parser.add_argument("expiry_period", nargs="?", help="amount of time (days), files are to be kept in the temp directory before deletion")
	parser.add_argument("log", nargs="?", help="log file of what files are deleted, and what files are kept")
	parser.add_argument('-f', '--file_types', nargs='+', required=True, help="file_types to search for deletion")

	args = parser.parse_args()

	tmp_dir = args.dir
	expiry_period = args.expiry_period
	log_file = args.log
	file_types = args.file_types
	#print (file_types)

	return tmp_dir, expiry_period, log_file, file_types

def main(tmp_dir, expiry_period, log_file, file_types):

	tmp_dir = check_tmp_dir(tmp_dir, log_file)
	file_list = create_file_list(file_types, tmp_dir, log_file)
	sorted_file_list = check_files_against_whitelist(file_list, tmp_dir, log_file)
	log_file = check_file_date(sorted_file_list, expiry_period, log_file, file_types)

if __name__ == "__main__":
    tmp_dir, expiry_period, log_file, file_types = parse_arguments()
    main(tmp_dir, expiry_period, log_file, file_types)

