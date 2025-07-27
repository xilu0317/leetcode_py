1. Design a URL Shortener (e.g., bit.ly)

Category: SCALABILITY, HASHING, DATABASE DESIGN

Problem:
Build a service that shortens long URLs and redirects them.

Functional Requirements:
Shorten a long URL

Redirect from a short URL to the original
Optional: Analytics (clicks, country, etc.)

Non-Functional Requirements:
High availability, scalability

Low latency redirection
Fault tolerance

Key Components:
API Server: Handles requests

Database: Stores mappings between short and long URLs
Encoder: Encodes IDs to base62 (a-zA-Z0-9)
Cache: For fast lookups (e.g., Redis)
URL Generation Approaches:
Auto-increment ID + Base62 encoding

Example: ID = 123456 → base62(123456) = "abc123"
Use database primary key or Redis counter
Hashing (MD5/SHA256)

Truncate to 6-8 characters
Use collision detection

Database Schema:
CREATE TABLE urls (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    long_url TEXT NOT NULL,
    short_code VARCHAR(10) UNIQUE,
    created_at TIMESTAMP DEFAULT NOW()
);