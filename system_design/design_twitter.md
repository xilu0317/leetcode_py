2. Design Twitter (News Feed System)

Category: FANOUT, DATABASE SCHEMA DESIGN, SCALABILITY

Problem:
Design the backend of Twitter: users can tweet, follow others, and see a timeline (feed).
Functional Requirements:

Post a tweet
Follow/unfollow a user

Timeline/feed generation
Non-Functional Requirements:

Real-time feed
Scalability (millions of users/tweets)

Key Components:
Users Service
Tweet Service

Follower Graph (many-to-many)
Feed Generator

Cache (Redis/Memcached)
Feed Generation Strategies:

Fan-out on write:
Push tweets to all followers’ feeds
Good for users with few followers

Fan-out on read:
Pull tweets from followed users at read time
Better for users with many followers

Hybrid approach: push for regular users, pull for celebrities

Data Model (simplified):
CREATE TABLE tweets (
    tweet_id BIGINT PRIMARY KEY,
    user_id BIGINT,
    content TEXT,
    created_at TIMESTAMP
);

CREATE TABLE followers (
    user_id BIGINT,
    follower_id BIGINT
);