from scrape_rag.exceptionHandling.exception import ScrapeRagException
import sys
import asyncio
from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig
from scrape_rag.entity.artifact import CrawlArtifacts


class Crawler:
    def __init__(self, url=""):
        self.url = url
    
    async def crawl(self) -> CrawlArtifacts:
        try:
            browser_config = BrowserConfig()  # Default browser configuration
            run_config = CrawlerRunConfig()   # Default crawl run configuration

            async with AsyncWebCrawler(config=browser_config) as crawler:
                result = await crawler.arun(
                    url=self.url,
                    config=run_config
                )
                # print(result.markdown)
                crawl_artifacts = CrawlArtifacts(
                    crawl_artifacts= result
                )
                return crawl_artifacts
        except Exception as e:
            raise ScrapeRagException(e, sys)