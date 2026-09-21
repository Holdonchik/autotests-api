from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
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

# Initialize PrivateUsersClient
private_users_client = get_private_users_client(user_auth_data)

# Get user data
get_user_response = private_users_client.get_user(create_user_response.user.id)
print('Get user data:', get_user_response)
