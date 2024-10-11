import csv #To get the csv library

def fetchData(): #Fetch the data 
    data = [] #An empty list to put in all of the data once it is read from file 
    with open("Resources\students_complete.csv") as file: #While the file is open
        fetchData = csv.reader(file) #it will read the file through a csv reader
        next(fetchData) #Skip the header row 
        for row in fetchData: #For each row in the fetchData, it will assign a value to each row
                studentID = row[0]  
                name = row[1]
                gender = row[2]
                grade = row[3]
                schoolName = row[4]
                readingScore = int(row[5])
                mathScore = int(row[6]) 
                #Then appends it to the list
                data.append([studentID, name, gender, grade, schoolName, readingScore, mathScore])
        return data #and return the data
    
def displayData(data):  #This will print out all of the data needed for this program
    print("First Few Records:") 
    for value in data[:5]: 
        print(value)
    
    #This will print out the top 5 math scores
    selection = sortData(data, len(data)) 
    print(f"\nMath Scores (First few Records Descending):") 
    for record in selection[:5]:
        print(record)
    
    #This will print out the top 5 reading scores
    insertion = insertionData(data, len(data))
    print("\nReading Scores (First few Records Ascending)")
    for record in insertion[:5]:
        print(record)
    
    #This will print out the searched student for their records
    userinput = int(input("\nEnter in the Student ID here"))
    studentRecords = linearSearch(data, userinput)
    if studentRecords:
        print(f"Student Records Found: {studentRecords}")
    else:
        print("Student Record not found.")
    
    #This will print out the student's reading score
    sortedReadingData = insertion[:]
    target = int(input("Enter Reading Score to search for: "))
    binary = binarySearch(data, target, len(data) - 1)
    if binary:
        print(f"Student with Reading Score {target} found: {binary}")
    else:
        print(f"No student with Reading Score {target} found.")
    
    #This will print out the average of each grade
    average = calculateAverage(data)
    print(f"\nAverage Score by Grade:{average}")
    
    #This will print out the % passages for each subject
    passPercentage = calculatePassage(data, len(data))
    print(f"\nPass Percentage: {passPercentage}")
     
def sortData(data, size): #Takes the top 5 Math Scores
    for index in range(size): #for each index in the range largest amount of data
        maxValue = index #the max will be set as the index
        for j in range(index + 1, size): #For j in range of the index + 1 and size 
            if data[j][6] > data[maxValue][6]: 
                maxValue = j #the max value will be set as j
        (data[index], data[maxValue]) = (data[maxValue], data[index]) #This will swap the data around
    return data

def insertionData(data, size): #Takes the top 5 Reading Scores
    for index in range(1, size): #For each index in range of 1 - total size of the Data
        key = data[index] #A key will be assign the data index
        j = index - 1 #J will be the index - 1 
        while j >= 0 and data[j][5] > key[5]: #while J is greater than or equal 0 and the data index number in the 5th column is greater than the key 5th column
            data[j + 1] = data[j] #The data will be set to the index + 1 
            j -= 1 
        data[j + 1]= key
    return data

def binarySearch(data, target, size):  #Takes the data and sort the reading score 
    low = 0 #The lowest min score possible
    while low <= size: #If the lowest is less than or equal to the size of the data
        mid = (low + size)//2 #The mid point is the low  possible score plus the size of the data divided and remainder by 2
        if data[mid][5] == target: #if the data mid value 5th column is equal to the target 
            return data[mid] #it will return the data
        elif data[mid][5]<target: #If it's lower
            low = mid + 1 #The lowest will be set to the mid + 1
        else: #Else the size of the data will decrease
            size = mid - 1
    return None #Or return none if nothing else
    
def linearSearch(data, studentID): #Takes a linearSearch to get the Student Record
    for record in data: #for each record in data
        if record[0] == studentID: #if the record exists in the data
            return record #it will return said data
        return None 
    
def calculateAverage(data): #This will calculate the Average data
    gradeData = {} #This dictionary will hold selected grade data
    for record in data: #for each record in data
        grade = record[3] #The grade is taken from the record 
        readingScore = record[5]# along with the reading 
        mathScore = record[6]# and math scores
        if grade not in gradeData: #if the grade is not in the grade data already
            gradeData[grade] = {'Reading Total':0, 'Math Total':0, 'Count':0} #It will enter in the keys and set them to 0
        
        #then it will add each data Total by subject and count
        gradeData[grade]['Reading Total'] += readingScore 
        gradeData[grade]['Math Total'] += mathScore
        gradeData[grade]['Count'] += 1
        
    for grade, scores in gradeData.items(): #for each grade and score in the gradeData items list 
        averageReadingScore = scores['Reading Total'] / scores['Count'] #It will take the average reading score and divide it by the score count
        averageMathScore = scores['Math Total'] / scores['Count'] #It will take the average math score and divide it by the score count
        print(f"Grade {grade} - Average Reading Score: {averageReadingScore:.2f} - Average Math Score: {averageMathScore:.2f}")  #then print it

def calculatePassage(data, size): #This calculate if each person pass or not 
    readingPass = sum(1 for record in data if record[5] >= 70) #reading passing level are the sum of 1 for each records in data if their reading column is greater or equal to 70
    mathPass = sum(1 for record in data if record[6] >= 70)#math passing level are the sum of 1 for each records in data if their reading column is greater or equal to 70


    #For each subject to be divided by the size then multiply by 100 for the percentage
    readingPassPercentage = (readingPass / size)* 100 
    mathPassPercentage = (mathPass / size)* 100
    
    #then printed out
    print(f"Reading Pass Percentage: {readingPassPercentage:.2f}% \nMath Pass Percentage: {mathPassPercentage:.2f}%")
    
def main():
    while True:
        try: 
            data = fetchData() #this will fetch the data 
            displayData(data)#and sent it to display the data
            repeat = input("Would you like to try that again?(Y|N)").upper()
            if repeat != "Y":
                print("Exiting Program")
                break
        except ValueError: #Catch the valueError 
            print("Value Error")
        except FileNotFoundError: #Catch the File not Found Error
            print("FileNotFound")
            
main()