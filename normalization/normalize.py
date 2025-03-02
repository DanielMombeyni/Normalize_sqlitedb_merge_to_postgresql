from normalization.fields import (
    normalize_title,
    normalize_game,
    normalize_price,
    normalize_location,
    normalize_url,
)


def normalize_ads(df):
    normalized_ads = []
    for _, row in df.iterrows():
        ad_id = row.get("id")
        title = normalize_title(row.get("title"))
        game = normalize_game(row.get("game"))
        price = normalize_price(row.get("price"))
        location = normalize_location(row.get("location"))
        url = normalize_url(row.get("url"))

        if ad_id and title and game and url:
            normalized_ads.append(
                {
                    "id": ad_id,
                    "title": title,
                    "game": game,
                    "price": price,
                    "location": location,
                    "url": url,
                }
            )

    return normalized_ads
