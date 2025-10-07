import re

_EMAIL_RE = re.compile(r"^(?=.{3,254}$)[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}$")

def validate_email(email):
    s = (email or "").strip()
    if not s:
        return ""
    if not _EMAIL_RE.match(s):
        raise ValueError("Invalid email format")
    return s

_PHONE_COMPACT_RE = re.compile(r"^\+?\d{7,15}$")

def normalize_phone(phone):
    raw = (phone or "").strip()
    if not raw:
        raise ValueError("Phone cannot be empty")

    if not _PHONE_COMPACT_RE.match(raw):

        compact = "".join(ch for ch in raw if ch.isdigit())
        if raw.startswith("+"):
            compact = "+" + compact
        if not _PHONE_COMPACT_RE.match(compact):
            raise ValueError("Invalid phone format (expect +1234567.. or 0401234..)")
        return compact

    return raw
