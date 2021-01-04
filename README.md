# fluke2022
Just another wedding website.
[fluke2022.uk](https://fluke2022.uk)

## Local testing
`docker build -t fluke2022 . && docker run -d --name fluke2022 -p 8080:8080 -e PORT=8080 fluke2022`

## Deployment
1. Get GCP
2. Enable Cloud Run API
3. Create a Cloud Build trigger pointing to this repo, using cloudbuild.yaml
4. Run pipeline manually, or push a commit to trigger it
5. Watch the magic happen

## Post-deployment
I added my domain to the Cloud Run service, as documented [here](https://cloud.google.com/run/docs/mapping-custom-domains).

