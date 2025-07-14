import pytest
import sys
import time
from pathlib import Path

class TestSmoke:
    
    @classmethod
    def setup_class(cls):
        """Configurar el entorno de pruebas"""
        cls.project_root = Path(__file__).parent.parent.parent
        
    def test_estructura_proyecto(self):
        """Verificar estructura básica del proyecto"""
        # Verificar que existen los directorios principales
        assert (self.project_root / "microservicio-A").exists()
        assert (self.project_root / "microservicio-B").exists()
        assert (self.project_root / "microservicio-C").exists()
        assert (self.project_root / "scripts").exists()
        
        # Verificar archivos principales
        assert (self.project_root / "docker-compose.yml").exists()
        assert (self.project_root / "requirements.txt").exists()
        assert (self.project_root / "makefile").exists()
        assert (self.project_root / "scripts" / "mesh.py").exists()
