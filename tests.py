# FCEWO Testing Configuration
# Unit and integration tests

import pytest
import asyncio
from fastapi.testclient import TestClient
from backend.main import app


@pytest.fixture
def client():
    """Test client fixture"""
    return TestClient(app)


@pytest.fixture
def async_client():
    """Async test client fixture"""
    return app


class TestHealthcheck:
    """Health check endpoint tests"""
    
    def test_health_check(self, client):
        """Test health check endpoint"""
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json()["status"] == "healthy"


class TestMarketData:
    """Market data endpoint tests"""
    
    def test_ingest_market_data(self, client):
        """Test market data ingestion"""
        response = client.post("/api/market/ingest", json={
            "asset_id": "BTC/USD",
            "price": 42350.50,
            "volume": 28500000000
        })
        assert response.status_code == 200
        assert response.json()["status"] == "ingested"
    
    def test_get_market_data(self, client):
        """Test fetching market data"""
        response = client.get("/api/market/latest/BTC/USD?limit=10")
        assert response.status_code == 200


class TestAlerts:
    """Alert endpoint tests"""
    
    def test_get_active_alerts(self, client):
        """Test getting active alerts"""
        response = client.get("/api/alerts/active")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
    
    def test_create_alert(self, client):
        """Test creating alert"""
        response = client.post("/api/alerts/create", json={
            "asset_id": "BTC/USD",
            "alert_type": "CRISIS_RISK",
            "severity": "high",
            "message": "Test alert"
        })
        assert response.status_code == 200


class TestPredictions:
    """Prediction endpoint tests"""
    
    def test_get_predictions(self, client):
        """Test fetching predictions"""
        response = client.get("/api/predictions/latest/BTC/USD?limit=50")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
    
    def test_get_prediction_status(self, client):
        """Test prediction status"""
        response = client.get("/api/predictions/status/BTC/USD")
        assert response.status_code == 200


class TestSystemEndpoints:
    """System endpoint tests"""
    
    def test_system_status(self, client):
        """Test system status endpoint"""
        response = client.get("/api/system/status")
        assert response.status_code == 200
        assert "status" in response.json()
    
    def test_system_metrics(self, client):
        """Test system metrics endpoint"""
        response = client.get("/api/system/metrics")
        assert response.status_code == 200
        assert "cpu" in response.json()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
