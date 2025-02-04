import test
from datetime import date, timedelta
from refinedCode import CarFactory, CapuletEngine, WilloughbyEngine, SternmanEngine, SpindlerBattery, NubbinBattery

class TestCarFactory(test.TestCase):
    def setUp(self):
        # Set up a common date for testing
        self.current_date = date.today()

    def test_create_calliope(self):
        car_factory = CarFactory()
        calliope = car_factory.create_calliope(self.current_date, self.current_date, 50000, 30000)

        self.assertIsInstance(calliope, Car)
        self.assertIsInstance(calliope.engine, CapuletEngine)
        self.assertIsInstance(calliope.battery, SpindlerBattery)

        # Test service needs for Calliope
        self.assertEqual(calliope.needs_service(), True)

    def test_create_glissade(self):
        car_factory = CarFactory()
        glissade = car_factory.create_glissade(self.current_date, self.current_date, 70000, 60000)

        self.assertIsInstance(glissade, Car)
        self.assertIsInstance(glissade.engine, WilloughbyEngine)
        self.assertIsInstance(glissade.battery, SpindlerBattery)

        # Test service needs for Glissade
        self.assertEqual(glissade.needs_service(), True)

    def test_create_palindrome(self):
        car_factory = CarFactory()
        palindrome = car_factory.create_palindrome(self.current_date, self.current_date, 50000, 0)

        self.assertIsInstance(palindrome, Car)
        self.assertIsInstance(palindrome.engine, SternmanEngine)
        self.assertIsInstance(palindrome.battery, SpindlerBattery)

        # Test service needs for Palindrome
        self.assertEqual(palindrome.needs_service(), False)

    def test_create_rorschach(self):
        car_factory = CarFactory()
        rorschach = car_factory.create_rorschach(self.current_date, self.current_date, 70000, 60000)

        self.assertIsInstance(rorschach, Car)
        self.assertIsInstance(rorschach.engine, WilloughbyEngine)
        self.assertIsInstance(rorschach.battery, NubbinBattery)

        # Test service needs for Rorschach
        self.assertEqual(rorschach.needs_service(), True)

    def test_create_thovex(self):
        car_factory = CarFactory()
        thovex = car_factory.create_thovex(self.current_date, self.current_date, 50000, 0)

        self.assertIsInstance(thovex, Car)
        self.assertIsInstance(thovex.engine, CapuletEngine)
        self.assertIsInstance(thovex.battery, NubbinBattery)

        # Test service needs for Thovex
        self.assertEqual(thovex.needs_service(), False)

if __name__ == '__main__':
    test.main()