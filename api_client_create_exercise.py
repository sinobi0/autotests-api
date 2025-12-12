from clients.courses.courses_client import get_courses_client, CreateCourseRequestSchema
from clients.exercises.exercises_client import get_exercises_client, CreateExerciseRequestSchema
from clients.files.files_client import get_files_client, CreateFileRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client, CreateUserRequestSchema
from tools.fakers import fake

#Инициализируем публичный клиент и создаем пользователя
public_users_client = get_public_users_client()
create_user_req = CreateUserRequestSchema(
    email=fake.email(),
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
create_course_req = CreateCourseRequestSchema(
    title="MyCourse",
    max_score=100,
    min_score=10,
    description="test",
    estimated_time="115",
    preview_file_id=create_file_response.file.id,
    created_by_user_id=create_user_response.user.id
)
create_course_response = courses_client.create_course(create_course_req)
print(f"Данные созданного курса: {create_course_response}")

#Создаем задание
create_exercise_req = CreateExerciseRequestSchema(
    title="MyExercise",
    course_id=create_course_response.course.id,
    max_score=100,
    min_score=10,
    description="test",
    order_index="123",
    estimated_time="115"
)
create_exercise_response = exercises_client.create_exercise(create_exercise_req)
print(f"Данные запроса: {create_exercise_req}")
print(f"Данные созданного упражнения: {create_exercise_response}")