# Parse-an-XML-file-using-python-and-its-libraries
# Objectives: 
 		
•	Our main objective is to extract data from the given XML file to the excel file.
•	How to parse XML files.
•	How to manipulate and modify excel sheets using python libs.
•	How to Save extracted data into excel file.
# Implementation:

I used the “xml.etree.elementTree” header file to implement parsing of an XML file. I also used “openpyxl” header file to manipulate and modify excel sheet. I replaced the “compiler.xml” in ET.parse() function and I placed the compiler.xml file in the same path where  python code file is saved. Then run the code file.

# Functional Commands:

	ET.parse()
	This function takes XML in file format to parse it.

	getroot()
	The getroot() method returns the root element of ‘compiler.xml’.

	workbook()
	This method creates a new excel file and adds a new empty work sheet by active() command’.

	append()
	The append() function is used to add a group of values at the end of the current worksheet. If it is a completely new worksheet, then it will simply add the values to this new worksheet.

	save()
	The save() function is used to save the entire workbook with the appended changes. The desired path where the workbook is to be saved is taken as a parameter to this function.
	
	get()
	The get() method returns the value of the item with the specified key.

	find()
	finds the first child element with specified tag.

# System Specifications:

•	Compiler (interpreter)

	PyCharm

•	Programming Language

	Python

•	Operating System:

	Windows 8,8.1,10,11 x64 bit
	Ubuntu

•	Hardware required:

	Processor: Core i3 or more with 4 cores 
	Dedicated video memory (at least 1 GB)
	Ram: 4 GB Ram
	Hard Disk: 100GB
# Processing of Code:

This program saves data from an XML file to an Excel sheet after processing it. The required libraries, openpyxl and xml.etree.ElementTree, are first imported into the code.
After that, the main() function is defined. The compiler.xml file is first parsed by this function using the ET.parse() method, which produces an ElementTree object. The getroot() method is then used to get the root element ,in our case it is “catalog”
The next step is to use the openpyxl library to create a new Excel workbook and add an empty sheet. The append() method is then used to add the data headings to the empty sheet. The data for each book is then extracted by the code after iterating over each book element in the root element. The ElementTree object's get() and find() functions are used to extract the data. The append() method is then used to insert the extracted data to the Excel sheet. Additionally print to the console. The workbook is then closed using the close() method and saved to a file called "200901104_Assign_03.xlsx" using the save() method. When the data is correctly saved and extracted, a message is printed to the console that your data has been extracted and saved successfully.
