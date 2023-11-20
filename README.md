# World Football Organization - Sports Statistics Database

## Project Description

This project aims to design a database for the World Football Organization, allowing it to keep up-to-date sports statistics for each match. The database will manage detailed information about participating countries, World Cup histories, team formations, coaching staff, players' history in previous World Cups, played matches, and general and individual statistics.

## Database Structure

### Participating Countries

- **Participated World Cups:**
  - History of World Cups each country participated in.
  - Position achieved in each World Cup.

### Teams and Players

- **Current Formation:**
  - Information about each player:
    - Last name and first names.
    - Passport number.
    - Age.
    - Position (goalkeeper, defense, etc.).
    - Current team they play for.
    - Shirt number in the World Cup.
    - Country to which the team belongs.

- **Coaching Staff:**
  - Data about people in the coaching staff.

### Played Matches

- **Match Information:**
  - Match instance (Qualifying, Round of 16, Quarterfinals, Semifinals, Final).

- **Individual Player Statistics:**
  - Player-specific data: goals, fouls, received cards.
  - Minute of occurrence and the corresponding match.

- **Team General Statistics:**
  - Number of minutes in attack.
  - Number of lateral moves.
  - Number of corners, etc.

## Exemplary Queries

- **Query Example:**
  - Retrieve information about Lionel Messi in the 2014 World Cup.
  - Details of the goal scored in the match between Argentina and the Netherlands.
