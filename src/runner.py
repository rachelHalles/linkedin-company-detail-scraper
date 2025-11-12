thonimport json
from extractors.linkedin_parser import parse_linkedin_page
from outputs.exporters import export_to_json
from config.settings import CONFIG

def run_scraper(input_file, output_file):
    with open(input_file, 'r') as file:
        company_urls = json.load(file)

    extracted_data = []
    for url in company_urls:
        data = parse_linkedin_page(url, CONFIG)
        extracted_data.append(data)
    
    export_to_json(extracted_data, output_file)

if __name__ == "__main__":
    input_file = 'data/inputs.sample.json'
    output_file = 'data/sample_output.json'
    run_scraper(input_file, output_file)