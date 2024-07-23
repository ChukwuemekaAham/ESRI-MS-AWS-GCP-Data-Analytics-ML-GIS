# Creating Reusable Pipelines in Cloud Data Fusion

The goal of this project was to illustrate how to build a reusable pipeline that reads data from Cloud Storage, performs data quality checks, and writes to Cloud Storage.

## Objectives
•	Use the Argument Setter plugin to allow the pipeline to read different input in every run.
•	Use the Argument Setter plugin to allow the pipeline to perform different quality checks in every run.
•	Write the output data of each run to Cloud Storage.

2.	Confirm that the default compute Service Account {project-number}-compute@developer.gserviceaccount.com is present and has the editor role assigned. 

## Task 1. Add necessary permissions for your Cloud Data Fusion instance
1.	Create the Data Fusion Instance.
Note: Creation of the instance takes around 10 minutes. Please wait for it to be ready.
2.  Grant neccessary permissions to the service account associated with the instance in the IAM & Admin console. +Grant Access to the `Cloud Data Fusion API Service Agent`
3.  Grant service account user permission to Google-managed Cloud Data Fusion service account that looks like service-{project-number}@gcp-sa-datafusion.iam.gserviceaccount.com and then copy the service account name to your clipboard.


Task 2. Set up the Cloud Storage bucket
Create Cloud Storage bucket for storing results when the pipeline runs.
```bash
export BUCKET=$GOOGLE_CLOUD_PROJECT
gsutil mb gs://$BUCKET
```

## Task 3. Navigate to the Cloud Data Fusion UI
click on Data Fusion, then click the View Instance link next to the Data Fusion instance. Sign in, if required. If prompted to take a tour of the service click on No, Thanks. You should now be in the Cloud Data Fusion UI.

## Task 4. Deploy the Argument Setter plugin
In the Cloud Data Fusion web UI, click Hub on the upper right. Click the Argument setter action plugin and click Deploy. Click Create a pipeline. The Pipeline Studio page opens.

## Task 5. Read from Cloud Storage
1. Select Google Cloud Storage for source drop-down menu
2.	Hover over the Cloud Storage node and click the Properties button that appears.
 
3.	In the Reference name field, enter a name.
4.	In the Path field, enter ${input.path}. This macro controls what the Cloud Storage input path will be in the different pipeline runs.
5.	In the Format field, select text.
6.	In the right Output Schema panel, remove the offset field from the output schema by clicking the trash icon in the offset field row.
 
7.	Click the X button to exit the Properties dialog box.

## Task 6. Transform the data
1.	In the left panel of the Pipeline Studio page, using the Transform drop-down menu, select Wrangler.
2.	In the Pipeline Studio canvas, drag an arrow from the Cloud Storage node to the Wrangler node.
 
3.	Hover over the Wrangler node and click the Properties button that appears.
4.	In the Input field name, type body.
5.	In the Recipe field, enter ${directives}. This macro controls what the transform logic will be in the different pipeline runs.
 
6.	Click the X button to exit the Properties dialog box.

## Task 7. Write to Cloud Storage
1.	In the left panel of the Pipeline Studio page, using the Sink drop-down menu, select Cloud Storage.
2.	On the Pipeline Studio canvas, drag an arrow from the Wrangler node to the Cloud Storage node you just added.
 
3.	Hover over the Cloud Storage sink node and click the Properties button that appears.
4.	In the Reference name field, enter a name.
5.	In the Path field, enter the path of your Cloud Storage bucket you created earlier.
 
6.	In the Format field, select json.
7.	Click the X button to exit the Properties menu.

## Task 8. Set the macro arguments
1.	In the left panel of the Pipeline Studio page, using the Conditions and Actions drop-down menu, select the Argument Setter plugin.
2.	In the Pipeline Studio canvas, drag an arrow from the Argument Setter node to the Cloud Storage source node.
 
3.	Hover over the Argument Setter node and click the Properties button that appears.
4.	In the URL field, add the following:
https://storage.googleapis.com/reusable-pipeline-tutorial/args.json
Copied!
content_copy
 
The URL corresponds to a publicly accessible object in Cloud Storage that contains the following content:

```json
{
  "arguments" : [
    {
      "name": "input.path",
      "value": "gs://reusable-pipeline-tutorial/user-emails.txt"
    },
    {
      "name": "directives",
      "value": "send-to-error !dq:isEmail(body)"
    }
  ]
}
```

The first of the two arguments is the value for input.path. The path gs://reusable-pipeline-tutorial/user-emails.txt is a publicly accessible object in Cloud Storage that contains the following test data:
alice@example.com
bob@example.com
craig@invalid@example.com

The second argument is the value for directives. The value send-to-error !dq:isEmail(body) configures Wrangler to filter out any lines that are not a valid email address. For example, craig@invalid@example.com is filtered out.
5.	Click the X button to exit the Properties menu.


## Task 9. Deploy and run your pipeline
1.	In the top bar of the Pipeline Studio page, click Name your pipeline. Give your pipeline a name (like Reusable-Pipeline), and then click Save.
 
2.	Click Deploy on the top right of the Pipeline Studio page. This will deploy your pipeline.
3.	Once deployed, click the drop-down menu on the Run button. Notice the boxes for the input.path and directives arguments. This notifies Cloud Data Fusion that the pipeline will set values for these required arguments during runtime provided through the Argument Setter plugin. Click Run.
4.	Wait for the pipeline run to complete and the status to change to Succeeded.
 

Finally the Argument Setter plugin was used to create the reusable pipeline, which can take in different input arguments with every run.
