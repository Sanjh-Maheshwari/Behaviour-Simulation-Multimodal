import pandas as pd
import re
import os
import requests
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

def download_image(url, folder='photos'):
    if not os.path.exists(folder):
        os.makedirs(folder)

   # Extracting image name from url
    image_name = url.split('/')[-1].split('?')[0] + '.jpg'
    image_path = os.path.join(folder, image_name)

    if os.path.exists(image_path): return image_path
    
    response = requests.get(url)
    if response.status_code == 200:
        with open(image_path, 'wb') as f:
            f.write(response.content)
        return image_path
    else:
        return 'Failed to download'
    

# Define the function to download images and extract the fullUrl from the media string
def download_and_extract_fullurl(index, row, folder='photos'):
    photo = row['media']
   
    path = ""
    try:
        # Regular expression to find the thumbnailUrl
        thumbnail_url_match = re.search("thumbnailUrl='(.*?)'", photo)
        
        # Extract the thumbnail URL if it's found
        thumbnail_url = thumbnail_url_match.group(1) if thumbnail_url_match else None
        
        # Regular expression to find the fullUrl
        full_url_match = re.search("fullUrl='(.*?)'", photo)
        
        # Extract the full URL if it's found
        full_url = full_url_match.group(1) if full_url_match else None

        if full_url:
            path = download_image(full_url, folder)
        else:
            path = download_image(thumbnail_url, folder)
    except Exception as e:
        print(f"Error downloading image at index {index}: {e}")
        pass
    
    return path

if __name__ == '__main__':
    df = pd.read_excel('behaviour_simulation_train.xlsx')
    df_small = df.copy()
    print(df_small.head())

    folder = 'photos'

    # Create the 'photos' directory if it does not exist
    if not os.path.exists(folder):
        os.makedirs(folder)

    # List to hold the paths
    path_list = [None] * df_small.shape[0]

    # Use ThreadPoolExecutor to download images in parallel
    with ThreadPoolExecutor(max_workers=48) as executor:
        # Wrap tqdm around the executor for progress bar functionality
        futures = {executor.submit(download_and_extract_fullurl, i, row, folder): i for i, row in df_small.iterrows()}
        
        for future in tqdm(as_completed(futures), total=len(futures)):
            index = futures[future]
            path = future.result()
            path_list[index] = path

    print(len(path_list))
    # Add the path list as a new column to the dataframe
    df_small['local_path'] = path_list

    df_small.to_excel('filtered_data.xlsx')