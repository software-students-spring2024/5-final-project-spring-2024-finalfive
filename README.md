![Python build & test](https://github.com/software-students-spring2024/5-final-project-spring-2024-finalfive/actions/workflows/web.yml/badge.svg) 

# StatMates

## Description

Our Web App, Stats Preacher, is an AI app that can provide easy-to-read sports-related information 
to the user based on user queries written in the natural language. 

While it is difficult for Large Language Models such as ChatGPT to provide updates sports statistics due to  lack of relevant sports information, Out app allows ChatGPT to gain access to sport statistics from Statmuse to provide an accurate and consise analysis of the user's queries.

Furthermore, the app allows you to save selected queries that the user may find interesting to their profile. You can even add a friend on the app and view their selected queries. 

## Configuration
Follow the following steps in order:

### 1. Clone our directory:
```
git clone https://github.com/software-students-spring2024/5-final-project-spring-2024-finalfive
```
### 2. Establish environment variables
```MONGO_URI``` You can create a .env file in the root directory and for local db storage you can set that variable to the following values: **mongodb://127.0.0.1:27017/** or **mongodb://localhost:27017/**


### 3. Build/run application containers and access site:
In order run the following in project directory:
```
docker-compose build
```
```
docker-compose up
```

Finally, you can access our site on your local device through following link: 
#### http://localhost:5001/

## Digital Ocean
### View our deployed version of the site: <br>
### http://167.71.104.143:5001/

## Docker Hub
https://hub.docker.com/r/jladrover/league_query


## Site Guide

### Sign Up/Log in
- **Register/Login:** To access features, you must have an account. Click "Register" to create an account or "Login" if you already have one.
- **Account Creation:** Fill in your username and password on the registration page. Ensure your username matches your personal preference as it will be your permanent identifier.

### Home
- **Navigation:** You can visit your profile from here or select a professional sports league to query.

### Profile Page
- **Profile:** Your profile shares your name, username, queries, and friends.
- **Add friends:** You can add friends from this page, and your saved queries are visible to those who add you.

### Queries Page
- **Queries:** When you click on a sports league on the home page, you are directed here.
- **Save:** You can then save a valid query to your profile, which would store the league, query, and result.
- **Note:** Invalid queries, where the api fails to get an answer for the query, are not able to be saved to a user profile.

### Adding/Viewing Friends' Queries
- **Adding:** Click on the add friend option in the profile page and type in a valid username.
- **Viewing:** This person will now be added as a friend to your account and click on their name on the profile page to view their queries!



## Team

Jean Luis Adrover: https://github.com/jladrover

Denzel Prudent: https://github.com/denprud

Sang In Kang: https://github.com/sik247

Rakshit Sridhar: https://github.com/RakSridhar23