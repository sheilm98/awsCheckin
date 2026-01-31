# Serverless Visitor Log Application

A full-stack cloud application that allows users to "Check In" via a web interface. This project demonstrates a serverless architecture using AWS, focusing on scalability, cost-efficiency (Pay-as-you-go), and Infrastructure-as-Code principles.

##  Architecture Overview



The application follows a modern serverless pattern:
1. **Frontend**: A responsive HTML5/JavaScript interface hosted via **AWS Amplify**.
2. **API Layer**: **AWS API Gateway** acts as the entry point, handling RESTful POST requests.
3. **Compute**: **AWS Lambda** (Python 3.x) processes business logic and data validation.
4. **Database**: **Amazon DynamoDB** provides a NoSQL persistent data store for visitor records.
5. **Security**: Integrated CORS headers and IAM roles following the principle of least privilege.

## Features
- **Real-time Check-in**: Users can submit their names and receive instant confirmation from the cloud.
- **Automated Timestamping**: The backend automatically generates UTC timestamps for every entry.
- **Serverless Scaling**: The app handles 1 or 1,000 visitors without manual server management.

##  Tech Stack
- **Frontend**: HTML5, CSS3, JavaScript (Fetch API)
- **Backend**: Python (Boto3 SDK)
- **Cloud Provider**: Amazon Web Services (AWS)
- **Hosting**: AWS Amplify

##  Project Structure
- `index.html`: The frontend user interface and API integration logic.
- `lambda_function.py`: The Python script handling database writes.
- `main.tf`: (Optional) Terraform configuration for infrastructure deployment.

##  Setup & Deployment
1. **Database**: Create a DynamoDB table named `VisitorLog` with a Partition Key `VisitorID` (String).
2. **Lambda**: Deploy the `lambda_function.py` code and attach the `AmazonDynamoDBFullAccess` policy.
3. **API**: Create a REST API in API Gateway with a `/checkin` resource and a `POST` method. Enable **Lambda Proxy Integration**.
4. **Frontend**: Update the `apiURL` in `index.html` and deploy via AWS Amplify.

##  Security Note
The API Gateway is configured with CORS enabled to allow requests specifically from the Amplify domain. IAM roles are scoped specifically to the `VisitorLog` table to maintain high security standards.
