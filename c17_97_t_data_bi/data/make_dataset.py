import os
from kaggle.api.kaggle_api_extended import KaggleApi
from pathlib import Path



def getProjectRoot() -> str:
    '''
    This function retrieves the absolute path of the project root directory.

    ## Parameters:
    - None

    ## Returns:
    - The absolute path of project's directory
    '''

    PATH = os.path.abspath(__file__)

    for i in range(3):
        PATH = os.path.dirname(PATH)

    return PATH


def downloadData() -> None:
    """
    This Script downloads relevant dataset files from the Kaggle API and creates the `/data/raw` directory 
    if it doesn't exists at project's root. 
    
    It's required to get an access token from the Kaggle account settings and follow the instructions.

    ## Parameters:
    - None

    ## Returns:
    - 9 .CSV Files downloaded in the ../data/raw directory
    """

    ROOT = getProjectRoot()
    DATADIR = os.path.join(ROOT,'data','raw')
    FILESPATH = Path(DATADIR)
    DATASET = 'olistbr/brazilian-ecommerce'

    if not FILESPATH.is_dir():
        print(f'Downloading files from {DATASET} in {FILESPATH}')
        api = KaggleApi()
        api.authenticate()
        api.dataset_download_files(dataset=DATASET, path=FILESPATH, unzip=True)
        print(f'Files from {DATASET} downloaded!')
    else:
        print(f'Files from {DATASET} in {FILESPATH} already downloaded')