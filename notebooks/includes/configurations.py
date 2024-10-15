# check: https://learn.microsoft.com/en-us/azure/databricks/connect/storage/azure-storage

# folder path syntax: "abfss://<container-name>@<storage-account-name>.dfs.core.windows.net/<path-to-data>"
bronze_folder_path = 'abfss://ctdatabronze@dbanurmentdevstacc01.dfs.core.windows.net/'

silver_folder_path = 'abfss://ctdatasilver@dbanurmentdevstacc01.dfs.core.windows.net/'
gold_folder_path = 'abfss://ctdatagold@dbanurmentdevstacc01.dfs.core.windows.net/'
