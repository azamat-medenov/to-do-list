from httpx import AsyncClient, Response


async def test_register_user(ac: AsyncClient):
    data = {
        "email": "user@example.com",
        "password": "string425",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
        "firstname": "string"
    }
    response = await ac.post('/api/register', json=data)
    assert response.status_code == 201, 'register test did not pass'
    assert data['email'] == response.json()['email']
    assert data['is_active'] == response.json()['is_active']
    assert data['is_verified'] == response.json()['is_verified']
    assert data['firstname'] == response.json()['firstname']
    assert data['is_superuser'] == response.json()['is_superuser']


async def test_login_user(ac: AsyncClient):
    response = await ac.post('/api/login', data={
        'username': 'user@example.com',
        'password': 'string425'})
    assert response.status_code == 200, 'login test did not pass'
    return response.json().get('access_token')


async def test_logout_user(ac: AsyncClient):
    jwt = await test_login_user(ac)
    response = await ac.post(
        '/api/logout',
        headers={'Authorization':f'Bearer {jwt}'}
    )
    assert response.status_code == 204, 'logout test did not pass'

