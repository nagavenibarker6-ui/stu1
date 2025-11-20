import sys
if len(sys.argv)!=3:
    print("Usuage: python stu1.py <name> <rollno>")
    sys.exit(1)
script_name=sys.argv[0]
name=sys.argv[1]
rollno=sys.argv[2]
print("Script Name:",script_name)
print("Student Name:",name)
print("Roll Nmuber:",rollno)
