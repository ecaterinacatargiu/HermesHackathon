class Student():
    '''
    Instances of this class represent the detailes abou a student, more specifically the Id and the name
    '''
    def __init__(self, studentID, name):
        """
        Constructor for Student class
        Input: studentId and the name of the student
        """
        self.__studentID = studentID
        self.__name = name
    def __str__(self):
        return "ID: " + str(self.__studentID) + ". Name:  " + str(self.__name) 
    def getId(self):
        """
        Getter for the Id of a student
        Output: The Id of a student
        """
        return self.__studentID
    def getNameStudent(self):
        """
        Getter for the Name of a student
        Output: The Name of a student
        """
        return self.__name
    def setName(self, newName):
        """
        Setter for the Name of a student
        Output: The Name of a student
        """
        self.__name = newName
    def setId(self, newId):
        """
        Setter for the Id of a student
        Output: The Id of a student
        """
        self.__studentID = newId

        
class Discipline:
    def __init__(self, disciplineID, name):
        self.__disciplineID = disciplineID
        self.__name = name
    def __str__(self):
        return "ID: " + str(self.__disciplineID) + ". Name: " + str(self.__name)
    def getId(self):
        """
        Getter for the Id of a discipline
        Output: The Id of a discipline
        """
        return self.__disciplineID
    def setName(self, newName):
        self.__name = newName
    def setId(self, newId):
        self.__disciplineID == newId
        

class Grade:
    def __init__(self, disciplineID, studentID, grade_value):
        self.__grade_value = grade_value
        self.__disciplineID = disciplineID
        self.__studentID = studentID
    def __str__(self):
        return "Discipline Id: " + str(self.__disciplineID) + ". Student Id:  " + str(self.__studentID) + ". Grade value: " + str(self.__grade_value)
    def getValue(self):
        return self.__getValue()
    
class Lista():
    def __init__(self):
        """
        Constructor for a list
        Input: A new empty list
        """
        self.__L = []
    def add(self, e):
        '''
        Input: The element that must be added
        Output: The new list with the element added to it 
        '''
        self.__L.append(e)
    def getAll(self):
        '''
        Getter for the list
        Output: The entire list
        '''
        return self.__L
    def findObjectById(self, id):
        '''
        Input: The id that the user want to know if already exists or not
        Output: -1 if the id does not exist or the index where the id has been found
        '''
        for i in range(len(self.__L)):
            if self.__L[i].getId() == id:
                return i
        return -1

    def remove(self, index):
        """
        Remove the entry at the given index from the list
        index - A natural number between 0 and the list size
        ListaException if the provided index is invalid
        """
        if index < 0 or index >= len(self.__L):
            raise RepositoryException("Invalid element position")
        return self.__L.pop(index)
    def setIdObject(self, old, new):
        """
        Setter for the Id of a student
        Output: The Id of a student
        """
        self.__L[old].setId(new)
    def setNameObject(self, old, new):
        """
        Setter for the name of a student
        Output: The name of a student
        """
        self.__L[old].setName(new)
       
    
class UI:
    def __init__(self, fun1, fun2, fun3):
        self.fun1 = fun1
        self.fun2 = fun2
        self.fun3 = fun3
    def menu(self):
        while True:
            print("1. Print the list of students and theirs IDs.")
            print("2. Add ID and name to the list of students.")
            print("3. Print the list of disciplines and the IDs of them.")
            print("4. Add ID and name to the list of disciplines.")
            print("5. Remove student.")
            print("6. Remove discipline.")
            print("7. Upgrade the list of students.")
            print("8. Upgrade the list of disciplines.")
            print("9. Add a student who attend a given discipline and add him grades.")
            print("10. Print the list of grades.")
            print("11. Grade students who attend a given doscipline.")
            print("0. Exit.")
            cmd = int(input("Choose an option: "))
            if cmd == 1:
                for i in self.fun1.getAll():
                    print(str(i))
            elif cmd == 2:
                s1 = int(input("Add ID: "))
                s2 = str(input("Add name: "))
                if self.fun1.findObjectById(s1) == -1:
                    self.fun1.add(Student(s1, s2))
                else:
                    print ("\tThe Id already exists. Give another Id.\n")
            elif cmd == 3:
                for j in self.fun2.getAll():
                    print(str(j))
            elif cmd == 4:
                d1 = int(input("Add ID of the discipline: "))
                d2 = str(input("Add name of discipline: "))
                if self.fun2.findObjectById(d1) == -1:
                    self.fun2.add(Discipline(d1, d2))
                else:
                    print("\tThe Id already exists. Give another Id.\n")
            elif cmd == 5:
                id = int(input("Give the id of the student that you want to be removed: "))
                if self.fun1.findObjectById(id) == -1:
                    print ("\tThe id has not been found! Give another id. \n")
                else:
                    self.fun1.remove(self.fun1.findObjectById(id))
            elif cmd == 6:
                id = int(input("Give the id of the discipline that you want to be removed: "))
                if self.fun2.findObjectById(id) == -1:
                    print ("\tThe id has not been found! Give another id. \n")
                else:
                    self.fun2.remove(self.fun2.findObjectById(id))
            elif cmd == 7:
                id = int(input("Give the id of the student that you want to upgrade: "))
                if self.fun1.findObjectById(id) == -1:
                    print ("\tThe id has not been found! Give another id. \n")
                else:
                    x = int(input("\tPress 1 if you want to change the id of the student.\n\tPress 2 if you want to change the name of the student."))
                    if x != 1 and x!= 2:
                        print ("Invalid command!!! Press only 1 or 2!")
                    elif x == 1:
                        y = int(input("Give new id: "))
                        if self.fun1.findObjectById(y) == -1:
                            self.fun1.setIdObject(self.fun1.findObjectById(id), y)
                        else:
                            print ("The Id already exist! Input another ID!!!")
                        self.fun1.setIdObject(self.fun1.findObjectById(id), y)
                    elif x == 2:
                         y = str(input("Give new name: "))
                         self.fun1.setNameObject(self.fun1.findObjectById(id), y)
            elif cmd == 8:
                id = int(input("Give the id of the discipline that you want to upgrade: ")) 
                if self.fun2.findObjectById(id) == -1:
                    print ("\tThe id has not been found! Give another id. \n")
                else:
                    x = int(input("\tPress 1 if you want to change the id of the discipline.\n\tPress 2 if you want to change the name of the discipline."))
                    if x != 1 and x!= 2:
                        print ("Invalid command!!! Press only 1 or 2!")
                    elif x == 1:
                        y = int(input("Give new id: "))
                        if self.fun2.findObjectById(y) == -1:
                            self.fun2.setIdObject(self.fun2.findObjectById(id), y)
                        else:
                            print ("The Id already exist! Input another ID!!!")
                    elif x == 2:
                         y = str(input("Give new name: "))
                         self.fun2.setNameObject(self.fun2.findObjectById(id), y)  
            elif cmd == 9:
                grade = []
                idStudent = int(input("Give the Id of the student that you want to grade: "))
                idDiscipline = int(input("Give the Id of the discipline: "))
                k = int(input("Enter the number of grades that you want to input: "))
                for i in range(k):
                    g = int(input("Enter grades:"))
                    if g > 0 and g <=10:
                        grade.append(g)
                    else:
                        print("The grade is not in range 1, 10")
                if self.fun1.findObjectById(idStudent) != -1 or self.fun2.findObjectById(idDiscipline) != -1:
                    self.fun3.add(Grade(idDiscipline, idStudent, grade))
                else:
                    print("\tThe Id of the student or of the discipline doesn't exist. Give another Id.\n")
            elif cmd == 10:
                for i in self.fun3.getAll():
                    print(str(i))
            elif cmd == 11:
                grade = []
                idStudent = int(input("Give the Id of the student that you want to grade: "))
                idDiscipline = int(input("Give the Id of the discipline: "))
                if self.fun1.findObjectById(idStudent) != -1 or self.fun2.findObjectById(idDiscipline) != -1:
                    if self.fun1.findObjectById(idStudent) == self.fun2.findObjectById(idDiscipline):
                        k = int(input("Enter the number of grades that you want to input: "))
                        for i in range(k):
                            g = int(input("Enter grades:"))
                            if g > 0 and g <=10:
                                grade.append(g)
                            else:
                                print("The grade is not in range 1, 10")
                    else:
                        print("The student is not enrolled at the given discipline\n")
                else:
                    print("\tThe Id of the student or of the discipline doesn't exist. Give another Id.\n")
                    
                
                              
stud = Lista()
def TestInit(stud):
    stud.add(Student(1, 'Ana Damaschin'))
    stud.add(Student(2, 'Pop Ioana'))
    stud.add(Student(3, 'Marian Sofia'))
    stud.add(Student(4, 'Boca Mihaela'))
    stud.add(Student(5, 'Popa Adela'))
    stud.add(Student(6, 'Costin Daniel'))
    stud.add(Student(7, 'Zaharia Vasile'))
    stud.add(Student(8, 'Mihnea Loredana'))
    stud.add(Student(9, 'Man Ionel'))
    stud.add(Student(10, 'Macovei Alin'))
    
TestInit(stud)

dis = Lista()

def TestInitDis(dis):
    dis.add(Discipline(1, 'Geography'))
    dis.add(Discipline(2, 'History'))
    dis.add(Discipline(3, 'English'))
    dis.add(Discipline(4, 'Informatics'))

TestInitDis(dis)

def testLista():
    L = Lista()
    x = Student(1, 'Ana')
    y = Student(2, 'Andrei')
    assert L.getAll() == []
    L.add(x)
    assert L.getAll() == [x]
    L.add(y)
    assert L.getAll() == [x,y]
    assert L.findObjectById(5) == -1
    assert L.findObjectById(1) == 0
    assert L.findObjectById(2) == 1

gr = Lista()
    
def testInitGrade(gr):
    gr.add(Grade(1, 1, 10))
    gr.add(Grade(1, 2, 5))
    gr.add(Grade(2, 3, 7))
    gr.add(Grade(2, 6, 6))
    gr.add(Grade(3, 9, 9))
    gr.add(Grade(4, 5, 4))
    gr.add(Grade(3, 4, 8))
    gr.add(Grade(1, 7, 6))
    gr.add(Grade(4, 8, 10))
    gr.add(Grade(3, 10, 7))
    gr.add(Grade(2, 1, 9))
    gr.add(Grade(1, 2, 2))
    
testInitGrade(gr)

     
testLista()                             

x = UI(stud, dis, gr)

x.menu()

        
        
