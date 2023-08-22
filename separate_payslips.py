import os
import PyPDF2

# Function that reads folder names in the directory and adds each employee's name to the active employees list
def create_employee_list(directory1):
    for folder_name in os.listdir(directory1):
        folder = os.path.join(directory1, folder_name)
        if os.path.isdir(folder):
            active_employees.append(folder_name)
    
    return active_employees.sort()

# Function to separate each PDF page to the respective employee's folder
def separate_pdf(pdf_path, employee_folders):
    # List to store names of employees for whom processing is completed
    completed = []
    
    # Open the PDF file containing payslips in binary read mode 'rb'. Using the 'with' block ensures proper file closure after use.
    with open(pdf_path, 'rb') as file:
        
        # Create a 'PdfReader' object from the PyPDF2 module to read the PDF file.
        pdf_reader = PyPDF2.PdfReader(file)
        
        # Iterate through PDF pages, in a loop from 0 to the total number of pages in the file.
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            # Extract text from the page and store it in the variable 'text'
            text = page.extract_text()
            
            # Iterate through the names of active employees in the list
            for employee in active_employees:
                # Action if the employee's name is found in the extracted PDF page text
                if employee in text:
                    completed.append(employee)
                    
                    # Function to find the respective employee's folder
                    destination = find_employee_folder(employee, employee_folders)
                    
                    # Action if the employee's folder is found
                    if destination:
                        # Complete the destination directory with the "Payslips" folder
                        payslips_folder = os.path.join(destination, "Payslips")
                        
                        # Create the "Payslips" folder if it doesn't exist within the employee's folder. The exist_ok=True parameter allows the function not to raise errors if the folder already exists.
                        os.makedirs(payslips_folder, exist_ok=True)
                        
                        # Create the destination for the new PDF by joining the "Payslips" folder directory with the file name to be saved, as specified in the 'final_pdf_name' variable
                        destination_pdf = os.path.join(payslips_folder, final_pdf_name)
                        
                        # Open the PDF file in binary write mode ('wb'), using a 'with' block to ensure proper file closure after use.
                        with open(destination_pdf, 'wb') as output_file:
                            # Create an instance of PyPDF2.PdfWriter() to handle PDF writing.
                            output_pdf = PyPDF2.PdfWriter()
                            
                            # Add the PDF page to the output_pdf object
                            output_pdf.add_page(page)
                            
                            # Write the PDF content to the output file
                            output_pdf.write(output_file)
    
    completed = sorted(completed)
    return completed

# Function to find the respective employee's folder
def find_employee_folder(employee, employee_folders):
    # Create the full folder path by joining the main folder path with the employee's name
    employee_folder = os.path.join(employee_folders, employee)
    
    # Check if it's a valid directory to perform the action
    if os.path.isdir(employee_folder):
        # Return the full directory path of the employee's folder
        return employee_folder
    return None

# Directory where folders with the names of each active employee are located
employee_folders = r"C:\Employees"

# Directory of the PDF that needs to be separated
pdf_path = r"C:\Payslips"

# Final name of the pdf file to be saved in the "Payslips" folder inside each employee's folder. Ex: Salary_July_2023.pdf
final_pdf_name = f"August_Salary.pdf"

# List to store the names of active employees
active_employees = []

# Execute the function, adding each employee's name to the list of active employees
create_employee_list(employee_folders)

# Separate PDF pages for each employee
separate_pdf(pdf_path, employee_folders)

print("Program completed!")
