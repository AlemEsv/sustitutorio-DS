from unittest.mock import Mock
from service import OrderService
from interfaces import IRepository


# Simulacion de objeto RequestData para no llamar a los metodos en si
class MockRequestData:
    def __init__(self, id, usuario, contraseña):
        self.id = id
        self.data = Mock()
        self.data.usuario = usuario
        self.data.contraseña = contraseña


def test_process():
    repo = Mock(spec=IRepository)
    repo.get_timestamp.return_value = "2025-05-01T00:00:00"
    repo.save.return_value = True

    service = OrderService(repo)
    # id / usuario / pass
    request_data = MockRequestData("123", "testuser", "testpass")

    result = service.process(request_data)

    assert result["id"] == "123"
    assert result["data_procesada"]["usuario_procesado"] == "TESTUSER"
    assert "contraseña" in result["data_procesada"]
    assert result["data_procesada"]["timestamp"] == "2025-05-01T00:00:00"

    # Verificar que se llamó al metodo save con los datos correctos
    repo.save.assert_called_once_with("123", result["data_procesada"])
