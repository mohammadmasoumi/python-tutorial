class University:
    uid: int
    name: str
    address: str

class Department: # 1:1
    did: int
    uid: int # ForeignKey(University)
    name: str
    # reverseRelation
    # SE  asghari sharif
    # SE  shasti  sharif

    # SE sharif

class Professor: # M:1
    pid: int
    name: str
    age: int
    level: str
    did: int # ForeignKey(University)

    # asghari did
    # shasti  did

class ProfessorDepartment:
    mid: int
    pid: int
    did: int
    start_date: int # EPOC
    end_date: int # EPOC

class Student:
    sid: int
    name: str
    age: int
    major: str
    did: int
    # uid: int
    entrance_date: int
    degree: str
    guide_professor: int # pid

class Course:
    cid: int
    did: int
    name: str
    duration: int

class ProfessorCourse:
    pcid: int
    pid: int
    cid: int
    semester: str

class ProfessorCourseStudent:
    pcsid: int
    pcid: int
    sid: int
    mark: int    

class Staff:
    sid: int
    uid: int
    name: str

"""
CREATE TABLE 
"""