# OVERVIEW, INSTRUCTIONS AND COMMANDS FOR BUILDING AZURE INFRASTRUCTURE  


## Install azure-cli  

[Instructions] (https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)  

Install in wsl2 with command:  
bash: `curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash`  

Login:  
   
Azure CLI: `az login`

## Key vault setup   

[Instructions] (https://learn.microsoft.com/en-us/azure/key-vault/secrets/quick-create-cli)  

### Create a resource group  

Azure CLI: `az group create --name "keyVault" --location "North Europe"`  

Azure CLI:

### Create a key vault

Azure CLI: `az keyvault create --name "keyVault-anurment" --resource-group "keyVault"`  

### Give your user account permissions to manage secrets in Key Vault  

Azure CLI: `az role assignment create --role "Key Vault Secrets Officer" --assignee "aleksi.nurmento_hotmail.com#EXT#@aleksinurmentohotmail.onmicrosoft.com" --scope "/subscriptions/d8eb9524-f301-476e-99f5-1b3ce79d9d9b/resourceGroups/keyVault/providers/Microsoft.KeyVault/vaults/keyVault-anurment"`




