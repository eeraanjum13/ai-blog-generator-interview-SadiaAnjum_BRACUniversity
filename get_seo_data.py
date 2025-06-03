def get_seo_data(keyword):
    # Mock data for demonstration purposes
    import random
    return {
        "search_volume": random.randint(1000, 10000),
        "keyword_difficulty": round(random.uniform(0.1, 0.9), 2),
        "avg_cpc": round(random.uniform(0.5, 5.0), 2)
    }
