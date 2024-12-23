import tldextract
import Levenshtein as lv
import pandas as pd

# Load legitimate domains from the dataset
def load_legitimate_domains(file_path):
    # Read the dataset
    df = pd.read_csv(file_path)
    # Extract URLs labeled as legitimate
    legitimate_urls = df[df['status'] == 'legitimate']['url']
    # Extract domain names from URLs
    legitimate_domains = set()
    for url in legitimate_urls:
        extracted = tldextract.extract(url)
        legitimate_domains.add(f"{extracted.domain}.{extracted.suffix}")
    return list(legitimate_domains)

def extract_domain_parts(url):
    extracted = tldextract.extract(url)
    return extracted.subdomain, extracted.domain, extracted.suffix

def is_mispelled_domain(domain, legitimate_domains, threshold=0.9):
    for legit_domain in legitimate_domains:
        similarity = lv.ratio(domain, legit_domain)
        if similarity >= threshold:
            return False  # It's a legitimate domain
    return True  # No close match found, possibly misspelled

def is_phishing_url(url, legitimate_domains):
    subdomain, domain, suffix = extract_domain_parts(url)
    full_domain = f"{domain}.{suffix}"

    # Check if it's a known legitimate domain
    if full_domain in legitimate_domains:
        return False

    # Check for misspelled domain names
    if is_mispelled_domain(domain, legitimate_domains):
        print(f"Potential phishing detected: {url}")
        return True

    # Additional checks for suspicious subdomains
    suspicious_keywords = ['security', 'update', 'verify', 'login']
    if any(keyword in subdomain for keyword in suspicious_keywords):
        print(f"Suspicious subdomain detected: {url}")
        return True

    return False

# Main function
if __name__ == '__main__':
    # Path to your dataset
    dataset_path = r"C:\Users\gunsm\Desktop\brainwave\phishing_link_scanner\dataset_phishing.csv"

    # Load legitimate domains from the dataset
    legitimate_domains = load_legitimate_domains(dataset_path)

    # Test URLs
    test_urls = [
        'http://example.co',
        'http://examp1e..com',
        'https://www.google.security-updatte.com',
        'http://faceb00k.com',
        'https://google.com'
    ]

    # Check each URL for phishing
    for url in test_urls:
        is_phishing_url(url, legitimate_domains)
