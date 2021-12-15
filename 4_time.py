import json

Could not parse 'event_date' as a timestamp. Required format is YYYY-MM-DD HH:MM[:SS[.SSSSSS]]

bigquery_client = bigquery.Client.from_service_account_json(CREDENTIALS_BIGQUERY, 'roas-164016')
dataset = bigquery_client.dataset(BQ_LOGS_DATASET_NAME)
table = dataset.table(BQ_EMAIL_SENDS_TABLE_NAME)

data = {}
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")#[.%f]]")
data['send_id'] = 'test'
data['uid'] = 'test'
data['account_id'] = 'test'
data['subaccount_id'] = 'test'
data['event_id'] = 'test'
data['event_date'] = now
data['html_content'] = 'test'
data['campaign_name'] = 'test'
data['subject'] = 'test'
data['send_type'] = 'test'

json_data = json.dumps(data)

data =  json.loads(json_data)
table.reload()

rows = [data]
errors = table.insert_data(rows)

# import re
# def change_date_format(dt):
#         return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)
# dt1 = "2026-01-02"
# print("Original date in YYY-MM-DD Format: ",dt1)
# print("New date in DD-MM-YYYY Format: ",change_date_format(dt1))
