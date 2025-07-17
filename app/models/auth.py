import requests
import os


class AuthModel:
    BASE_URL = os.getenv("BackendUrl", "http://localhost:5000/auth")

    @staticmethod
    def login(email, password):
        url = f"{AuthModel.BASE_URL}/login"
        try:
            response = requests.post(
                url, json={"email": email, "password": password}, timeout=10
            )
            content_type = response.headers.get("Content-Type", "")
            if response.status_code >= 500:
                return {"error": "Error interno del servidor"}, response.status_code
            if "application/json" in content_type:
                data = response.json()
                return data, response.status_code
            else:
                return {
                    "error": f"Respuesta inesperada del servidor: {response.text[:200]}"
                }, response.status_code
        except Exception as e:
            return {"error": f"Error de conexión: {str(e)}"}, 500

    @staticmethod
    def register(email, password):
        url = f"{AuthModel.BASE_URL}/register"
        try:
            response = requests.post(
                url, json={"email": email, "password": password}, timeout=10
            )
            content_type = response.headers.get("Content-Type", "")
            if response.status_code >= 500:
                return {"error": "Error interno del servidor"}, response.status_code
            if "application/json" in content_type:
                data = response.json()
                return data, response.status_code
            else:
                return {
                    "error": f"Respuesta inesperada del servidor: {response.text[:200]}"
                }, response.status_code
        except Exception as e:
            return {"error": f"Error de conexión: {str(e)}"}, 500
