# -*- coding: utf-8 -*-

# Sample Python code for youtube.commentThreads.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os
from dotenv import load_dotenv
import googleapiclient.discovery
from typing import List
import re
import pandas as pd
import sys
import random

def main():
  if len(sys.argv) <= 1:
    print("Need to enter at least one youtube video id as arguments")
    exit(0)
  
  ids = sys.argv[1:]

  comments = []
  for id in ids:
    comments.extend(getComments(id))

  random.shuffle(comments)

  filtered = filterComments(comments)

  annotatedComments = []
  pro = 0
  anti = 0
  for item in filtered:
    print("\nYou have annotated ", pro, "pro comments and ", anti, "anti comments")
    print("Next comment:")
    print(item)
    annotation = input("\nAnnotate: Anti-vacc = \"0\", pro vacc = \"1\", \"ENTER\" to skip, \"exit\" to finish > \n")
    if annotation == "0":
      anti += 1
      annotatedComments.append((0, item))
    elif annotation == "1":
      pro += 1
      annotatedComments.append((1, item))
    elif annotation == "exit":
      break
    else:
      continue
    
    
  writeToExcel(annotatedComments)

def writeToExcel(annotated):
  df = pd.DataFrame.from_records(annotated, columns=None)
  df.to_excel("assignment3.xlsx", index=False, header=False)

def filterComments(comments: List[str]):
  filtered = []
  for comment in comments:
    if re.search("vaccine|drug.|vaxxer|safe|immunity", comment.lower()):
      filtered.append(comment)
  
  return filtered

def getComments(videoId: str):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    load_dotenv()
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = os.getenv('DEVELOPER_KEY')

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        part="snippet",
        videoId=videoId,
        maxResults=2000,
        textFormat="plainText"
    )
    response = request.execute()

    return [response["items"][i]["snippet"]["topLevelComment"]["snippet"]["textOriginal"] for i in range(len(response["items"]))]


if __name__ == "__main__":
    main()