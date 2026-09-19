from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from clients.exercises.exercises_client import get_exercises_client, CreateExerciseRequestDict
from clients.files.files_client import get_files_client, CreateFileRequestDict
from clients.private_http_builder import AuthenticationUserDict
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict
from tools.fakers import get_random_email


# Initialize public user client
public_users_client = get_public_users_client()

# Create user
create_user_request = CreateUserRequestDict(
    email=get_random_email(),
    password="1234567890",
    lastName="John",
    firstName="Doe",
    middleName="James"
)
create_user_response = public_users_client.create_user(request=create_user_request)

# Created user authentication data
user_auth_data = AuthenticationUserDict(
    email=create_user_request['email'],
    password=create_user_request['password']
)

# Initialize files client
files_client = get_files_client(user=user_auth_data)

# Upload file
create_file_request = CreateFileRequestDict(
    filename="Botticelli-primavera.jpg",
    directory="courses",
    upload_file="./testdata/files/Botticelli-primavera.jpg"
)
create_file_response = files_client.create_file(request=create_file_request)
print("Create file data:", create_file_response)

# Initialize courses client
courses_client = get_courses_client(user=user_auth_data)

# Create course
create_course_request = CreateCourseRequestDict(
    title="Test",
    maxScore=96,
    minScore=1,
    description="Best course ever",
    estimatedTime="16 hours",
    previewFileId=create_file_response['file']['id'],
    createdByUserId=create_user_response['user']['id']
)
create_course_response = courses_client.create_course(request=create_course_request)
print("Create course data:", create_course_response)

# Initialize exercises client
exercises_client = get_exercises_client(user=user_auth_data)

# Create exercise
create_exercise_request = CreateExerciseRequestDict(
    title="Exercise 1",
    courseId= create_course_response['course']['id'],
    maxScore=12,
    minScore=1,
    orderIndex=1,
    description="Test exercise description",
    estimatedTime="2 hours"
)
create_exercise_response = exercises_client.create_exercise(request=create_exercise_request)
print("Create exercise data:", create_exercise_response)
