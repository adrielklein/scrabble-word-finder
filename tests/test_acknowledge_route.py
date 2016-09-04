def test_when_acknowledge_route_is_hit_then_it_returns_ok(app):
    with app.test_client() as test_client:
        response = test_client.get('/acknowledge')
        assert 200 == response.status_code
        assert 'OK' == response.get_data().decode()
