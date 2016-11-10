import sys

def lexis_nexis_splitter(input_filename, max):
	input_file = open(input_filename)
	output_file_path = "/".join(input_filename.split("/")[:-1])
	output_file_path += "/output"
	output_file_suffix = "_" + input_filename.split("/")[-1]
	output_file = None
	writeFlag = False

	for line in input_file :
		if " of " + str(max) + " DOCUMENTS" in line :
			doc_number = line.split(" of " + str(max) + " DOCUMENTS")[0].strip()
			output_file = open(output_file_path + "/" + doc_number + output_file_suffix, "w")
			writeFlag = False
		if "LENGTH: " in line :
			writeFlag = True
			continue
		if "LOAD-DATE: " in line :
			writeFlag = False
		if output_file is not None and writeFlag:
			output_file.write(line)

if __name__ == "__main__" :
		lexis_nexis_splitter(sys.argv[1], sys.argv[2])
