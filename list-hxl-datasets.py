import ckancrawler, csv, json, logging, re, sys

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(sys.argv[0])

HEADERS = [
    ('ID', '#dataset+id',),
    ('Title', '#dataset+title',),
    ('Provider', '#org+provider+name',),
    ('Source', '#org+source+name',),
    ('Country name', '#country+name',),
    ('Country code', '#country+code',),
    ('Subnational?', '#indicator+subnational+bool',),
    ('Geocoded?', '#indicator+geocoded+bool',),
    ('CKAN tags', '#indicator+tags+list',),
    ('Resource count', '#indicator+resources+int',),
    ('Start year', '#date+year+start',),
    ('End year', '#date+year+end',),
]
""" Headers and hashtags """
    

crawler = ckancrawler.Crawler('https://data.humdata.org', user_agent="HDX-Developer-2015", delay=0)

csvout = csv.writer(sys.stdout)
csvout.writerow([header[0] for header in HEADERS])
#csvout.writerow([header[1] for header in HEADERS])

counter = 0
for package in crawler.packages(fq='vocab_Topics:hxl'):

    counter += 1
    if (counter % 100) == 0:
        logger.info("Read %d datasets...", counter)
        
    result = re.match(r'\d{2}/\d{2}/(\d{4})-\d{2}/\d{2}/(\d{4})', package['dataset_date'])
    if result:
        start_year = result.group(1)
        end_year = result.group(2)
    else:
        result = re.match(r'\d{2}/\d{2}/(\d{4})', package['dataset_date'])
        start_year = end_year = result.group(1)

    for group in package['groups']:
        for tag in package['tags']:
            csvout.writerow([
                package['name'],
                package['title'],
                package['organization']['name'],
                package['dataset_source'],
                group['title'],
                group['name'],
                package['subnational'],
                package['has_geodata'],
                tag['name'],
                package['num_resources'],
                start_year,
                end_year,
            ])
