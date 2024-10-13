## 1. Strategy and Decisions for Implementing the Application

In developing this project, I aimed for simplicity and efficiency. I chose **Flask**, a lightweight Python framework, to build the application due to its minimal overhead and quick setup. Given the straightforward nature of the challenge, I avoided more complex solutions like containerization with Docker, as they would be overkill. Instead, I focused on selecting tools and technologies appropriate for the project's scope while considering factors such as time complexity and development effort.

## 2. Adapting the Solution for Future Changes

If future requirements included additional fields, such as **"Bill Voted On Date"** or **"Co-Sponsors"**, the solution would be easy to extend. I would update the models to incorporate the new fields and adjust any related access methods as necessary. If a database was involved, considerations for **database migrations and version control** would come into play to accommodate the changes seamlessly.

## 3. Modifying the Solution for Different Input Formats

Switching the data source from CSVs to other formats, such as a list of legislators or bills, would also be straightforward. The **data parsing methods** would need to be adjusted to handle different input formats. For example, handling **text files or PDFs** would require using specific libraries, but the core implementation would remain largely the same. Generating a CSV output could be done manually using **native Python functionality** or with the help of specialized libraries.

## 4. Time Spent on the Assignment

I spent approximately **3 hours** working on this assignment.
