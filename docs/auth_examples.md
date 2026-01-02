# Auth example requests

Register a new user:

curl -X POST http://localhost:8000/api/auth/registration/ \
  -d "username=tester" \
  -d "email=tester@example.com" \
  -d "password1=strong-password-123" \
  -d "password2=strong-password-123"

Login (returns `key` token):

curl -X POST http://localhost:8000/api/auth/login/ \
  -d "username=tester" \
  -d "password=strong-password-123"

Get current user (replace <TOKEN> with returned key):

curl -H "Authorization: Token <TOKEN>" http://localhost:8000/api/users/me/
