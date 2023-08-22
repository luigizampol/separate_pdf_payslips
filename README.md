#PDF Page Separation for Employee Payslips

This Python script is designed to automate the process of separating PDF pages corresponding to employee payslips into individual folders based on employee names. It reads a given PDF file containing payslips, extracts employee names from the payslips, and organizes the pages into respective folders for each employee.

#Prerequisites
Python 3.x
Required Python libraries: os, PyPDF2

#Usage
1. Clone or download this repository to your local machine.

2. Ensure that Python 3.x is installed on your system.

3. Install the necessary Python libraries by running:
pip install PyPDF2

#Edit the script:

- Set the employee_folders variable to the directory where folders with employee names are located.
- Set the pdf_path variable to the path of the PDF file that needs to be separated.
- Set the final_pdf_name variable to the desired name format for the separated PDF files.

#Run the script:
The script will process the PDF file and separate the pages into the respective "Payslips" folders within the employee folders.

The program will print "Program completed!" once the process is finished.

#Notes
- Make sure that the PDF pages contain the names of the employees you want to separate.
- The script assumes that the PDF pages' text is readable and contains the employee names.

License
This project is licensed under the MIT License.