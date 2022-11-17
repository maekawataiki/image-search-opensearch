# Image Similarity Search with OpenSearch

Sample code to search similar image on OpenSearch.

This sample uses [image-match](https://github.com/ProvenanceLabs/image-match) library which uses image signature to search similar image in elasticsearch.

This sample code shows how to use [image-match](https://github.com/ProvenanceLabs/image-match) library with OpenSearch.

## Usage

1. Install required library
   1. `pip install image_match`
      1. For more info, visit [image_match document](https://image-match.readthedocs.io/en/latest/start.html)
2. Create OpenSearch Cluster
3. (Optional) Prepare image dataset
   1. Put few images in `data/images_original` and refer to `generate_dataset.py`. This script generates 5 slightly cropped image with random offset per input image.
4. Refer to `image_search.py`
