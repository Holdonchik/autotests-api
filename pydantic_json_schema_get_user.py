from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, GetUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import get_random_email

# Initialize public user client
public_users_client = get_public_users_client()

# Create user
create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="1234567890",
    last_name="John",
    first_name="Doe",
    middle_name="James"
)
create_user_response = public_users_client.create_user(request=create_user_request)

# Initialize user authentication data
user_auth_data = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
# Initialize PrivateUsersClient
private_users_client = get_private_users_client(user_auth_data)

# Get user data
get_user_response = private_users_client.get_user_api(create_user_response.user.id)

# Get JSON schema for get user response
get_user_response_schema = GetUserResponseSchema.model_json_schema()

# Verify that JSON response complies with expected JSON schema
validate_json_schema(instance=get_user_response.json(), schema=get_user_response_schema)
