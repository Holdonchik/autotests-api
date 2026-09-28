import httpx


response = httpx.options("http://localhost:8000/api/v1")
print(response)