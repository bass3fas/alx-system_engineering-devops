
### Author: Bassant Aboelhassan

# Postmortem

During the deployment of a new feature on our web application, an outage occurred on our production server, affecting user access to specific API endpoints. The outage lasted from 09:00 AM to 11:30 AM (UTC-7) on April 10th, 2024, impacting approximately 15% of our users who were unable to complete transactions through the affected API endpoints.

## Debugging Process

Issue Detection: The issue was first detected by monitoring alerts indicating increased error rates and response time deviations for the affected API endpoints at 09:00 AM.

## Initial Investigation:

Engineering team member JohnBasil (GitHub: thaboyjuicee) was alerted and began investigating immediately.
Assumed root cause to be a deployment-related issue due to recent code changes in the affected API endpoints.
Actions Taken:

Checked server logs and observed HTTP 500 errors for requests to the affected endpoints.
Reviewed recent code deployments and identified a recent update to the authentication middleware for the affected endpoints.
Misleading Paths:

Initially suspected database performance issues but ruled out after monitoring database metrics.
Considered network connectivity issues but found no anomalies in network logs.
Escalation:

Escalated the incident to the DevOps team for further analysis and assistance at 10:15 AM.
Resolution:

Identified that the recent authentication middleware update caused unexpected token validation errors, leading to HTTP 500 responses.
Rolled back the authentication middleware changes to the last stable version at 11:00 AM.
Conducted extensive testing and confirmed the restoration of normal operations by 11:30 AM.
Root Cause and Resolution

### Root Cause: The outage resulted from a recent update to the authentication middleware, causing unexpected token validation errors and HTTP 500 responses for affected API endpoints.

### Resolution: Rolled back the authentication middleware changes to the last stable version, ensuring proper token validation and restoring normal API functionality.

## Corrective and Preventative Measures

### Improvements/Fixes:

Enhance automated testing and staging environment validation for code deployments involving critical components like authentication.
Implement canary deployments or feature flags to gradually roll out changes and monitor for unexpected behavior.
Develop comprehensive rollback procedures and documentation for rapid response to similar incidents.
Tasks to Address the Issue:

Update deployment pipelines to include thorough testing of authentication mechanisms before production deployment.
Review and revise monitoring and alerting thresholds for quicker detection and response to similar incidents in the future.
By implementing these measures and ensuring rigorous testing and monitoring practices, we aim to minimize the impact of unexpected issues during future deployments and maintain high availability and reliability for our users.


        +-----------------------+
        |    User Experience    |
        +-----------------------+
                    |
                    v
        +-----------------------+
        |   Production Server   |
        |        (API)          |
        +-----------|-----------+
                    |
                    v
        +-----------------------+
        |  Deployment Pipeline  |
        +-----------|-----------+
                    |
                    v
        +-----------------------+
        |   Code Deployment     |
        |   (Authentication)    |
        +-----------|-----------+
                    |
                    v
        +-----------------------+
        |       Incident        |
        |      Investigation    |
        +-----------|-----------+
                    |
                    v
        +-----------------------+
        |      Root Cause       |
        |   Authentication Bug |
        +-----------|-----------+
                    |
                    v
        +-----------------------+
        |       Resolution      |
        | Rollback Authentication|
        +-----------|-----------+
                    |
                    v
        +-----------------------+
        |     Post-Incident     |
        |      Actions Taken    |
        +-----------------------+
