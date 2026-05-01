from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel

app = FastAPI()

# Basic Auth credentials
basic_auth = HTTPBasic()

class User(BaseModel):
    username: str
    password: str

# Basic Auth funksiyasi
def basic_auth_check(credentials: HTTPBasicCredentials = Depends(basic_auth)):
    if credentials.username != "admin" or credentials.password != "password":
        raise HTTPException(status_code=401, detail="Basic Auth error")

# Admin panel route
@app.get("/admin-panel")
def read_admin_panel(credentials: HTTPBasicCredentials = Depends(basic_auth_check)):
    return {"message": "Admin panel"}
```

Kodni ishga tushirish uchun FastAPI serveri ochish kerak. Bu quyidagicha qilinishi mumkin:

```bash
uvicorn main:app --reload
```

Bu yerda `main.py` - bu kodni saqlagan file nomi. `--reload` parametri serverni qayta ishga tushirish uchun kerak.
