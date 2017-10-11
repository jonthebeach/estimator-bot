## Estimator-bot

Never again get worried about giving an estimation when having no idea at all what to answer in a Scrum planning/grooming meeting. This basic bot will assit you in estimating user stories. It estimates user stories based on its contents and uses deep learning to improve estimations over time. It currently works only for Jira and estimations are given as fibonacci based story points.

### Running the bot

```python
pip install -r requirements.txt
SLACK_BOT_TOKEN=<bot> python src/main.py
```
