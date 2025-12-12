# FCEWO - Financial Crisis Early-Warning Orchestrator

**AI-Driven Real-Time Crisis Detection System**

---

## 🚀 Run the Application - 3 Simple Steps

### **Step 1: Setup Python Environment**
```powershell
cd e:\red3
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip setuptools wheel
pip install --only-binary :all: numpy pandas scikit-learn
pip install fastapi uvicorn streamlit websockets requests prometheus-client
```

### **Step 2: Start Backend (Terminal 1)**
```powershell
cd e:\red3
.\venv\Scripts\Activate.ps1
uvicorn backend.main:app --reload --port 8000
```
✅ **FastAPI Available at:** http://localhost:8000/docs

### **Step 3: Start Frontend (Terminal 2)**
```powershell
cd e:\red3
.\venv\Scripts\Activate.ps1
streamlit run frontend/app.py --server.port 8501
```
✅ **Streamlit Dashboard at:** http://localhost:8501

---

## 🐳 Alternative: Run with Docker Compose

```powershell
cd e:\red3
docker-compose up -d
```
All services start automatically! Access:
- Dashboard: http://localhost:8501
- API: http://localhost:8000
- Grafana: http://localhost:3000
- Prometheus: http://localhost:9090

---

## ⚡ Quick Fixes

| Problem | Solution |
|---------|----------|
| numpy build error | `pip install --only-binary :all: numpy` |
| Port 8000 in use | `uvicorn backend.main:app --port 8001` |
| venv won't activate | `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` |
| Docker won't start | `docker system prune -a` then `docker-compose up -d` |

---

## 📊 Service URLs

| Service | URL |
|---------|-----|
| Streamlit | http://localhost:8501 |
| FastAPI | http://localhost:8000 |
| API Docs | http://localhost:8000/docs |
| Prometheus | http://localhost:9090 |
| Grafana | http://localhost:3000 |

---

## 📁 Project Structure

```
backend/          → FastAPI REST API & WebSocket server
frontend/         → Streamlit dashboard
config/           → Configuration files
monitoring/       → Prometheus & Grafana setup
tests.py          → Unit tests
requirements.txt  → Python dependencies
docker-compose.yml → Service orchestration
```

---

## ✨ Features

- 🤖 AI Crisis Prediction (Machine Learning)
- 📊 Real-Time Market Data Streaming (WebSockets)
- 🚨 Intelligent Alert System
- 📈 Technical Indicators Analysis
- 💾 Data Persistence (Supabase)
- 📉 Grafana Dashboards
- 📊 Prometheus Metrics

---

## 🔗 API Endpoints

```
GET  /api/market-data        → Market data
GET  /api/predictions        → Crisis predictions
GET  /api/alerts             → Alert list
GET  /api/system/health      → System status
WS   /ws                     → Real-time stream
```

---

**For detailed information, see QUICKSTART.md**
