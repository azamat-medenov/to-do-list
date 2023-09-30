from fastapi_users.authentication import AuthenticationBackend
from src.adapter.auth.bearer import bearer_transport
from src.adapter.auth.jwt_config import get_jwt_strategy

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)
