from clients.courses.courses_client import get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.exercises.exercises_client import get_exercises_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema


# Initialize PublicUserClient
public_users_client = get_public_users_client()

# Initialize user data
create_user_request = CreateUserRequestSchema()

# Create user
create_user_response = public_users_client.create_user(request=create_user_request)

# Initialize user authentication data
user_auth_data = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

# Initialize FilesClient
files_client = get_files_client(user=user_auth_data)

# Initialize data for file upload
create_file_request = CreateFileRequestSchema(upload_file="./testdata/files/Botticelli-primavera.jpg")

# Upload file
create_file_response = files_client.create_file(request=create_file_request)
print("Create file data:", create_file_response.file)

# Initialize CoursesClient
courses_client = get_courses_client(user=user_auth_data)

# Initialize data for course creation
create_course_request = CreateCourseRequestSchema(
    preview_file_id=create_file_response.file.id,
    created_by_user_id=create_user_response.user.id
)

# Create course
create_course_response = courses_client.create_course(request=create_course_request)
print("Create course data:", create_course_response.course)

# Initialize ExercisesClient
exercises_client = get_exercises_client(user=user_auth_data)

# Initialize exercise data
create_exercise_request = CreateExerciseRequestSchema(
    title="Exercise 1",
    course_id= create_course_response.course.id,
    max_score=12,
    min_score=1,
    order_index=1,
    description="Test exercise description",
    estimated_time="2 hours"
)

# Create exercise
create_exercise_response = exercises_client.create_exercise(request=create_exercise_request)
print("Create exercise data:", create_exercise_response.exercise)
