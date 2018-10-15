## Estimator-bot

Never again get worried about giving an estimation when having no idea at all what to answer in a Scrum planning/grooming meeting. This basic bot will assist you in estimating user stories. It estimates user stories based on its contents and uses deep learning to improve estimations over time. It currently works only for Jira and estimations are given as fibonacci based story points. Recorded live demo [here](http://recordit.co/5SVQ2KMX5J)

### Running the bot

```
pip install -r requirements.txt
SLACK_BOT_TOKEN=<bot_token> SLACK_BOT_JIRA_USER=<jira_username> SLACK_BOT_JIRA_PASS=<jira_password> python src/main.py
```
