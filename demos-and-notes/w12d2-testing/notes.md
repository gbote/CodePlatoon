# Web App Testing

## How to Run the Puppeteer Tests

1. Confirm chromium is installed - on command line run `which chromium`
2. Start your app the way you would normally when running it.
3. Confirm in a browser your app is running.
4. In test file, confirm puppeteer is telling chromium to load the correct URL. It should be the host & port for your app - something like http://localhost:5173
5. Run the tests! : )

## Goals
- Example of how to set up a config & basic tests for frontend
- Learn about testing concepts & jargon, for interviews & for your career
- Understand why engineering orgs care about testing

## Value of Testing
- It is a huge plus to understand testing when looking for your first job.
    - Demonstrates professional understanding of software engineering.
    - Demonstrates understanding of how tests improve reliabity. 

- Test give the business certainty that things are behaving as expected
    - Automatable 
    - Reliable
    - Repeatable

- In complex apps, tests can catch regressions
    - Regressions
        - Reintroducing a bug
        - Missing/forgetting/breaking an existing or new feature

- Engineering orgs care about tests because it gives us certainty about our application behavior
    - This lets us make commitments to the business with less pain

- Tests alone are insufficient
    - A test is only as good as what you are testing for
    - Tests are usually coupled with a QA Team
        - Combining human QA testing and automated testing
    - Tests are a pragmatic tool; a testing strategy is never developed in isolation.

### Tests improve reliability, code quality, dev experience
- Gives us confidence in complex logic
- Confirm code works in a production environment & catch regressions
- **Gives us confidence in refactoring code without breaking something**
    - Specifically with refactoring legacy (old) codebases, this is called writing a "Test Harness". Source - "Refactoring", by Martin Fowler.  
- Helps enable continuous delivery (deploying to production frequently - maybe even daily), to ship code more frequently.
- Prevents regressions (bugs that get reintroduced).
- **Serves as strong documentation for code**
    - If we keep our tests up to date, tests for a class or function tell us a lot about the intent & behavior of that class/function. 
    - "Tests-as-documentation" is increasingly a standard practice in industry
        - Where the test works as 50% or more of the documentation.

## Who writes tests

- Developers test their own code
    - In the tech industry & particularly in startups, this approach is preferred
    - Positives:
        - Developers understand requirements better
        - Gives developers more ownership/responsibility of features

- Dedicated Test/QA Engineering Team to write tests
    - Probably more common with mission-critical software.

- For us, we are concerned with developers testing their own code. 

## Testing Tradeoffs
- Tests take time & energy to write **and** maintain.
- Tests don't directly deliver business value.
- Figuring a maintainable (in terms of time & energy) testing strategy isn't always obvious.

## Next Steps
- Gain experience writing tests
    - At some point add tests to a portfolio project
- Use your knowledge of testing to stand out from other candidates
    - Be prepared to talk about testing in interviews & actively look for opportunities to do so

## Types of Testing
- Terms
    - Test runner: The library/program actually running the tests
    - Assertion library: Tool that helps us write an individual

### Unit testing
- Tests the smallest pieces of our application. We test each part indepdendently
- For example, tests to confirm a function/method (or maybe a simple class) is working correctly
- Probably most common kind of testing
- Usually we are testing the inputs & outputs of a function/method
- **Should be fast**. 
- JS libraries
    - Jasmine (assertion library)
    - Mocha (testing framework - includes test runner)
    - Chai (assertion library)
    - Jest (by Facebook, often used w/React)
        - vitest - plays nice with vite, Jest compatible.
        - https://vitest.dev/

- Sometimes you have refactor your code to make testing possible
- Sometimes you have to mock certain functions or behaviors
    - We do this either to improve test speed, for consistency, or because the test is running
    in a different environment
    - Things we mock/fake:
        - Database calls
            - Maybe a DB takes a long time and slows down the test
            - Maybe we want to make sure we always use the same data for our test
            - Maybe we want to be able to run our test in an environment where the database
            doesn't exist.
                - Common with larger infrastructures.
        - HTTP requests
            - API calls or Ajax calls
        - Sometimes for frontend testing we have to fake browser
            - Example: 
                - DOM functions such as window.location.href()
                - getCookie(), 
                - getCSRFToken()

### How to write a unit test
1. Determine inputs of the function to test
    - Inputs for our *optimistic* case or happy path.
    - Inputs for our *pessimistic* case or bad path. 
    - Inputs for edge cases
2. Create assertion (expectations) for our test cases
3. Run unit tests
    - When you write a new test, **confirm that your test will also fail as expected**
4. Verify test results (assertions) are what we expect to see.

### Unit Testing Setup with Vitest
1. Install: `npm install --save-dev vitest`
2. In package.json add a test script so we can run vitest:

```
"scripts": {
     "test": "vitest run"
}
```

3. Write our test file. File name must be `my_name.test.js` 
    - vitest looks for *.test.js files and runs them.

## Functional / End-to-End Testing
- Test an entire feature, from the client to the server and back.
    - That's why it's called "end-to-end".
- The slowest kind of testing, but also gives you the strongest guarantees.
- Often you will have to automate a web browser to do e2e tests for web apps.
    - We are testing our app from the user's perspective
    - And we can "drive" the browser, click on links, check that divs with a certain class or id exist and have specific value, etc

- E2E testing involves all parts of our application
    - The UI, APIs, Database, etc

- Web app E2E testing
    - Automates a browser
        - Useually uses Chromium
        - Can run Chromium in "headless" mode
            - Running the browser code WITHOUT the actual window/GUI
    - Tools to automate a browser:
        - Selenium (old). **AVOID**
        - Puppeteer (new) **USE**

### Puppeteer E2E test config
See comments & instructions/documentation in example-puppeteer.test.js

### Running Puppeteer E2E Tests
1. Start your actual app
2. Make sure your test code is using the right hostname/port for your actual app
3. Run the Puppeteer E2E test


## Asides / Notes
- Snapshot testing
    - The frontend runs in the browser and a screenshot is taken.
        - This screenshot is compared with saved, "good" screenshot from a previous test run.
        - Used to confirm that a web page / web app UI **looks** exactly like it should
            - Good for catching regressions in CSS.
