from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from clients.exercises.exercises_client import get_exercises_client, CreateExerciseRequestDict
from clients.files.files_client import get_files_client, CreateFileRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client, CreateUserRequestSchema
from tools.fakers import get_random_email

#Инициализируем публичный клиент и создаем пользователя
public_users_client = get_public_users_client()
create_user_req = CreateUserRequestSchema(
    email=get_random_email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)
create_user_response = public_users_client.create_user(create_user_req)
print(f"Данные созданного пользователя: {create_user_response}")

# Инициализируем клиенты
authentication_user = AuthenticationUserSchema(
    email=create_user_req.email,
    password=create_user_req.password
)
files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)
exercises_client = get_exercises_client(authentication_user)

#Загружаем файл
create_file_req = CreateFileRequestSchema(
    filename="image_3.jpg",
    directory="test115",
    upload_file="./testdata/files/image_3.jpg"
)
create_file_response = files_client.create_file(create_file_req)
print(f"Данные созданного файла: {create_file_response}")

#Создаем курс
create_course_req = CreateCourseRequestDict(
    title="MyCourse",
    maxScore=100,
    minScore=10,
    description="test",
    estimatedTime="115",
    previewFileId=create_file_response.file.id,
    createdByUserId=create_user_response.user.id
)
create_course_response = courses_client.create_course(create_course_req)
print(f"Данные созданного курса: {create_course_response}")

#Создаем задание
create_exercise_req = CreateExerciseRequestDict(
    title="MyExercise",
    courseId=create_course_response['course']['id'],
    maxScore=100,
    minScore=10,
    description="test",
    estimatedTime="115"
)
create_exercise_response = exercises_client.create_exercise(create_exercise_req)
print(f"Данные созданного упражнения: {create_exercise_response}")