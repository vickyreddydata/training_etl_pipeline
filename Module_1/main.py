from extraction import extraction_functional_enhanced
import os
from config import log_config

if __name__ == "__main__":
    print(os.getcwd())
    log_config.log_config()
    df_parquit,_,_,_,_ = extraction_functional_enhanced.extracted_data()
    print(df_parquit.head())