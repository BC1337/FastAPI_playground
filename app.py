from fastapi import FastAPI
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
