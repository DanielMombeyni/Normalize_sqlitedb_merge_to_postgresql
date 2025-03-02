from db.sqlite_reader import get_ads_data
from normalization.normalize import normalize_ads
from db.postgres_writer import insert_ads

def main():
    print("📥 در حال خواندن داده‌های تبلیغات از SQLite...")
    ads_df = get_ads_data()

    print("🔄 در حال نرمال‌سازی داده‌ها...")
    normalized_ads = normalize_ads(ads_df)

    print(f"✅ {len(normalized_ads)} تبلیغ معتبر برای درج در PostgreSQL پیدا شد.")

    if normalized_ads:
        print("📤 در حال ذخیره تبلیغات در PostgreSQL...")
        insert_ads(normalized_ads)

    print("🎉 انتقال داده‌ها با موفقیت انجام شد.")

if __name__ == "__main__":
    main()
