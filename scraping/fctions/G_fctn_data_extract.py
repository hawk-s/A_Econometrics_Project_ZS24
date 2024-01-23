#this should be a more efficient fction to extract the data.
def extract_card_data_from_html(soup):
    data = {}

    # Extracting set name and card name
    head_container = soup.find('div', class_='head-container')
    card_head = soup.find('div', class_="col-sm-8 psas")

    data['set_name'] = head_container.get_text(strip=True) if head_container else 'Set Name Not Found'
    data['card_name'] = card_head.h3.get_text(strip=True) if card_head and card_head.h3 else 'Card Name Not Found'

    # Extracting population report
    data['population_report'] = []
    if card_head:
        for div in card_head.find_all('div', class_="col-sm-3 psabox"):
            spans = div.find_all('span')
            if spans:
                label = spans[0].get_text(strip=True)
                value = spans[1].get_text(strip=True) if len(spans) > 1 else 'Value Not Found'
                data['population_report'].append((label, value))

    # Extracting population report date
    pop_report_date = card_head.find('p', class_="popreport") if card_head else None
    data['pop_report_date'] = pop_report_date.get_text(strip=True) if pop_report_date else 'Date Not Found'

    # Extracting prices data
    data['prices_data'] = []
    prices_tables = soup.find_all('div', class_="pricehistory")
    for table in prices_tables:
        tbody = table.find('tbody')
        if tbody:
            for row in tbody.find_all('tr')[1:]:
                tds = row.find_all('td')
                price_info = {
                    'Date': tds[0].get_text(strip=True) if len(tds) > 0 else None,
                    'Grade': tds[1].get_text(strip=True) if len(tds) > 1 else None,
                    'Price': tds[2].get_text(strip=True) if len(tds) > 2 else None,
                    'Sale Type': tds[6].get_text(strip=True) if len(tds) > 6 else None
                }
                data['prices_data'].append(price_info)

    return data
