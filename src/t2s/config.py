from __future__ import annotations

import datetime as dt
from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT = Path(__file__).resolve().parents[2]

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix='T2S_', env_file=ROOT / ".env", extra='ignore')

    dwh_ro_dsn: str = 'postgresql://t2s_ro:t2s_ro_pwd@localhost:5432/dwh'
    statement_timeout_ms: int = 60_000
    max_rows: int = 10_000
    today: str = ''

    def today_date(self) -> dt.date:
        return dt.date.fromisoformat(self.today) if self.today else dt.date.today()

@lru_cache
def get_settings() -> Settings:
    return Settings()