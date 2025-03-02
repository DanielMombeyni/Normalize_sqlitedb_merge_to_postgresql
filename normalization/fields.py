import re


def normalize_title(title):
    """نرمال‌سازی عنوان تبلیغ (حذف فاصله‌های اضافی و تنظیم کپیتالایز)"""
    return title.strip().title() if isinstance(title, str) and title.strip() else False


def normalize_game(game):
    """نرمال‌سازی نام بازی (بررسی مقدار صحیح)"""
    return game.strip().title() if isinstance(game, str) and game.strip() else False


def normalize_price(price):
    """نرمال‌سازی قیمت (حذف تمامی حروف، نمادها و کاراکترهای غیرعددی)"""
    if not price or not isinstance(price, str):
        return None

    price = re.sub(r"[^\d.]", "", price)

    return float(price) if price.replace(".", "").isdigit() else None


def normalize_location(location):
    """نرمال‌سازی موقعیت جغرافیایی (حذف فاصله‌های اضافی)"""
    return (
        location.strip().title()
        if isinstance(location, str) and location.strip()
        else None
    )


def normalize_url(url):
    """اعتبارسنجی URL"""
    pattern = r"^(https?|ftp)://[^\s/$.?#].[^\s]*$"
    return (
        url.strip()
        if isinstance(url, str) and re.match(pattern, url.strip())
        else False
    )
