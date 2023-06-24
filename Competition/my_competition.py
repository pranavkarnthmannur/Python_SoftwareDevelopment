"""
Final Coding Challenge - Programming Fundamentals
------------------------------------------------------Documentation:----------------------------------------------------------
Name: Pranav Karnth Mannur    StudentID: s3828461

1. Requirements met by the program:
-> All the levels have been attempted
-> Highest level attempted: HD

2. Requirements not met by the program:
-> High distinction level was Challenging
-> In the Last part of HD level, Score and WScore column in high distinction level not implemented
-> In the Last part of HD level, Tables not sorted according to lowtohigh and hightolow.

3. analysis/discussion/reflection of the Program:
-> Entire program is Object Oriented
-> High distinction level was very challenging
-> Code quality is very good, can be improved with more time
-> Modularity is very good, can be improved with more time
-> Creating and raising exceptions with classes can be implemented

4. Reflection:
-> If the program is to be implemented in real life, the order in which we pass the command line arguments will not be in the same order every time
-> Everytime the program is run, the content can be written in a new file instead of the same, because statistics may vary in real life scenario
-------------------------------------------------------------------------------------------------------------------------------
"""

import sys
from datetime import datetime

class Student():
    # Student class to support student ID, student Name, student Type
    studentID = None
    studentName = None
    studentType = None

    studentavgtime = {} #storing student statistics - average time
    studentongoing = {} #storing student statistics - ongoing challenge

    def __init__(self,studentID=None, studentName=None, studentType=None):
        self.studentID = studentID
        self.studentName = studentName
        self.studentType = studentType


    def get_studentID(self):
        return self.studentID


    def set_studentID(self, studentID):
        self.studentID = studentID


    def get_studentName(self):
        return self.studentName


    def set_studentName(self, studentName):
        self.studentName = studentName


    def get_studentType(self):
        return self.studentType


    def set_studentType(self, studentType):
        self.studentType = studentType

    def display_info(self):
        print(str(self.studentID)+'\t'+str(self.studentName)+'\t'+str(self.studentType))

    def beststudent(self):
        #To calculate total number of students and challenges and print the top student with the average time (Results file)
        studentvalue = {} #storing student statistics - averagetime

        for x in range(len(comp.final_list)):
            for i in range(len(comp.final_list[x])):
                if comp.final_list[x][i].student_challenge.strip() != '444' and comp.final_list[x][i].student_challenge.strip() != '-1' and comp.final_list[x][i].student_challenge.strip() != 'NA' \
                        and comp.final_list[x][i].student_challenge.strip() != 'x' and comp.final_list[x][i].student_challenge.strip() != 'TBA' and comp.final_list[x][i].student_challenge.strip() != 'tba':

                    if comp.final_list[x][i].studentID in studentvalue.keys():
                        studentvalue[comp.final_list[x][i].studentID] += [float(comp.final_list[x][i].student_challenge)]
                    else:
                        studentvalue[comp.final_list[x][i].studentID] = [float(comp.final_list[x][i].student_challenge)]

        for key, value in studentvalue.items():
            studentvalue[key] = sum(value) / len(value)

        lowest = sorted(studentvalue.values())
        print('There are {} students and {} challenges'.format(len(comp.final_list), len(comp.challenge_list)))
        print('The top student is {} with an average time of {:.2f}'.format(min(studentvalue, key=studentvalue.get),
                                                                            float(lowest[0])))

    def studentstatistics(self):
        #To calculate the students statistics and compute the student with the fastest average time (Students file)

        for x in range(len(comp.student_list)):
            Student.studentongoing[comp.student_list[x].studentID] = int(0)

        count = 0
        for x in range(len(comp.final_list)):
            for i in range(len(comp.final_list[x])):
                if comp.final_list[x][i].student_challenge.strip() != '444' and comp.final_list[x][i].student_challenge.strip() != '-1' and comp.final_list[x][i].student_challenge.strip() != 'NA' \
                        and comp.final_list[x][i].student_challenge.strip() != 'x' and comp.final_list[x][i].student_challenge.strip() != 'TBA' and comp.final_list[x][i].student_challenge.strip() != 'tba':

                    if comp.final_list[x][i].studentID in Student.studentavgtime.keys():
                        Student.studentavgtime[comp.final_list[x][i].studentID] += [float(comp.final_list[x][i].student_challenge)]
                    else:
                        Student.studentavgtime[comp.final_list[x][i].studentID] = [float(comp.final_list[x][i].student_challenge)]

                if comp.final_list[x][i].student_challenge.strip() == '444':
                    count += 1
                    if comp.final_list[x][i].studentID in Student.studentongoing.keys():
                        Student.studentongoing[comp.final_list[x][i].studentID] += count
                        count = 0

        for key, value in Student.studentavgtime.items():
            Student.studentavgtime[key] = [sum(value) / len(value), len(value)]

        Student.fastest = sorted(Student.studentavgtime.values())



class Challenge():
    # Challenge class to support challenge ID, challenge Name, challenge Type and challenge weight
    challengeID = None
    challengeName = None
    challengeWeight = None
    challengeType = None

    avgtime = {} #storing challenge statistics - average time
    ongoing = {} #storing challenge statistics - ongoing challenge
    averagetime = {} #storing challenge statistics - average time
    count = 0 #storing challenge statistics - no: of challenges

    def __init__(self,challengeID=None, challengeName=None, challengeWeight=None, challengeType=None):
        self.challengeType = challengeType
        self.challengeWeight = challengeWeight
        self.challengeName = challengeName
        self.challengeID = challengeID


    def get_challengeID(self):
        return self.challengeID


    def set_challengeID(self, challengeID):
        self.challengeID = challengeID


    def get_challengeName(self):
        return self.challengeName


    def set_challengeName(self, challengeName):
        self.challengeName = challengeName


    def get_challengeWeight(self):
        return self.challengeWeight


    def set_challengeWeight(self, challengeWeight):
        self.challengeWeight = challengeWeight


    def get_challengeType(self):
        return self.challengeType


    def set_challengeType(self, challengeType):
        self.challengeType = challengeType

    def display_info(self):
        print(str(self.challengeID)+'\t'+str(self.challengeName)+'\t'+str(self.challengeWeight)+'\t'+str(self.challengeType))

    def challengestatistics(self):
        # To calculate challenge statistics and print the most difficult challenge with the average time
        count = 0

        for x in range(len(comp.challenge_list)):
            Challenge.ongoing[comp.challenge_list[x].challengeID] = int(0)

        for x in range(len(comp.final_list)):
            for i in range(len(comp.final_list[x])):
                if comp.final_list[x][i].student_challenge.strip() != '444' and comp.final_list[x][i].student_challenge.strip() != '-1' and comp.final_list[x][i].student_challenge.strip() != 'NA' \
                        and comp.final_list[x][i].student_challenge.strip() != 'x' and comp.final_list[x][i].student_challenge.strip() != 'TBA' and comp.final_list[x][i].student_challenge.strip() != 'tba':

                    if comp.final_list[x][i].challengeID in Challenge.avgtime.keys():
                        Challenge.avgtime[comp.final_list[x][i].challengeID] += [float(comp.final_list[x][i].student_challenge)]
                    else:
                        Challenge.avgtime[comp.final_list[x][i].challengeID] = [float(comp.final_list[x][i].student_challenge)]

                if comp.final_list[x][i].student_challenge.strip() == '444':
                    count += 1
                    if comp.final_list[x][i].challengeID in Challenge.ongoing.keys():
                        Challenge.ongoing[comp.final_list[x][i].challengeID] += count
                    count = 0

        for key, value in Challenge.avgtime.items():
            Challenge.averagetime[key] = [sum(value) / len(value), len(value)]

        Challenge.highest = sorted(Challenge.averagetime.values())

class FilePrinter:
    # File printer class is to print all the contents to the console and the file along with the datetime(competition_report)
    def __init__(self, filename,dateandtime):
        self.out_file = open(filename, "w")
        self.out_file.seek(0,0)
        self.old_stdout = sys.stdout
        sys.stdout = self
        self.out_file.write(dateandtime)
        self.out_file.write("\n")

    def write(self, text):
        self.old_stdout.write(text)
        self.out_file.write(text)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        sys.stdout = self.old_stdout


class Competition(Student, Challenge):
    challenge_list = [] #To store challenge information
    student_list = [] #To store student information

    final_list = [] #To store the student records: studentID, ChallengeID, Time
    forchallenge = [] #To store student information
    forstudent = [] #To store challenge information


    def __init__(self, studentID=None, studentName=None, studentType=None, student_challenge = 0, challengeID=None, challengeName=None, challengeWeight=None, challengeType=None ):
        super().__init__()
        self.student_challenge = student_challenge

    def get_student_challenge(self):
        return self.student_challenge

    def set_student_challenge(self,student_challenge):
        self.student_challenge = student_challenge

    def read_results(fileresults,filechallenge,filestudent):

        # Reading the results file
        try:
            file1 = open(fileresults, 'r')
            students = []
            studvalue = {}
            for line in file1.readlines():
                readline = line.strip().split(',')

                if (len(readline)>0):
                    if readline[0]=='':
                        challenge = []
                        for i in range(1, len(readline)):
                            c = Challenge()
                            c.challengeID = readline[i]

                            if readline[i] not in challenge:

                                comp.challenge_list.append(c)
                                challenge.append(readline[i])

                    else:
                        s = Student()

                        if readline[0] not in students:

                            comp.student_list.append(s)
                            students.append(readline[0])
                            student_rec = []

                            for i in range(1, len(readline)):
                                studentrecord = Competition()
                                s.studentID = readline[0]
                                studentrecord.studentID = readline[0]
                                studentrecord.student_challenge = readline[i]
                                studentrecord.challengeID = comp.challenge_list[i-1].challengeID

                                student_rec.append(studentrecord)

                            comp.final_list.append(student_rec)

                else:
                    # If the results file is empty
                    print('No results to be displayed')
                    sys.exit()

            file1.close()


        except Exception as e:
            #If the file is not found/ missing
            print(e)
            sys.exit()

        try:
            # Reading the challenge file
            file2 = open(filechallenge, 'r')

            for line in file2.readlines():
                readline = line.strip().split(',')


                if len(readline)>3:
                    c = Challenge()
                    c.challengeID = readline[0].strip()
                    c.challengeType = readline[1].strip()
                    c.challengeName = readline[2].strip()
                    c.challengeWeight = readline[3].strip()
                    comp.forchallenge.append(c)

            file2.close()

        except Exception as e:
            # If the file is not found/ missing
            print(e)
            sys.exit()

        try:
            # Reading the students file
            file3 = open(filestudent, 'r')

            for line in file3.readlines():
                readline = line.strip().split(',')

                if len(readline)>2:
                    s = Student()
                    s.studentID = readline[0].strip()
                    s.studentName = readline[1].strip()
                    s.studentType = readline[2].strip()
                    comp.forstudent.append(s)

            file3.close()

        except Exception as e:
            # If the file is not found/ missing
            print(e)
            sys.exit()


    def display_results(self):
        #To display all the results in the specific format

        challengelst = [] #To store and print Challenge details
        challengelst.append("Result")

        for x in range(len(comp.challenge_list)):
            challengelst.append(comp.challenge_list[x].challengeID)

        records = []
        records.append(challengelst)

        for x in range(len(comp.final_list)):
            stud = []
            stud.append(comp.final_list[x][0].studentID)
            for i in range(len(comp.final_list[x])):

                if(comp.final_list[x][i].student_challenge.strip() == '-1' or comp.final_list[x][i].student_challenge.strip() == 'NA' or comp.final_list[x][i].student_challenge.strip() == 'x'):
                    stud.append(" ")
                elif(comp.final_list[x][i].student_challenge.strip() == '444' or comp.final_list[x][i].student_challenge.strip() == 'TBA' or comp.final_list[x][i].student_challenge.strip() == 'tba'):
                    stud.append("--")
                else:
                    stud.append(comp.final_list[x][i].student_challenge)

            records.append(stud)

        #To display the contents of the results file in the specific format
        print('COMPETITION DASHBOARD')
        print('------+'*6)
        for i in range(len(records)):
            for j in range(len(challengelst) - 1):
                print(records[i][j].center(6), end="|")
            print(records[i][len(challengelst) - 1].center(6), end="|")
            if (i == 0):
                print()
                for j in range(len(challengelst) - 1):
                    print('-' * 6, end="|")
                print('-' * 6, end="|")
            print()
        for j in range(len(challengelst) - 1):
            print('-' * 6, end="+")
        print('-' * 6, end="+")
        print()
        print()

        s = Student()
        s.beststudent()

        c = Challenge()
        c.challengestatistics()

        print()
        print()

        # To display the contents of the challenges file in the specific format
        print('CHALLENGE INFORMATION')
        print('+------------'+('+---------------'*5)+'+')
        print('|'+'Challenge'.center(12)+'|'+'Name'.center(15)+'|'+'Weight'.center(15)+'|'+'Nfinish'.center(15)+'|'+'Nongoing'.center(15)+'|'+'AverageTime'.center(15)+'|')
        print('+------------'+('+---------------'*5)+'+')

        for x in comp.forchallenge:
            for key1 in c.ongoing.keys():
                for key2 in c.averagetime.keys():
                    if key1.strip() == x.challengeID and key2.strip() == x.challengeID:

                        print('|' + x.challengeID.center(12) + '|' + (str(x.challengeName)+'('+str(x.challengeType)+')').center(15) + '|' + x.challengeWeight.center(15) + '|' + str(c.averagetime[key2][1]).center(15) + '|' + str(c.ongoing[key1]).center(15) + '|' + str(round(c.averagetime[key2][0],2)).center(15) + '|')

        print('+------------' + ('+---------------' * 5) + '+')
        print('The most difficult challenge is ({}) with an average time of {:.2f} minutes'.format(max(c.avgtime, key=c.avgtime.get).strip(), c.highest[-1][0]))

        print()
        print()

        s.studentstatistics()

        # To display the contents of the students file in the specific format
        print('STUDENT INFORMATION')

        print('+------------' + ('+---------------' * 5) + '+')
        print('|' + 'StudentID'.center(12) + '|' + 'Name'.center(15) + '|' + 'Type'.center(15) + '|' + 'Nfinish'.center(15) + '|' + 'Nongoing'.center(15) + '|' + 'AverageTime'.center(15) + '|')
        print('+------------' + ('+---------------' * 5) + '+')
        for x in comp.forstudent:
            for key1 in s.studentongoing.keys():
                for key2 in s.studentavgtime.keys():
                    if key1.strip() == x.studentID and key2.strip() == x.studentID:

                        print('|' + x.studentID.center(12) + '|' + (str(x.studentName).center(15) + '|' + str(x.studentType).center(15) + '|' + str(s.studentavgtime[key2][1]).center(15) + '|' + str(s.studentongoing[key1]).center(15) + '|' + str(round(s.studentavgtime[key2][0], 2)).center(15) + '|'))

        print('+------------' + ('+---------------' * 5) + '+')
        print('The student with the fastest average time is ({}) with an average time of {:.2f} minutes'.format(min(s.studentavgtime, key=s.studentavgtime.get).strip(), s.fastest[0][0]))

comp = Competition

def main(): #Main function

    args = sys.argv[1:]

    #Check if the user has enetered the file name (arguements) correctly
    if len(args) < 1 or len(args) > 3:
        print("[Usage]: python my_tournament.py <results file> <challenges file> <students file>")

    elif len(args) == 3:

        fileresults = args[0]
        filechallenge = args[1]
        filestudent = args[2]

        comp.read_results(fileresults,filechallenge,filestudent)

        #To print all the contents to the competition_report file
        data = "";
        now = datetime.now()
        dateandtime = now.strftime("%d/%m/%Y %H:%M:%S")
        with open('competition_report.txt', 'r') as f:
            data = f.readlines()

        with FilePrinter("competition_report.txt", dateandtime):
            Competition().display_results()

        with open('competition_report.txt', 'a') as f:
            if (data != ""):
                for i in data:
                    f.write(i)

    else:
        #If the user does not enter the files correctly
        print("[Usage]: python my_tournament.py <results file> <challenges file> <students file>")
        sys.exit()


if __name__ == "__main__":
    main()
