from template_python.app import main


class TestApp:
    def test_main(self: "TestApp") -> None:
        expected = 13
        got = main()
        assert got == expected
