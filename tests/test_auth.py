from httpx import AsyncClient, Response


async def test_register_user(ac: AsyncClient):
    response = await ac.post('/api/register', json={
        "email": "user@example.com",
        "password": "string425",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
        "firstname": "string"
    })
    assert response.status_code == 201, 'register test did not pass'


async def test_login_user(ac: AsyncClient) -> Response:
    response = await ac.post('/api/login', data={
        'username': 'user@example.com',
        'password': 'string425'})
    assert response.status_code == 200, 'login test did not pass'
    return response


async def test_logout_user(ac: AsyncClient):
    login = await test_login_user(ac)
    jwt_token = login.json().get('access_token')
    response = await ac.post('/api/logout', headers={'Authorization': f'Bearer {jwt_token}'})
    assert response.status_code == 204, 'logout test did not pass'
