from scrape_rag.entity.artifact import websiteURLArtifacts
from scrape_rag.exceptionHandling.exception import ScrapeRagException
from scrape_rag.logging.logger import logging
import sys
import asyncio
from scrape_rag.components.crawler import Crawler

class CrawlingPipeline:
    def __init__(self):
        pass

    def get_website_url(self) -> websiteURLArtifacts:
        try:
            logging.info("Getting URL")
            url = input("Enter website url")

            url_artifact = websiteURLArtifacts(
                url=url
            )
            logging.info("URL get successfully.")
            return url_artifact
        except Exception as e:
            raise ScrapeRagException(e, sys)

async def main():
    try:
        pipeline = CrawlingPipeline()
        # url_artifact = pipeline.get_website_url()  # Uncomment for user input
        url = "https://github.com/deepakkhokhar1313/NetworkSecurity_MLops"
        crawler = Crawler(url=url)
        
        # Await the async crawl method
        crawl_result = await crawler.crawl()
        
        # Access markdown through the artifacts
        print(crawl_result.crawl_artifacts.markdown)  # Fixed attribute access
        
    except Exception as e:
        raise ScrapeRagException(e, sys)

if __name__ == "__main__":
    asyncio.run(main())




