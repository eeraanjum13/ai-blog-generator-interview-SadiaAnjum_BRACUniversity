def get_seo_data(keyword):
    # Mock data for demonstration purposes
    import random
    return {
        "search_volume": random.randint(1000, 10000),
        "keyword_difficulty": round(random.uniform(0.1, 0.9), 2),
        "avg_cpc": round(random.uniform(0.5, 5.0), 2)
    }

def get_seo_real_data(keyword):
    # In a real implementation, this function would fetch data from an SEO API
    # or database. Here we return mock data for demonstration purposes.
    pass