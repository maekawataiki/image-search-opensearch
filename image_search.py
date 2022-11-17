# %%

from PIL import Image
import numpy as np

import boto3
from image_match.elasticsearch_driver import SignatureES
from opensearchpy import OpenSearch, RequestsHttpConnection, AWSV4SignerAuth

# %%

# cluster endpoint, for example: my-test-domain.us-east-1.es.amazonaws.com
host = 'search-wikipedia-data-xu2yxamrsofjjhee54oksbdmf4.us-west-2.es.amazonaws.com'
region = 'us-west-2'  # e.g. us-west-1
index_name = 'images'

credentials = boto3.Session().get_credentials()
auth = AWSV4SignerAuth(credentials, region)

client = OpenSearch(
    hosts=[{'host': host, 'port': 443}],
    http_auth=auth,
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection
)

# %%

ses = SignatureES(client, index=index_name)

# %%


def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        # img = Image.open(os.path.join(folder, filename))
        # img = np.array(img)
        # if img is not None:
        #     images.append(img)
        images.append(os.path.join(folder, filename))
    return sorted(images)


images = load_images_from_folder('data/images_cropped')
print(images)

# %%

ses.add_image(images[0])
ses.add_image(images[1])
ses.add_image(images[6])
ses.add_image(images[7])

# %%

ses.search_image(images[8])

# %%

# response = client.indices.delete(
#     index = index_name
# )

# %%
