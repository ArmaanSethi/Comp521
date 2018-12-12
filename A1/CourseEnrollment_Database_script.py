DEPARTMENT = Relation(('did', 'name'),
[Tuple(did=1, name='COMP'), Tuple(did=2, name='MATH'), Tuple(did=3, name='ANTH')],
{'PK':(Key, ['did'])})

STUDENT = Relation(('sid', 'did', 'fname', 'lname'),
[Tuple(sid=1, did=1, fname='MARY', lname='Smith'), Tuple(sid=2, did=1, fname='PATRICIA', lname='Johnson'), Tuple(sid=3, did=1, fname='JAMES', lname='Williams'), Tuple(sid=4, did=1, fname='ROBERT', lname='Jones'), Tuple(sid=5, did=2, fname='MICHAEL', lname='Brown'), Tuple(sid=6, did=2, fname='WILLIAM', lname='Davis'), Tuple(sid=7, did=2, fname='LINDA', lname='Miller'), Tuple(sid=8, did=3, fname='BARBARA', lname='Wilson'), Tuple(sid=9, did=3, fname='DAVID', lname='Moore'), Tuple(sid=10, did=3, fname='RICHARD', lname='Taylor'), Tuple(sid=11, did=3, fname='MICHAEL', lname='Jordan')],
{'PK':(Key, ['sid']),
'FKS':(ForeignKey, ('DEPARTMENT', {'did': 'did'}))})

COURSE = Relation(('cid', 'did', 'name', 'num', 'creditHours'),
[Tuple(cid=1, did=1, name='Data Structures', num=410, creditHours=3), Tuple(cid=2, did=1, name='Computer Organization', num=411, creditHours=3), Tuple(cid=3, did=1, name='Files and Databases', num=521, creditHours=3), Tuple(cid=4, did=1, name='Software Engineering Laboratory', num=523, creditHours=4), Tuple(cid=5, did=2, name='Discrete Mathematics', num=381, creditHours=3), Tuple(cid=6, did=2, name='First Course in Differential Equations', num=383, creditHours=3), Tuple(cid=7, did=2, name='Advanced Calculus I', num=521, creditHours=3), Tuple(cid=8, did=3, name='The Past in the Present', num=452, creditHours=3), Tuple(cid=9, did=3, name='Anthropology of the Body and the Subject', num=473, creditHours=4), Tuple(cid=10, did=3, name='Visual Anthropology', num=477, creditHours=3)],
{'PK':(Key, ['cid']),
'FKS':(ForeignKey, ('DEPARTMENT', {'did': 'did'}))})

ENROLLED_IN = Relation(('eid', 'sid', 'cid'),
[Tuple(eid=1, sid=1, cid=1), Tuple(eid=2, sid=1, cid=3), Tuple(eid=3, sid=1, cid=9), Tuple(eid=4, sid=1, cid=4), Tuple(eid=5, sid=2, cid=1), Tuple(eid=6, sid=2, cid=2), Tuple(eid=7, sid=2, cid=3), Tuple(eid=8, sid=2, cid=4), Tuple(eid=9, sid=3, cid=1), Tuple(eid=10, sid=3, cid=3), Tuple(eid=11, sid=3, cid=4), Tuple(eid=12, sid=3, cid=9), Tuple(eid=13, sid=4, cid=2), Tuple(eid=14, sid=4, cid=3), Tuple(eid=15, sid=4, cid=5), Tuple(eid=16, sid=4, cid=10), Tuple(eid=17, sid=5, cid=5), Tuple(eid=18, sid=5, cid=3), Tuple(eid=19, sid=5, cid=7), Tuple(eid=20, sid=6, cid=5), Tuple(eid=21, sid=6, cid=6), Tuple(eid=22, sid=6, cid=7), Tuple(eid=23, sid=7, cid=3), Tuple(eid=24, sid=7, cid=6), Tuple(eid=25, sid=7, cid=9), Tuple(eid=26, sid=8, cid=8), Tuple(eid=27, sid=8, cid=9), Tuple(eid=28, sid=8, cid=10), Tuple(eid=29, sid=9, cid=3), Tuple(eid=30, sid=9, cid=9), Tuple(eid=31, sid=9, cid=10), Tuple(eid=32, sid=10, cid=8), Tuple(eid=33, sid=10, cid=9), Tuple(eid=34, sid=10, cid=10)],
{'PK':(Key, ['eid']),
'FKS':(ForeignKey, ('STUDENT', {'sid': 'sid'})),
'FKC':(ForeignKey, ('COURSE', {'cid': 'cid'}))})

