thonimport requests
from bs4 import BeautifulSoup

def parse_linkedin_page(url, config):
    headers = {
        'User-Agent': config['user_agent'],
        'Authorization': f'Bearer {config["access_token"]}',
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data for {url}")

    soup = BeautifulSoup(response.content, 'html.parser')
    company_data = extract_company_data(soup)
    return company_data

def extract_company_data(soup):
    name = soup.find('h1', {'class': 'org-top-card-summary__title'}).text.strip()
    description = soup.find('div', {'class': 'org-top-card-summary__tagline'}).text.strip()
    industry = soup.find('div', {'class': 'org-top-card-summary__industry'}).text.strip()
    website = soup.find('a', {'class': 'link-without-visited-state'}).text.strip()
    
    company_data = {
        'name': name,
        'description': description,
        'industry': industry,
        'website': website,
    }
    
    return company_data