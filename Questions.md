1. Discuss your strategy and decisions implementing the application. Please, consider time complexity, effort cost, technologies used, and any other variable that you understand important in your development process.

The project seemed quite simple to me, so I decided to use the lightest framework I know in Python, Flask. I believe that some technologies, such as containerization using Docker, would be overkill for the purpose of this challenge, so I mainly used tools that were suitable for such a simple task.

2. How would you change your solution to account for future columns that might be requested, such as “Bill Voted On Date” or “Co-Sponsors”?

It would be quite simple. Basically, some models would need to be modified to accommodate the new fields, and the access methods would also be updated if necessary. If the solution were using a database, I would need to think about migrations and version control for the database.

3. How would you change your solution if instead of receiving CSVs of data, you were given a list of legislators or bills that you should generate a CSV for?

It would be quite straightforward. The parsing method would need to be adjusted, and receiving any input file such as txt or even pdf would not significantly change the implementation; only different libraries would be used. To generate a CSV, it could be done manually using native Python or with the help of libraries.

4. How long did you spend working on the assignment?
About 3 hours
