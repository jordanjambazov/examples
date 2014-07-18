import unittest
import game


class TestVehicleObserver(unittest.TestCase):

    def test_vehicle_communication(self):
        vehicle = game.Vehicle()
        self.assertFalse(vehicle.hit)

        cell = game.Cell()
        cell.add_callback(vehicle.receive_callback)
        cell.hit()
        self.assertTrue(vehicle.hit)


    def test_get_vehicle_initials_from_cell(self):
        vehicle = game.Vehicle()
        cell = game.Cell()
        cell.add_return_callback(vehicle.return_self())

        self.assertEqual(cell.get_vehicle(), vehicle)


    def test_multiple_vehicles(self):
        vehicle_1 = game.Vehicle()
        vehicle_1.initials = "baba"
        vehicle_2 = game.Vehicle()
        vehicle_2.initials = "dqdo"
        vehicle_3 = game.Vehicle()
        vehicle_3.initials = "vnuche"
        vehicle_4 = game.Vehicle()
        vehicle_4.initials = "tate"
        cell_1 = game.Cell()
        cell_1.add_return_callback(vehicle_1.return_self())
        cell_2 = game.Cell()
        cell_2.add_return_callback(vehicle_2.return_self())
        cell_3 = game.Cell()
        cell_3.add_return_callback(vehicle_3.return_self())
        cell_4 = game.Cell()
        cell_4.add_return_callback(vehicle_4.return_self())

        self.assertEqual("baba", cell_1.get_vehicle().initials)
        self.assertEqual("dqdo", cell_2.get_vehicle().initials)
        self.assertEqual("vnuche", cell_3.get_vehicle().initials)
        self.assertEqual("tate", cell_4.get_vehicle().initials)






if __name__ == "__main__":
    unittest.main()
