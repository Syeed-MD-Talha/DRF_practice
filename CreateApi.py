import json
import requests
response=requests.get(url='http://127.0.0.1:8000/aiquest_info/')
data={
        "id": 4,
        "teacher_name": "Syeed MD Talhaxasdfa",
        "course_name": "Problem Solving",
        "course_duration": 3,
        "seat": 220
    }

json_data=json.dumps(data)
requests.post(url='http://127.0.0.1:8000/aiquest_info/',data=json_data)