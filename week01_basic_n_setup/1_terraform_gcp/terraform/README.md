
### Execution
use windows
run on power shell


```shell
# setting key file
  -- -----------
   1 cd C:\BI\data-engineering-zoomcamp-1\week_1_basics_n_setup\1_terraform_gcp\terraform
  
   4 gcloud auth activate-service-account --key-file stoked-duality-375907-2f5bb2d7.json
   5 gcloud auth list
   6 gcloud projects list --sort-by=projectId![image](https://user-images.githubusercontent.com/46880933/214941904-6d583c74-c9ff-4a39-bf1a-de0e4d17c488.png)

#terraform commend
# Initialize state file (.tfstate)
terraform init

# Check changes to new infra plan
terraform plan -var="project=<your-gcp-project-id>"
```

```shell
# Create new infra
terraform apply -var="project=<your-gcp-project-id>"
```

```shell
# Delete infra after your work, to avoid costs on any running services
terraform destroy
```
