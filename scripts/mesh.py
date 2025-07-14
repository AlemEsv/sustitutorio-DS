import requests
import time
import logging
from typing import Dict, Any, Optional

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ServiceMesh:
    """Manejador de comunicación entre microservicios A, B, C"""
    
    def __init__(self):
        # Referencias a los microservicios
        self.service_a_url = "http://localhost:5001"
        self.service_b_url = "http://localhost:5002"
        self.service_c_url = "http://localhost:5003"
        
        # Configuraciones
        self.max_retries = 3
        self.timeout_threshold = 0.5  # 500ms
        
    def _call_service_a(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Llama al servicio A con reintentos"""
        for attempt in range(self.max_retries):
            try:
                response = requests.post(
                    f"{self.service_a_url}/process",
                    json=data,
                    timeout=5
                )
                response.raise_for_status()
                return response.json()
            except Exception as e:
                logger.warning(f"Intento {attempt + 1} fallido para servicio A: {e}")
                if attempt == self.max_retries - 1:
                    raise Exception(f"Servicio A falló después de {self.max_retries} intentos")
                time.sleep(1)  # Esperar antes del siguiente intento
    
    def _call_service_b(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Llama al servicio B y gestiona respuestas lentas"""
        start_time = time.time()
        try:
            response = requests.post(
                f"{self.service_b_url}/process",
                json=data,
                timeout=5
            )
            response.raise_for_status()
            
            # Verificar si la respuesta fue lenta
            elapsed_time = time.time() - start_time
            if elapsed_time > self.timeout_threshold:
                logger.warning(f"Servicio B respondió lento: {elapsed_time:.2f}s")
            
            return response.json()
        except Exception as e:
            logger.error(f"Error en servicio B: {e}")
            raise
    
    def _call_service_c(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Llama al servicio C y realiza logging del ID"""
        try:
            response = requests.post(
                f"{self.service_c_url}/process",
                json=data,
                timeout=5
            )
            response.raise_for_status()
            result = response.json()
            
            # Logging del ID en stdout
            request_id = data.get('id', 'unknown')
            print(f"Servicio C procesó ID: {request_id}")
            logger.info(f"Servicio C procesó ID: {request_id}")
            
            return result
        except Exception as e:
            logger.error(f"Error en servicio C: {e}")
            raise
    
    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Ejecuta el flujo completo:
        1. Envía a A con reintentos
        2. Envía a B y gestiona respuestas lentas
        3. Envía a C y realiza logging
        """
        results = {}
        
        try:
            # Paso 1: Llamar servicio A
            logger.info("Llamando servicio A...")
            result_a = self._call_service_a(data)
            results['service_a'] = result_a
            
            # Paso 2: Llamar servicio B
            logger.info("Llamando servicio B...")
            result_b = self._call_service_b(data)
            results['service_b'] = result_b
            
            # Paso 3: Llamar servicio C
            logger.info("Llamando servicio C...")
            result_c = self._call_service_c(data)
            results['service_c'] = result_c
            
            logger.info("Flujo completado exitosamente")
            return results
            
        except Exception as e:
            logger.error(f"Error en el flujo: {e}")
            raise

# Ejemplo de uso
if __name__ == "__main__":
    mesh = ServiceMesh()
    
    # Datos de ejemplo
    test_data = {
        "id": "test-123",
        "message": "Hello from mesh",
        "timestamp": time.time()
    }
    
    try:
        results = mesh.execute(test_data)
        print("Resultados:")
        for service, result in results.items():
            print(f"- {service}: {result}")
    except Exception as e:
        print(f"Error: {e}")
