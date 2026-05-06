import requests
import json
from config import base_url,base_dir,headers
from get_atp_ranking import endpoint
from datetime import datetime, timezone

# date setting
batch_id = datetime.now().strftime("%Y%m%d_%H%M%S")
ingestion_timestamp = datetime.now(timezone.utc).isoformat()

# dir setting
raw_dir = base_dir / "data" / "raw" / f"{endpoint.replace("/","_")}"
data_dir = base_dir / raw_dir
file_dir = data_dir / f"atp_ranking_{batch_id}.json"

# api setting
url = base_url+endpoint
response = requests.get(url, headers=headers)
raw_data = response.json()

print(f"Starting {endpoint.replace("/"," ").title()} ingestion")
if response.status_code == 200:
	print("API request successful")


wrapped_data = {
	"metadata": {
		"source": "tennis-api",
		"entity": endpoint, #  tu zmiana bedzie na vara
		"batch_id": batch_id,
		"ingestion_timestamp": ingestion_timestamp
		},
	"raw_data":raw_data
}

# saving file
with open(file_dir, "w", encoding="utf-8") as file:
	json.dump(wrapped_data, file, indent=2)

print(f"Saved file to {data_dir}")
print("Ingestion finished")
