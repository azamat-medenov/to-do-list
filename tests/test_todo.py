from httpx import AsyncClient


async def test_create_todo(ac: AsyncClient):
    register_data = {
        "email": "user2@example.com",
        "password": "string425",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
        "firstname": "string"
    }
    register_response = await ac.post('/api/register', json=register_data)

    assert register_response.status_code == 201

    response = await ac.post('/api/login', data={
        'username': register_data.get('email'),
        'password': register_data.get('password')})

    assert response.status_code == 200, 'login test did not pass'

    jwt = response.json().get('access_token')

    response = await ac.post('/api/todo', json={
        "task": "do something",
        "description": "Long description",
        "done": False
    }, headers={'Authorization': f'Bearer {jwt}'})
    assert response.status_code == 200, 'creation wasn\'t completed'


async def test_update_todo(ac: AsyncClient):
    response = await ac.post('/api/login', data={
        'username': 'user2@example.com',
        'password': 'string425'})

    assert response.status_code == 200, 'login test did not pass'

    jwt = response.json().get('access_token')

    response = await ac.get('/api/todo',
                           headers={'Authorization': f'Bearer {jwt}'})

    todo_id = response.json()[0].get('id')

    response = await ac.put(f'/api/todo/{todo_id}', json={
        "task": "do something",
        "description": "changed",
        "done": False
    }, headers={'Authorization': f'Bearer {jwt}'})
    assert response.status_code == 200, 'update wasn\'t completed'
