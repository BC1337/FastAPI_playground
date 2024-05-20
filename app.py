from fastapi import FastAPI, HTTPException
from typing  import Optional 

students = [
	{'name': 'Student 1', 'age': 20},
	{'name': 'Student 2', 'age': 18},
	{'name': 'Student 3', 'age': 16}
]

app = FastAPI()

@app.get('/students')
def user_list(min: Optional[int] = None, max: Optional[int] = None):

	if min and max:
		
		filtered_students = list(
			filter(lambda student: max >= student['age'] >= min, students)
		)

		return {'students': filtered_students}

	return {'students': students}


@app.get('/students/{student_id}')
def user_detail(student_id: int):
	student_check(student_id)
	return {'student': students[student_id]}

def student_check(student_id):
	if not students[student_id]:
		raise HTTPException(status_code=404, detail='Student Not Found')