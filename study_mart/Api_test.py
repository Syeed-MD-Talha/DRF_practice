import requests

url = "http://127.0.0.1:8000/7"
data= {
        "id": 7,
        "teacher_name": "Syeed MD Talha",
        "course_name": "Python and Django",
        "course_duration": 6,
        "seat": 160
    }

requests.delete(url)
# response=requests.put(url,data)
# print(response.json())


