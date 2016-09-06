def test_when_front_end_route_is_hit_then_render_template(app):
    with app.test_client() as test_client:
        response = test_client.get('/')
        assert 200 == response.status_code
        # TODO: Add logic that asserts that the correct template is rendered
