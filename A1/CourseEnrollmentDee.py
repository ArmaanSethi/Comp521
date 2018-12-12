from Dee import *
from DeeDatabase import Database

class CourseEnrollment_Database(Database):
	def __init__(self, name):
		Database.__init__(self, name)

		if 'DEPARTMENT' not in self:
			self.DEPARTMENT = Relation(["did", "name"],
                                 [(1, 'COMP'),
                                  (2, 'MATH'),
                                  (3, 'ANTH')
                                 ],
								 {'PK':(Key, ["did"])}
                                )
		if 'STUDENT' not in self:
			self.STUDENT = Relation(["sid", "did", 'fname', 'lname'],
                                 [(1,1,'MARY','Smith'),
                                  (2,1,'PATRICIA','Johnson'),
                                  (3,1,'JAMES','Williams'),
								  (4,1,'ROBERT','Jones'),
								  (5,2,'MICHAEL','Brown'),
								  (6,2,'WILLIAM','Davis'),
								  (7,2,'LINDA','Miller'),
								  (8,3,'BARBARA','Wilson'),
								  (9,3,'DAVID','Moore'),
								  (10,3,'RICHARD','Taylor'),
								  (11,3,'MICHAEL','Jordan')
                                 ],
								 {'PK':(Key, ["sid"]),
								  'FKS':(ForeignKey, ('DEPARTMENT', {"did":"did"}))}
                                )
		if 'COURSE' not in self:
			self.COURSE = Relation(["cid", "did", 'name', 'num', 'creditHours'],
                                 [(1,1,'Data Structures',410,3),
                                  (2,1,'Computer Organization',411,3),
                                  (3,1,'Files and Databases',521,3),
								  (4,1,'Software Engineering Laboratory',523,4),
								  (5,2,'Discrete Mathematics',381,3),
								  (6,2,'First Course in Differential Equations',383,3),
								  (7,2,'Advanced Calculus I',521,3),
								  (8,3,'The Past in the Present',452,3),
								  (9,3,'Anthropology of the Body and the Subject',473,4),
								  (10,3,'Visual Anthropology',477,3)
                                 ],
								 {'PK':(Key, ["cid"]),
								 'FKS':(ForeignKey, ('DEPARTMENT', {"did":"did"}))}
                                )
		if 'ENROLLED_IN' not in self:
			self.ENROLLED_IN = Relation(["eid", "sid", 'cid'],
								 [(1,1,1),
								  (2,1,3),
								  (3,1,9),
								  (4,1,4),
								  (5,2,1),
								  (6,2,2),
								  (7,2,3),
								  (8,2,4),
								  (9,3,1),
								  (10,3,3),
								  (11,3,4),
								  (12,3,9),
								  (13,4,2),
								  (14,4,3),
								  (15,4,5),
								  (16,4,10),
								  (17,5,5),
								  (18,5,3),
								  (19,5,7),
								  (20,6,5),
								  (21,6,6),
								  (22,6,7),
								  (23,7,3),
								  (24,7,6),
								  (25,7,9),
								  (26,8,8),
								  (27,8,9),
								  (28,8,10),
								  (29,9,3),
								  (30,9,9),
								  (31,9,10),
								  (32,10,8),
								  (33,10,9),
								  (34,10,10)
								 ],
								 {'PK':(Key, ["eid"]),
								 'FKS':(ForeignKey, ('STUDENT', {"sid":"sid"})),
								 'FKC':(ForeignKey, ('COURSE', {"cid":"cid"}))}
								)
DeeDB = Database.open(CourseEnrollment_Database, "DeeDB")
