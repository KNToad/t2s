import datetime as dt

import pytest
from pydantic import ValidationError

from t2s.config import Settings, get_settings

def test_env_override(monkeypatch):
    monkeypatch.setenv('T2S_MAX_ROWS', '5')
    assert Settings().max_rows == 5

def test_defaults():
    s = Settings(dwh_ro_dsn='postgresql://x')
    assert s.statement_timeout_ms == 60000
    assert s.max_rows == 10000
    assert s.today == ''

def test_today_fixed(monkeypatch):
    monkeypatch.setenv('T2S_TODAY', '2026-10-22')
    assert Settings().today_date() == dt.date(2026, 10, 22)

def test_wrong_type_fails(monkeypatch):
    monkeypatch.setenv('T2S_MAX_ROWS', 'много')
    with pytest.raises(ValidationError):
        Settings()