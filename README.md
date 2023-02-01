# Annotation tool of youtube comments for machine learning

This is a simple tool that fetches youtube comments using google's API that then prompts the user and allows the user to annotate whether the comments are positive to the covid vaccine or negative towards it. 

### How to run

1. First install the required packages
  `pip install pandas`
  `pip install google-api-python-client`

2. Put your google api key in a file named .env
  Instructions for getting the api key can be found [here](https://www.geeksforgeeks.org/youtube-data-api-set-1/)

3. Run the program
  `python CommentScraper.py [arg1] [arg2] ...`
  The arguments supplied to the program are one or more youtube video ids. 

