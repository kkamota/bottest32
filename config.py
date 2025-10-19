from dataclasses import dataclass
from typing import Sequence
import os


@dataclass(slots=True)
class Settings:
    bot_token: str
    channel_username: str
    admin_ids: Sequence[int]
    min_withdrawal: int = 15
    start_bonus: int = 3
    referral_bonus: int = 3
    daily_bonus: int = 1


def load_settings() -> Settings:
    token = os.getenv("BOT_TOKEN", "7968942203:AAGGFBRqSNWWpvAueFct54dQ3UthnJbPCRc")
    channel = os.getenv("CHANNEL_USERNAME", "@giftsauctionsru")
    raw_admins = os.getenv("ADMIN_IDS", "5838432507")
    admin_ids = tuple(
        int(admin_id.strip())
        for admin_id in raw_admins.split(",")
        if admin_id.strip().isdigit()
    )
    return Settings(
        bot_token=token,
        channel_username=channel,
        admin_ids=admin_ids or (123456789,),
    )
