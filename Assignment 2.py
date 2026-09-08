def report_formayt(function):
    def wrapper(self):
        print("="*40)
        print("REPORT GENERATOR")
        print("="*40)

        function(self)
        print("="*40)
        print("END OF REPORT")
        print("="*40)
    return wrapper

#Report Class
class Report:
    #Magic Method:
    def  __init__(self,title,sections):
        self.title = title
        self.sections = sections
    

#Class Method
@classmethod
def sample_report(Us):
    title = "Student Performane Report"

    sections = {
        "Student Name : Rahul",
        "Marks : 89",
        "Grade : A"
    }
    return Us(title,sections)

#Decorator
@report_formayt
def display(self):

    print("Title:",self.title)
    print()

    for item in self.section:
        print(item)

#Magic Method
def __str__(self):
    return("Report Title: {self.title}")

#Magic Method
def __len__(self):
    return len(self.sections)

#Main Program 
report = Report.sample_report()
print(report)
print("Total sections:",len(report))
#print()

report.display()
