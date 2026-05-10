import requests
import json
from config import BASE_URL,BASE_DIR,HEADERS,TIMEOUT
from datetime import datetime, timezone

# date setting
batch_id = datetime.now().strftime("%Y%m%d_%H%M%S")
ingestion_timestamp = datetime.now(timezone.utc).isoformat()

def fetch_data(endpoint):
	# dir setting
	endpoint_name = endpoint.replace("/","_")
	raw_dir = BASE_DIR / "data" / "raw" / endpoint_name
	file_dir = raw_dir / f"{endpoint_name}_{batch_id}.json"
	raw_dir.mkdir(parents=True, exist_ok=True)

	# api setting
	url = BASE_URL+endpoint
	response = requests.get(url, headers=HEADERS, timeout=TIMEOUT)

	print(f"Starting {endpoint.replace('/',' ').title()} ingestion")
	if response.status_code != 200:
		print(f"API request failed with code {response.status_code}")
		print(response.text)
		return

	print("API request successful")

	raw_data = response.json()



	wrapped_data = {
		"metadata": {
			"source": "tennis-api",
			"entity": endpoint,
			"batch_id": batch_id,
			"ingestion_timestamp": ingestion_timestamp
			},
		"raw_data":raw_data
	}

	# saving file
	with open(file_dir, "w", encoding="utf-8") as file:
		json.dump(wrapped_data, file, indent=2)

	print(f"Saved file to {raw_dir}")
	print("Ingestion finished")

