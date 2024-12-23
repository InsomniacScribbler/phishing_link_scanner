
# Phishing Link Scanner

The **Phishing Link Scanner** is a Python-based tool designed to detect phishing links by analyzing URL characteristics and comparing them with known legitimate domains. It uses **Levenshtein distance** to check for possible misspellings and other heuristics to flag potential phishing attempts.

## Features

- **Domain Extraction**: Extracts and analyzes the subdomain, domain, and suffix of a given URL.
- **Misspelling Detection**: Uses the Levenshtein distance algorithm to detect possible misspellings of legitimate domain names.
- **Phishing URL Detection**: Flags URLs that are potentially phishing attempts based on domain comparison and misspelling heuristics.
- **Dataset Integration**: Includes a dataset of legitimate domains that can be used to train and improve detection accuracy.

## Dataset

The project includes a dataset of legitimate domains (`dataset_phishing.csv`) that is used to compare URLs for phishing detection. The dataset can be updated or expanded by adding new legitimate domains to improve detection accuracy.

### Dataset Fields

The dataset includes the following columns:

- **url**: The URL to be analyzed.
- **length_url**: Length of the URL.
- **length_hostname**: Length of the hostname.
- **ip**: Indicates if the URL has an IP address.
- **nb_dots, nb_hyphens, nb_at, nb_qm, nb_and, nb_or, nb_eq, nb_underscore, nb_tilde, nb_percent, nb_slash, nb_star, nb_colon, nb_comma, nb_semicolumn, nb_dollar, nb_space**: Counts of specific characters in the URL.
- **nb_www, nb_com, nb_dslash**: Counts of 'www', 'com', and double slashes.
- **http_in_path, https_token**: Boolean indicators for the presence of HTTP/HTTPS in the path or token.
- **phish_hints**: Indicators of potential phishing behavior based on the URL structure.

The dataset can be cloned alongside the project to maintain the same path, ensuring that no additional configuration is necessary.

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/phishing-link-scanner.git
   cd phishing-link-scanner
   ```

2. **Install dependencies**:
   You need to install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

   If `requirements.txt` doesn't exist yet, manually install the required packages:
   ```bash
   pip install tldextract python-Levenshtein
   ```

3. **Dataset**:
   The dataset (`dataset_phishing.csv`) will be used automatically during the URL analysis process. Ensure the dataset is in the same directory as your project or update the file path in the code accordingly.

## How to Use

1. **Run the Phishing URL Detection Script**:
   ```bash
   python phishing_link_scanner.py
   ```

2. **Input URLs**: The script will process a list of URLs (`test_urls`) and detect potential phishing attempts based on the dataset of legitimate domains.

3. **Detect Phishing**: The script will print any suspicious URLs that match the phishing detection criteria:
   ```bash
   Potential phishing detected: https://example.com
   ```

## Example Code Snippet

```python
test_urls = ['http://example.co', 'http://examp1e..com', 'https://www.google.security-updatte.com']

for url in test_urls:
    is_phishing_url(url, legitimate_domains)
```

## Contributing

If you'd like to contribute to the project:

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.


## Acknowledgments

- **tldextract**: Used for extracting domain parts from URLs.
- **Levenshtein**: Used for calculating the similarity between domain names.
