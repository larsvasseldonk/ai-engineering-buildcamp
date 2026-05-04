# Project ideas

A big part of the course is working on your capstone project in which you build your own AI application. Here you find ideas I collected over time.

## Personal

- (1) Language learner
  - Problem: I don't write and speak enough Italian.
- Problem: plant's always die
- Automat grocery shopper:
  - Problem: hard to always think of a nice recipes and order ingredients
- Wedding coach: that helps you with planning your wedding
- Voice notes to tasks
- Email organiser: 
  - Problem: too many spam emails: newsletters, commercials, etc. I want to get rid of it but can't keep track of it. For many I can unsubscribe. I would great to have a agent that helps met organiszing my email, unsubscribing from unuseful newsletters.

## Work

- Data Quality Agent:
  - Agents that runs data tests and takes action when tests are failing, such as: trying to implement fixes, communication to stakeholders, etc.
- Code organiser / cleaner / checker:
  - CI/CD AI Agent that checks whether the data dictionary is up to date
  - Automate PR requests
- Automated data analysis
- Automated data quality checks
- RAG for structured data
- Ops helper:
  - Morning report
  - Pain: 

## Project Cards

### Language-learner

I will build a WhatsApp and Telegram-based Italian language learning assistant for intermediate learners to improve by sending voice or text messages.  
Input: the user’s messages.  
Processing: a conversational AI that gives instant, personalized grammar corrections and vocabulary recommendations.  
Output: improved writing and speaking skills, with clear explanations.  
Success metric: users report feeling more confident in their Italian after a few weeks.

### Data assistant

I will build a WhatsApp-based data assistant that allows users to query a relational data warehouse using both natural language and reusable command shortcuts.

Problem:
- Business users cannot easily retrieve data from a complex data warehouse without relying on data engineers, due to the need for SQL and fragmented reporting tools.
- Data engineers spend significant time repeatedly answering similar questions and manually querying data, leading to inefficiency.
- There is no simple, trusted interface where users can quickly access validated data insights or reuse common queries.

Input: 
User messages via WhatsApp, either as natural language queries or predefined commands (e.g., /today, /revenue).

Processing: 
Classify user intent; retrieve relevant schema and similar past queries from a query memory system; generate and validate SQL using retrieval-augmented generation; execute queries in DuckDB; and compute trust signals based on similarity to previously validated queries.

Output: 
Concise answers delivered in WhatsApp, including results, explanations, SQL traces, and trust indicators (e.g., similar queries, tables used).

Success metric: 
Reduction in repeated manual queries and improved user trust, measured by reuse of shortcuts and accuracy on predefined business questions.

### Ad-hoc analyzing AGENT

Problem: spend too much time on doing simple analysis that business users cannot do.

That's why: I will build an data assitant agent takes a data question as input, searches the relevant data and documents, create visualizations, add this to a quarto presentation, makes it reproducable, and e-mails it back to the user.

What is important:
- analysis is reproducable, transparant, and includes an explanations of results
- visualisations are easy to read, and follow visualisation best practices
- it uses colors from our company