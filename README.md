# Inshorts News API [Unofficial]
---
This API is capable of fetching news contents from various sources as gathered by Inshorts app.

---
### Show some :heart: and :star: the repo to support the project

[![GitHub stars](https://img.shields.io/github/stars/cyberboysumanjay/inshorts-news-api.svg?style=social&label=Star)](https://github.com/cyberboysumanjay/Inshorts-News-API)

[![Twitter Follow](https://img.shields.io/twitter/follow/cyberboysj.svg?style=social)](https://twitter.com/CyberboySj)

![GitHub followers](https://img.shields.io/github/followers/cyberboysumanjay.svg?style=social&label=Follow)

[![Telegram Channel](https://img.shields.io/badge/Telegram-Channel-orange)](https://t.me/sjprojects)

---

## News Categories

This API supports category wise news. Here is a complete list of all categories.

1. all
2. national //Indian News only
3. business
4. sports
5. world
6. politics
7. technology
8. startup
9. entertainment
10. miscellaneous
11. hatke
12. science
13. automobile

---

## Usage

Make a get request specifying the category of news you want
```
https://inshortsapi.vercel.app/news?category={category_name}
```
Example - https://inshortsapi.vercel.app/news?category=science

---

## Response Format

The response JSON Object looks something like this - 

```JSON
{
  "category": "technology",
  "data": [
    {
      "author": "Pragya Swastik",
      "content": "American actor Aaron Paul, who portrayed Jesse Pinkman in 'Breaking Bad', revealed that he uses a 'credit card-sized dumb phone' that cannot store any apps and can only make calls and send texts. \"There's no camera or emailing,\" Paul said, adding that he's planning to buy a flip phone. \"I haven't owned a computer in over 10 years,\" he added.",
      "date": "15 Mar 2020,Sunday",
      "imageUrl": "https://static.getinpix.com/public/images/v1/variants/jpg/m/2020/03_mar/15_sun/img_1584273701082_423.jpg",
      "readMoreUrl": "https://www.dailymail.co.uk/tvshowbiz/article-8111761/Breaking-Bad-star-Aaron-Paul-reveals-owned-computer-decade-prefers-FLIP-PHONE.html?utm_campaign=fullarticle&utm_medium=referral&utm_source=inshorts ",
      "time": "06:17 pm",
      "title": "\nI use a 'dumb phone' that only makes calls & sends texts: 'Breaking Bad' actor\n",
      "url": "https://www.inshorts.com/en/news/i-use-a-dumb-phone-that-only-makes-calls-sends-texts-breaking-bad-actor-1584276455594"
    },
    {
      "author": "Pragya Swastik",
      "content": "Google recently shared five basic protective measures against coronavirus that can be followed by people worldwide. These include washing hands often, coughing into the elbow, not touching the face, staying over three feet apart from others and staying at home on feeling sick. Google engineers are also building a website to screen potential coronavirus patients in the US.",
      "date": "16 Mar 2020,Monday",
      "imageUrl": "https://static.getinpix.com/public/images/v1/variants/jpg/m/2020/03_mar/15_sun/img_1584292734587_739.jpg",
      "readMoreUrl": "https://twitter.com/Google/status/1238893403821113344?s=20&utm_campaign=fullarticle&utm_medium=referral&utm_source=inshorts ",
      "time": "07:00 am",
      "title": "\nGoogle shares 5 basic protective measures against coronavirus\n",
      "url": "https://www.inshorts.com/en/news/google-shares-5-basic-protective-measures-against-coronavirus-1584322241969"
    }
    ],
  "success": true
}
```
---
## Setup

Install all dependencies listed in *requirements.txt* file. 

1. To install all dependencies run - 

    ```bash
    $ sudo -H pip3 install -r requirements.txt
    ```

2. Start the server

    ```bash 
    $ python app.py
    ```
---
## Apps using this API
#### [Telegram Channel](https://telegram.dog/news_inshorts) of Inshorts News
[![Telegram Channel](https://img.shields.io/badge/Telegram-Channel-orange)](https://t.me/news_inshorts)

---

### You can fork the repo and deploy on VPS, Heroku or Vercel :)  
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/cyberboysumanjay/Inshorts-News-API/tree/master)

[![Deploy to Vercel](https://vercel.com/button)](https://vercel.com/import/project?template=https://github.com/cyberboysumanjay/Inshorts-News-API/tree/master)

---
#### :star: the Repo in case you liked it :)
#### Made with :heart: in India

# © [Sumanjay](https://cyberboysumanjay.github.io)
