mkdir techlog-solutions
cd techlog-solutions

# Ambiente virtual python
python3 -m venv venv
# No Windows:
venv\Scripts\activate
# No Mac/Linux:
source venv/bin/activate

# Instalando fastapi + uvicorn
pip install fastapi[standard] uvicorn[standard]

# Instalar o pytest
pip install pytest pytest-asyncio