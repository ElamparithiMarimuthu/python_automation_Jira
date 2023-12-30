GitHub to Jira Integration Automation

Overview
This project aims to automate the process of creating Jira tickets from valid GitHub issues, reducing the manual workload for developers and fostering a seamless integration between GitHub and Jira.

Problem Statement
Developers often face the challenge of manually creating Jira tickets for valid GitHub issues. This manual process not only consumes valuable time but also adds unnecessary workload to their daily tasks.

Solution
The solution involves the implementation of a Flask application in Python, acting as an intermediary between GitHub and Jira. The process can be summarized as follows:

GitHub Repository Usage:

Developers use GitHub repositories for their application development.
Issues are created on the GitHub repository to report problems or improvements.
Issue Validation:

QE engineers or other developers assess the validity of GitHub issues.
Automation Request:

Developers request automation by commenting "/jira" on valid GitHub issues.
Flask Application Workflow:

The Flask application, deployed on an AWS EC2 server, acts as a webhook for GitHub events.
When the "/jira" command is detected in a GitHub issue comment, the Flask application is triggered.
Jira Integration:

The Flask application interacts with the Jira API to automatically create a corresponding Jira ticket.
Implementation Details
Technologies Used
Python
Flask
AWS EC2
GitHub Webhooks
Jira API
Configuration
Jira API token, Jira email address, and Jira URL are configured within the Flask application for secure authentication.
Deployment
The Flask application is deployed on an AWS EC2 server for accessibility and reliability.
How to Use
GitHub Repository Setup:

Developers continue using GitHub repositories as usual.
Issue Validation:

Developers validate GitHub issues and identify those requiring Jira tickets.
Automation Trigger:

Developers trigger automation by commenting "/jira" on valid GitHub issues.
GitHub to Jira Integration:

The Flask application handles the automation process, creating corresponding Jira tickets.
Acknowledgments
A special thanks to the DevOps team for their collaboration in recognizing the need for automation and successfully implementing this solution.

Contribution
Contributions are welcome! Feel free to fork the repository, make improvements, and create pull requests.

License
This project is licensed under the MIT License.
