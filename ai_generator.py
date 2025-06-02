from get_seo_data import get_seo_data

# keyword = "wireless headphones"
# seo_data = get_seo_data(keyword)

import openai
import os
from dotenv import load_dotenv
# Load environment variables from .env file

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
AFF_LINK_1 = "hhttps://en.wikipedia.org/wiki/Cat"
AFF_LINK_2 = "https://en.wikipedia.org/wiki/Dog"


def generate_blog_post(keyword, seo_data):
    prompt = f"""
    Write a blog post about "{keyword}" targeting SEO. 
    Use the following SEO metrics:
    - Search volume: {seo_data['search_volume']}
    - Keyword difficulty: {seo_data['keyword_difficulty']}
    - Average CPC: ${seo_data['avg_cpc']}

    The post should be structured with:
    - A headline
    - An intro
    - At least 3 subheadings
    - A conclusion
    - At least 2 placeholders like {{AFF_LINK_1}} and {{AFF_LINK_2}} for affiliate links.

    Format: Markdown
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content.strip()

# print("Generating blog post...")
# blog_post = generate_blog_post(keyword, seo_data)
# print("Blog post generated successfully!")
# # print(blog_post)
# # # Save the generated blog post to a file
# with open(f"{keyword}.md", "w") as file:
#     file.write(blog_post)
# # Save the generated blog post to a file
# print("Blog post saved to blog_post.md")
