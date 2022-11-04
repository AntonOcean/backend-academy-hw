import helloworld

def test_hello():
    data = helloworld.hello()

    assert data == "Hello C extension!"
