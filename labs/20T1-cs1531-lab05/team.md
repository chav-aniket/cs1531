# Lab05 Exercise 1
## How we're breaking work up
There are 32 overall routes, with 4 active people in our team we decided to aim to give everyone around 8 functions each. </br>
| Bundle | Components | Assigned To |
|--------|------------|-------------|
| **Bundle 1** | Messages + Tokens (8 Routes) | @Aniket chavan |
| **Bundle 2** | Channel + Search (8 Routes) | @Ashish Dutta |
| **Bundle 3** | User + Workspace Reset (7 Routes) | @Tina Lam |
| **Bundle 4** | Auth + Channels + Standup (9 Routes) | @Karim Saad |
As Search and Workspace Reset routes have relatively large functions, they've been offset with by distributing more functions to others such as 1 extra route for Karim and token functions for Aniket to complete. Having people complete entire route sections for files allows them to specialise and spend less time learning the intricacies of every file.

## How work intersects
This can most simply be explained through a short incomplete list of examples for intersections
1. validate_token() is used in every function that takes in a token
2. User class which Tina will be building will hold the valid token for the session which Aniket will build the generation function for
3. Ashish's search function will use Aniket's message local storage
4. Ashish's channel and Karim's channels will use Tina's user local storage
5. Karim's auth will be using Tina's User class and Aniket's token functions

Again, this is a small shortlist of only 5 ways in which our work will coincide with each other. In order to carry this out we are actively communicating to get each other's opinions and advice on how to build out our functions.

