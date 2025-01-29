from dataclasses import dataclass
from crawl4ai.models import CrawlResult
'''
Dataclasses are used as a decorator to make an empty class like without funtions
'''

@dataclass
class websiteURLArtifacts:
    url : str

@dataclass
class CrawlArtifacts:
    crawl_artifacts: CrawlResult