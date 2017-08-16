# aws-cli-sample-with-python
This script is a pretty simple way to help you automatically create everything you need on aws iot

# Setup
* Specify THING_NAME, and POLICY_NAME in config.json like
```sh
{
    "THING_NAME": "N8GSFWW00372501A676600",
    "POLICY_NAME": "PubSubToAnyTopic"
}
```
* You can modify iotpolicy.json to change permissions if needed
```sh
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "iot:Publish",
        "iot:Subscribe",
        "iot:Connect",
        "iot:Receive"
      ],
      "Resource": [
        "*"
      ]
    }
  ]
}
```
# How to use it
* python aws-cli-sample.py


